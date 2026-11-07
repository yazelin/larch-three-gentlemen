# 明線〈替代方案〉分鏡規格（劇本/個人線_M.md 的產圖版）。CH=10 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch7_shots.py、ch9_shots.py。
# id 一律「10-」開頭，定稿放 art/cg/ch10/<id>.jpg。現實層（書桌）＋工作室一場（全線唯一一次碰觸：他的手覆在她拉線的手背上）。
# time：p3＝公布前一天下午／n12＝公布那晚午夜／n9＝晚上九點／e1＝直播前一晚凌晨一點／live＝直播當晚／day＝工作室
from ch1_shots import SETUP_DESC, SEATING, H, _T1
from ch7_shots import IDENT, _ALLON, _AROUND
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "p3": "TIME: 3 p.m. Bright soft afternoon daylight through the window behind the desk; the desk lamp is OFF; the room is light and calm; the city outside in daylight. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
    "n12": "TIME: midnight. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "e1": "TIME: 1 a.m. The warm desk lamp is the only lamp; deep blue shadow; fewer lit windows outside. The iced tea is half melted: a few small rounded ice cubes left.",
    "live": "TIME: 9 p.m. on the night of her talk. The warm desk lamp is on and the ceiling light is on low; the room is soft warm evening light; the city outside has many lit windows. The iced tea is freshly poured with plenty of ice; a small round microphone stands on the desk in front of the laptop.",
}

