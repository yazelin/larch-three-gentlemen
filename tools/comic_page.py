# 間章的 2×2 合頁：把四格（8-01～8-04）照漫畫順序排成一頁，只是排版，不重畫、不改格子內容。
#   python3 tools/comic_page.py      # → art/cg/ch8/8-P.jpg（之後照常跑 paper.py、assets.py）
# 順序照台灣漫畫的讀法：右上 1、左上 2、右下 3、左下 4（由右往左、由上往下）。
import pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "art/cg/ch8"
PAPER, GAP, M = (244, 238, 226), 36, 56   # 紙色、格與格的間距、外框留白

def page(ids=("8-01", "8-02", "8-03", "8-04"), out=D / "8-P.jpg"):
    ims = [Image.open(D / f"{i}.jpg").convert("RGB") for i in ids]
    w, h = ims[0].size
    ims = [im.resize((w, h)) for im in ims]
    W, H = M * 2 + w * 2 + GAP, M * 2 + h * 2 + GAP
    pg = Image.new("RGB", (W, H), PAPER)
    pos = [(M + w + GAP, M), (M, M), (M + w + GAP, M + h + GAP), (M, M + h + GAP)]   # 右上、左上、右下、左下
    for im, p in zip(ims, pos): pg.paste(im, p)
    pg.thumbnail((2304, 2304))
    pg.save(out, quality=90)
    return out

if __name__ == "__main__":
    print(page())
