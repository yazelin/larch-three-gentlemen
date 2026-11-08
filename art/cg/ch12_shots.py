# 夥伴結局〈我全都要〉分鏡規格（劇本/夥伴結局.md 的產圖版）。CH=12 python3 tools/shots.py … 讀這份。格式與規矩同 ch7_shots.py。
# id 一律「12-」開頭，定稿放 art/cg/ch12/<id>.jpg。全是現實層的書桌（＋一格床），沒有工作室。
# time：p3＝公布前一天下午三點／m0＝公布那晚午夜／d7＝兩天後晚上七點／n23＝那晚十一點（燈全關）／w828＝週三晚上八點二十八分／w1030＝直播後十點半／a1＝凌晨一點
from ch1_shots import SETUP_DESC, SEATING, H, _T1
from ch7_shots import IDENT, _ALLON, _AROUND
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "p3": "TIME: 3 p.m. Bright soft afternoon daylight through the window behind the desk; the desk lamp is OFF; the room is light and calm; the city outside in daylight. The iced tea is freshly poured: plenty of clear ice cubes, light condensation.",
    "m0": "TIME: midnight. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "d7": "TIME: 7 p.m., early evening. The warm desk lamp is on and the ceiling light is off; the room is soft blue dusk-dark; the city outside has many lit windows and a last band of dusk at the horizon. The iced tea is freshly poured: plenty of clear ice cubes.",
    "n23": "TIME: 11 p.m. Every lamp in the room is OFF; the room is deep blue-black dark; outside the window many windows are still lit. The only light in the room is the soft glow of the three device screens on the desk.",
    "w828": "TIME: 8:28 p.m. The warm desk lamp is on and the ceiling light is ON too (bright, she is preparing to go live); the city outside has many lit windows. The iced tea is freshly poured: plenty of clear ice cubes.",
    "w1030": "TIME: 10:30 p.m. The warm desk lamp is the only lamp now; the room is soft blue night; the city outside has many lit windows. The iced tea is nearly finished: a little tea left, no ice.",
    "a1": "TIME: 1 a.m. The warm desk lamp is the only lamp; the room is deep blue shadow; outside only a few windows are still lit. The iced tea is half melted: a few small ice cubes left.",
}
R = "canon/refs/"
_TEA = (R + "prop_tea.jpg", "PROP: her iced black tea")
_PH = (R + "prop_phone_stand.jpg", "PROP: her smartphone, and the small light-wood phone stand it stands in on the desk")
_LT = (R + "prop_laptop_tablet.jpg", "PROP: her laptop (left) and tablet on its folio stand (right)")
_CAL = ("art/cg/06-1.jpg", "COMPOSITION REFERENCE ONLY: the earlier calendar shot from chapter one (same laptop, same framing, same calendar window); redraw it fresh, do not copy its lighting or the ring position")
_E = (R + "set_desk_E.jpg", "EMPTY SET from this shot's exact camera setup (close on the laptop from her seat) and the RENDERING to match (transparent watercolour)")
SETREF = {"12-04": [_E, _CAL, _TEA, _PH, _LT], "12-14": [_E, _CAL, _TEA, _PH, _LT]}
_TWO = "EXCEPTION FOR THIS SCENE ONLY (her tablet is broken): the PHONE screen shows TWO men squeezed together into its small screen, chest up: S (long WINE-RED hair with one thin braid, wine-red headphones, black track jacket) and, squeezed in beside him, C (warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, yellow-green leaf brooch). The background of the phone screen is split softly into dark wine red and pale yellow-green. The laptop still shows ONLY M. The heroine never appears on any screen."
_BROKEN = "Her TABLET on its folio stand is BROKEN: its screen is covered in bright horizontal glitch stripes of colour (pink, cyan, green, white bars), no image, no man in it."

