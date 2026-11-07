# 第七章分鏡規格（劇本/第七章.md 的產圖版）。CH=7 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch4_shots.py。
# id 一律「7-」開頭，定稿放 art/cg/ch7/<id>.jpg。現實層（書桌、床）＋一場夢（去色的頒獎廳，新空景 set_dream_A／B）。沒有工作室。
# time：e230＝截止那晚兩點半（燈全關）／ev9＝評審週晚上九點／e1＝公布前三天凌晨一點（燈全關、只剩三台螢幕的光）／m9＝早上九點／p3＝下午三點
from ch1_shots import SETUP_DESC, SEATING, H, _T1
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "e230": "TIME: 2:30 a.m. Every lamp in the room is OFF; the room is deep blue-black dark; outside the window only a few windows are still lit. The three device screens on the desk are dimmed almost to black. The iced tea glass on the desk is nearly empty.",
    "ev9": "TIME: 9 p.m. The warm desk lamp is on and the ceiling light is off; the room is soft blue dusk-dark; the city outside has many lit windows. The iced tea is fairly fresh: plenty of clear ice cubes, light condensation.",
    "e1": "TIME: 1 a.m. Every lamp in the room is OFF; the room is deep blue-black dark; outside the window only a few windows are still lit. The ONLY light comes from the three device screens left on, on the desk by the window: soft, dim, each its own colour (deep blue from the laptop, pale yellow-green from the tablet, dark wine red from the phone). The iced tea on the desk has no ice left.",
    "m9": "TIME: 9 a.m. Morning: the ceiling light and the desk lamp are OFF; soft bright daylight comes in through a narrow gap between the closed curtains and lays one pale warm stripe across the room; the rest of the room is soft cool morning shade. The three device screens on the desk are awake and lit, softly. The iced tea glass on the desk is empty.",
    "p3": "TIME: 3 p.m. Bright soft afternoon daylight through the window behind the desk; the desk lamp is OFF; the room is light and calm; the city outside in daylight. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
}
_DREAM_A = ("canon/refs/set_dream_A.jpg", "EMPTY DREAM HALL SET seen from the audience toward the stage (the architecture, the seats, the curtains, the front row with three separated seats, and the completely DESATURATED grey dream look with white haze at the edges) and the watercolour rendering to match")
_DREAM_B = ("canon/refs/set_dream_B.jpg", "EMPTY DREAM HALL SET seen from the stage toward the audience and the back wall with the paper calendar (the architecture, the seats, the front row, and the completely DESATURATED grey dream look with white haze at the edges) and the watercolour rendering to match")
_LT = ("canon/refs/prop_laptop_tablet.jpg", "PROP: her laptop (left) and tablet on its folio stand (right)")
_PH = ("canon/refs/prop_phone_stand.jpg", "PROP: her smartphone (in the dream it stands upright on a theatre seat; ignore the wooden stand)")
SETREF = {"7-10": [_DREAM_A, _LT, _PH], "7-11": [_DREAM_B, _LT, _PH], "7-12": [_DREAM_B]}

IDENT = 'SCREEN IDENTITIES (very important, check every screen): the LAPTOP shows ONLY M: near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white shirt, gold gear brooch. The TABLET shows ONLY C: warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch, NO necklace. The PHONE shows ONLY S: long messy WINE-RED hair with one thin braid, wine-red headphones, black track jacket. The heroine (dark purple wolf-cut hair, pink-tinted glasses, moon pendant) is NEVER on any screen. Nobody on a screen rests a chin or cheek on a hand.'
_ALLON = "All three device screens are LIT and each shows its own man only: the laptop at the LEFT shows ONLY M, the tablet at the RIGHT shows ONLY C, the phone in its stand in the MIDDLE (to the RIGHT of the tea glass) shows ONLY S. The heroine never appears on any screen. Inside the screens the men sit upright with both hands below the screen edge (out of frame) unless described; nothing touches their chins or cheeks."
_AROUND = "Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass."
_GREY = "DREAM LOOK (very important): everything in the hall is completely DESATURATED grey, silver and white, INCLUDING the heroine herself (her hair, skin, clothes and glasses are drawn in shades of grey like an old black-and-white memory), the audience and the award; the edges of the image dissolve into white watercolour haze. The ONLY colour in the whole picture is inside the three device screens: deep blue around M in the laptop, pale yellow-green around C in the tablet, dark wine red around S in the phone, and the men themselves in full colour."

