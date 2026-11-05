# 驗收用：python3 tools/sheet.py out.png id1 id2 …（art/gen/ch1/<id>.png，四張一張大圖，左上角標編號）
import sys, pathlib
from PIL import Image, ImageDraw
ROOT = pathlib.Path(__file__).resolve().parent.parent
out, ids = sys.argv[1], sys.argv[2:]
W, H = 768, 512
c = Image.new("RGB", (W * 2, H * ((len(ids) + 1) // 2)), "white")
for n, i in enumerate(ids):
    im = Image.open(ROOT / f"art/gen/ch1/{i}.png").convert("RGB").resize((W, H))
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 120, 34), fill="black"); d.text((8, 8), i, fill="white")
    c.paste(im, ((n % 2) * W, (n // 2) * H))
c.save(out)
