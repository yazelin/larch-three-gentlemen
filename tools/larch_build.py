# 把劇本組成 Larch 白板並推上私人專案（不上架）。
#   python3 tools/larch_build.py             # 只組卡、印統計、寫 dist/board_ch1.json
#   python3 tools/larch_build.py --push      # 推上 Larch（第一次建專案，id 存在 larch_project.json）
#   CH=2 python3 tools/larch_build.py --push # 第二章：只換 board-ch2，其他章的白板原封不動；上一章結尾自動接一張跳章卡
# 圖走 jsDelivr（repo 公開、檔名 ASCII），不上傳 Larch 媒體庫。立繪、BGM、配音之後再補。
import json, time, re, sys, pathlib, subprocess, urllib.request, urllib.error, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://larch.ink/api/agent"
STATE = ROOT / "larch_project.json"
SHA = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
CDN = f"https://cdn.jsdelivr.net/gh/yazelin/larch-three-gentlemen@{SHA}/"
sys.path.insert(0, str(ROOT / "tools")); import chapter as C
BOARD = C.BOARD
NAME = "夜後明月．晨前朝霞．慕詩客"

import assets as _assets
_ST = {}
def A(path):   # 素材網址：走各章的孤兒 tag（tools/assets.py），圖自動換成 WebP。repo 整包超過 jsDelivr 50 MB，不能再用 CDN + 路徑
    if not _ST: _ST.update(_assets.tags())
    return _assets.url(path, _ST)
def cg_url(cid): return A(C.paper_rel(cid))   # 遊戲用疊了全畫面紙紋的版本（tools/paper.py）
sys.path.insert(0, str(ROOT / "art/cg"))
VARIANTS = set()   # 表情差分不進 CG 收藏（各章分鏡表裡 kind 是 var 的）
for _n in range(1, 10):
    try: VARIANTS |= {k for k, v in C.shots(_n).S.items() if v["kind"] == "var"}
    except ImportError: pass
BGM = {"枷鎖與選擇": "chains_and_choice", "夜的書桌": "night_desk", "工作室": "studio_day", "耳機裡的歌": "chains_muffled",
       "明天一定寫": "ch2/tomorrow_i_write", "合唱團": "ch5/concert_hymn", "詩的合唱": "ch5/last_note", "茶葉": "ch6/tea_leaves_soft"}   # 第二章起的曲子放 art/bgm/ch2/，自成 bgm-ch2 組   # 劇本裡的曲名 → art/bgm/ 檔名（ASCII）
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
    body = md.split("## CG 清單")[0].split("## 取材對照")[0].split("## 歌詞草稿")[0]   # 製作用的表格不進遊戲
    first = re.search(r"【CG ([^｜\s】]+)", body)
    segs, title, lines, cgs, mode, last_desk, pend_bg = [], "", [], [], None, cg_url(first[1] if first and C.CH > 1 else "01-1"), None
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
        m = re.match(r"【小遊戲 ([^】（]+?)(?:（([^】）]*)）[^】]*)?】", l)
        if m:
            name = f"{m[1]}（{m[2]}）" if f"{m[1]}（{m[2]}）" in MINI else m[1]   # 同一個網頁的另一種玩法（第七章打了又刪＝只能刪）
            if name not in MINI or not (ROOT / f"art/ui/minigame_{MINI[name][0]}.html").exists():   # ponytail: 小遊戲網頁還沒做好就先略過，劇情照走
                print("  小遊戲還沒接上，先略過：", name); continue
            close(); segs.append(("mini", name, {"第一次": "bug", "第二次": "fixed", "第七章": "erase"}.get(m[2] or "", "fixed"), [])); mode = None; continue
        m = re.match(r"【音效 (\w+)】", l)
        if m: pend["sfxUrl"] = f"/sfx/{m[1]}.mp3"; continue
        m = re.match(r"【CG ([^｜\s】]+)(?:｜運鏡 (\S+?))?(?:｜.*)?】", l)
        if m:
            cid = m[1]
            if not (ROOT / C.cg_rel(cid)).exists():   # ponytail: 圖還沒好就沿用上一張，補圖後重建即可
                print("  缺圖，暫用上一張：", cid); continue
            cgs.append(cid); pend_bg = cg_url(cid)
            if m[2] and m[2] != "定": pend["video"] = f"{cid}|{m[2]}"
            if cid != "01-5": last_desk = pend_bg
            continue
        m = re.match(r"【背景 (\w+)", l)
        if m: pend_bg = cg_url("01-5") if m[1] == "studio" else last_desk; continue
        m = re.match(r"₩(.+?)（([CMS])＋1）", l) or re.match(r"₩(.+?)（進入〈(.+?)〉）", l) or re.match(r"₩(.+)()", l)   # 沒寫（X＋1）的是純選擇：分支照出現順序對應，不加好感
        if m:
            m = [m[0], m[1], ROUTE.get(m[2], m[2])]   # 第七章好感三角：（進入〈線名〉）→ ch7Route 的值
            close()
            if segs and segs[-1][0] == "mini" and MINI[segs[-1][1]][4]: segs[-1][3].append(m[2]); continue   # 分歧小遊戲後面的 ₩ 只是說明
            if segs and segs[-1][0] == "choice": segs[-1][1].append((m[1].strip(), m[2] or None))
            else: segs.append(("choice", [(m[1].strip(), m[2] or None)]))
            continue
        if re.fullmatch(r"（[CMS]）", l): close(); mode = l[1]; continue
        if re.fullmatch(r"（[^）完]{1,10}）", l) and l != "（共通）": close(); mode = l[1:-1]; continue   # 純選擇的分支標籤
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

