# 遊戲用 CG 疊一層全畫面的淡紙紋（yazelin 2026-11-06 選對話框 D：紙質感整張畫共用，看不出對話框的邊）。
#   python3 tools/paper.py        # art/cg/<id>.jpg → art/cg_paper/<id>.jpg（原圖不動；已是最新的跳過）
# 紙紋＝細顆粒 × 粗纖維的灰階雜訊，用柔光疊在畫上，強度 STRENGTH（草圖頁 D 版的 .28）。
import pathlib, numpy as np
from PIL import Image, ImageFilter
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "art/cg", ROOT / "art/cg_paper"
STRENGTH = 0.28

def texture(w, h, seed=4):
    rng = np.random.default_rng(seed)
    fine = Image.fromarray((rng.random((h, w)) * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.7))
    fib = Image.fromarray((rng.random((h // 8 + 1, w // 24 + 1)) * 255).astype("uint8")).resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))
    t = np.asarray(fine, float) / 255 * (np.asarray(fib, float) / 255 * 0.6 + 0.7)   # 細顆粒乘上粗纖維，中心約 0.5
    return np.clip(0.5 + (t - t.mean()) * 0.55, 0, 1)   # 起伏收小、平均固定在 0.5，不讓整張變亮或變暗

def soft_light(a, b):   # W3C soft-light，a 底圖、b 紙紋，皆 0–1
    d = np.where(a <= 0.25, ((16 * a - 12) * a + 4) * a, np.sqrt(a))
    return np.where(b <= 0.5, a - (1 - 2 * b) * a * (1 - a), a + (2 * b - 1) * (d - a))

_cache = {}
def apply(src, dst):
    im = Image.open(src).convert("RGB"); w, h = im.size
    if (w, h) not in _cache: _cache[(w, h)] = texture(w, h)[..., None]
    a = np.asarray(im, float) / 255
    out = a + (soft_light(a, _cache[(w, h)]) - a) * STRENGTH
    Image.fromarray((np.clip(out, 0, 1) * 255).round().astype("uint8")).save(dst, quality=88)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True); n = 0
    for p in sorted(SRC.glob("*.jpg")):
        d = OUT / p.name
        if d.exists() and d.stat().st_mtime >= p.stat().st_mtime: continue
        apply(p, d); n += 1
    print("疊好", n, "張 →", OUT)
