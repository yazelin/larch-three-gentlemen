# 真結局的 3D 小島：產地形（Larch 3D 的 terrain 格式），並畫一張俯視預覽給作者確認。
#   python3 tools/island.py preview   # 輸出 真結局/island_preview.png
# 座標：x 往東、z 往南（俯視圖上方是北）。地形格式見 tools/l3d_terrain.py。
import sys, math, json
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).parent))
import l3d_terrain as T

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "真結局"
SIZE = RES = 140
N = RES + 1
SEA = -1.2
MATS = ["grass", "meadow", "dirt", "sand", "rock", "snow"]

# 各區中心（世界座標）
SPOT = {
    "home": (0, -2),        # 四個人的家（露天工作室）
    "pier": (6, -33),       # 北邊碼頭，玩家從這裡上岸
    "C": (30, 2),           # 晨：東邊朝霞丘頂
    "M": (-52, 5),          # 明：西邊月光岬尖端的鐘塔
    "S": (4, 36),           # 詩：南邊海灘舞台
}

def g(x, z, cx, cz, sx, sz=None):
    sz = sz or sx
    return np.exp(-(((x - cx) / sx) ** 2 + ((z - cz) / sz) ** 2))

def build():
    ax = np.linspace(-SIZE / 2, SIZE / 2, N)
    x, z = np.meshgrid(ax, ax)          # z 是列（j）、x 是行（i）：index = i + j*N
    th = np.arctan2(z, x); r = np.hypot(x, z)
    # 海岸線半徑：低頻起伏＋東邊鼓起（丘）＋南邊寬（海灘）＋北邊一個灣（碼頭）
    wob = 2.2 * np.sin(3 * th + 0.7) + 1.4 * np.sin(5 * th + 2.1) + 0.8 * np.sin(8 * th + 0.3)
    R = 37 + wob + 6 * np.clip(np.cos(th), 0, 1) ** 2 + 5 * np.clip(np.sin(th), 0, 1) - 9 * np.exp(-((th + math.pi / 2 - 0.12) / 0.28) ** 2)
    land = np.clip((R - r) / 6, -1, 1)                       # 1＝內陸，-1＝外海
    # 西邊伸出去的岬：沿一條微彎的線，越往尖端越窄
    t_ = np.clip((-x - 28) / 30, 0, 1)                         # 0＝岬根，1＝岬尖
    mid = 3 + 4 * np.sin(t_ * math.pi * 0.9)
    wid = 8 - 4.5 * t_
    cape = np.where((x < -24) & (x > -62), np.minimum(np.clip((wid - np.abs(z - mid)) / 3, -1, 1), np.clip((x + 60) / 3, -1, 1)), -1.0)
    land = np.maximum(land, cape)
    cape = cape.clip(0)
    h = np.where(land > 0, 0.4 + 1.6 * land, SEA - 0.3 + 5 * land)
    h += land.clip(0) * 1.2 * g(x, z, *SPOT["home"], 14)      # 中央緩坡上的家（平台）
    h += 7.5 * g(x, z, *SPOT["C"], 13, 11) * (land > 0)       # 東：朝霞丘
    h += 8.5 * g(x, z, -50, 6, 9, 4.5) * (cape > 0.2)          # 西：岬上的岩稜
    beach = np.clip((z - 24) / 10, 0, 1) * (land > 0)          # 南：海灘往海裡緩降
    h = h - beach * (h - 0.15) * 0.85
    # 家前面整平
    hx, hz = SPOT["home"]; flat = g(x, z, hx, hz, 7)
    h = h * (1 - flat) + 2.6 * flat
    # 材質權重（6 通道，加總 255）
    W = np.zeros((N, N, 6))
    W[..., 0] = 1
    W[..., 3] = np.clip((1.0 - h) / 0.8, 0, 1) + beach * 1.5               # 沙
    W[..., 1] = 1.6 * g(x, z, *SPOT["C"], 15, 12) * (h > 1)                 # 東丘草甸
    W[..., 4] = np.clip((cape - 0.2) * 1.5, 0, 1) * np.clip((h - 1.5) / 3, 0, 1) * 1.8   # 西岬岩石
    W[..., 2] = 0.9 * flat                                                  # 家門前泥土地
    W[..., 0] = np.clip(1 - W[..., 1:].sum(-1), 0, 1)
    W = W / W.sum(-1, keepdims=True)
    ground = (W * 255).round().astype(np.uint8)
    grass = (200 * W[..., 0] + 230 * W[..., 1]).clip(0, 255).astype(np.uint8)
    flowers = (255 * np.clip(1.4 * g(x, z, *SPOT["C"], 12, 10), 0, 1) * (h > 1.5) + 120 * g(x, z, hx, hz, 12) * (1 - flat)).clip(0, 255).astype(np.uint8)
    return x, z, h, ground, grass, flowers, land

