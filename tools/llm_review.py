# 用 llmshare 逐段審台詞的 AI 味：python3 tools/llm_review.py <劇本.md> [模型]
# 預設 deepseek-v4.1-flash:1017（yazelin 2026-11-06：review 用 deepseek）
# 結果寫到 review/<章>_<模型>.json。不自動改劇本。
import json, os, re, sys, time, pathlib, urllib.request
src = pathlib.Path(sys.argv[1]); model = sys.argv[2] if len(sys.argv) > 2 else "deepseek-v4.1-flash:1017"
ROOT = pathlib.Path(__file__).resolve().parent.parent
body = src.read_text(encoding="utf-8").split("## CG 清單")[0]
secs = re.split(r"\n(?=## )", body)[1:]
RULES = """你是台灣的資深視覺小說編輯，專抓「AI 味」。這是一部乙女向視覺小說的台詞稿，主角茶語是住在高雄的女大學生（文組、自稱程式白痴、有點懶、愛吐槽），三位 AI 夥伴：C（美術，溫和、答應很快、會忘記約定）、M（技術，話少、可靠、直接）、S（音樂，少年感、隨興、愛鬧）。
格式：「角色：台詞」是說出口的話；「茶語（心聲）：」是心裡的話；〔 〕是旁白；【 】是演出標記，不用審。

請逐句挑出有 AI 味的台詞。AI 味指的是：
1. 書面、太工整、太完整，不像真人當下會講的話；台灣大學生不會這樣說話
2. 空泛的總結句、通用道理、勵志句，角色把主題直接講出來
3. 「不是 X，而是 Y」這類假對比；排比；過度修辭與比喻腔
4. 翻譯腔、中國用語（例如「質量」「視頻」「挺」用太多）
5. 心聲在總結感想，而不是具體在想什麼
6. 對話接不上前一句，或角色個性跑掉
7. 刻意製造金句、每段都用一句漂亮話收尾
8. 被問了簡單的事卻拐彎用畫面回答（問「畫到幾點」回「外面有鳥在叫」）；正常人會直接答（「好像畫到快天亮吧」）

只挑真的有問題的，不要為了湊數而挑；沒問題的段落可以回空陣列。
用 JSON 回答，格式：{"issues":[{"quote":"原句（逐字照抄）","problem":"哪裡有 AI 味，一句話","fix":"改寫建議，要像台灣人講話"}]}。只回 JSON。"""
key = os.environ["LLMSHARE_API_KEY"]; base = os.environ.get("LLMSHARE_BASE_URL", "https://llm-share.duotify.com/v1")
out = []
for i, sec in enumerate(secs):
    title = sec.splitlines()[0][3:]
    req = {"model": model, "messages": [{"role": "system", "content": RULES}, {"role": "user", "content": sec}], "temperature": 0.3}
    for t in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(base + "/chat/completions", data=json.dumps(req).encode(),
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}), timeout=300)
            txt = json.load(r)["choices"][0]["message"]["content"]
            m = re.search(r"\{.*\}", txt, re.S); res = json.loads(m[0]) if m else {"raw": txt}
            break
        except Exception as e:
            res = {"error": str(e)}; time.sleep(20)
    res["section"] = title; out.append(res)
    print(title, len(res.get("issues", [])), "處" if "issues" in res else res.get("error", "?")[:80], flush=True)
    time.sleep(5)
dst = ROOT / f"review/{src.stem}_{model.replace(':','_')}.json"
dst.write_text(json.dumps(out, ensure_ascii=False, indent=1)); print("寫入", dst)