# 劇本裡的小遊戲名 → (art/ui/minigame_<檔>.html, 卡片說明, 讀的變數, 寫的變數, 分歧變數)
# 分歧變數不是 None 的：小遊戲卡直接接條件邊到後面的（C）（M）（S）分支，劇本裡跟在後面的 ₩ 只是分支的說明，不再做成選擇卡，也不再加好感（HTML 自己加）
AFF = ["affC", "affM", "affS"]
MINI = {"拉線": ("link", "親手拉出第一條線。", [], [], None), "敲鎖": ("challenge", "敲三下中央的鎖報名。", [], [], None),
        "打了又刪": ("message", "打了又刪，留下一句送出去。", AFF, AFF + ["ch2Msg"], "ch2Msg"),
        "猜硬幣": ("coin", "猜正面還是反面。", [], [], None), "塗地圖": ("paint", "把最後幾格塗完。", [], [], None),
        "找不同": ("diff", "找出地圖跑掉的地方。", [], ["ch4DiffSec"], None), "最後一個音": ("note", "替曲子選最後一個音。", ["affS"], ["affS", "ch5Note"], None),
        "擦紅茶": ("wipe", "把打翻的紅茶擦乾。", [], [], None), "好感三角": ("triangle", "這個夢，想先跟誰講。", AFF, ["ch7Route"], "ch7Route"),
        "打了又刪（第七章）": ("message", "打了一句，又一個字一個字刪掉。", [], [], None)}
ROUTE = {"兩個月": "C", "替代方案": "M", "聖歌": "S", "我全都要": "ALL"}   # 個人線與夥伴結局 → 好感三角寫回的 ch7Route

def segs_first_bg(segs):
    for s in segs:
        for ln in (s[2] if s[0] in ("card", "branch") else []):
            if ln.get("background"): return ln["background"]
    return cg_url("01-1")

