# 把劇本組成 Larch 白板並推上私人專案（不上架）。
#   python3 tools/larch_build.py             # 只組卡、印統計、寫 dist/board_ch1.json
#   python3 tools/larch_build.py --push      # 推上 Larch（第一次建專案，id 存在 larch_project.json）
# 圖走 jsDelivr（repo 公開、檔名 ASCII），不上傳 Larch 媒體庫。立繪、BGM、配音之後再補。
import json, re, sys, pathlib, subprocess, urllib.request, urllib.error, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://larch.ink/api/agent"
STATE = ROOT / "larch_project.json"
SHA = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
CDN = f"https://cdn.jsdelivr.net/gh/yazelin/larch-three-gentlemen@{SHA}/"
BOARD = "board-ch1"
NAME = "慕詩客，邀明月，對朝霞"

def cg_url(cid): return CDN + f"art/cg/{cid}.jpg"

# ---------- 第一步：劇本 → 段落 ----------
def segments(md):
    """[('card', title, lines, cgs) | ('choice', [(text, key)]) | ('branch', key, lines, cgs)]；每句 line 可帶 background。"""
    body = md.split("## CG 清單")[0]
    segs, title, lines, cgs, mode, last_desk, pend_bg = [], "", [], [], None, cg_url("01-1"), None
    def close():
        nonlocal lines, cgs
        if lines:
            segs.append(("branch", mode, lines, cgs) if mode else ("card", title, lines, cgs))
        lines, cgs = [], []
    def add(sp, tx, emo):
        nonlocal pend_bg
        ln = {"id": f"l{len(lines)}", "speaker": sp, "text": tx, "emotion": emo}
        if pend_bg: ln["background"], pend_bg = pend_bg, None
        lines.append(ln)
    for raw in body.splitlines():
        l = raw.strip()
        if not l or l.startswith((">", "---", "# ", "【立繪")): continue
        if l.startswith("## "): close(); title = l[3:]; continue
        m = re.match(r"【CG ([^｜\s】]+)", l)
        if m:
            cid = m[1]; cgs.append(cid); pend_bg = cg_url(cid)
            if cid != "01-5": last_desk = pend_bg
            continue
        m = re.match(r"【背景 (\w+)", l)
        if m: pend_bg = cg_url("01-5") if m[1] == "studio" else last_desk; continue
        m = re.match(r"₩(.+?)（([CMS])＋1）", l)
        if m:
            close()
            if segs and segs[-1][0] == "choice": segs[-1][1].append((m[1].strip(), m[2]))
            else: segs.append(("choice", [(m[1].strip(), m[2])]))
            continue
        if re.fullmatch(r"（[CMS]）", l): close(); mode = l[1]; continue
        if l == "（共通）": close(); mode = None; continue
        if re.fullmatch(r"（第.+完）", l): add("旁白", l, "描述動作"); continue
        if l.startswith("〔"): add("旁白", l.strip("〔〕"), "描述動作"); continue
        m = re.match(r"([^：]{1,8}?)（心聲）：(.*)", l)
        if m: add(m[1], f"（{m[2]}）", "心聲"); continue
        m = re.match(r"([^：]{1,8})：(.*)", l)
        if m: add(m[1], m[2], ""); continue
        add("旁白", l, "描述動作")
    close()
    return segs

# ---------- 第二步：段落 → 卡片與連線 ----------
def build(segs, ch="ch1"):
    nodes, edges, cg_order = [], [], []
    bg = [cg_url("01-1")]
    def new_id(): return f"{ch}-{len(nodes):03d}"
    def base(title, x, y):
        return {"id": new_id(), "type": "story", "position": {"x": x, "y": y}}
    def dialogue(title, lines, cgs, x, y):
        n = base(title, x, y)
        for ln in lines:
            if ln.get("background"): bg[0] = ln["background"]
        first_bg = lines[0].get("background") or bg_before
        d = {"type": "dialogue", "title": title, "speaker": lines[0]["speaker"], "text": lines[0]["text"],
             "emotion": lines[0]["emotion"], "dialogueLines": lines, "background": first_bg,
             "stage": {"actors": []}, "characterLayers": [], "transition": "fade", "transitionMs": 360, "voiceMode": "off"}
        if cgs:
            d["cgOps"] = [{"id": f"cg-{c}", "mode": "unlock", "url": cg_url(c)} for c in cgs]
            cg_order.extend(c for c in cgs if c not in cg_order)
        n["data"] = d; nodes.append(n); return n["id"]
    def link(a, b, h=None):
        e = {"id": f"e-{a}-{b}", "source": a, "target": b}
        if h: e["sourceHandle"] = h
        edges.append(e)
    x, prev, tails, choice, keys = 0, [], [], None, []
    for s in segs:
        bg_before = bg[0]
        if s[0] == "card":
            x += 400; nid = dialogue(s[1], s[2], s[3], x, 0)
            for p in prev: link(p, nid)
            prev = [nid]
            if tails: prev = [nid]; tails = []
        elif s[0] == "choice":
            x += 400; n = base("先問誰", x, 0)
            n["data"] = {"type": "choice", "title": "先問誰", "text": "先問誰的意見？", "choices": [t for t, _ in s[1]],
                         "choiceMode": "branch", "choicePlacement": "center", "choiceConditions": [None] * len(s[1]),
                         "choiceLinks": [None] * len(s[1]), "background": bg[0], "stage": {"actors": []}, "characterLayers": []}
            nodes.append(n)
            for p in prev: link(p, n["id"])
            choice, keys, prev, bx = n["id"], [k for _, k in s[1]], [], x
        elif s[0] == "branch":
            k, lines = s[1], list(s[2]); i = keys.index(k); y = (i - 1) * 300
            last = lines.pop() if len(lines) > 1 else {"speaker": "旁白", "text": "……", "emotion": "描述動作"}
            bid = dialogue(f"選 {k}", lines, s[3], bx + 400, y)
            link(choice, bid, f"choice-{i}")
            sv = base(f"{k} 好感 +1", bx + 800, y)
            sv["data"] = {"type": "setVariable", "title": f"{k} 好感 +1", "speaker": last["speaker"], "text": last["text"],
                          "variableOps": [{"kind": "add", "value": 1, "variable": f"aff{k}"}],
                          "background": bg[0], "stage": {"actors": []}, "characterLayers": []}
            nodes.append(sv); link(bid, sv["id"]); prev.append(sv["id"]); x = bx + 800
    return nodes, edges, cg_order