def terrain():
    x, z, h, ground, grass, flowers, _ = build()
    return {"v": 1, "size": SIZE, "res": RES, "seaLevel": SEA,
            "heights": T.enc(h.ravel().tolist(), N), "ground": T.enc_u8(ground.ravel().tobytes()),
            "grass": T.enc_u8(grass.ravel().tobytes()), "flowers": T.enc_u8(flowers.ravel().tobytes()),
            "water": T.enc([float("nan")] * (N * N), N, nan=-32767)}

def preview():
    from PIL import Image, ImageDraw, ImageFont
    x, z, h, ground, grass, flowers, land = build()
    col = np.array([[118, 168, 82], [168, 196, 96], [150, 118, 82], [230, 214, 160], [128, 124, 120], [240, 240, 240]], float)
    img = (ground[..., :6] / 255.0) @ col
    img[..., :] = np.where((flowers > 120)[..., None], img * 0.7 + np.array([250, 230, 120]) * 0.3, img)
    gy, gx = np.gradient(h); shade = np.clip(0.85 + (gx - gy) * 0.35, 0.55, 1.25)
    img = img * shade[..., None]
    sea = h < SEA
    depth = np.clip((SEA - h) / 4, 0, 1)[..., None]
    img = np.where(sea[..., None], np.array([120, 190, 210]) * (1 - depth) + np.array([40, 80, 130]) * depth, img)
    S = 6
    im = Image.fromarray(img.clip(0, 255).astype(np.uint8)).resize((N * S, N * S), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 26, index=4) if Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc").exists() else ImageFont.load_default()
    def px(p): return ((p[0] + SIZE / 2) * S, (p[1] + SIZE / 2) * S)
    lab = {"home": ("四個人的家", (40, 36, 30)), "pier": ("碼頭（上岸）", (40, 36, 30)),
           "C": ("晨・朝霞丘", (90, 110, 20)), "M": ("明・月光岬鐘塔", (30, 70, 160)), "S": ("詩・海灘舞台", (150, 30, 60))}
    for k, (t, c) in lab.items():
        X, Y = px(SPOT[k]); d.ellipse((X - 9, Y - 9, X + 9, Y + 9), fill=c, outline=(255, 255, 255), width=3)
        d.text((X + 14, Y - 16), t, font=f, fill=(255, 255, 255), stroke_width=4, stroke_fill=c)
    d.text((14, 10), "北 ↑　一格 = 1 公尺，全島約 110 × 95 公尺", font=f, fill=(255, 255, 255), stroke_width=3, stroke_fill=(30, 40, 60))
    OUT.mkdir(exist_ok=True); im.save(OUT / "island_preview.png")
    print("陸地格數", int((h > SEA).sum()), "最高", round(float(h.max()), 2), "→", OUT / "island_preview.png")

if __name__ == "__main__":
    if sys.argv[1:2] == ["preview"]: preview()
    elif sys.argv[1:2] == ["terrain"]: print(json.dumps(terrain())[:200])