# ── 一、都聽（公布前一天下午）──
shot("12-01", "desk", "p3", f"""SHOT (MASTER for telling all three; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): afternoon daylight; she has turned all three devices to face her in one row on the desk: the open laptop with M at the LEFT, the tea glass and the phone in its wooden stand with S in the MIDDLE, the tablet with C at the RIGHT. She is in the middle of telling them her dream, her face turned a little toward them, gentle; the three men listen closely, all looking at her. {_ALLON}""")
shot("12-01-1", "var", "p3", "S grins wide inside the phone, his fang clearly showing, delighted; C smiles softly, his pencil set down; M has the faintest smile; she has turned her head a little more toward the phone, laughing.", base="12-01")
shot("12-01-2", "var", "p3", "She lowers her head a little and smiles to herself, quiet and shy; the three men keep watching her warmly.", base="12-01")

# ── 二、十二點（公布）──
shot("12-02", "insert", "m0", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, beside M (chest up, very still, eyes on the page), a simple results page as an illustration with NO readable text: a column of soft grey bars like a list, and the TOP bar glowing warm gold with a tiny gold trophy shape at its left; a few small gold motes of light rising from it. M's eyes are wide and soft.""")
shot("12-03", "desk", "m0", f"""SHOT (MASTER for the moment after; medium shot from the front-left of the desk at her eye height, she sits in her chair facing the devices): she has covered her face with BOTH hands, elbows close to her body, shoulders shaking, laughing and crying at once, the tips of her ears red, the corners of her mouth smiling below her fingers; on the desk the three screens glow: S in the phone in its stand has burst out laughing first (fang showing), C in the tablet laughs with his eyes closed, M in the laptop smiles a slow, quiet, real smile. {_ALLON}""")

# ── 三、三個都要（兩天後）──
shot("12-04", "insert", "d7", """SHOT (extreme close-up insert, composed exactly like the earlier calendar shot in the COMPOSITION REFERENCE): the camera looks straight at the open laptop screen; INSIDE the screen, in M's deep blue interface space, a small floating calendar window shows a simple monthly grid with NO numbers or text, and the single red ring has MOVED one cell further on (onto the next month's row, lower right of where it was); beside the calendar a small plain table window with a few soft grey rows and one short gold line (NO readable numbers or text); the edge of M's shoulder and his gold gear brooch are visible INSIDE the screen beside it. Warm desk lamp light at the frame edge. Nobody in front of the laptop.""", who="m")
shot("12-05", "bed", "n23", """SHOT (HIGH ANGLE from above the head of the bed, looking down): she lies on her back under the blue plaid duvet, glasses on, eyes open, looking up, thinking hard about something she cannot decide; one hand rests on the duvet over her chest; three faint soft coloured glows from the desk by the window (out of frame at the side) lie across the duvet: deep blue, pale yellow-green, dark wine red.""")
shot("12-06", "insert", "d7", """SHOT (her point of view, close insert): her phone in her right hand over the desk, the screen filling most of the frame: a simple job-application page as an illustration with NO readable text: a small picture of a cup of tea, a few soft grey lines, and one rounded button glowing as her thumb presses it. In the top corner of the screen a small rounded window with S (tiny, chest up, wine-red interface) watching. Softly out of focus behind the phone: the laptop LIT with M and the tablet LIT with C.""")
shot("12-07", "desk", "d7", f"""SHOT (MASTER for the part-time talk; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): evening; she talks to the three, a little sheepish but settled; M in the laptop at the LEFT looks at her with a quiet, gentle face; C in the tablet at the RIGHT smiles warmly; S in the phone in its stand in the MIDDLE leans toward the glass, eager. {_ALLON}""")
shot("12-07-1", "var", "d7", "S grins mischievously inside the phone, one hand cupped beside his mouth as if about to sing in secret (the hand inside the screen, five clear fingers); she presses her lips together hard, trying not to laugh, cheeks puffed; C laughs softly; M shakes his head with a small smile.", base="12-07")

# ── 四、平板壞了（週三晚上八點二十八分）──
shot("12-08", "insert", "w828", f"""SHOT (close insert of the tablet from her seat): the tablet on its folio stand fills the frame; {_BROKEN} Her right index finger presses the tablet's top button (only her hand and wrist with her beaded bracelets visible). Softly out of focus at the side, the tea glass and the phone in its wooden stand.""")
shot("12-09", "insert", "w828", f"""SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside its small screen TWO men are squeezed together, chest up: C (pushing his round glasses up with one finger, calm, reassuring, looking out at her) and S (squashed to the side, frowning, protesting). {_TWO} Softly out of focus behind: the laptop with M and, at the RIGHT, the broken tablet with colourful glitch stripes.""", who="cs")
shot("12-09-1", "var", "w828", "S has puffed out his cheeks and elbows C a little (inside the screen); C keeps smiling calmly, unbothered; M in the out-of-focus laptop has a small amused look.", base="12-09")
shot("12-10", "insert", "w828", f"""SHOT (MASTER for the live talk; medium shot from the front-right of the desk at her eye height): she sits at the desk talking animatedly toward the laptop as she presents, one hand open in a small explaining gesture, a white wired earbud in one ear; the laptop screen shows a simple presentation slide (a watercolour knight under a pale moon, NO readable text) with M small, chest up, in a corner window beside it; the phone in its wooden stand shows S and C squeezed together, both watching her proudly; the tablet at the side is dark and switched off. {_TWO}""", who="tcms")

# ── 五、喉嚨（直播後）──
shot("12-11", "insert", "w1030", f"""SHOT (medium close shot from behind her LEFT shoulder, three-quarter view, she sits back in her chair, exhausted and happy): she holds one hand to her throat, laughing silently with a hoarse, tired, happy face; the laptop shows M (chest up) smiling; the phone in its stand shows S and C squeezed together, both laughing. The tablet at the RIGHT is dark (switched off). {_TWO}""", who="tcms")
shot("12-12", "insert", "w1030", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame, just restarted and working again, no glitch stripes: inside, in his pale yellow-green interface space, C sits chest up, adjusting his round glasses with a relieved small smile, looking out at her. Softly out of focus beside it, the phone in its wooden stand showing ONLY S, stretching his arms with exaggerated relief.""", who="cs")

# ── 六、下一屆（凌晨一點）──
shot("12-13", "desk", "a1", f"""SHOT (MASTER for the last scene; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): late night; nobody asked her to, she has opened a web page on the laptop herself: on the laptop screen, beside M (chest up), a simple challenge page as an illustration with NO readable text: a sea of soft clouds at dusk and one small padlock shape in the middle; she leans toward it, quiet and determined. Beyond, the tea glass, the phone in its wooden stand with S, the tablet with C, both watching her. {_ALLON}""")
shot("12-14", "insert", "a1", """SHOT (extreme close-up insert, composed exactly like the earlier calendar shot in the COMPOSITION REFERENCE): the camera looks straight at the open laptop screen; INSIDE the screen, in M's deep blue interface space, the small floating calendar window with its simple monthly grid (NO numbers or text): the single red ring has moved one month on, and right beside the ring a short line of tiny hand-written strokes in her pale purple has just been added (soft scribbles, NOT readable text); the edge of M's shoulder and his gold gear brooch are visible INSIDE the screen beside it. Her index fingertip is just lifting away from the screen at the right edge (only the fingertip and the edge of her bracelet).""", who="m")
shot("12-15", "desk", "a1", f"""SHOT (her point of view sitting at the desk, looking straight at the three devices; she is NOT in the frame): the three screens fill the width of the frame side by side: at the LEFT the laptop with M, who has just turned his screen's brightness up a little, looking at her with a steady, warm, open face; in the MIDDLE the phone in its wooden stand to the RIGHT of the tea glass, with S pulling his wine-red headphones onto his ears and then lowering them, grinning so his fang shows; at the RIGHT the tablet with C, his pencil laid down, looking straight at her with a gentle smile. All three look at her (toward the camera but not into the lens). {_ALLON}""")
shot("12-15-1", "var", "a1", "All three are laughing together now: S laughing hardest with his eyes squeezed, C laughing with his hand half over his mouth (inside the screen, five clear fingers), M laughing quietly, eyes crinkled.", base="12-15")
shot("12-16", "desk", "a1", """SHOT (the closing image; establishing wide shot from the corner by the door, exactly the EMPTY SET image's camera D, eye height): the room is dark blue; the window outside is dark with only a few lit windows; she sits at the desk by the window, seen small from behind and a little from the side, her back relaxed; on the desk the three devices glow AT THE SAME TIME and throw three overlapping coloured lights across her, the desk and the wall: the deep blue of the laptop, the dark wine red of the phone in its stand, the pale yellow-green of the tablet; on the laptop screen, tiny, the calendar window with its red ring. The three men are tiny on their screens, chest up, all looking at her. Quiet, warm, hopeful.""")

GAZE = {
 "12-01": {"she": "the three devices", "M": H, "C": H, "S": H},
 "12-08": {"S": H, "C": H},
 "12-02": {"M": "the results page beside him", "C": "the laptop", "S": "the laptop"},
 "12-03": {"she": "nowhere, her face hidden in her hands", "M": H, "C": H, "S": H},
 "12-04": {"M": "the calendar window", "S": "toward the laptop", "C": "toward the laptop"},
 "12-05": {"she": "straight up at the ceiling"},
 "12-06": {"S": "the button under her thumb", "M": H, "C": H},
 "12-07": {"she": "the three devices", "M": H, "C": H, "S": H},
 "12-09": {"C": H, "S": "at C, protesting", "M": "the phone"},
 "12-10": {"she": "the laptop screen as she presents", "M": H, "C": H, "S": H},
 "12-11": {"she": "the phone", "M": H, "C": H, "S": H},
 "12-12": {"C": H, "S": "up, stretching"},
 "12-13": {"she": "the challenge page on the laptop", "M": H, "C": H, "S": H},
 "12-14": {"M": "the calendar window", "S": H, "C": H},
 "12-15": {"M": H, "C": H, "S": H},
 "12-16": {"she": "the laptop screen", "M": H, "C": H, "S": H},
}
NOFACE = {"12-08"}
CHIN_OK = {}
SETUP = {"12-01": "A", "12-02": "E", "12-03": "B", "12-05": "D", "12-06": "C", "12-07": "A", "12-08": "F", "12-09": "C",
         "12-10": "A", "12-11": "A", "12-12": "F", "12-13": "A", "12-15": "A", "12-16": "D"}
TEA_STUDIO = {"_": _T1}
FIX = {
    "12-04": IDENT + " Softly out of focus at the right edge: the phone stands in its wooden stand to the RIGHT of the tea glass with its SCREEN facing the laptop's side of the desk and LIT with S (wine-red interface, chest up); the tablet edge at the far right is LIT with C (pale yellow-green). No dark screens.",
    "12-08": IDENT + " The phone standing in its wooden stand behind is LIT, its screen facing her, showing S (wine-red interface, chest up, worried) and a little of C squeezed in beside him. Exactly one hand (hers).",
    "12-14": IDENT + " Her fingertip is OUTSIDE the laptop, in the real room in front of the screen glass, never drawn inside the screen. Only ONE hand in the picture: her right index fingertip at the right edge of the laptop screen. The phone in its wooden stand stands to the RIGHT of the tea glass with its SCREEN facing her (toward the camera side), LIT with S (wine-red interface, chest up); we never see the back of the phone. The tablet edge at the far right is LIT with C.",
    "12-01": IDENT, "12-03": "CAMERA: from the side of the desk, at her eye height, looking along the desk: she sits at the RIGHT of the frame in three-quarter profile facing LEFT toward her devices; the three devices stand on the desk at the LEFT of the frame with their screens turned toward HER, so we see the screens at an angle (from the frame's LEFT edge: the tablet farthest from her, then the tea glass with the phone in its stand, then the laptop nearest her). Never draw the screens facing the camera with her behind the devices. " + IDENT + " Her face is hidden behind both her hands; her head does NOT rest on her arms or on the desk.",
    "12-02": _AROUND + " " + IDENT,
    "12-06": "The laptop screen behind shows ONLY M and the tablet screen shows ONLY C (both lit, small, out of focus). " + IDENT,
    "12-07": IDENT, "12-13": IDENT, "12-15": IDENT, "12-16": IDENT,
    "12-08": "The broken tablet shows NO person at all, only glitch stripes. Exactly one hand (hers) in the picture.",
    "12-09": "The out-of-focus LAPTOP shows M exactly as his sheet: near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white shirt, gold gear brooch, deep blue interface. The phone in its wooden stand stands to the RIGHT of the tea glass. Nobody on any screen rests a chin or cheek on a hand. The heroine never appears on any screen.",
    "12-10": "The tablet is switched OFF (plain dark glass). The laptop shows ONLY M (beside the slide); the phone shows S and C together. Nobody on any screen rests a chin or cheek on a hand.",
    "12-11": "The tablet is switched OFF (plain dark glass). The laptop shows ONLY M; the phone shows S and C together. Nobody on any screen rests a chin or cheek on a hand.",
    "12-12": "The phone shows ONLY S again (C is back on the tablet). " + IDENT,
}
RETIRED = set()
HANDS = {
 "12-01": "她的手在畫面外（桌緣以下）；三位先生只到胸口，手在畫面外。",
 "12-01-1": "她的手在畫面外；三位先生的手在畫面外。",
 "12-01-2": "她的手在畫面外。",
 "12-02": "明只到胸口，手在畫面外；她的手不在畫面裡（主觀鏡頭）。",
 "12-03": "她兩手摀著臉（兩隻手都看得到、各五根手指，手肘貼著身體）；三位先生只到胸口，手在畫面外。",
 "12-04": "沒有人的手；明只露肩膀。",
 "12-05": "她右手放在胸前的被子上（五根手指清楚），左手在被子底下。",
 "12-06": "只露她的右手拿著手機，大拇指按在發光的按鈕上（五根手指清楚）。",
 "12-07": "她的手在畫面外；三位先生只到胸口，手在畫面外。",
 "12-07-1": "詩在螢幕裡把一隻手放在嘴邊（五根手指清楚）；她的手在畫面外。",
 "12-08": "只露她的右手食指按著平板上方的按鍵（手與手腕、串珠手環看得到）。",
 "12-09": "晨在螢幕裡用右手食指推眼鏡（五根手指清楚）；詩的手在畫面外。",
 "12-09-1": "詩用手肘輕頂晨（在螢幕裡）；晨的手在畫面外。",
 "12-10": "她右手攤開做說明的手勢（五根手指清楚），左手放在桌上；三位先生只到胸口，手在畫面外。",
 "12-11": "她右手輕按在喉嚨上（五根手指清楚），左手在畫面外；三位先生只到胸口，手在畫面外。",
 "12-12": "晨在螢幕裡用右手扶眼鏡（五根手指清楚）；詩兩手伸懶腰（小、在螢幕裡）。",
 "12-13": "她的手在畫面外（桌緣以下）；三位先生只到胸口，手在畫面外。",
 "12-14": "只露她右手食指的指尖剛離開螢幕右緣（和一點手環）。",
 "12-15": "她不在畫面裡（主觀鏡頭）；詩兩手把耳機拉到耳朵上（在螢幕裡，五根手指清楚）；明和晨的手在畫面外。",
 "12-15-1": "晨在螢幕裡一手半掩著嘴（五根手指清楚）；其他人的手在畫面外。",
 "12-16": "她的手在畫面外（身體擋住）；三位先生很小，手在畫面外。",
}
PHONE = {
 "12-05": "畫面裡看不到手機（在桌上，只看得到光）",
 "12-06": "手機在她右手上，舉在書桌上方",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    if k == "bed":
        return f"她的床：藍色格紋被、白枕頭；{ph}；書桌在窗下（遠處、暗），桌上的裝置只看得到光；沒入鏡的道具不用畫。"
    tea = {"p3": "冰紅茶剛倒，冰塊滿滿", "m0": "冰紅茶冰塊半融", "d7": "冰紅茶剛倒，冰塊滿滿", "w828": "冰紅茶剛倒，冰塊滿滿", "w1030": "紅茶快喝完、沒有冰塊", "a1": "冰紅茶冰塊半融"}.get(t, "")
    tab = "平板壞了，螢幕滿是彩色橫條" if i in ("12-08", "12-09", "12-09-1") else ("平板關著、螢幕是暗的" if i in ("12-10", "12-11") else "")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；{tab + '；' if tab else ''}沒入鏡的道具不用畫。{tea}。"