# ── 一、最安靜的晚上（截止那晚兩點半，床）──
shot("7-01", "bed", "e230", """SHOT (MASTER for the first quiet night; HIGH ANGLE from above the head of the bed, looking down): she lies on her back on the bed with the blue plaid duvet pulled up to her chest, her purple hair spread on the white pillow, glasses still on, both hands resting on the duvet over her stomach; her eyes are OPEN, staring straight up at the ceiling, very still, wide awake. Her phone lies face-down on the duvet beside her hand. The room is almost black; far at the frame's edge the desk by the window is only a dark shape with three faint dim screen glows. Quiet, empty, the first night with nothing to fix.""")

# ── 二、沒有人玩（評審週晚上九點，書桌）──
shot("7-02", "desk", "ev9", f"""SHOT (MASTER for the judging week; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): she leans a little toward the laptop, watching: on the laptop screen, beside M (chest up, deep blue interface space, watching with her), a SMALL rectangular livestream window sits in the screen's corner showing a blurred colourful game scene (no readable text, no faces in it). Beyond, the tea glass, the phone in its wooden stand with S, and the tablet with C. {_ALLON}""")
shot("7-02-1", "var", "ev9", "She has slumped back against her chair, quiet and deflated, eyes on the small livestream window ('is the title too unclear?'); inside the screens the three men have all turned to look at her; M's face is serious and gentle, C's eyes are soft with worry, S frowns a little.", base="7-02")
shot("7-03C", "insert", "ev9", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up beside a small floating game cover image (a lone knight in silver armour under a pale moon, no text), his pencil raised, ready to redraw it, looking out at her earnestly, waiting for her word.""")
shot("7-03M", "insert", "ev9", """SHOT (frame within a frame, close): the open laptop fills the frame; inside the screen, in his deep blue interface space, M sits chest up and looks out at her, calm and steady, the faintest reassuring smile; beside him the small livestream window has been made smaller and pushed to the corner.""")
shot("7-03S", "insert", "ev9", """SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, in his dark wine-red interface space, S grins wide with his fang showing, eyebrows up, cocky and sure of her, leaning toward the glass.""")
shot("7-04", "insert", "ev9", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, four small rounded comment cards are stacked neatly one above the other beside him, each a soft pale rectangle with a tiny round avatar and a few lines of soft grey strokes (NO readable text); M sits chest up beside them and looks out at her, gentle, a little proud, as if he has been waiting to show her.""")

