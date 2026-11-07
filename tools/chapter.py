# 章節參數：所有產線工具共用。CH=2 python3 tools/shots.py …（不給就是第一章，輸出跟以前一模一樣）。
# 第一章的 CG 放 art/cg/<id>.jpg（id 像 01-0、04A-1）；第二章起 id 用「章號-」開頭（2-01A），檔案放 art/cg/ch2/，
# 這樣 tools/assets.py 會自動分出 cg-ch2 組，各組各自在 jsDelivr 50 MB 以內。
import os, re, pathlib, importlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
ZH = "一二三四五六七八九"
# 第八章以後不是正篇：8＝間章、9＝晨線、10＝明線、11＝詩線、12＝夥伴結局（CG id 一樣用「章號-」開頭：9-01、10-01）
EXTRA = {8: "間章", 9: "個人線_C", 10: "個人線_M", 11: "個人線_S", 12: "夥伴結局"}
ROUTES = {9, 10, 11, 12}   # 個人線與結局：結尾不自動跳到下一個章號，也不讓前一章跳進來（由第七章好感三角分歧）
def script_of(ch): return ROOT / (f"劇本/{EXTRA[ch]}.md" if ch in EXTRA else f"劇本/第{ZH[ch - 1]}章.md")
CH = int(os.environ.get("CH", "1"))
SCRIPT = script_of(CH)
GEN = ROOT / f"art/gen/ch{CH}"                                              # 模型原始輸出（png）
PROMPTS = ROOT / "art/cg/ch1" if CH == 1 else ROOT / f"art/prompts/ch{CH}"   # 第一章沿用舊位置；之後不跟定稿 jpg 混在一起
BOARD = f"board-ch{CH}"

def chap_of(cid):
    m = re.match(r"([1-9]\d?)-", cid)   # 2-01A → 2、10-03 → 10；01-0、04A-1、06-4 → 1（第一章的 id 以 0 開頭或數字後面不是減號）
    return int(m[1]) if m else 1

def cg_rel(cid):
    c = chap_of(cid)
    return f"art/cg/{cid}.jpg" if c == 1 else f"art/cg/ch{c}/{cid}.jpg"

def paper_rel(cid):
    c = chap_of(cid)
    return f"art/cg_paper/{cid}.jpg" if c == 1 else f"art/cg_paper/ch{c}/{cid}.jpg"

def shots(ch=None):
    sys.path.insert(0, str(ROOT / "art/cg"))
    return importlib.import_module(f"ch{ch or CH}_shots")

NAMES = {9: "晨線　兩個月", 10: "明線　替代方案", 11: "詩線　聖歌", 12: "夥伴結局　我全都要"}
def label(ch=None):   # 驗收、試玩紀錄的檔名用：第三章、晨線…
    ch = ch or CH
    return NAMES[ch].split("　")[0] if ch in NAMES else (EXTRA[ch] if ch in EXTRA else f"第{ZH[ch - 1]}章")
def board_name(ch=None):
    if (ch or CH) in NAMES: return NAMES[ch or CH]
    p = script_of(ch or CH)
    return p.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()

if __name__ == "__main__":
    assert chap_of("01-0") == 1 and chap_of("04A-1") == 1 and chap_of("2-01A") == 2 and chap_of("06-4") == 1
    assert cg_rel("01-0") == "art/cg/01-0.jpg" and cg_rel("2-03") == "art/cg/ch2/2-03.jpg"
    assert paper_rel("2-03") == "art/cg_paper/ch2/2-03.jpg"
    assert chap_of("10-03") == 10 and chap_of("9-01") == 9 and cg_rel("10-03") == "art/cg/ch10/10-03.jpg"
    assert script_of(9).name == "個人線_C.md" and script_of(7).name == "第七章.md"
    print("ok")
