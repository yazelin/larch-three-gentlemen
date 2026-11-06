# 把 art/ui/ 的 title.html、dialogue.html 與 choices.css、menu.css、gallery.css 寫進 Larch 的自訂介面（PUT /interface，expectedHtml 當樂觀鎖）。
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import larch_build as lb
pid = json.loads(lb.STATE.read_text())["id"]
proj, _ = lb.call("GET", f"/projects/{pid}")
cur = (proj.get("project", proj).get("settings", {}).get("customInterfaces") or {})
PARTS = {"title": "title.html", "dialogue": "dialogue.html", "choices": "choices.css", "menu": "menu.css", "gallery": "gallery.css"}
NAME = {"title": "標題畫面", "dialogue": "對話框", "choices": "選項", "menu": "選單與設定", "gallery": "回憶收藏"}
for surface in PARTS:
    html = (lb.ROOT / "art/ui" / PARTS[surface]).read_text(encoding="utf-8")
    assert len(html) < 200000, surface
    exp = (cur.get(surface) or {}).get("html") or ""
    lb.call("PUT", f"/projects/{pid}/interface", {"surface": surface, "html": html, "enabled": True, "expectedHtml": exp,
                                                   "summary": f"自訂{NAME[surface]}"})
back, _ = lb.call("GET", f"/projects/{pid}")
ci = back.get("project", back)["settings"]["customInterfaces"]
for surface in PARTS:
    ok = (ci.get(surface) or {}).get("html") == (lb.ROOT / "art/ui" / PARTS[surface]).read_text(encoding="utf-8")
    print(surface, "讀回一致" if ok else "讀回不一致", (ci.get(surface) or {}).get("enabled"))