# ---------- 第二步：段落 → 卡片與連線 ----------
def build(segs, ch=None):
    ch = ch or f"ch{C.CH}"
    nodes, edges, cg_order = [], [], []
    bg = [segs_first_bg(segs)]
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
    x, prev, tails, choice, keys, cond = 0, [], [], None, [], None
    for s in segs:
        bg_before = bg[0]
        if s[0] == "card":
            x += 400; nid = dialogue(s[1], s[2], s[3], x, 0, s[4])
            for p in prev: link(p, nid)
            prev = [nid]
            if tails: prev = [nid]; tails = []
        elif s[0] == "mini":
            x += 400; n = base("小遊戲", x, 0)
            fn, txt, rv, wv, bv = MINI[s[1]]
            html = (ROOT / f"art/ui/minigame_{fn}.html").read_text(encoding="utf-8").replace("{{MODE}}", s[2])
            html = re.sub(r"\{\{ASSET:([^}]+)\}\}", lambda m: A(m[1]), html)
            # showTitle False：不然畫面下緣會有一條「小遊戲：拉線」的標題列，很出戲
            n["data"] = {"type": "miniGame", "title": f"小遊戲：{s[1]}", "text": txt, "miniGameHtml": html,
                         "miniGamePresentation": "fullscreen", "miniGameSkippable": not bv, "miniGameReadVars": rv, "miniGameWriteVars": wv,
                         "miniGameAutoContinue": True, "miniGameFrame": {"showButton": False, "showTitle": False}, "background": bg[0], "voiceMode": "off", "stage": {"actors": []}}
            nodes.append(n)
            for p_ in prev: link(p_, n["id"])
            prev = [n["id"]]
            if bv: choice, keys, prev, bx, cond = n["id"], list(s[3]), [], x, bv   # 後面的分支接條件邊
        elif s[0] == "choice":
            x += 400; plain = all(k is None for _, k in s[1]); ttl = "怎麼回" if plain else "先問誰"
            n = base(ttl, x, 0)
            n["data"] = {"type": "choice", "title": ttl, "text": "怎麼回？" if plain else "先問誰的意見？", "choices": [t for t, _ in s[1]],
                         "choiceMode": "branch", "choicePlacement": "center", "choiceConditions": [None] * len(s[1]),
                         "choiceLinks": [None] * len(s[1]), "background": bg[0], "stage": {"actors": []}, "characterLayers": []}
            nodes.append(n)
            for p in prev: link(p, n["id"])
            choice, keys, prev, bx, cond = n["id"], [k for _, k in s[1]], [], x, None
        elif s[0] == "branch":
            k, lines = s[1], list(s[2])
            if k not in keys: keys[keys.index(None)] = k   # 純選擇：分支標籤照出現順序填進空位
            i = keys.index(k); y = (i - 1) * 300
            bid = dialogue(f"選 {k}", lines, s[3], bx + 400, y, s[4])   # 分支最後一句留在對話卡：以前搬進好感卡當文字，顯示成黑底字
            if cond:   # 分歧小遊戲：同一個出口多條條件邊（整張白板 PUT 保得住，POST /nodes 會丟掉條件）
                edges.append({"id": f"e-{choice}-{bid}", "source": choice, "target": bid, "sourceHandle": "right",
                              "data": {"condition": {"kind": "variable", "variable": cond, "op": "eq", "value": k}}})
                if i == 0: edges.append({"id": f"e-{choice}-{bid}-default", "source": choice, "target": bid, "sourceHandle": "right"})   # 保險：變數沒寫回時走第一條，不會卡死
                prev.append(bid); x = bx + 400; continue
            link(choice, bid, f"choice-{i}")
            if k not in "CMS": prev.append(bid); x = bx + 400; continue   # 純選擇不加好感
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
              "cgGalleryItems": [{"url": cg_url(c), "title": f"CG {c}", "locked": True} for c in gallery_cgs(cgs) if c not in VARIANTS]})
    # 對話框外框透明滿版：露出 art/ui/dialogue.html 自己的夜色漸層（這個欄位 PATCH 不收，只能隨整包 PUT 寫）
    s["dialogueUi"] = {"preset": "custom", "fontSize": 22, "textColor": "#f4eee6", "fontFamily": "iansui", "panelColor": "#05070f", "panelWidth": 100,
                       "accentColor": "#e9cf9a", "borderColor": "#05070f", "panelOffset": 0, "backdropBlur": 0, "borderRadius": 0, "nameFontSize": 17,
                       "panelOpacity": 0, "panelPadding": 0, "presentation": "gradient", "speakerColor": "#e9cf9a", "textOverflow": "grow"}
    s["titleScreen"] = {**(s.get("titleScreen") or {}), "bgm": A("art/bgm/main_theme.mp3"), "bgmVolume": 0.45, "bgmLoop": True}
    p["variables"] = [{"id": f"aff{k}", "name": f"aff{k}", "type": "number", "label": f"{k} 好感", "defaultValue": 0} for k in "CMS"]
    p["languages"] = p.get("languages") or [{"code": "zh-Hant", "label": "繁體中文", "voiceMode": "off"}]
    if C.CH == 1: nodes[0]["data"]["start"] = True
    # 白板：別章原封不動帶回去（整包 PUT 會用這份陣列取代全部白板），自己那張先放空殼，下面再單獨推
    before = {b["id"]: len(b.get("nodes", [])) for b in p.get("boards", []) if b["id"] != BOARD}
    others = [b for b in p.get("boards", []) if b["id"] != BOARD]
    p["boards"] = sorted(others + [{"id": BOARD, "kind": "story", "mode": "story", "name": C.board_name(), "description": "", "nodes": [], "edges": []}], key=lambda b: b["id"])
    _, etag = call("PUT", f"/projects/{pid}", {"project": p}, etag)
    _, etag = call("GET", f"/projects/{pid}")
    _, etag = call("PUT", f"/projects/{pid}/boards/{BOARD}", {"name": C.board_name(), "nodes": nodes, "edges": edges,
                                                              "summary": f"{C.board_name()}：劇本組卡（CG 走 jsDelivr）"}, etag)
    back, _ = call("GET", f"/projects/{pid}/boards/{BOARD}")
    b = back.get("board", back)
    print("回讀：卡", len(b.get("nodes", [])), "／", len(nodes), "　線", len(b.get("edges", [])), "／", len(edges))
    assert len(b.get("nodes", [])) == len(nodes) and len(b.get("edges", [])) == len(edges), "回讀數字對不上"
    for oid, n in before.items():
        ob, _ = call("GET", f"/projects/{pid}/boards/{oid}")
        got = len(ob.get("board", ob).get("nodes", []))
        print(f"  別章 {oid}：卡 {got} ／ 推之前 {n}")
        assert got == n, f"{oid} 被動到了"
    st = json.loads(STATE.read_text()); st["pushed"] = sorted(set(st.get("pushed", []) + [BOARD])); STATE.write_text(json.dumps(st, ensure_ascii=False, indent=1))
    pv, _ = call("GET", f"/projects/{pid}/preview?boardId={BOARD}&hours=168")
    print("預覽（私人，7 天）：", pv.get("playUrl") or pv.get("url"))