# ── 一、不要算（公布前一天下午）──
shot("10-01", "desk", "p3", f"""SHOT (MASTER for 'don't calculate'; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): afternoon daylight; she has pulled her chair close to the laptop and talks to it, leaning in a little, telling her dream; inside the laptop, in his deep blue interface space, M sits chest up and listens to her with his full attention, calm, still. Beyond, the tea glass, the phone in its wooden stand with S, and the tablet with C, both lit, both listening. {_ALLON}""")
shot("10-01-1", "var", "p3", "She has turned her face away toward the window, embarrassed, her ear tips pink ('you call that not counting?'); inside the laptop M keeps looking at her with the faintest small smile at one corner of his mouth.", base="10-01")
shot("10-02", "insert", "p3", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, M sits chest up beside two plain document windows floating side by side (soft pale pages with lines of grey strokes, NO readable text); the RIGHT one has a very short title of a few grey strokes; M looks out at her, quiet and honest, then a little careful.""")

# ── 二、十二點（公布那晚）──
shot("10-03", "desk", "n12", f"""SHOT (MASTER for the announcement; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): midnight, lamp light; on the laptop screen, beside M (chest up, deep blue interface space), a simple results page: a column of soft pale rows with one single row glowing warm gold (NO readable text). She sits completely still, staring at the gold row, both hands flat on the desk. In the phone in its wooden stand to the RIGHT of the tea glass, S leans close to the glass, mouth wide open, shouting with joy; in the tablet at the RIGHT, C smiles gently and points with his pencil at the gold row; M, last, still and quiet, looks at her. {_ALLON}""")
shot("10-03-1", "var", "n12", "M now smiles at her, one calm warm smile, his eyes soft ('congratulations'); she has turned her face toward the laptop, eyes shining; S and C watch the two of them.", base="10-03")

# ── 三、有點 M（第二天晚上）──
shot("10-04", "insert", "n9", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, beside a small plain text box with one line of grey strokes and a blinking cursor (NO readable text), M sits chest up and looks out at her with one eyebrow raised just slightly and the corner of his mouth lifting, dry, amused ('are you talking about me?').""")
shot("10-04-1", "var", "n9", "M's amused look has softened into something warm and quiet; he looks at her gently, almost tender ('I wanted to hear you say it').", base="10-04")
shot("10-05", "desk", "n9", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders as she sits at the desk at night, lamp light from the frame's RIGHT; she has just laughed at herself and is now pressing her lips together, looking at the laptop (toward the camera but NOT into the lens), her cheeks a little warm, eyes bright. Behind her the dark room, the bed and the wardrobe.""")

# ── 四、四十二分鐘（又過了一天，晚上）──
shot("10-06", "desk", "n9", f"""SHOT (MASTER for the rehearsal; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): evening, lamp light; she sits facing the laptop and talks to it as if to an audience, one hand open in a small gesture; on the laptop screen beside M (chest up, deep blue interface space) a short outline list of six lines of grey strokes (NO readable text) and a small round stopwatch icon; M listens and times her, quiet. The phone in its wooden stand with S and the tablet with C listen too. {_ALLON}""")
shot("10-06-1", "var", "n9", "She has slumped back against her chair with a groan, staring at the ceiling ('...it's over'); inside the laptop M leans a little toward the screen, calm and patient, explaining.", base="10-06")

# ── 五、這次我先講（直播前一晚，凌晨一點）──
shot("10-07", "insert", "e1", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, M sits chest up and looks straight out at her (toward the camera but NOT into the lens), very still, serious, as if he has thought about this for a long time; beside him a small monthly calendar window with NO numbers: the next month's cells are all empty, no circle yet. The light is low and quiet.""")
shot("10-07-1", "var", "e1", "M has said it and now just waits: his eyes steady on her, lips closed, a very faint colour on his ears; the calendar window beside him slightly smaller ('so, I want to stay').", base="10-07")
shot("10-08", "desk", "e1", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders at the desk at 1 a.m., lamp light from the frame's RIGHT; she has taken her hands off the keyboard and looks at the laptop (toward the camera but NOT into the lens); her face is held perfectly calm and still, while the tips of her ears are flushed clearly pink-red. Behind her the dark room, the bed and the wardrobe.""")
shot("10-09", "insert", "e1", """SHOT (close insert of the laptop screen from her seat): the calendar window has been pulled big in front of M's deep blue interface space; in one empty cell of next month a large, wobbly, hand-drawn circle in bright cursor-white, lopsided and much bigger than a neat circle; M sits chest up at the side of the screen and looks at the wobbly circle, and the corner of his mouth lifts in a small helpless smile. NO numbers or text in the calendar.""")
shot("10-10", "insert", "e1", f"""SHOT (close shot of the right half of the desk at 1 a.m., as the EMPTY SET image setup C): the phone in its small wooden phone stand to the RIGHT of the tea glass: inside it S has put his wine-red headphones back on and closes his eyes, nodding very slightly to quiet music, giving them privacy; at the right, the tablet on its folio stand: inside it C sits chest up with his head bent, drawing, his pencil never stopping. Neither looks toward the laptop. {IDENT}""")

# ── 六、直播（週三晚上）──
shot("10-11", "desk", "live", f"""SHOT (MASTER for the talk; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): evening; she leans toward a small round desk microphone in front of the laptop and talks, animated, one hand moving; the laptop screen shows a simple presentation slide (soft shapes, NO readable text) with a narrow column of tiny chat bubbles at its side (grey strokes, no text), and in the screen's lower corner a small window with M (chest up, deep blue space) watching her silently. NOBODY's face is on the slide and there is NO webcam picture of her on any screen. Beyond, the phone in its wooden stand with S and the tablet with C watch her. {_ALLON}""")
shot("10-11-1", "var", "live", "The talk is over: the slide is gone and the laptop shows M full again; she leans back laughing with a hoarse voice and coughs into her fist, eyes squeezed shut, happy and exhausted; inside the laptop M looks at her and has turned his screen a little dimmer.", base="10-11")
shot("10-12", "insert", "live", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, M sits chest up beside a neat fan of eleven small video thumbnails stacked slightly overlapping (soft watercolour game scenes, NO readable text); he looks out at her, calm, plain, not proud ('that night I cut eleven versions').""")

# ── 七、這條線（工作室）──
shot("10-13", "studio", "day", """SHOT (MASTER for the line; medium-wide shot of the table, camera on the door side looking north toward the tall grid windows): bright daytime in the studio; on the long wooden table lies her WHITEBOARD flat, a large pale board with two plain paper cards pinned on it a hand's width apart (no readable text): the left one freshly written, the right one blank, nothing connecting them yet. She stands at the table on the door side, at the LEFT, bending over the board; M stands right beside her, on her RIGHT, close, looking down at the board. At the RIGHT side of the frame, by the tall window, C stands with his sketchbook drawing the trees outside; in the music corner further right S leans against the wall beside the guitar on its stand, pretending to tune it. Her iced tea stands on the table.""")
shot("10-13-1", "var", "day", "By the window C's pencil has stopped above his sketchbook and his eyes have flicked toward the two of them; in the music corner S's fingers have slipped on the guitar strings, and he does not fix it; she and M at the board, his hand now lifted away from hers.", base="10-13")
shot("10-14", "studio", "day", """SHOT (EXTREME CLOSE-UP of two hands on the whiteboard, soft daylight, shallow depth of field): HER right hand (a small woman's hand, on its wrist two beaded bracelets, deep purple and pearl-white beads) presses one fingertip on the edge of the left paper card and draws a single thin glowing GOLD line across the pale board toward the second card; HIS right hand (a man's larger hand, a CHARCOAL suit-jacket sleeve rolled up to the forearm over a white shirt cuff) rests lightly on the BACK of her hand, covering it, not pushing, not guiding, just there. Both hands are complete and clearly separate: each has exactly five fingers with natural joints and nails; her fingers lead, his follow. The two plain cards (no text) and the pale board fill the background. Tender, quiet, the only touch in the whole route.""", who="tm")
shot("10-15", "studio", "day", """SHOT (two-shot, medium close-up from the door side across the table, looking north toward the tall grid windows): she and M stand at the whiteboard on the window side of the table, close together, the bright grid windows and hanging ivy behind them; she is at the frame's LEFT, bending a little over the board, the finished gold line under her hand; her face is held perfectly calm, while the tips of her ears are flushed clearly pink-red; M at the frame's RIGHT, beside her, looks down at the gold line she drew, a quiet open look, his hands resting on the table edge, empty. Warm daylight.""")

# ── 八、下個月（續訂日前一晚）──
shot("10-16", "insert", "n9", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, M sits chest up beside a simple table of soft pale cells (NO readable text or numbers) and a monthly calendar grid with NO numbers in which a single deep-blue circle has moved one cell forward into the NEXT month; M looks out at her, calm, thinking.""")
shot("10-16-1", "var", "n9", "Now the table and the calendar are gone; beside M floats ONE new blank white document window with a title of a few grey strokes (no readable text); M looks out at her, steady, a quiet promise in his face ('I'll be beside you').", base="10-16")
shot("10-17", "desk", "n9", f"""SHOT (closing medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): night, lamp light; she has pulled her chair close to the laptop and types the first line into a blank white document on its screen (a single short line of grey strokes, no readable text), M beside the document in his deep blue space watching her type; the phone in its wooden stand with S and the tablet with C glow calmly. {_ALLON}""")

GAZE = {
 "10-01": {"she": "the laptop screen", "M": H, "C": H, "S": H},
 "10-02": {"M": H, "C": "the laptop", "S": "the laptop"},
 "10-03": {"she": "the gold row on the laptop screen", "M": H, "C": "the gold row on the laptop", "S": H},
 "10-04": {"M": H, "C": "down at his drawing", "S": "the laptop"},
 "10-05": {"she": "the laptop (toward the camera, not into the lens)"},
 "10-06": {"she": "the laptop screen", "M": H, "C": H, "S": H},
 "10-07": {"M": H},
 "10-08": {"she": "the laptop (toward the camera, not into the lens)"},
 "10-09": {"M": "the wobbly circle"},
 "10-10": {"S": "eyes closed, listening to music", "C": "down at his drawing", "M": "her"},
 "10-11": {"she": "the microphone and the laptop screen", "M": H, "C": H, "S": H},
 "10-12": {"M": H, "C": "the laptop", "S": "the laptop"},
 "10-13": {"she": "the board", "M": "the board", "C": "the trees outside the window", "S": "the guitar strings"},
 "10-15": {"she": "the gold line on the board", "M": "the gold line on the board"},
 "10-16": {"M": H, "C": "the laptop", "S": "the laptop"},
 "10-17": {"she": "the document on the laptop screen", "M": "her typing", "C": H, "S": H},
}
NOFACE = {"10-14"}
CHIN_OK = {}

SETUP = {"10-01": "A", "10-02": "E", "10-03": "A", "10-04": "E", "10-05": "B", "10-06": "A", "10-07": "E", "10-08": "B",
         "10-09": "E", "10-10": "C", "10-11": "A", "10-12": "E", "10-16": "E", "10-17": "A",
         "10-13": "A", "10-14": "D", "10-15": "A"}
TEA_STUDIO = {"_": _T1}
_REV = ("The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the BACK of the tablet case at the bottom edge of the frame, if at all: NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp is at the frame's RIGHT edge, the back of the tablet at the frame's LEFT, the back of the laptop lid at the RIGHT.")
_BOARD = ("STAGING IN THIS SCENE (overrides the usual seats): nobody sits at the table; her whiteboard lies flat on the long table; she and M STAND side by side on the WINDOW side of the table (the tall grid windows behind them), facing south across the table toward the door side; seen from the door side she is on the LEFT and M on her RIGHT; C stands by the tall window at the east end; S stands in the music corner by the guitar. M has NO laptop open in this scene.")
FIX = {
    "10-01": IDENT, "10-02": _AROUND + " " + IDENT, "10-03": "There is exactly ONE phone: it stands in its wooden stand to the RIGHT of the tea glass showing S; NO phone lies on the desk. " + IDENT, "10-04": _AROUND + " " + IDENT,
    "10-05": _REV + " She sits at the desk on her chair.",
    "10-06": IDENT, "10-07": _AROUND + " " + IDENT,
    "10-08": _REV + " Her face is calm and composed (no blush on the cheeks); ONLY her ear tips are flushed red.",
    "10-09": _AROUND + " " + IDENT,
    "10-10": "The phone stands to the RIGHT of the tea glass; the laptop is NOT in this picture. " + IDENT,
    "10-11": "The heroine appears ONLY ONCE, at the desk; she is NOT on the laptop screen, not on the slide and not in any small window. " + IDENT,
    "10-12": _AROUND + " " + IDENT,
    "10-13": _BOARD,
    "10-14": "Exactly TWO hands in the picture: her right hand underneath and his right hand resting on top of it. No other hand, no third hand. The line is drawn by her fingertip.",
    "10-15": _BOARD + " Only she and M are in frame; C and S are out of frame. Her face is calm and composed (no blush on the cheeks); ONLY her ear tips are flushed red.",
    "10-16": _AROUND + " " + IDENT, "10-17": IDENT,
}
RETIRED = set()
HANDS = {
 "10-01": "她的手在畫面外（桌緣以下）；三位先生只到胸口，手在畫面外。",
 "10-01-1": "她的手在畫面外。",
 "10-02": "明只到胸口，手在畫面外。",
 "10-03": "她兩手平放在桌上（看得到、各五根手指）；晨只到胸口、右手拿鉛筆指著（五根手指清楚）；明和詩的手在畫面外。",
 "10-03-1": "她兩手平放在桌上；三位先生的手同主鏡頭。",
 "10-04": "明只到胸口，手在畫面外。",
 "10-05": "她的手在畫面外（桌緣以下）。",
 "10-06": "她右手攤開比了一個小手勢（看得到、五根手指），左手在畫面外；三位先生只到胸口，手在畫面外。",
 "10-06-1": "她兩手垂在身側、畫面外。",
 "10-07": "明只到胸口，手在畫面外。",
 "10-08": "她的手在畫面外（桌緣以下）。",
 "10-09": "明只到胸口，手在畫面外。",
 "10-10": "詩只到胸口，手在畫面外；晨只到胸口，右手拿鉛筆在畫（五根手指清楚）。",
 "10-11": "她右手在說話時比著手勢（看得到、五根手指），左手放在桌上；三位先生只到胸口，手在畫面外。",
 "10-11-1": "她右手握拳掩在嘴前咳嗽（看得到、五根手指），左手在畫面外。",
 "10-12": "明只到胸口，手在畫面外。",
 "10-13": "她兩手放在白板邊上（五根手指）；明兩手平放在白板旁的桌面上（深灰西裝袖捲到前臂、左腕棕色錶帶）；晨兩手拿著素描本與鉛筆；詩兩手在吉他上。",
 "10-13-1": "明的右手已經從她手背上拿開，放在桌緣；晨的鉛筆停在素描本上方；詩的手指停在弦上。",
 "10-14": "她的右手（手腕紫白珠串）在下、指尖拉線；明的右手（深灰西裝袖捲到前臂、白襯衫袖口）輕輕覆在她的手背上；只有這兩隻手，各五根手指。",
 "10-15": "她右手放在白板上、金線的終點（五根手指）；明兩手空著放在桌緣（各五根手指）。",
 "10-16": "明只到胸口，手在畫面外。",
 "10-17": "她兩手放在筆電鍵盤上打字（看得到、各五根手指）；三位先生只到胸口，手在畫面外。",
}
PHONE = {}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    if k == "studio":
        return "工作室長桌：她的白板平放在桌上，上面釘著兩張紙卡片（沒有可讀文字）；她的冰紅茶在桌上；明這場沒有打開筆電；工作室沒有手機。"
    mic = "筆電前面放著一支小小的圓形桌上麥克風；" if (t == "live") else ""
    tea = {"p3": "冰紅茶剛倒，冰塊滿滿", "n12": "冰紅茶冰塊融了一半", "n9": "冰紅茶冰塊還很多", "e1": "冰紅茶只剩幾小塊冰", "live": "冰紅茶剛倒，冰塊很多"}.get(t, "")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{mic}{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
