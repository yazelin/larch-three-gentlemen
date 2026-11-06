# 把劇本組成 Larch 白板並推上私人專案（不上架）。
#   python3 tools/larch_build.py             # 只組卡、印統計、寫 dist/board_ch1.json
#   python3 tools/larch_build.py --push      # 推上 Larch（第一次建專案，id 存在 larch_project.json）
# 圖走 jsDelivr（repo 公開、檔名 ASCII），不上傳 Larch 媒體庫。立繪、BGM、配音之後再補。
import json, time, re, sys, pathlib, subprocess, urllib.request, urllib.error, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://larch.ink/api/agent"
STATE = ROOT / "larch_project.json"
SHA = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
CDN = f"https://cdn.jsdelivr.net/gh/yazelin/larch-three-gentlemen@{SHA}/"
BOARD = "board-ch1"
NAME = "夜後明月．晨前朝霞．慕詩客"

import assets as _assets
_ST = {}
def A(path):   # 素材網址：走各章的孤兒 tag（tools/assets.py），圖自動換成 WebP。repo 整包超過 jsDelivr 50 MB，不能再用 CDN + 路徑
    if not _ST: _ST.update(_assets.tags())
    return _assets.url(path, _ST)
def cg_url(cid): return A(f"art/cg_paper/{cid}.jpg")   # 遊戲用疊了全畫面紙紋的版本（tools/paper.py）
sys.path.insert(0, str(ROOT / "art/cg"))
try:
    from ch1_shots import S as _SHOTS
    VARIANTS = {k for k, v in _SHOTS.items() if v["kind"] == "var"}   # 表情差分不進 CG 收藏
except ImportError:
    VARIANTS = set()
BGM = {"枷鎖與選擇": "chains_and_choice", "夜的書桌": "night_desk", "工作室": "studio_day", "耳機裡的歌": "chains_muffled"}   # 劇本裡的曲名 → art/bgm/ 檔名（ASCII）
VIDEOS = ROOT / "art/video/media.json"     # "cg|運鏡" → {mediaId, url}，tools/motion.py 產生
_VFU = {}
def _video_files():
    # 媒體庫裡每支影片都有直接的 mp4（videoFileUrl）。只給 Stream 的 iframe 網址時，播放器用 Stream 內嵌框播，fit 管不到，寬螢幕會左右黑邊
    if not _VFU:
        p, _ = call("GET", f"/projects/{json.loads(STATE.read_text())['id']}")
        _VFU.update({x["id"]: x["videoFileUrl"] for x in p.get("project", p).get("media", []) if x.get("videoFileUrl")})
    return _VFU
def video_layer(key):
    m = json.loads(VIDEOS.read_text()) if VIDEOS.exists() else {}
    if key not in m: raise SystemExit(f"缺運鏡影片 {key}，先跑 tools/motion.py")
    vf = _video_files().get(m[key]["mediaId"])
    if not vf: raise SystemExit(f"媒體庫找不到 {key} 的 mp4（videoFileUrl）")
    return {"id": "v-" + key.replace("|", "-"), "mediaId": m[key]["mediaId"], "url": m[key]["url"], "videoFileUrl": vf,
            "fill": True, "fit": "cover", "videoLoop": False, "volume": 0}

