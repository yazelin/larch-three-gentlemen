# 產生公開站 docs/：python3 tools/build_site.py [逐字稿字幕.srt]
# 來源：canon/cast.json、設計.md 的角色表、劇本/*.md（含檔尾取材對照表）。站上的字都從這裡來，不手抄。
import json, re, sys, html, shutil, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"; IMG = DOCS / "img"
REPO = "https://github.com/yazelin/larch-three-gentlemen"
LIVE = "https://ai-workshop-backend.yazelinj303.workers.dev/live/lesson?id=1104"
WORK = "https://zuihoudeshengzhan.larch.games"
SRT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
e = html.escape

# 逐字稿第 N 行 = 字幕第 N 段（2026-11-05 核對過，2903 行對 2903 段）
cue = {}
if SRT and SRT.exists():
    for m in re.finditer(r"(\d+)\n(\d\d):(\d\d):(\d\d),\d+ -->", SRT.read_text(encoding="utf-8")):
        h, mi, s = int(m[2]), int(m[3]), int(m[4]); cue[int(m[1])] = h * 3600 + mi * 60 + s

def ts(sec):
    h, r = divmod(sec, 3600); m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def link_sources(text):
    """取材欄位：逐字稿行號換成錄影時間；repo 內的路徑換成 GitHub 連結。"""
    text = e(text)
    text = re.sub(r"`(sources/[^`]+)`", lambda m: f'<a href="{REPO}/blob/main/{m[1]}">{m[1].split("/")[-1]}</a>', text)
    def lines(m):
        out = []
        for part in re.split(r"、", m[2]):
            n = re.match(r"\s*(\d+)", part)
            if n and cue.get(int(n[1])) is not None:
                out.append(f'<a href="{LIVE}">錄影 {ts(cue[int(n[1])])}</a>')
            else:
                out.append(part)
        return "、".join(out)
    return re.sub(r"(逐字稿|直播)\s*([\d–\-、 ]+\d)", lines, text)

def kind(src, adapt):
    if src.strip() == "無": return "原創"
    if adapt.strip() == "無": return "真實"
    return "改編"

def img(src, dst, w):
    p = IMG / dst
    if not p.exists():
        im = Image.open(ROOT / src).convert("RGB"); im.thumbnail((w, w)); im.save(p, "JPEG", quality=82)
    return f"img/{dst}"

# ---------- 讀來源 ----------
cast = json.loads((ROOT / "canon/cast.json").read_text(encoding="utf-8"))
design = (ROOT / "設計.md").read_text(encoding="utf-8")
roles = {}
for row in design.splitlines():
    m = re.match(r"\| (茶語|C 先生|M 先生|S 先生)[^|]*\| ([^|]+)\| ([^|]+)\| ([^|]+)\|", row)
    if m and m[1] not in roles: roles[m[1]] = {"title": m[2].strip(), "does": m[3].strip(), "who": m[4].strip()}

chapters = []
for f in sorted((ROOT / "劇本").glob("第*章.md")):
    t = f.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", t, re.M)[1]
    body = t.split("## CG 清單")[0]
    table = []
    if "## 取材對照" in t:
        for row in t.split("## 取材對照")[1].splitlines():
            c = [x.strip() for x in row.strip().strip("|").split("|")]
            if len(c) == 3 and c[0] not in ("段落", "---") and not set(c[0]) <= {"-"}:
                table.append(c)
    chapters.append({"slug": f"ch{len(chapters)+1}", "title": title, "body": body, "table": table})

