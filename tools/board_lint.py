# 分鏡表檢查（新流程第三層）：產圖前跑，有「錯」就不准產。
#   python3 tools/board_lint.py
# 檢查的是試玩抓過的那幾類錯：手沒寫死、工作室出現手機、看錯方向、劇本與分鏡對不上。
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools")); import chapter as C   # CH=2 python3 tools/board_lint.py
_m = C.shots(); S, GAZE, HANDS, RETIRED, NOFACE, props = (getattr(_m, k) for k in "S GAZE HANDS RETIRED NOFACE props".split())
CHIN_OK_EXTRA = getattr(_m, "CHIN_OK", {})

err, warn = [], []
CHIN_OK = {"01A-5b": "下巴一收的表情", "04B": "寫的是下巴不碰任何東西", "05A-2": "抱膝、下巴靠膝蓋，分鏡本來就是這樣"}   # 人看過、確認不是撐頭
CHIN_OK.update(CHIN_OK_EXTRA)
md = C.SCRIPT.read_text(encoding="utf-8")
used = set(re.findall(r"【CG ([^｜\s】]+)", "\n".join(l for l in md.splitlines() if not l.startswith(">"))))

# 回收前幾章已定稿的 CG（例：第六章快切回收前幾章的痕跡）：別章的 id、定稿檔已在，就不算缺
xref = {i for i in used - set(S) if C.chap_of(i) != C.CH and (C.ROOT / C.cg_rel(i)).exists()}
for i in sorted(used - set(S) - xref): err.append(f"{i}：劇本用到，分鏡表沒有")
for i in sorted(used & RETIRED): err.append(f"{i}：已標不再使用，劇本還在用")
for i, d in S.items():
    if i in RETIRED: continue
    base = d["base"]; kind = S[base]["kind"] if d["kind"] == "var" else d["kind"]
    if not (HANDS.get(i) or HANDS.get(base or "")): err.append(f"{i}：沒寫露出來的手")
    body = d["body"].lower()
    if kind == "studio" and re.search(r"\bphones?\b", body) and "no phone" not in body:
        err.append(f"{i}：工作室的描述提到手機（工作室不放手機）")
    if i not in CHIN_OK and any(not re.search(r"(no|never|nobody|not|without)\b[^.]{0,40}$", body[:m.start()]) for m in re.finditer(r"\bchin\b", body)):
        warn.append(f"{i}：描述裡有托腮、撐頭的字眼，確認是不是禁止句")
    if d["kind"] != "var" and kind in ("desk", "studio") and i not in GAZE and i not in NOFACE and "not in frame" not in body and "nobody" not in body:
        warn.append(f"{i}：有人入鏡的主鏡頭沒有視線表")
    if i not in used and d["kind"] != "var" and not any(x["base"] == i for x in S.values()): warn.append(f"{i}：分鏡表有、劇本沒用到")
    if not props(i) and kind in ("desk", "studio", "room", "insert"): err.append(f"{i}：沒有道具狀態")

_iss = ROOT / f"review/第{C.ZH[C.CH - 1]}章_試玩問題.md"
issues = _iss.read_text(encoding="utf-8") if _iss.exists() else ""
todo = [l.split("|")[1].strip() for l in issues.splitlines() if l.startswith("| ") and "已重畫" not in l and "已修好" not in l and "已推上去" not in l and not l.startswith("| 格")]
for t in todo: warn.append(f"試玩清單還沒處理：{t}")

for x in err: print("錯：", x)
for x in warn: print("注意：", x)
print(f"錯 {len(err)} 個、注意 {len(warn)} 個（{len([i for i in S if i not in RETIRED])} 格）")
sys.exit(1 if err else 0)
