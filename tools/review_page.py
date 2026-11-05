# 產生四人定稿確認頁：python3 tools/review_page.py <輸出.html> id=圖檔 ...
import sys, json, base64, io, html
from PIL import Image
out, pairs = sys.argv[1], [a.split("=", 1) for a in sys.argv[2:]]
import os
D = json.load(open("canon/cast.json", encoding="utf-8")); cast = {**D["cast"], **D["world"], **D.get("cg", {}), "lineup": D["lineup"]}
TITLE = os.environ.get("REVIEW_TITLE", "四人定稿確認"); INTRO = os.environ.get("REVIEW_INTRO", "")
notes = json.load(open(os.environ.get("REVIEW_NOTES", "art/gen/review_notes.json"), encoding="utf-8"))
def b64(p):
    im = Image.open(p).convert("RGB"); im.thumbnail((1400, 1400))
    b = io.BytesIO(); im.save(b, "JPEG", quality=82); return base64.b64encode(b.getvalue()).decode()
cards = []
for cid, path in pairs:
    c = cast[cid]; ver = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    must = "".join(f"<li>{html.escape(x)}</li>" for x in c["must"])
    mustnot = "".join(f"<li>{html.escape(x)}</li>" for x in c["must_not"])
    cards.append(f'''<article class="card" data-id="{cid}" data-ver="{ver}">
<header><h2>{html.escape(c["name"])}</h2><span class="ver">{ver}</span><span class="state" data-state>未回覆</span></header>
<button class="shot" type="button" aria-label="放大 {html.escape(c["name"])}"><img src="data:image/jpeg;base64,{b64(path)}" alt="{html.escape(c["name"])} 設定圖候選 {ver}"></button>
<div class="spec"><div><h3>必須有</h3><ul>{must}</ul></div><div><h3>不可以有</h3><ul class="no">{mustnot}</ul></div></div>
<p class="mine"><b>我的檢查：</b>{html.escape(notes.get(cid, ""))}</p>
<div class="act"><div class="choices" role="group" aria-label="決定">
<button type="button" data-pick="approved">定稿</button><button type="button" data-pick="revise">要修改</button></div>
<label for="note-{cid}">修改意見（選「要修改」時寫哪裡不對）</label>
<textarea id="note-{cid}" rows="3" placeholder="例：眼睛顏色要再淡一點"></textarea>
<button type="button" class="save" data-save>送出</button><p class="msg" data-msg aria-live="polite"></p></div></article>''')
DEFAULT_INTRO = "每張都是從原始設定圖重畫的候選。茶葉飲料改成女性骨架，三位先生照區分表拉開身高、年紀、臉型。點圖可以放大看細節。每個人選「定稿」或「要修改」再按送出，通過的才會搬進正典，之後所有 CG 都以它為準。"
page = open("tools/review_page.tpl.html", encoding="utf-8").read().replace("<!--CARDS-->", "\n".join(cards)).replace("<!--TITLE-->", TITLE).replace("<!--INTRO-->", INTRO or DEFAULT_INTRO)
open(out, "w", encoding="utf-8").write(page); print("wrote", out, len(page)//1024, "KB")
