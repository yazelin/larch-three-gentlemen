# 台詞即興：每一句叫那個角色自己演（角色卡＋前文＋這句要表達什麼），兩家模型各給三種說法，再挑最像真人講的。
#   GEMINI_CHAT_URL=… GEMINI_IMAGE_KEY=… python3 tools/improv.py gen 劇本/第一章.md     # 產候選 → 劇本/即興/<章>.json（可續跑）
#   python3 tools/improv.py judge 劇本/第一章.md                                         # 讀稿人挑句 → 同檔加 pick
#   python3 tools/improv.py show 劇本/第一章.md                                          # 列出要換的句子給人看
# 服務網址與金鑰只從環境變數讀，不寫進 repo。llmshare 只用 deepseek-v4.1-flash:1017，每分鐘最多 15 次。
import json, os, re, ssl, subprocess, sys, threading, time, pathlib, urllib.request, concurrent.futures as cf
ROOT = pathlib.Path(__file__).resolve().parent.parent
CARD = {"茶語": "茶語", "M": "M", "明": "M", "C": "C", "晨": "C", "S": "S", "詩": "S"}
LINE = re.compile(r"^(茶語（心聲）|茶語|M|C|S|明|晨|詩)：(.+)$")
CHOICE = re.compile(r"^₩(.*?)：「(.+)」（(.)＋1）$")
DS = "deepseek-v4.1-flash:1017"

def parse(md):
    items = []   # (kind, speaker, text, raw)
    for raw in md.split("## CG 清單")[0].split("## 取材對照")[0].splitlines():
        t = raw.strip()
        if not t or t.startswith(("【", ">", "---", "# ")): continue
        if t.startswith("## "): items.append(("head", "", t[3:], raw)); continue
        m = CHOICE.match(t)
        if m: items.append(("line", "茶語", m.group(2), raw)); continue
        m = LINE.match(t)
        if m: items.append(("line", m.group(1), m.group(2), raw)); continue
        items.append(("ctx", "", t, raw))
    return items

def ctx_text(items, k, n=10):
    out = []
    for kind, sp, tx, _ in items[max(0, k - n):k]:
        out.append(tx if kind != "line" else f"{sp}：{tx}")
    return "\n".join(out)

def prompt(items, k):
    kind, sp, tx, raw = items[k]
    who = "茶語" if sp.startswith("茶語") else sp
    card = (ROOT / "劇本/角色卡" / f"{CARD[who]}.md").read_text(encoding="utf-8")
    nxt = next((f"{s}：{t}" if kk == "line" else t for kk, s, t, _ in items[k + 1:k + 2]), "（場景結束）")
    head = next((t for kk, _, t, _ in reversed(items[:k]) if kk == "head"), "")
    inner = "這是她心裡的聲音，不說出口，" if sp == "茶語（心聲）" else ""
    choice = "這是玩家可以選的一句話，要短，像她真的會脫口而出的，" if raw.lstrip().startswith("₩") else ""
    return (f"你要演這個角色，只當這個人，不當作家。\n\n{card}\n\n場景：{head}\n前面發生的事與對話：\n{ctx_text(items, k)}\n\n"
            f"現在輪到「{who}」說下一句。{inner}{choice}劇本的草稿寫的是：「{tx}」\n下一句會接：「{nxt}」\n"
            "草稿只是參考，很可能不自然、有 AI 味：不要沿用草稿的句型和用詞，不要跟前一句套同一個句型，不要文青、詩意、抽象的漂亮句，不要替自己總結心情。"
            "只要做到這一句的作用：該傳達的劇情資訊、情緒、笑點，以及讓下一句接得上。用這個人在這個當下真的會脫口而出的台灣口語重講一次。"
            "不要加劇本裡沒有的設定。給三種說法，一行一句，只寫台詞本身：不要引號、不要編號、不要動作、不要說明。")

_lock, _last = threading.Lock(), [0.0]
def ask_ds(p):
    with _lock:   # ponytail: 全域節流 4.2 秒一次，剛好卡在每分鐘 15 次以內
        w = 4.2 - (time.time() - _last[0])
        if w > 0: time.sleep(w)
        _last[0] = time.time()
    r = subprocess.run(["llmshare", "raw", DS, p], capture_output=True, text=True, timeout=240, stdin=subprocess.DEVNULL)
    return r.stdout