def gallery_cgs(cgs):
    """CG 收藏照章節順序收全部章（各章 build 時寫進 dist/board_chN.json 的 cgs）。"""
    out = []
    for n in range(1, 10):
        f = ROOT / f"dist/board_ch{n}.json"
        got = cgs if n == C.CH else (json.loads(f.read_text()).get("cgs", []) if f.exists() else [])
        out += [c for c in got if c not in out]
    return out

def jump_to_next(nodes, edges):
    """下一章的白板已經組過（dist 有檔）就在章末接一張跳章卡。"""
    nxt = ROOT / f"dist/board_ch{C.CH + 1}.json"
    pushed = json.loads(STATE.read_text()).get("pushed", []) if STATE.exists() else []
    if not nxt.exists() or f"board-ch{C.CH + 1}" not in pushed: return   # 下一章還沒推上去就不接，免得跳到不存在的白板
    tgt = json.loads(nxt.read_text())["nodes"][0]["id"]
    last = nodes[-1]
    j = {"id": f"ch{C.CH}-jump", "type": "story", "position": {"x": last["position"]["x"] + 400, "y": 0},
         "data": {"type": "boardJump", "title": f"接{C.board_name(C.CH + 1)}", "text": "", "jumpBoardId": f"board-ch{C.CH + 1}", "jumpNodeId": tgt,
                  "chapterEnd": True, "background": last["data"].get("background"), "stage": {"actors": []}, "characterLayers": []}}
    nodes.append(j); edges.append({"id": f"e-{last['id']}-{j['id']}", "source": last["id"], "target": j["id"]})

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
    segs = segments(C.SCRIPT.read_text(encoding="utf-8"))
    if "--sample" in sys.argv:   # 只組某一節，推到樣片白板：--sample 五
        sec = sys.argv[sys.argv.index("--sample") + 1]
        segs = [x for x in segs if x[0] == "card" and x[1].startswith(sec + "、")]
        BOARD = f"board-sample-{'一二三四五六七'.index(sec) + 1}"   # 白板代號只能 ASCII
    nodes, edges, cgs = build(segs)
    if "--sample" not in sys.argv: jump_to_next(nodes, edges)
    check(nodes, edges)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / f"dist/board_ch{C.CH}.json").write_text(json.dumps({"nodes": nodes, "edges": edges, "cgs": cgs}, ensure_ascii=False, indent=1))
    lines = sum(len(n["data"].get("dialogueLines", [])) or 1 for n in nodes)
    print(f"卡 {len(nodes)}、線 {len(edges)}、句 {lines}、CG {cgs}")
    if "--push" in sys.argv:
        warm(nodes)
        if "--sample" in sys.argv: push_board_only(nodes, edges, f"樣片：第{sec}節")
        else: push(nodes, edges, cgs)
