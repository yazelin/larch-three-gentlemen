# 本機預覽：不推 Larch，用 Larch 自己的播放器（~/larch-preview）看最新的第一章。
#   python3 tools/local_preview.py          # 組 dist/local/project.json（圖、音樂讀本機檔），印出啟動指令
# 專案設定、運鏡影片、直式封面沿用線上 Larch 專案的那份（讀一次、不寫回）；卡片、介面、CG 用本機最新的。
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import larch_build as lb
ROOT = lb.ROOT; OUT = ROOT / "dist/local"; OUT.mkdir(parents=True, exist_ok=True)
pid = json.loads(lb.STATE.read_text())["id"]
proj, _ = lb.call("GET", f"/projects/{pid}")
p = proj.get("project", proj)
board = json.loads((ROOT / "dist/board_ch1.json").read_text(encoding="utf-8"))
p["boards"] = [{"id": lb.BOARD, "kind": "story", "mode": "story", "name": "第一章　茶", "description": "", "nodes": board["nodes"], "edges": board["edges"]}]
s = p.setdefault("settings", {})
s.update({"arrowKeyBack": True, "arrowKeyNext": True, "stageFit": "cover"})
s.setdefault("dialogueUi", {})["fontFamily"] = "iansui"   # 芫荽手寫字（同 larch_build.py）   # 左右鍵翻頁：預設關，要明寫才開
for part, fn in {"title": "title.html", "dialogue": "dialogue.html", "choices": "choices.css", "menu": "menu.css", "gallery": "gallery.css"}.items():
    s.setdefault("customInterfaces", {})[part] = {"enabled": True, "html": (ROOT / "art/ui" / fn).read_text(encoding="utf-8")}
txt = json.dumps(p, ensure_ascii=False)
# ponytail: 把 jsDelivr 上任何版號的網址換成本機 /files/（serve.py 把 /files/ 對到這個檔所在的資料夾，所以檔案放在 repo 根目錄算起）
import re
txt = re.sub(r"https://cdn\.jsdelivr\.net/gh/yazelin/larch-three-gentlemen@[^/]+/", "/files/", txt)
(ROOT / "project.local.json").write_text(txt, encoding="utf-8")
print("寫好", ROOT / "project.local.json")
print("啟動：python3 ~/larch-preview/serve.py", ROOT / "project.local.json", "--port 8795")