def ask_gm(p):
    req = urllib.request.Request(os.environ["GEMINI_CHAT_URL"], data=json.dumps({"prompt": p}).encode(),
          headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_IMAGE_KEY"]})
    ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    return json.load(urllib.request.urlopen(req, timeout=180, context=ctx)).get("text", "")

def clean(out):
    c = []
    for l in out.splitlines():
        l = re.sub(r"^\s*(\d+[.、．)]|[-*•])\s*", "", l).strip().strip("「」\"“”")
        l = re.sub(r"^(茶語（心聲）|茶語|M|C|S|明|晨|詩)：", "", l).strip()
        if l and len(l) < 120 and not l.startswith(("說法", "以下", "好的")): c.append(l)
    return c[:3]

def path_for(md): return ROOT / "劇本/即興" / (pathlib.Path(md).stem + ".json")

def gen(md):
    items = parse(pathlib.Path(md).read_text(encoding="utf-8"))
    out = path_for(md); out.parent.mkdir(exist_ok=True)
    done = {d["k"]: d for d in json.loads(out.read_text(encoding="utf-8"))} if out.exists() else {}
    todo = [k for k, it in enumerate(items) if it[0] == "line" and not (k in done and done[k]["ds"] and done[k]["gm"])]
    print("要演", len(todo), "句", flush=True)
    save_lock = threading.Lock()
    def one(k):
        p = prompt(items, k); d = done.get(k) or {"k": k, "speaker": items[k][1], "orig": items[k][2], "raw": items[k][3], "ds": [], "gm": []}
        for name, fn in (("ds", ask_ds), ("gm", ask_gm)):
            if not d[name]:
                for _ in range(2):
                    try: d[name] = clean(fn(p)); break
                    except Exception as e: print(k, name, "失敗", e, flush=True); time.sleep(5)
        with save_lock:
            done[k] = d
            out.write_text(json.dumps(sorted(done.values(), key=lambda x: x["k"]), ensure_ascii=False, indent=1), encoding="utf-8")
        print(k, d["speaker"], d["orig"][:16], "|", (d["ds"] + d["gm"])[:1], flush=True)
    with cf.ThreadPoolExecutor(3) as ex: list(ex.map(one, todo))

BAD = re.compile(r"——|—|[,!?;:()]|不是.{1,12}而是|這讓我|彷彿|宛如")
def judge(md):
    items = parse(pathlib.Path(md).read_text(encoding="utf-8")); out = path_for(md)
    data = json.loads(out.read_text(encoding="utf-8"))
    def one(d):
        if "pick" in d: return d
        cands = [d["orig"]] + [c for c in d["ds"] + d["gm"] if not BAD.search(c)]
        cands = list(dict.fromkeys(cands))
        who = "茶語" if d["speaker"].startswith("茶語") else d["speaker"]
        card = (ROOT / "劇本/角色卡" / f"{CARD[who]}.md").read_text(encoding="utf-8")
        p = (f"你是台灣的視覺小說編輯，專門把 AI 味的台詞挑掉。\n\n角色卡：\n{card}\n\n前文：\n{ctx_text(items, d['k'])}\n\n"
             f"下面是「{d['speaker']}」這一句的候選，0 號是原稿。挑一句最像這個人在這個當下真的會講的話："
             "口語、自然、不解說設定、不像金句、不像翻譯、資訊沒有少、跟前文接得上。下面這些都算 AI 味，一律不選：跟前一句套同一個句型接力（例：「結論是…」「結論是…」）；文青、詩意、抽象的漂亮句（例：「我知道主角會怎麼跪下去」）；對稱的口號；替角色總結心情。原稿有這些毛病就不要選 0；原稿已經很自然才選 0。\n"
             + "\n".join(f"{i}. {c}" for i, c in enumerate(cands)) + "\n\n只回答一個數字。")
        try: n = int(re.search(r"\d+", ask_ds(p)).group())
        except Exception: n = 0
        d["cands"], d["pick"] = cands, cands[n] if n < len(cands) else d["orig"]
        return d
    data = [one(d) for d in data]
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("換掉", sum(d["pick"] != d["orig"] for d in data), "/", len(data))

def show(md):
    for d in json.loads(path_for(md).read_text(encoding="utf-8")):
        if d.get("pick") and d["pick"] != d["orig"]: print(f"{d['k']}\t{d['speaker']}\t{d['orig']}\t→\t{d['pick']}")

if __name__ == "__main__":
    {"gen": gen, "judge": judge, "show": show}[sys.argv[1]](sys.argv[2])