# ---------- 第一步：劇本 → 段落 ----------
def segments(md):
    """[('card', title, lines, cgs) | ('choice', [(text, key)]) | ('branch', key, lines, cgs)]；每句 line 可帶 background。"""
    body = md.split("## CG 清單")[0]
    segs, title, lines, cgs, mode, last_desk, pend_bg = [], "", [], [], None, cg_url("01-1"), None
    pend, opts = {}, {}   # pend：下一句要帶的 video/bgm/sfx；opts：這張卡的轉場與自動前進
    def close():
        nonlocal lines, cgs, opts
        if lines:
            segs.append(("branch", mode, lines, cgs, opts) if mode else ("card", title, lines, cgs, opts))
            opts = {}
        lines, cgs = [], []
    def add(sp, tx, emo):
        nonlocal pend_bg, pend
        ln = {"id": f"l{len(lines)}", "speaker": sp, "text": tx, "emotion": emo}
        if pend_bg: ln["background"], pend_bg = pend_bg, None
        ln.update(pend); pend = {}
        lines.append(ln)
    for raw in body.splitlines():
        l = raw.strip()
        if not l or l.startswith((">", "---", "# ", "【立繪")): continue
        if l.startswith("## "): close(); title = l[3:]; continue
        m = re.match(r"【轉場 (\w+)(?: (\d+))?】", l)
        if m: close(); opts = {"transition": m[1], "transitionMs": int(m[2] or 600)}; continue
        m = re.match(r"【自動 ([\d.]+)】", l)
        if m: opts["autoAdvance"] = {"enabled": True, "mode": "delay", "delayMs": int(float(m[1]) * 1000), "uninterruptible": True}; continue
        m = re.match(r"【BGM (.+?)】", l)
        if m:
            pend["bgmAction" if m[1] in ("停", "淡出") else "bgm"] = {"停": "stop", "淡出": "fadeOut"}.get(m[1]) or A(f"art/bgm/{BGM[m[1]]}.mp3")
            continue
        m = re.match(r"【小遊戲 (\S+?)】", l)
        if m: close(); segs.append(("mini", m[1])); continue
        m = re.match(r"【音效 (\w+)】", l)
        if m: pend["sfxUrl"] = f"/sfx/{m[1]}.mp3"; continue
        m = re.match(r"【CG ([^｜\s】]+)(?:｜運鏡 (\S+?))?(?:｜.*)?】", l)
        if m:
            cid = m[1]
            if not (ROOT / f"art/cg/{cid}.jpg").exists():   # ponytail: 圖還沒好就沿用上一張，補圖後重建即可
                print("  缺圖，暫用上一張：", cid); continue
            cgs.append(cid); pend_bg = cg_url(cid)
            if m[2] and m[2] != "定": pend["video"] = f"{cid}|{m[2]}"
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
        if l.startswith("〔"): add("旁白", l.strip("〔〕") or "……", "描述動作"); continue
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
    def dialogue(title, lines, cgs, x, y, opts=None):
        n = base(title, x, y)
        lines = [dict(ln) for ln in lines]
        for ln in lines:
            v = ln.pop("video", None)
            ln["stage"] = {"actors": [], "videos": [video_layer(v)] if v else []}
            if v: ln["background"] = A(json.loads(VIDEOS.read_text())[v]["end"])   # 影片播完停在最後一格
            if ln.get("background"): bg[0] = ln["background"]
        first_bg = lines[0].get("background") or bg_before
        d = {"type": "dialogue", "title": title, "speaker": lines[0]["speaker"], "text": lines[0]["text"],
             "emotion": lines[0]["emotion"], "dialogueLines": lines, "background": first_bg,
             "stage": lines[0]["stage"], "characterLayers": [], "transition": "fade", "transitionMs": 360, "voiceMode": "off"}
        for k in ("bgm", "bgmAction", "sfxUrl"):
            if lines[0].get(k): d[k] = lines[0][k]
        d.update(opts or {})
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
            x += 400; nid = dialogue(s[1], s[2], s[3], x, 0, s[4])
            for p in prev: link(p, nid)
            prev = [nid]
            if tails: prev = [nid]; tails = []
        elif s[0] == "mini":
            x += 400; n = base("小遊戲", x, 0)
            fn, txt = {"拉線": ("link", "親手拉出第一條線。"), "敲鎖": ("challenge", "敲三下中央的鎖報名。")}[s[1]]
            html = (ROOT / f"art/ui/minigame_{fn}.html").read_text(encoding="utf-8")
            html = re.sub(r"\{\{ASSET:([^}]+)\}\}", lambda m: A(m[1]), html)
            # showTitle False：不然畫面下緣會有一條「小遊戲：拉線」的標題列，很出戲
            n["data"] = {"type": "miniGame", "title": f"小遊戲：{s[1]}", "text": txt, "miniGameHtml": html,
                         "miniGamePresentation": "fullscreen", "miniGameSkippable": True, "miniGameReadVars": [], "miniGameWriteVars": [],
                         "miniGameAutoContinue": True, "miniGameFrame": {"showButton": False, "showTitle": False}, "background": bg[0], "voiceMode": "off", "stage": {"actors": []}}
            nodes.append(n)
            for p_ in prev: link(p_, n["id"])
            prev = [n["id"]]
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
            bid = dialogue(f"選 {k}", lines, s[3], bx + 400, y, s[4])   # 分支最後一句留在對話卡：以前搬進好感卡當文字，顯示成黑底字
            link(choice, bid, f"choice-{i}")
            sv = base(f"{k} 好感 +1", bx + 800, y)
            sv["data"] = {"type": "setVariable", "title": f"{k} 好感 +1", "text": "",
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
    empty = [n["id"] for n in nodes if n["data"]["type"] == "dialogue" and not str(n["data"].get("text", "")).strip()]
    nobg = [n["id"] for n in nodes if not n["data"].get("background")]
    assert not (bad or orphans or dead or empty or nobg), dict(bad=bad, orphans=orphans, dead=dead, empty=empty, nobg=nobg)

def warm(nodes):
    """推之前把用到的 jsDelivr 網址全部打一次：新版本第一次被抓時偶爾回 403，之後就一直失敗（2026-11-06 敲鎖小遊戲的鎖圖就是這樣不見的）。"""
    import re, urllib.request, concurrent.futures as cf
    urls = sorted(set(re.findall(r"https://cdn\.jsdelivr\.net/gh/[A-Za-z0-9@._/~%-]+\.[A-Za-z0-9]+", json.dumps(nodes, ensure_ascii=False))))
    def get(u):
        for k in range(6):
            try:
                with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                    if r.status == 200: r.read(1); return None
            except Exception: pass
            if k == 1:   # 失敗會被 jsDelivr 快取住，清掉再抓
                try: urllib.request.urlopen(u.replace("://cdn.jsdelivr.net/", "://purge.jsdelivr.net/"), timeout=60).read()
                except Exception: pass
            time.sleep(8)
        return u
    with cf.ThreadPoolExecutor(8) as ex: bad = [u for u in ex.map(get, urls) if u]
    if bad: raise SystemExit("CDN 讀不到，先不推：\n" + "\n".join(bad))
    print("CDN 都讀得到：", len(urls), "個網址")

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
    p["name"] = NAME
    s = p.setdefault("settings", {})
    s.update({"arrowKeyBack": True, "arrowKeyNext": True, "stageFit": "cover",   # 3:2 的 CG 填滿 16:9 螢幕，左右不留黑邊
              "keepActorsInFrame": False, "textSpeed": 55, "returnToTitleOnEnd": True,
              "titleScreenEnabled": True, "titleCoverImage": A("art/cg_paper/title_kv.jpg"), "projectThumbnail": A("art/cg_paper/title_kv.jpg"),
              "cgGalleryEnabled": True, "cgGallerySource": "picked",
              "cgGalleryItems": [{"url": cg_url(c), "title": f"CG {c}", "locked": True} for c in cgs if c not in VARIANTS]})
    # 對話框外框透明滿版：露出 art/ui/dialogue.html 自己的夜色漸層（這個欄位 PATCH 不收，只能隨整包 PUT 寫）
    s["dialogueUi"] = {"preset": "custom", "fontSize": 22, "textColor": "#f4eee6", "fontFamily": "iansui", "panelColor": "#05070f", "panelWidth": 100,
                       "accentColor": "#e9cf9a", "borderColor": "#05070f", "panelOffset": 0, "backdropBlur": 0, "borderRadius": 0, "nameFontSize": 17,
                       "panelOpacity": 0, "panelPadding": 0, "presentation": "gradient", "speakerColor": "#e9cf9a", "textOverflow": "grow"}
    s["titleScreen"] = {**(s.get("titleScreen") or {}), "bgm": A("art/bgm/main_theme.mp3"), "bgmVolume": 0.45, "bgmLoop": True}
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

def push_board_only(nodes, edges, name):
    """只推一塊白板，不動專案設定與其他白板（樣片用）。"""
    pid = json.loads(STATE.read_text())["id"]
    nodes[0]["data"]["start"] = True
    _, etag = call("GET", f"/projects/{pid}")
    _, etag = call("PUT", f"/projects/{pid}/boards/{BOARD}", {"name": name, "nodes": nodes, "edges": edges}, etag)
    back, _ = call("GET", f"/projects/{pid}/boards/{BOARD}")
    b = back.get("board", back)
    print("回讀：卡", len(b.get("nodes", [])), "／", len(nodes))
    assert len(b.get("nodes", [])) == len(nodes)
    pv, _ = call("GET", f"/projects/{pid}/preview?boardId={BOARD}&hours=168")
    print("預覽（私人，7 天）：", pv.get("playUrl") or pv.get("url"))

if __name__ == "__main__":
    segs = segments((ROOT / "劇本/第一章.md").read_text(encoding="utf-8"))
    if "--sample" in sys.argv:   # 只組某一節，推到樣片白板：--sample 五
        sec = sys.argv[sys.argv.index("--sample") + 1]
        segs = [x for x in segs if x[0] == "card" and x[1].startswith(sec + "、")]
        BOARD = f"board-sample-{'一二三四五六七'.index(sec) + 1}"   # 白板代號只能 ASCII
    nodes, edges, cgs = build(segs)
    check(nodes, edges)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist/board_ch1.json").write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1))
    lines = sum(len(n["data"].get("dialogueLines", [])) or 1 for n in nodes)
    print(f"卡 {len(nodes)}、線 {len(edges)}、句 {lines}、CG {cgs}")
    if "--push" in sys.argv:
        warm(nodes)
        if "--sample" in sys.argv: push_board_only(nodes, edges, f"樣片：第{sec}節")
        else: push(nodes, edges, cgs)
