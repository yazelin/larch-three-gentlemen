# 把 art/ui/title.html、dialogue.html 寫進 Larch 的自訂介面（PUT /interface，expectedHtml 當樂觀鎖）。
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import larch_build as lb
pid = json.loads(lb.STATE.read_text())["id"]
proj, _ = lb.call("GET", f"/projects/{pid}")
cur = (proj.get("project", proj).get("settings", {}).get("customInterfaces") or {})
for surface in ("title", "dialogue"):
    html = (lb.ROOT / f"art/ui/{surface}.html").read_text(encoding="utf-8")
    assert len(html) < 200000, surface
    exp = (cur.get(surface) or {}).get("html") or ""
    lb.call("PUT", f"/projects/{pid}/interface", {"surface": surface, "html": html, "enabled": True, "expectedHtml": exp,
                                                   "summary": f"自訂{ {'title': '標題畫面', 'dialogue': '對話框'}[surface] }"})
back, _ = lb.call("GET", f"/projects/{pid}")
ci = back.get("project", back)["settings"]["customInterfaces"]
for surface in ("title", "dialogue"):
    ok = ci[surface]["html"] == (lb.ROOT / f"art/ui/{surface}.html").read_text(encoding="utf-8")
    print(surface, "讀回一致" if ok else "讀回不一致", ci[surface].get("enabled"))