# ---------- 共用版面 ----------
CSS = """
:root{--paper:#f7f2ea;--paper-2:#efe7da;--ink:#3b3440;--ink-2:#6d6372;--line:#ddd2c2;
--plum:#7a5a86;--wine:#9b4a5e;--sage:#6f8a6a;--navy:#3f4a6e;
--f-display:"LXGW WenKai TC","Kaiti TC",serif;--f-body:"Noto Serif TC","Songti TC",serif;--f-ui:"Noto Sans TC","PingFang TC",sans-serif}
*{box-sizing:border-box}
html{background:var(--paper)}
body{margin:0;color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.9;
background:radial-gradient(ellipse 60% 40% at 12% 8%,rgb(122 90 134/.10),transparent 70%),
radial-gradient(ellipse 50% 35% at 92% 30%,rgb(155 74 94/.08),transparent 70%),
radial-gradient(ellipse 55% 40% at 30% 92%,rgb(111 138 106/.10),transparent 70%),var(--paper);min-height:100vh}
a{color:var(--wine)}
.wrap{max-width:980px;margin:0 auto;padding-block:0 64px;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
.top{display:flex;gap:18px;flex-wrap:wrap;align-items:center;padding:18px 0;font-family:var(--f-ui);font-size:14px}
.top b{font-family:var(--f-display);font-size:19px;font-weight:700;margin-right:auto}
.top a{color:var(--ink-2);text-decoration:none}.top a:hover{color:var(--wine)}
h1,h2,h3{font-family:var(--f-display);font-weight:700;line-height:1.35;text-wrap:balance}
h2{font-size:28px;margin:56px 0 14px}
.hero{position:relative;border-radius:6px;overflow:hidden;margin-top:4px}
.hero img{display:block;width:100%;height:auto;-webkit-mask-image:radial-gradient(ellipse 95% 90% at 50% 45%,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 95% 90% at 50% 45%,#000 70%,transparent 100%)}
.hero-copy{text-align:center;margin:-8px auto 0;max-width:640px}
.hero-copy h1{font-size:clamp(34px,6vw,56px);margin:10px 0 4px;letter-spacing:.06em}
.hero-copy .q{font-family:var(--f-display);font-size:20px;color:var(--plum)}
.note{font-family:var(--f-ui);font-size:14.5px;line-height:1.8;color:var(--ink-2);background:rgb(255 255 255/.55);border:1px solid var(--line);border-radius:6px;padding:14px 18px;margin:22px 0}
.lede{max-width:40em}
.cast{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:22px}
.person{background:rgb(255 255 255/.5);border:1px solid var(--line);border-radius:6px;overflow:hidden}
.person img{display:block;width:100%;height:auto}
.person div{padding:12px 16px 16px}
.person h3{margin:0;font-size:22px}
.person .role{font-family:var(--f-ui);font-size:13px;letter-spacing:.1em;color:var(--ink-2)}
.person p{margin:6px 0 0;font-size:15.5px;line-height:1.8}
.person .from{font-family:var(--f-display);color:var(--plum);font-size:16px}
.poem{font-family:var(--f-display);font-size:20px;line-height:2;margin:18px 0;padding:14px 22px;border-left:3px solid var(--plum);background:rgb(255 255 255/.45)}
.poem b{color:var(--wine);font-weight:700}
.chlist{list-style:none;padding:0;margin:0;display:grid;gap:12px}
.chlist li{display:flex;flex-wrap:wrap;gap:6px 18px;align-items:baseline;border-bottom:1px dashed var(--line);padding:10px 0}
.chlist .t{font-family:var(--f-display);font-size:21px}
.chlist a{font-family:var(--f-ui);font-size:14px}
/* 閱讀 */
.read{max-width:38em;margin:0 auto}
.read h1{font-size:34px;text-align:center;margin:28px 0 8px}
.read h2{font-size:22px;margin:44px 0 10px;color:var(--plum)}
.read p{margin:0 0 10px}
.narr{color:var(--ink-2);font-size:16px}
.line b{font-family:var(--f-ui);font-size:14px;font-weight:700;margin-right:8px}
.line.C b{color:var(--sage)}.line.M b{color:var(--navy)}.line.S b{color:var(--wine)}.line.T b{color:var(--plum)}
.inner{color:var(--plum);font-style:italic}
.cg{margin:22px -6px}
.cg img{display:block;width:100%;height:auto;border-radius:4px}
.cg.todo{border:1px dashed var(--line);border-radius:6px;padding:16px;text-align:center;font-family:var(--f-ui);font-size:13.5px;color:var(--ink-2)}
.choice{border-left:3px solid var(--plum);padding:6px 0 6px 14px;margin:18px 0;font-family:var(--f-ui);font-size:15px}
.choice div{margin:3px 0}
.branch{font-family:var(--f-ui);font-size:13px;letter-spacing:.1em;color:var(--ink-2);margin:22px 0 6px}
.end{text-align:center;color:var(--ink-2);margin:36px 0}
/* 取材對照 */
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:640px;font-family:var(--f-ui);font-size:14.5px;line-height:1.7;background:rgb(255 255 255/.5)}
th,td{border:1px solid var(--line);padding:8px 10px;vertical-align:top;text-align:left}
th{background:var(--paper-2);font-weight:700}
.k{display:inline-block;padding:1px 8px;border-radius:99px;font-size:12.5px;white-space:nowrap;color:#fff}
.k.真實{background:var(--sage)}.k.改編{background:var(--plum)}.k.原創{background:var(--wine)}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-family:var(--f-ui);font-size:14px;margin:8px 0 16px}
footer{border-top:1px solid var(--line);margin-top:56px;padding-top:18px;font-family:var(--f-ui);font-size:13.5px;color:var(--ink-2)}
@media (max-width:600px){body{font-size:16px}h2{font-size:24px}}
"""
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC:wght@400;700&family=Noto+Serif+TC:wght@400;600&family=Noto+Sans+TC:wght@400;700&display=swap">'