def check(nodes, edges):
    ids = {n["id"] for n in nodes}
    bad = [e for e in edges if e["source"] not in ids or e["target"] not in ids]
    has_in = {e["target"] for e in edges}; has_out = {e["source"] for e in edges}
    orphans = [n["id"] for n in nodes if n["id"] not in has_in][1:]
    dead = [n["id"] for n in nodes if n["id"] not in has_out][:-1]
    empty = [n["id"] for n in nodes if n["data"]["type"] in ("dialogue", "setVariable") and not str(n["data"].get("text", "")).strip()]
    nobg = [n["id"] for n in nodes if not n["data"].get("background")]
    assert not (bad or orphans or dead or empty or nobg), dict(bad=bad, orphans=orphans, dead=dead, empty=empty, nobg=nobg)

# ---------- 推上 Larch ----------
def call(method, path, body=None, etag=None):
    key = (pathlib.Path.home() / ".config/larch/key").read_text().strip()
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    if etag: h["If-Match"] = etag
    for t in range(4):
        try:
            r = urllib.request.urlopen(urllib.request.Request(API + path, method=method, headers=h,
                                       data=json.dumps(body).encode() if body is not None else None), timeout=180)
            return json.loads(r.read() or b"{}"), r.headers.get("ETag")
        except urllib.error.HTTPError as ex:
            msg = ex.read().decode()[:300]
            if ex.code in (429, 502, 503) and t < 3:
                time.sleep(55 if ex.code == 429 else 8); continue
            raise SystemExit(f"{method} {path} → {ex.code} {msg}")

def push(nodes, edges, cgs):
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    if not st.get("id"):
        r, _ = call("POST", "/projects", {"name": NAME, "description": "乙女向視覺小說，製作中。", "tags": ["慕詩客"]})
        st["id"] = (r.get("project") or r)["id"]; STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1))
    pid = st["id"]
    proj, etag = call("GET", f"/projects/{pid}")
    p = proj.get("project", proj)
    if p.get("settings", {}).get("organization", {}).get("tags") and "慕詩客" not in p["settings"]["organization"]["tags"]:
        raise SystemExit("專案標籤不對，停下來，不覆寫")
    # 專案層設定（整份 PUT 會清白板，之後白板再推一次）
    s = p.setdefault("settings", {})
    s.update({"stageFit": "auto", "keepActorsInFrame": False, "textSpeed": 55, "returnToTitleOnEnd": True,
              "titleScreenEnabled": True, "titleCoverImage": cg_url("01-5"), "projectThumbnail": cg_url("01-5"),
              "cgGalleryEnabled": True, "cgGallerySource": "picked",
              "cgGalleryItems": [{"url": cg_url(c), "title": f"CG {c}", "locked": True} for c in cgs]})
    p["variables"] = [{"id": f"aff{k}", "name": f"aff{k}", "type": "number", "label": f"{k} 好感", "defaultValue": 0} for k in "CMS"]
    p["languages"] = p.get("languages") or [{"code": "zh-Hant", "label": "繁體中文", "voiceMode": "off"}]
    nodes[0]["data"]["start"] = True
    p["boards"] = [{"id": BOARD, "kind": "story", "mode": "story", "name": "第一章　茶", "description": "", "nodes": [], "edges": []}]
    _, etag = call("PUT", f"/projects/{pid}", {"project": p}, etag)
    _, etag = call("GET", f"/projects/{pid}")
    _, etag = call("PUT", f"/projects/{pid}/boards/{BOARD}", {"name": "第一章　茶", "nodes": nodes, "edges": edges,
                                                              "summary": "第一章：劇本組卡（CG 走 jsDelivr）"}, etag)
    back, _ = call("GET", f"/projects/{pid}/boards/{BOARD}")
    b = back.get("board", back)
    print("回讀：卡", len(b.get("nodes", [])), "／", len(nodes), "　線", len(b.get("edges", [])), "／", len(edges))
    assert len(b.get("nodes", [])) == len(nodes) and len(b.get("edges", [])) == len(edges), "回讀數字對不上"
    pv, _ = call("GET", f"/projects/{pid}/preview?boardId={BOARD}&hours=168")
    print("預覽（私人，7 天）：", pv.get("playUrl") or pv.get("url"))

if __name__ == "__main__":
    segs = segments((ROOT / "劇本/第一章.md").read_text(encoding="utf-8"))
    nodes, edges, cgs = build(segs)
    check(nodes, edges)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist/board_ch1.json").write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1))
    lines = sum(len(n["data"].get("dialogueLines", [])) or 1 for n in nodes)
    print(f"卡 {len(nodes)}、線 {len(edges)}、句 {lines}、CG {cgs}")
    if "--push" in sys.argv: push(nodes, edges, cgs)
