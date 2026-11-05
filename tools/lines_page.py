# 台詞＋CG 確認頁：python3 tools/lines_page.py <輸出.html> <候選.json> [cgid=圖檔=說明 ...]
# 候選格式：[id, 段落, 講者, 原句, 審稿意見, 審稿版本, 我的版本, 我的看法]；回覆寫進頁面 db 的 lines/<id> 與 reviews/<cgid>
import json, base64, io, html, sys
from PIL import Image
e = html.escape
out, cand = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
cgs = [a.split("=", 2) for a in sys.argv[3:]]
def b64(p):
    im = Image.open(p).convert("RGB"); im.thumbnail((1400, 1400)); b = io.BytesIO(); im.save(b, "JPEG", quality=82)
    return base64.b64encode(b.getvalue()).decode()
cg_html = "".join(f'''<div class="box cg" data-cg="{cid}" data-ver="{e(path.rsplit('/',1)[-1])}"><h3>CG {cid}</h3><img src="data:image/jpeg;base64,{b64(path)}" alt="CG {cid}"><p>{e(note)}</p>
<div class="choices"><button type="button" class="sec" data-v="approved">定稿</button><button type="button" class="sec" data-v="revise">要修改</button></div>
<textarea rows="2" placeholder="要修改的話寫哪裡不對"></textarea></div>''' for cid, path, note in cgs)
cards = []
for iid, sec, sp, orig, prob, alt, mine, note in cand:
    opts = [("keep", "保持原句", orig), ("alt", "審稿的版本", alt), ("mine", "我的版本", mine)]
    radios = "".join(f'<label class="opt"><input type="radio" name="{iid}" value="{v}"><span class="tag">{t}</span><span class="txt">{e(x)}</span></label>' for v, t, x in opts)
    cards.append(f'''<article class="item" data-id="{iid}"><div class="meta"><b>{e(sec)}</b>｜{e(sp)}</div>
<p class="prob">審稿意見：{e(prob)}</p><p class="mynote">我的看法：{e(note)}</p>{radios}
<label class="opt"><input type="radio" name="{iid}" value="custom"><span class="tag">自己寫</span><input class="custom" type="text" placeholder="改成這句"></label><p class="msg"></p></article>''')
title = sys.argv[1].rsplit("/", 1)[-1].replace(".html", "")
page = f'''<title>{e(title)}</title>
<style>
:root{{--bg:#f6f1ea;--card:#fffdf9;--ink:#3b3440;--muted:#6d6372;--line:#ddd2c2;--plum:#7a5a86;--ok:#4f7a55;--f:"Noto Sans TC","PingFang TC",sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1c1a20;--card:#26232b;--ink:#ece6f0;--muted:#a79fae;--line:#3d3744;--plum:#c3a2d0;--ok:#8fc49a;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#1c1a20;--card:#26232b;--ink:#ece6f0;--muted:#a79fae;--line:#3d3744;--plum:#c3a2d0;--ok:#8fc49a;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font-family:var(--f);line-height:1.7}}
.wrap{{max-width:900px;margin:0 auto;padding-block:24px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1{{font-size:26px;margin:0 0 6px}} h2{{font-size:20px;margin:30px 0 10px;color:var(--plum)}} h3{{margin:0 0 8px;font-size:17px}}
.lede{{color:var(--muted)}} .cg img{{width:100%;height:auto;border-radius:6px;display:block}}
.box,.item{{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:14px 16px;margin:14px 0}}
.meta{{font-size:14px;color:var(--muted)}} .prob,.mynote{{margin:6px 0;font-size:14.5px}} .mynote{{color:var(--plum)}}
.opt{{display:flex;gap:10px;align-items:flex-start;padding:8px 10px;border:1px solid var(--line);border-radius:4px;margin:6px 0;cursor:pointer}}
.opt .tag{{flex:0 0 6.5em;font-size:13px;color:var(--muted)}} .opt .txt{{flex:1;min-width:0}}
.custom{{flex:1;min-width:0;font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:6px 8px}}
.opt:has(input:checked){{border-color:var(--plum);background:color-mix(in srgb,var(--plum) 10%,transparent)}}
button{{font:inherit;padding:8px 18px;border-radius:4px;border:1px solid var(--plum);background:var(--plum);color:#fff;cursor:pointer}}
.choices{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}} .choices button.sec{{background:transparent;color:var(--ink);border-color:var(--line)}}
.choices button[aria-pressed="true"]{{outline:2px solid var(--ok)}}
.msg{{margin:4px 0 0;font-size:13px;color:var(--ok);min-height:1.2em}}
#save{{position:sticky;bottom:max(12px,env(safe-area-inset-bottom,0px));box-shadow:0 4px 14px rgb(0 0 0/.18)}}
textarea{{width:100%;box-sizing:border-box;font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:8px}}
</style>
<div class="wrap"><h1>{e(title)}</h1>
<p class="lede">先看 CG，再逐句選台詞版本（或自己寫），最後按「全部送出」。沒選的句子維持原句。</p>
<h2>CG</h2>{cg_html}<h2>台詞（{len(cand)} 處）</h2>{"".join(cards)}
<button id="save" type="button">全部送出</button><p class="msg" id="allmsg" aria-live="polite"></p></div>
<script>
document.querySelectorAll('.cg').forEach(c=>c.querySelectorAll('.choices button').forEach(b=>b.onclick=()=>{{c.dataset.pick=b.dataset.v;c.querySelectorAll('.choices button').forEach(x=>x.setAttribute('aria-pressed',x===b))}}));
document.querySelectorAll('.custom').forEach(i=>i.addEventListener('focus',()=>i.closest('.opt').querySelector('input[type=radio]').checked=true));
(async()=>{{const db=await claude.use('db');const m=document.getElementById('allmsg');
 if(!db){{m.textContent='登入後才能送出';document.getElementById('save').disabled=true;return}}
 document.getElementById('save').onclick=async()=>{{m.textContent='送出中';let n=0,c=0;
  try{{for(const g of document.querySelectorAll('.cg')){{if(!g.dataset.pick)continue;await db.doc('reviews/'+g.dataset.cg).set({{status:g.dataset.pick,note:g.querySelector('textarea').value.trim(),ver:g.dataset.ver,at:Date.now()}});c++}}
   for(const a of document.querySelectorAll('.item')){{const r=a.querySelector('input[type=radio]:checked');if(!r)continue;
    const text=r.value==='custom'?a.querySelector('.custom').value.trim():r.closest('.opt').querySelector('.txt').textContent;
    await db.doc('lines/'+a.dataset.id).set({{pick:r.value,text,at:Date.now()}});a.querySelector('.msg').textContent='已送出';n++}}
   m.textContent='已送出 '+n+' 句、'+c+' 張 CG';}}catch(e){{m.textContent='送出失敗：'+(e&&e.message||'請再試一次')}}}};
}})();
</script>'''
open(out, "w", encoding="utf-8").write(page); print("wrote", out, len(page) // 1024, "KB")