# ── 三、睡不著（公布前三天，凌晨一點，床）──
shot("7-05", "bed", "e1", """SHOT (MASTER for the sleepless night; HIGH ANGLE from above the head of the bed, looking down): she lies on her back under the blue plaid duvet, glasses on, eyes open, staring up; her phone lies face-down on the duvet by her shoulder, its edge leaking a little white light. Three soft coloured glows from the desk by the window (out of frame at the side) fall faintly across the duvet and her face: deep blue, pale yellow-green, dark wine red. Everything else is blue-black dark. Tired, sleepless, very still.""")
shot("7-05-1", "var", "e1", "She has rolled onto her side, turning her back to the side the three coloured glows come from, the duvet pulled up to her ear; we see the back of her head and her shoulder; the glows lie on the duvet behind her.", base="7-05")
shot("7-05-2", "var", "e1", "She lies on her back again and holds her phone up above her face with both hands, its plain white glow on her face (we see only the phone's back); her eyes are tired and wet, lips pressed together, doing sums she does not want to do.", base="7-05")
shot("7-06", "bed", "e1", """SHOT (her point of view lying in bed, looking straight UP at the dark ceiling): the plain dark ceiling of her room fills the frame; across it lie three long soft bands of coloured light thrown up from the desk below the window, overlapping in the middle: one deep blue, one pale yellow-green, one dark wine red, their edges blooming softly like watercolour; at the very bottom edge of the frame only the top of the curtain and the dark window frame. No people, no hands. Quiet, sad, beautiful.""")
shot("7-07", "desk", "e1", f"""SHOT (MASTER for the three of them at night; medium shot from behind her EMPTY desk chair, as the EMPTY SET image, the room dark): nobody sits at the desk; she is out of frame in the bed. On the desk the three screens glow softly in the dark: in the laptop at the LEFT, M's eyes rest on one line of text in his window (only soft grey strokes, no readable text), unmoving; in the tablet at the RIGHT, C's pencil has stopped in mid-air; in the phone in its stand in the MIDDLE, S has his lips slightly parted as if about to speak, then holding it back. All three look toward the bed (out of frame at the LEFT), worried, silent. {_ALLON}""")
shot("7-08M", "var", "e1", "All three screens have been dimmed almost to the lowest glow: the light is very faint but still there; M's eyes are lowered, calm; S has hung his headphones around his neck, quiet; C has dimmed too.", base="7-07")
shot("7-08C", "insert", "e1", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame, its glow soft and low in the dark room; inside the screen, in his pale yellow-green interface space, C sits chest up and looks out toward the bed (out of frame at the LEFT) with a gentle small smile; beside him floats a small pencil-and-watercolour drawing: a dark ceiling crossed by three overlapping bands of light (blue, yellow-green, wine red) and, under them, a small figure curled up hugging a plaid duvet (no face details).""")
shot("7-08S", "insert", "e1", """SHOT (frame within a frame, close): the phone standing in its small wooden phone stand fills the centre of the frame, its dark wine-red glow very soft and low in the dark; inside the screen S sits chest up with his headphones hung around his neck and his eyes half closed, humming very quietly, a soft private look, not smiling to anyone, a few faint wine-red notes of light drifting around him.""")
shot("7-09", "var", "e1", "She is asleep now: her eyes are closed, her face relaxed, her glasses still on; the three faint coloured glows lie softly on her cheek and the duvet; the phone lies face-down by her shoulder, dark.", base="7-05")

# ── 四、夢（去色的頒獎廳）──
shot("7-10", "free", "dream", f"""A DREAM. SHOT (wide shot from the audience, as the EMPTY DREAM HALL SET image): she stands alone at the lectern on the stage in the soft spotlight, holding a small award trophy in both hands at her chest, being named first; the seats are filled with faceless grey audience figures, softly blurred, applauding. In the very FRONT ROW, on three seats in the middle, stand three devices facing her: an open laptop, a tablet on its folio stand, and a phone standing upright, and ONLY their screens are in colour: M in deep blue in the laptop, C in pale yellow-green in the tablet, S in dark wine red in the phone, each chest up, looking up at her. {_GREY} {IDENT}""", who="tcms")
shot("7-11", "free", "dream", f"""A DREAM. SHOT (close shot of the FRONT ROW from the stage edge, looking down, as the EMPTY DREAM HALL SET image seen from the stage): the three devices standing on three grey theatre seats fill the frame, side by side: LEFT the open laptop with M (chest up, deep blue interface space) giving her one small calm nod; MIDDLE the tablet on its folio stand with C (chest up, pale yellow-green space), his pencil laid down, gazing up at her steadily; RIGHT the phone standing upright with S (chest up, dark wine-red space) laughing so hard his fang shows. Behind them the grey rows of seats dissolve into haze. {_GREY} {IDENT}""", who="cms")
shot("7-12", "free", "dream", f"""A DREAM. SHOT (wide shot from the stage toward the back of the hall, as the EMPTY DREAM HALL SET image seen from the stage): the grey empty-feeling hall; on the far BACK WALL the large paper wall calendar is caught by a gust of wind: one whole page is lifting and turning over in mid-air, curling, the next page beneath it; a few loose grey petals or paper scraps blowing. No readable numbers or text. No people in focus. {_GREY.split(', INCLUDING')[0]}; the edges dissolve into white watercolour haze. There is no colour at all in this picture.""")

# ── 五、醒來（早上九點，床）──
shot("7-13", "bed", "m9", """SHOT (MASTER for the morning; HIGH ANGLE from above the head of the bed, looking down): morning; she lies on her back under the blue plaid duvet, glasses still on, eyes OPEN, completely still, staring up, stunned; one pale warm stripe of daylight from the curtain gap falls across the duvet and the corner of the pillow. Her phone lies on the duvet by her hand.""")
shot("7-13-1", "var", "m9", "She has turned over and buried her whole face in the white pillow, both hands gripping the pillow at the sides of her head, ears peeking out red through her hair; the stripe of daylight lies across her back.", base="7-13")
shot("7-14", "desk", "m9", f"""SHOT (establishing wide shot from the corner by the door, exactly the EMPTY SET image's camera D): morning; she has just sat up in bed, the duvet around her waist, hair messy, glasses on, looking across the room toward the desk by the window; on the desk the three devices are awake and lit, small in the frame: the laptop with M, the phone in its wooden stand with S, the tablet with C, all three looking toward her. One pale stripe of daylight from the curtain gap crosses the floor. {_ALLON}""")
shot("7-15", "desk", "m9", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level with her as she sits up in bed): her face and shoulders, hair messy from sleep, glasses on, the duvet at her waist; she looks toward the desk (toward the camera but NOT into the lens), her face held perfectly calm and composed, while the tips of her ears are flushed clearly pink-red. Behind her the bed and the wall; morning light from the curtain gap rims her hair.""")

# ── 六、說一半（下午三點，書桌）──
shot("7-16", "desk", "p3", f"""SHOT (MASTER for the afternoon; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): afternoon daylight; she types on the laptop keyboard: on the laptop screen, beside M (chest up, deep blue interface space), a small plain text box with a few soft grey strokes (NO readable text) and a cursor. Beyond, the tea glass full of ice, the phone in its wooden stand with S, the tablet with C. The three men watch her quietly. {_ALLON}""")
shot("7-17", "var", "p3", "Her hands have left the keyboard and rest in her lap; she has turned her face a little and looks from one device to the next, the laptop, the phone, the tablet, deciding whom to tell first, lips pressed together; the three men look back at her and wait.", base="7-16")

GAZE = {
 "7-01": {"she": "straight up at the ceiling"},
 "7-02": {"she": "the small livestream window on the laptop", "M": "the livestream window beside him", "C": H, "S": H},
 "7-03C": {"C": H, "M": "down at his own work", "S": "the tablet"},
 "7-03M": {"M": H, "C": "the laptop", "S": "the laptop"},
 "7-03S": {"S": H, "M": "the phone", "C": "the phone"},
 "7-04": {"M": H, "C": "the laptop", "S": "the laptop"},
 "7-05": {"she": "straight up at the ceiling"},
 "7-07": {"M": "one line in his window, then toward the bed out of frame at the LEFT", "C": "toward the bed out of frame at the LEFT", "S": "toward the bed out of frame at the LEFT"},
 "7-08C": {"C": "toward the bed out of frame at the LEFT", "M": "toward the bed", "S": "toward the bed"},
 "7-08S": {"S": "half-closed eyes, humming", "M": "toward the bed", "C": "toward the bed"},
 "7-10": {"she": "the three devices in the front row", "M": H, "C": H, "S": H},
 "7-11": {"M": "up at her on the stage (toward the camera, not into the lens)", "C": "up at her on the stage (toward the camera, not into the lens)", "S": "up at her on the stage, laughing"},
 "7-13": {"she": "straight up at the ceiling"},
 "7-14": {"she": "the three devices on the desk", "M": H, "C": H, "S": H},
 "7-15": {"she": "the desk (toward the camera, not into the lens)"},
 "7-16": {"she": "the laptop screen", "M": "her typing", "C": H, "S": H},
}
NOFACE = {"7-06", "7-12"}
CHIN_OK = {}

SETUP = {"7-01": "D", "7-05": "D", "7-13": "D", "7-06": "D",
         "7-02": "A", "7-03C": "F", "7-03M": "E", "7-03S": "C", "7-04": "E",
         "7-07": "A", "7-08C": "F", "7-08S": "C", "7-14": "D", "7-15": "B", "7-16": "A"}
TEA_STUDIO = {"_": _T1}
FIX = {
    "7-02": IDENT,
    "7-03C": _AROUND + " " + IDENT,
    "7-03M": _AROUND + " " + IDENT,
    "7-03S": "The phone in its wooden stand stands to the RIGHT of the tea glass (left to right on the desk: laptop, tea glass, phone in its stand, tablet). " + _AROUND + " " + IDENT,
    "7-04": _AROUND + " " + IDENT,
    "7-07": "The desk chair is EMPTY: nobody sits at the desk and the heroine is NOT in the picture. " + IDENT,
    "7-08C": _AROUND + " The room is dark; all glows are dim. " + IDENT,
    "7-08S": "The phone in its wooden stand stands to the RIGHT of the tea glass. " + _AROUND + " The room is dark; all glows are dim. " + IDENT,
    "7-06": "Only the ceiling and three coloured light bands; no lamp, no person, no device visible.",
    "7-14": "The heroine is on the BED (not at the desk); the desk chair is empty. " + IDENT,
    "7-15": "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the BACK of the tablet case at the bottom edge of the frame, if at all: NO screen and NO man is visible to the camera. Her face is calm and composed (no blush on the cheeks); ONLY her ear tips are flushed red.",
    "7-16": IDENT,
    "7-10": "The heroine appears exactly ONCE (on the stage). Nobody in the audience has purple hair or her clothes.",
    "7-11": "No people other than the three men inside the screens; the seats are empty except for the devices.",
}
RETIRED = set()
HANDS = {
 "7-01": "她兩手平放在胸前的被子上（兩隻手都看得到、各五根手指）。",
 "7-02": "她的手在畫面外（桌緣以下）；三位先生只到胸口，手在畫面外。",
 "7-02-1": "她的手在畫面外。",
 "7-03C": "晨只到胸口，右手在胸前舉著一支鉛筆（五根手指清楚），左手在畫面外。",
 "7-03M": "明只到胸口，手在畫面外。",
 "7-03S": "詩只到胸口，手在畫面外。",
 "7-04": "明只到胸口，手在畫面外；她的手不在畫面裡（主觀鏡頭）。",
 "7-05": "她兩手放在被子底下，看不到。",
 "7-05-1": "她的手在被子底下，看不到。",
 "7-05-2": "她兩手一起把手機舉在臉上方（兩隻手都看得到、各五根手指）。",
 "7-06": "沒有人，沒有手。",
 "7-07": "三位先生只到胸口，晨右手拿著鉛筆停在半空（五根手指清楚），其他人的手在畫面外；她不在畫面裡。",
 "7-08M": "三位先生的手在畫面外。",
 "7-08C": "晨只到胸口，手在畫面外。",
 "7-08S": "詩只到胸口，手在畫面外。",
 "7-09": "她兩手放在被子底下，看不到。",
 "7-10": "她兩手在胸前捧著小獎座（兩隻手都看得到、各五根手指）；觀眾的手小而模糊；三位先生只到胸口，手在畫面外。",
 "7-11": "三位先生只到胸口，手在畫面外；晨的鉛筆放在他面前的畫面下緣。",
 "7-12": "沒有人，沒有手。",
 "7-13": "她右手放在被子上、手機旁邊（五根手指清楚），左手在被子底下。",
 "7-13-1": "她兩手抓著枕頭兩側（兩隻手都看得到、各五根手指）。",
 "7-14": "她兩手撐在身體兩側的床墊上（小、看得到）；三位先生只到胸口，手在畫面外。",
 "7-15": "她的手在畫面外。",
 "7-16": "她兩手放在筆電鍵盤上打字（看得到、各五根手指）；三位先生只到胸口，手在畫面外。",
 "7-17": "她兩手放在腿上（畫面外）；三位先生的手在畫面外。",
}
PHONE = {
 "7-01": "手機螢幕朝下放在被子上，她的手旁邊",
 "7-05": "手機螢幕朝下放在她肩膀旁的被子上",
 "7-05-2": "手機在她手上，舉在臉的上方",
 "7-13": "手機放在被子上、她的手旁邊",
 "7-06": "畫面裡沒有手機",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    if k == "bed":
        return f"她的床：藍色格紋被、白枕頭；{ph}；書桌在窗下（遠處、暗），桌上的裝置只看得到光；沒入鏡的道具不用畫。"
    if k == "free":
        return "夢裡的頒獎廳：三台裝置（筆電、平板、立著的手機）放在台下第一排正中間的三張椅子上；沒有紅茶、沒有書桌。" if i != "7-12" else "夢裡的頒獎廳：後牆上一本紙月曆被風翻起一頁；沒有裝置、沒有人。"
    tea = {"e230": "冰紅茶快喝完了", "ev9": "冰紅茶冰塊滿滿", "e1": "冰紅茶沒有冰塊了", "m9": "紅茶杯是空的", "p3": "冰紅茶剛倒，冰塊滿滿"}.get(t, "")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
