# 畫平面配置圖：每個機位一張，只標那一台攝影機與視野扇形。python3 tools/plans.py
# 座標單位是公分，原點在房間西北角，x 往東、y 往南。
import math
from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
ROOMS = {
 "studio": {"size": (900, 700), "items": [
   ("WINDOW WALL (floor-to-ceiling grid windows)", (0, 0, 900, 18), "#9cc9e8"),
   ("sketches", (0, 60, 14, 330), "#e9c46a"),
   ("low cabinets", (14, 200, 90, 440), "#c8b49a"),
   ("desk + monitor", (110, 40, 390, 110), "#c8b49a"),
   ("bookshelf", (840, 30, 900, 330), "#a47e5b"),
   ("keyboard + speakers", (660, 160, 840, 230), "#555"),
   ("guitar", (845, 380, 885, 430), "#d9a15b"),
   ("rug", (170, 270, 760, 640), "#ece3d3"),
   ("LONG TABLE", (250, 330, 690, 470), "#deb887"),
   ("red chair (HER SEAT)", (300, 480, 370, 550), "#c0614a"),
   ("green chair", (560, 480, 630, 550), "#7f9c7a"),
   ("cream chair", (300, 250, 370, 320), "#efe6d2"),
   ("wood chair", (560, 250, 630, 320), "#b5835a"),
   ("ENTRANCE DOOR", (380, 690, 500, 700), "#7a5230"),
   ("sideboard", (560, 655, 760, 700), "#c8b49a"),
 ], "cams": {
   "A": ((450, 690), 0, 60, "wide establishing, standing eye level"),
   "B": ((450, 40), 180, 60, "reverse, from the window looking at the door, standing eye level"),
   "C": ((240, 600), 35, 45, "close, seated eye level, just behind her seat looking across the table to the music corner"),
   "D": ((450, 360), None, 0, "top-down bird's-eye from the ceiling"),
 }},
 "desk": {"size": (360, 340), "items": [
   ("WINDOW (night city view)", (70, 0, 330, 12), "#4a5a8a"),
   ("DESK", (60, 12, 340, 82), "#a0764e"),
   ("lamp", (80, 20, 105, 45), "#f2c14e"),
   ("laptop", (165, 25, 225, 60), "#999"),
   ("iced tea", (238, 35, 252, 49), "#b5651d"),
   ("phone", (225, 62, 255, 78), "#222"),
   ("tablet", (270, 25, 315, 45), "#666"),
   ("BED", (0, 40, 60, 240), "#c9c3d8"),
   ("bookshelf above bed", (0, 12, 60, 40), "#a47e5b"),
   ("HER CHAIR", (175, 95, 235, 150), "#7d7480"),
   ("wardrobe", (280, 230, 360, 340), "#b59c80"),
   ("DOOR", (120, 330, 210, 340), "#7a5230"),
 ], "cams": {
   "A": ((120, 210), -20, 60, "seated eye level from behind-left of the chair, looking at the desk and window"),
   "B": ((200, 30), 180, 65, "reverse from the desk/window side looking back into the room at her chair, the bed and the door"),
   "C": ((300, 135), -25, 45, "close over-the-shoulder at desk height onto the phone, tea and tablet"),
   "D": ((180, 170), None, 0, "top-down bird's-eye from the ceiling"),
 }},
}
def draw(room, cam):
    R = ROOMS[room]; W, H = R["size"]; s = 1000 / max(W, H); pad = 60
    im = Image.new("RGB", (int(W*s)+2*pad, int(H*s)+2*pad+60), "white"); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(F, 16); fb = ImageFont.truetype(F, 22)
    P = lambda x, y: (pad + x*s, pad + y*s)
    d.rectangle([P(0,0), P(W,H)], outline="black", width=4)
    for name, (x0,y0,x1,y1), col in R["items"]:
        d.rectangle([P(x0,y0), P(x1,y1)], fill=col, outline="#333")
        cx, cy = P((x0+x1)/2, (y0+y1)/2); d.text((cx, cy), name, fill="black", font=f, anchor="mm")
    (x, y), ang, fov, desc = R["cams"][cam]
    cx, cy = P(x, y)
    if ang is None:
        d.ellipse([cx-28, cy-28, cx+28, cy+28], outline="red", width=6); d.line([cx-20, cy, cx+20, cy], fill="red", width=4); d.line([cx, cy-20, cx, cy+20], fill="red", width=4)
    else:
        # ang: 0 = facing north (up), clockwise
        L = 2000
        pts = [(cx, cy)] + [(cx + L*math.sin(math.radians(ang+a)), cy - L*math.cos(math.radians(ang+a))) for a in (-fov/2, fov/2)]
        ov = Image.new("RGBA", im.size); ImageDraw.Draw(ov).polygon(pts, fill=(255,0,0,55)); im.paste(ov, (0,0), ov); d = ImageDraw.Draw(im)
        d.ellipse([cx-14, cy-14, cx+14, cy+14], fill="red")
    d.text((cx+18, cy-30), f"CAMERA {cam}", fill="red", font=fb)
    d.text((pad, im.size[1]-45), f"{room} camera {cam}: {desc}. North (window) is up.", fill="black", font=f)
    im.save(f"canon/plans/{room}_{cam}.png")
for r in ROOMS:
    for c in ROOMS[r]["cams"]: draw(r, c)
print("ok")
