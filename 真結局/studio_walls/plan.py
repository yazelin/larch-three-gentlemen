# 工作室橫向捲軸的整圈配置（色塊）。一格 = 48px（遊戲裡），這張預覽一格畫 16px。
# 地圖高 15 格：第 0–11 列是牆，第 12–14 列是能走的地板；牆腳在第 12 列上緣。
# 從左到右：南（門）→ 西（美術牆）→ 北（大窗）→ 東（音樂角）→ 再重複南面開頭 27 格（接回起點用）。
from PIL import Image, ImageDraw, ImageFont
T = 16; WALL_LEN = 40; REPEAT = 27; H = 15; BASE = 12
W = WALL_LEN * 4 + REPEAT
F = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 13, index=4)
FB = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 18, index=4)
# 物件：(x 起, 寬, 上緣列, 下緣列, 名稱, 顏色)  x 以該面牆左端起算；下緣列 12＝立在地上
ITEMS = {
 "南": [(4, 6, 4, 7, "衣架與開襟衫", "#e8d9b8"), (11, 5, 3, 6, "小畫", "#c9d8e8"), (17, 5, 4, 12, "圓拱門", "#a0683c"),
        (25, 3, 2, 4, "圓鐘", "#f2f2f2"), (24, 7, 9, 12, "矮櫃＋盆栽", "#c8a47a"), (31, 6, 4, 7, "小畫", "#c9d8e8")],
 "西": [(2, 26, 2, 8, "水彩畫與色票", "#c9d8e8"), (28, 3, 1, 3, "壁燈", "#666"), (6, 22, 9, 12, "白色抽屜矮櫃＋筆與顏料", "#f4f0ea"),
        (30, 5, 5, 12, "畫架", "#b88a5a"), (35, 3, 9, 12, "蕨類", "#8fbf6a")],
 "北": [(3, 34, 0, 11, "格子大窗（窗外是海）", "#bfe0f0"), (4, 32, 9, 12, "窗下書桌＋螢幕", "#c8a47a"),
        (9, 22, 10, 12, "長桌與四張椅子（靠後）", "#d9b48a")],
 "東": [(3, 34, 1, 11, "整面書櫃", "#b88a5a"), (24, 2, 4, 6, "耳機", "#8c2a3c"), (12, 12, 8, 12, "電子琴＋兩個音箱", "#555a66"),
        (9, 3, 10, 12, "紅色圓凳", "#c0505a"), (28, 3, 7, 12, "吉他", "#d9a05a")],
}
WHO = {"西": (25, "晨", "#b9cf6a"), "北": (8, "明", "#5b8fd9"), "東": (20, "詩", "#c4506a")}
ORDER = ["南", "西", "北", "東"]
im = Image.new("RGB", (W * T, H * T + 60), "white"); d = ImageDraw.Draw(im)
def wall(k, x0, xmax=None):
    d.rectangle((x0 * T, 0, (x0 + (xmax or WALL_LEN)) * T, BASE * T), fill="#efe4ea")
    for (x, w, top, bot, name, col) in ITEMS[k]:
        if xmax and x >= xmax: continue
        ww = min(w, xmax - x) if xmax else w
        box = ((x0 + x) * T, top * T, (x0 + x + ww) * T, bot * T)
        d.rectangle(box, fill=col, outline="#333", width=1)
        d.text((box[0] + 3, box[1] + 2), name, font=F, fill="#222")
    d.text((x0 * T + 6, BASE * T + 50 - 40), f"{k}面", font=FB, fill="#333")
for i, k in enumerate(ORDER): wall(k, i * WALL_LEN)
wall("南", 4 * WALL_LEN, REPEAT)
d.rectangle((0, BASE * T, W * T, H * T), fill="#c48c60")                       # 地板（可走 3 格）
d.rectangle((0, BASE * T - 4, W * T, BASE * T), fill="#faf6f0")                  # 踢腳板
for i in range(1, 5): d.line((i * WALL_LEN * T, 0, i * WALL_LEN * T, BASE * T), fill="#8a7a88", width=3)   # 牆角
for k, (x, n, col) in WHO.items():
    xx = (ORDER.index(k) * WALL_LEN + x) * T; d.ellipse((xx, (BASE + 0.5) * T, xx + 2 * T, (BASE + 2.5) * T), fill=col, outline="#222")
    d.text((xx + 6, (BASE + 0.8) * T), n, font=FB, fill="white")
xx = (2 * WALL_LEN + 12) * T; d.ellipse((xx, (BASE + 0.5) * T, xx + 2 * T, (BASE + 2.5) * T), fill="#e9a98f", outline="#222"); d.text((xx + 2, (BASE + 0.8) * T), "起點", font=F, fill="#222")
d.rectangle((4 * WALL_LEN * T, 0, W * T, H * T), outline="#d04040", width=3)
d.text((4 * WALL_LEN * T + 6, H * T + 8), "← 重複南面開頭（走到這裡無縫接回最左邊）", font=F, fill="#d04040")
d.text((6, H * T + 30), "地圖高 15 格：上 12 格是牆，下 3 格是能走的地板。每面牆 40 格（約 1.5 個畫面），全長 187 格。圓點是人物站的位置。", font=F, fill="#333")
im.save("plan_full.png")
# 兩排版（方便看）
half = (2 * WALL_LEN) * T
top = im.crop((0, 0, half, im.height)); bot = im.crop((half, 0, im.width, im.height))
two = Image.new("RGB", (max(top.width, bot.width), im.height * 2 + 10), "white"); two.paste(top, (0, 0)); two.paste(bot, (0, im.height + 10)); two.save("plan_two_rows.png")
print(im.size)