def page(title, body, desc="", depth=0):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="https://yazelin.github.io/larch-three-gentlemen/img/hero.jpg">
{FONTS}<link rel="stylesheet" href="{up}style.css"></head><body><div class="wrap">
<nav class="top"><b>夜後明月，晨前朝霞</b><a href="{up}index.html">首頁</a><a href="{up}index.html#cast">角色</a><a href="{up}index.html#names">名字</a><a href="{up}{chapters[0]['slug']}.html">讀第一章</a><a href="{up}sources.html">取材對照</a></nav>
{body}
<footer><p>茶語是虛構角色。人設與製作經過取材自 Larch 創作者茶葉飲料，經她本人同意；她的作品《最後的聖戰》：<a href="{WORK}">{WORK}</a>。劇本、設定與圖採 CC BY-NC 4.0，程式採 MIT，詳見 <a href="{REPO}/blob/main/LICENSE.md">LICENSE</a>。</p>
<div class="title-footer"><a href="{REPO}" aria-label="GitHub" title="GitHub">GitHub</a> · <a href="https://www.facebook.com/yaze.lin.gm" aria-label="Facebook" title="Facebook">Facebook</a> · <a href="https://buymeacoffee.com/yazelin" aria-label="Buy Me a Coffee" title="Buy Me a Coffee">Buy Me a Coffee</a> · <a href="https://yazelin.github.io/" aria-label="亞澤的部落格" title="亞澤的部落格">部落格</a></div></footer>
</div></body></html>
"""

# ---------- 閱讀頁 ----------
SPK = {"茶語": "T", "C": "C", "M": "M", "S": "S"}
def render(body):
    out, choice = [], []
    def flush():
        if choice: out.append('<div class="choice">' + "".join(f"<div>{e(c)}</div>" for c in choice) + "</div>"); choice.clear()
    for raw in body.splitlines():
        l = raw.strip()
        if not l or l.startswith((">", "---", "【背景", "【立繪", "# ")): continue
        if l.startswith("₩"):
            choice.append(re.sub(r"（[CMS]＋1）", "", l[1:])); continue
        flush()
        if l.startswith("## "): out.append(f"<h2>{e(l[3:])}</h2>")
        elif l.startswith("【CG"):
            cid = re.match(r"【CG ([^｜\s】]+)", l)[1]; f = ROOT / f"art/cg/{cid}.jpg"
            if f.exists(): out.append(f'<figure class="cg"><img src="{img(f"art/cg/{cid}.jpg", f"cg-{cid}.jpg", 1600)}" alt="CG {cid}" loading="lazy"></figure>')
            else: out.append(f'<div class="cg todo">CG {e(cid)} 製作中</div>')
        elif l.startswith("〔"): out.append(f'<p class="narr">{e(l.strip("〔〕"))}</p>')
        elif re.match(r"（[CMS]）$|（共通）$", l): out.append(f'<div class="branch">{"選 " + l[1] + " 的話" if l[1] in "CMS" else "之後"}</div>')
        elif re.match(r"（第.+完）", l): out.append(f'<p class="end">{e(l)}</p>')
        else:
            m = re.match(r"([^：]{1,8})(（心聲）)?：(.*)", l)
            if m and m[2]: out.append(f'<p class="inner">{e(m[3])}</p>')
            elif m: out.append(f'<p class="line {SPK.get(m[1], "")}"><b>{e(m[1])}</b>{e(m[3])}</p>')
            else: out.append(f"<p>{e(l)}</p>")
    flush()
    return "\n".join(out)

# ---------- 輸出 ----------
if DOCS.exists(): shutil.rmtree(DOCS)
IMG.mkdir(parents=True)
(DOCS / "style.css").write_text(CSS, encoding="utf-8")
(DOCS / ".nojekyll").write_text("")
hero = img("canon/refs/style_anchor_full.jpg", "hero.jpg", 1800)

# 名字出自元稹〈一字至七字詩．茶〉（設計.md「三位先生的名字定案」）
people = [("茶語", "tea", "茶語", "創作者，大學生，住在高雄", ""),
          ("C 先生", "c", "晨", "C 先生", "晨前命對朝霞"),
          ("M 先生", "m", "明", "M 先生", "夜後邀陪明月"),
          ("S 先生", "s", "詩", "S 先生", "慕詩客")]
def card(n, k, name, sub, line):
    title = roles.get(n, {}).get("title", "")
    role = f"{sub}｜{title}" if line else sub
    src = f'<p class="from">名字出自「{e(line)}」</p>' if line else ""
    return f'''<article class="person"><img src="{img(f"canon/refs/{k}_full.jpg", f"{k}.jpg", 1200)}" alt="{e(name)}設定圖" loading="lazy"><div><h3>{e(name)}</h3><div class="role">{e(role)}</div>{src}<p>{e(roles.get(n, {}).get("who", ""))}</p></div></article>'''
cards = "".join(card(*p) for p in people)
POEM = """<h2 id="names">名字的由來</h2>
<p class="lede">三位先生原本只是 C、M、S，是工具本來的叫法。茶語後來讀到唐朝元稹的〈一字至七字詩．茶〉，這首詩的第一個字就是「茶」，她從詩裡替他們取了名字。</p>
<blockquote class="poem">茶。<br>香葉，嫩芽。<br><b>慕詩客</b>，愛僧家。<br>碾雕白玉，羅織紅紗。<br>銚煎黃蕊色，碗轉麴塵花。<br>夜後邀陪<b>明</b>月，<b>晨</b>前命對朝霞。<br>洗盡古今人不倦，將知醉後豈堪誇。</blockquote>
<p class="lede">作品名就是第六句「夜後邀陪明月，晨前命對朝霞」：入夜後是明陪著她，天亮前是晨陪著她。詩只有七句，從一個字長到七個字，共通線的七章就用這七句當章名。作歌的人，就是詩客。詩見《全唐詩》卷 423，個別字句在不同版本有出入。</p>"""
chl = "".join(f'<li><span class="t">{e(c["title"])}</span><a href="{c["slug"]}.html">線上閱讀</a><a href="sources.html#{c["slug"]}">這一章的取材</a></li>' for c in chapters)
index = f"""<div class="hero"><img src="{hero}" alt="茶語與三位先生第一次在工作室，桌上浮著三把發光的鎖"></div>
<div class="hero-copy"><h1>夜後明月，晨前朝霞</h1><p class="q">三位先生，都讓我心動</p></div>
<p class="lede">Larch 創作者挑戰「自由與限制」那三個禮拜，大學生茶語在高雄的書桌前，做一部聖騎士與信仰的 RPG。她的三個 AI 夥伴升級之後有了人形介面：畫圖的 C 先生、寫程式的 M 先生、做音樂的 S 先生。她想說一個好故事。他們知道一件她不知道的事。</p>
<div class="note">茶語是虛構角色。她的人設與製作經過取材自 Larch 創作者茶葉飲料（第三屆挑戰最佳作品《最後的聖戰》作者），經她本人同意。哪些情節是真的、哪些是改編，逐段寫在<a href="sources.html">取材對照</a>。作品製作中，還沒有可以玩的版本。</div>
<h2 id="cast">角色</h2><div class="cast">{cards}</div>
{POEM}
<h2>章節</h2><ul class="chlist">{chl}</ul>
<p class="note">先去玩讓這一切開始的那部作品：<a href="{WORK}">《最後的聖戰》</a>。</p>"""
(DOCS / "index.html").write_text(page("夜後明月，晨前朝霞", index, "乙女向視覺小說：大學生茶語與三個 AI 夥伴的三個禮拜。"), encoding="utf-8")

for c in chapters:
    body = f'<article class="read"><h1>{e(c["title"])}</h1>{render(c["body"])}<p class="note">這一章哪些是真的、哪些是改編：<a href="sources.html#{c["slug"]}">取材對照</a>。</p></article>'
    (DOCS / f'{c["slug"]}.html').write_text(page(f'{c["title"]}｜夜後明月，晨前朝霞', body, f'{c["title"]}，線上閱讀。'), encoding="utf-8")

sec = []
for c in chapters:
    rows = "".join(f'<tr><td><span class="k {kind(s, a)}">{kind(s, a)}</span></td><td>{e(p)}</td><td>{link_sources(s)}</td><td>{e(a)}</td></tr>' for p, s, a in c["table"])
    sec.append(f'<h2 id="{c["slug"]}">{e(c["title"])}</h2><div class="scroll"><table><thead><tr><th>類別</th><th>段落</th><th>真實的出處</th><th>改了什麼</th></tr></thead><tbody>{rows}</tbody></table></div>')
src = f"""<h1 style="font-size:36px;margin:24px 0 6px">取材對照</h1>
<p class="lede">茶語的故事取材自茶葉飲料做《最後的聖戰》的真實經過：她在 2026-11-04 週三直播的分享、她在 Larch 茶館與市集的公開發文、作品的版本記錄，以及挑戰頁本身。每一段都標出是真的、改編的，還是原創的。直播出處附錄影時間點，可以自己去對。</p>
<div class="legend"><span><span class="k 真實">真實</span> 照記錄寫</span><span><span class="k 改編">改編</span> 真實的事，換了說的人或形式</span><span><span class="k 原創">原創</span> 為了故事新寫的</span></div>
<div class="note">沒有轉貼她未公開的內容；其他真實的人只寫角色，不寫名字。錄影：<a href="{LIVE}">週三直播記錄 1104</a>。</div>
{"".join(sec)}"""
(DOCS / "sources.html").write_text(page("取材對照｜夜後明月，晨前朝霞", src, "哪些情節是真的、哪些是改編：逐章逐段對照。"), encoding="utf-8")
import subprocess
apply = pathlib.Path.home() / ".claude/skills/promo-footer/apply.py"
if apply.exists():
    for f in sorted(DOCS.glob("*.html")): subprocess.run(["python3", str(apply), str(f), "larch-three-gentlemen"], check=True, capture_output=True)
print("built", [p.name for p in DOCS.iterdir()], "cues", len(cue))
