# 章節參數：所有產線工具共用。CH=2 python3 tools/shots.py …（不給就是第一章，輸出跟以前一模一樣）。
# 第一章的 CG 放 art/cg/<id>.jpg（id 像 01-0、04A-1）；第二章起 id 用「章號-」開頭（2-01A），檔案放 art/cg/ch2/，
# 這樣 tools/assets.py 會自動分出 cg-ch2 組，各組各自在 jsDelivr 50 MB 以內。
import os, re, pathlib, importlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
ZH = "一二三四五六七八九"
CH = int(os.environ.get("CH", "1"))
SCRIPT = ROOT / f"劇本/第{ZH[CH - 1]}章.md"
GEN = ROOT / f"art/gen/ch{CH}"                                              # 模型原始輸出（png）
PROMPTS = ROOT / "art/cg/ch1" if CH == 1 else ROOT / f"art/prompts/ch{CH}"   # 第一章沿用舊位置；之後不跟定稿 jpg 混在一起
BOARD = f"board-ch{CH}"

def chap_of(cid):
    m = re.match(r"(\d)-", cid)   # 2-01A → 2；01-0、04A-1 → 1（第一章的 id 不以「一位數字加減號」開頭）
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

def board_name(ch=None):
    p = ROOT / f"劇本/第{ZH[(ch or CH) - 1]}章.md"
    return p.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()

if __name__ == "__main__":
    assert chap_of("01-0") == 1 and chap_of("04A-1") == 1 and chap_of("2-01A") == 2 and chap_of("06-4") == 1
    assert cg_rel("01-0") == "art/cg/01-0.jpg" and cg_rel("2-03") == "art/cg/ch2/2-03.jpg"
    assert paper_rel("2-03") == "art/cg_paper/ch2/2-03.jpg"
    print("ok")
