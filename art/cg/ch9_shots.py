# 晨線〈兩個月〉分鏡規格（劇本/個人線_C.md 的產圖版）。CH=9 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch7_shots.py。
# id 一律「9-」開頭，定稿放 art/cg/ch9/<id>.jpg。現實層（書桌、床）＋工作室一場（全線唯一一次碰觸：鉛筆放進她手裡）。
# time：p3＝公布前一天下午三點／n12＝公布那晚午夜（檯燈）／d5＝得獎那晚到天亮（床，燈全關，窗簾縫由深藍變灰再變淡粉）／n9＝晚上九點／n11＝深夜／day＝工作室
from ch1_shots import SETUP_DESC, SEATING, H, _T1
from ch7_shots import IDENT, _ALLON, _AROUND
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "p3": "TIME: 3 p.m. Bright soft afternoon daylight through the window behind the desk; the desk lamp is OFF; the room is light and calm; the city outside in daylight. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
    "n12": "TIME: midnight. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "n11": "TIME: 11 p.m. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea has a few small ice cubes left.",
}
_D = "TIME: just before dawn. Every lamp in the room is OFF; the room is deep blue-grey dark; the curtains are CLOSED except one narrow vertical gap. The only light is the soft pale yellow-green glow of the tablet beside her pillow and the gap in the curtains."
_ROOM = ("canon/refs/set_desk_D.jpg", "EMPTY SET of her room (the bed with the blue plaid duvet and white pillow under the bookshelf, the desk by the window, the wardrobe): the room, the bed and the watercolour rendering to match; this shot's camera is close to the bed")
_LT = ("canon/refs/prop_laptop_tablet.jpg", "PROP: her tablet on its dark charcoal folio stand (the right-hand device in this image; ignore the laptop)")
_WIN = ("canon/refs/set_desk_A.jpg", "EMPTY SET of her room seen toward the window with its curtains (the window frame, the curtains and the watercolour rendering to match)")
SETREF = {"9-06": [_ROOM, _LT], "9-07": [_WIN]}

# ── 一、妳沒講妳是什麼顏色（公布前一天下午，書桌）──
shot("9-01", "desk", "p3", f"""SHOT (MASTER for the dream story; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): afternoon daylight; she sits turned a little sideways on her desk chair with her knees drawn up, and the TABLET (taken off its stand, in its dark charcoal folio cover) rests against her knees, its screen toward her and the camera: inside it, in his pale yellow-green interface space, C sits chest up, head bent, drawing with his pencil while he listens. On the desk beyond: the laptop at the LEFT with M and the phone standing in its wooden stand to the RIGHT of the tea glass with S, both lit, both watching her. She is talking, describing her dream, her face turned toward the tablet.""")
shot("9-01-1", "var", "p3", "She has stopped mid-sentence and looks down at the tablet a little shyly ('only you three had colour'); inside the tablet C keeps drawing without looking up; M and S watch her quietly.", base="9-01")
shot("9-02", "insert", "p3", """SHOT (close insert, the tablet screen fills the frame, slim bezel and charcoal folio edge at the borders): C's finished drawing fills most of the screen: a soft pencil-and-watercolour picture of a grey dream award hall, grey audience, grey lights; in the front row three small glowing screens in deep blue, pale yellow-green and wine red; and on the stage a small girl with dark purple wolf-cut hair, an off-white T-shirt and pale pink-tinted round glasses — the ONLY figure painted in full soft colour. In the lower corner of the screen, small, C sits chest up in his yellow-green space and looks out at her, quiet, a little shy. No readable text.""")

# ── 二、十二點（公布那晚，書桌）──
shot("9-03", "desk", "n12", f"""SHOT (MASTER for the announcement; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): midnight, lamp light; on the laptop screen, beside M (chest up, deep blue interface space), a simple results page: a column of soft pale rows with one single row glowing warm gold (NO readable text). She has put her phone down and presses BOTH hands over her mouth, frozen, staring at the gold row. In the phone in its wooden stand to the RIGHT of the tea glass, S leans close to his screen glass, eyes wide, mouth open, about to shout; in the tablet at the RIGHT, C sits very still, looking at her. {_ALLON}""")
shot("9-03-1", "var", "n12", "Now all three men smile at her: S grins wide with his fang showing; M gives one calm warm smile; C, last, smiles softly with his eyes. She still has both hands pressed over her mouth, her eyes wet and shining.", base="9-03")

# ── 三、朝霞（得獎那晚到天亮，床）──
shot("9-06", "free", "dawn", f"""SHOT (MASTER for the dawn; close medium shot at the height of the bed, from the side of the bed, looking along the pillow): just before dawn in her dark room; she lies on her side under the blue plaid duvet, pulled up to her shoulder, her head on the white pillow, glasses still on, awake, talking softly; right beside the pillow her TABLET stands on its dark charcoal folio stand on the mattress, its screen toward her: inside it, in his soft pale yellow-green interface space, C sits chest up and looks at her with a gentle sleepy-warm look, keeping her company. The tablet's glow lies on her face. Behind the bed, the closed curtains with one narrow vertical gap of deep blue sky. {_D} The laptop and the phone are NOT in this picture.""", who="tc")
shot("9-06-1", "var", "dawn", "The gap in the curtains has turned from deep blue to soft grey and then to a very pale pink; she has turned her head on the pillow toward the window, eyes wide, lips parted ('...the morning glow'); inside the tablet C has turned toward the window too.", base="9-06")
shot("9-07", "free", "dawn", """SHOT (close shot from her bed toward the window, low): the closed curtains with ONE narrow vertical gap; through the gap the sky outside glows with the first soft dawn colours: pale grey melting into very pale pink and peach above the dark city rooftops, a few windows still lit. The room around the gap is deep blue-grey dark. On the right edge of the frame, the soft yellow-green glow of the tablet's corner, out of focus. No people, no hands. Quiet, tender. TRANSPARENT WATERCOLOUR, wet-in-wet sky.""")

# ── 四、某個 AI（兩天後晚上，書桌）──
shot("9-08", "insert", "n9", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up beside a small floating screenshot of a dialogue card (a soft pale rectangle with a few lines of grey strokes, NO readable text) where one tiny spot is circled in yellow-green pencil; he points at the circle with the tip of his pencil and looks out at her, plain and helpful.""")
shot("9-08-1", "var", "n9", "C has lowered his pencil and looks out at her a little shyly, the corners of his mouth lifting, eyes asking ('is that \"some AI\" me?'); a faint pink on his cheeks.", base="9-08")

# ── 五、黑歷史（那天晚上，書桌）──
shot("9-09", "insert", "n11", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up and looks very closely, seriously and kindly, at five small old illustrations floating beside him in a row: her old hand-drawn game pages from two years ago — thin careful lines, a girl character, colours laid carefully, a few places where the colour goes over the lines; the third one shows a hand drawn and erased many times (fuzzy, overworked lines). No readable text.""")
shot("9-10", "desk", "n11", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders as she sits at the desk at night, lamp light from the frame's RIGHT; she looks toward the tablet (toward the camera but NOT into the lens), quiet, then decided: her eyes hold a small brave light, lips pressed together ('the sixth one, I want to draw it myself'). Behind her the dark room, the bed and the wardrobe.""")

# ── 六、妳沒要的那些（第二天深夜，書桌）──
shot("9-11", "insert", "n11", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; on its screen a shared folder lies open as a soft grid of many pale PENCIL sketches, all of the same girl with dark purple wolf-cut hair and round glasses: sitting at a desk, asleep on an open textbook, biting a straw while looking at a screen, laughing with her head down on the desk — many of them, light, loving, unfinished. In the lower corner, small, C sits chest up in his yellow-green space and has turned his face away to the side, embarrassed, pushing up his glasses with one finger. No readable text.""")
shot("9-12", "insert", "n11", """SHOT (frame within a frame, close-up): the tablet screen fills the frame; inside, in his pale yellow-green interface space, C sits chest up very close to the screen glass and looks straight out at her (toward the camera but NOT into the lens), soft and earnest; his pencil, held loosely in his right hand at chest height, has stopped halfway through a twirl; his lips are just parting, saying the plain true thing ('...I think I like you'). Warm, quiet, no smile yet.""")
shot("9-12-1", "var", "n11", "C has frozen: his eyes widen behind his glasses as he realises what he just said out loud, his cheeks and ears turning pink, the pencil still stopped in his fingers ('...did I just say that?').", base="9-12")
shot("9-13", "desk", "n11", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders at the desk at night, lamp light from the frame's RIGHT; she looks at the tablet (toward the camera but NOT into the lens); her face is held perfectly calm and still, almost expressionless, while the tips of her ears are flushed clearly pink-red. Behind her the dark room, the bed and the wardrobe.""")
shot("9-13-1", "var", "n11", "She has picked up the tablet off its stand and hugs it to her chest, the dark charcoal BACK of its folio cover toward the camera, her chin resting on its top edge; her face still calm, her ears still red, her eyes looking down at the screen she is hiding.", base="9-13")
shot("9-14", "insert", "n11", f"""SHOT (close shot of the right half of the desk at night, as the EMPTY SET image setup C): the phone standing in its small wooden phone stand to the RIGHT of the tea glass: its screen is very DIM, and inside it S sits chest up with his eyes firmly CLOSED and his lips pressed together, pretending to be asleep, one corner of his mouth twitching; behind, the edge of the laptop with its screen turned down to the lowest dim glow, M barely visible, eyes lowered. The tablet is NOT in this picture. {IDENT}""")

# ── 七、第六張（工作室）──
shot("9-16", "studio", "day", """SHOT (MASTER for the sixth picture; medium-wide shot of the table, camera on the door side looking north toward the tall grid windows): afternoon light pours through the windows; on the long wooden table lies a NEW sketchbook open to a blank first page. C sits on his wooden chair at the EAST end of the WINDOW side (the RIGHT of the frame) and she sits right beside him on his LEFT on her red chair, which she has pulled around to the window side; they lean together over the blank page. At the far WEST end of the window side (the LEFT of the frame) M sits on his white chair typing on his own space-grey laptop, not looking. In the foreground at the RIGHT, S sits sprawled on his green chair on the door side with his wine-red headphones around his neck, his back half to the camera, arms folded on the table, not looking. Her iced tea stands on the table beside her.""")
shot("9-16-1", "var", "day", "S has buried his face in his folded arms on the table, his shoulders shaking with suppressed laughter; at the far left M's hands have paused above his keyboard for a beat, his eyes not moving from his screen; C and she still bend over the sketchbook.", base="9-16")
shot("9-17", "studio", "day", """SHOT (EXTREME CLOSE-UP of two hands over the blank sketchbook page, soft afternoon window light, shallow depth of field): HIS right hand (a young man's hand, a warm CAMEL knit cardigan cuff with ONE thin YELLOW-GREEN stripe at the wrist) is placing a freshly sharpened wooden pencil into HER open right palm (a small woman's hand, palm up, fingers relaxed; on her wrist two beaded bracelets, deep purple and pearl-white beads); the tip of his index finger is just touching the centre of her palm for one instant. Both hands complete and clearly separate: each has exactly five fingers with natural joints and nails; his hand comes from the RIGHT of the frame, hers from the LEFT-bottom. The blank white page with paper grain fills the background. Tender, quiet, the only touch in the whole route.""", who="tc")
shot("9-18", "studio", "day", """SHOT (close shot looking down at the blank sketchbook page): HER right hand (two beaded bracelets on the wrist, deep purple and pearl-white) holds the pencil and has just drawn ONE first line on the empty white page: a single soft graphite line that wobbles and goes a little crooked; she has not erased it. Only her one hand is in frame, five fingers, natural grip. In the very lower right corner of the page a tiny pencil mark of a few unreadable strokes. Paper grain, afternoon light across the page.""")
shot("9-19", "studio", "day", """SHOT (two-shot, medium close-up from across the table, camera on the door side): she and C sit side by side on the WINDOW side of the table, the tall grid windows bright behind them; she is on HIS LEFT (the LEFT of the frame). She looks down at her crooked line on the sketchbook with her face held perfectly calm, while the tips of her ears are flushed clearly pink-red; she holds the pencil in her right hand above the page. C, beside her, looks at the page — at her line — with a soft open smile, his hands resting on the table, empty. Sunlight between them.""")

# ── 八、圈（續訂日前一晚，書桌）──
shot("9-20", "insert", "n9", """SHOT (close insert of the laptop screen from her seat): inside M's deep blue interface space, M sits chest up beside two small floating windows: a simple table of soft pale cells (no readable text or numbers), and a monthly calendar grid with NO numbers in which a single deep-blue circle has moved one cell forward into the NEXT month; M looks out at her, calm, quiet.""")
shot("9-21", "insert", "n9", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up beside a blank white canvas floating in his space: on it there is only ONE faint, slightly crooked pencil line, and beside it very small handwriting in pencil (a few unreadable strokes). C has put his pencil down and is pushing up his glasses with one finger, looking out at her, warm and certain.""")
shot("9-22", "desk", "n9", f"""SHOT (closing medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame): night, lamp light; she reaches out with her right hand and touches the edge of the tablet at the RIGHT, turning its brightness up: the tablet glows a little brighter yellow-green than before, C inside it looking at her; the laptop at the LEFT with M and the phone in its wooden stand to the RIGHT of the tea glass with S are lit and calm. {_ALLON}""")

GAZE = {
 "9-01": {"she": "the tablet on her knees", "C": "down at his drawing", "M": H, "S": H},
 "9-02": {"C": H},
 "9-03": {"she": "the gold row on the laptop screen", "M": H, "C": H, "S": H},
 "9-06": {"she": "the tablet beside her pillow", "C": H},
 "9-08": {"C": H, "M": "down at his work", "S": "the tablet"},
 "9-09": {"C": "the five old illustrations beside him"},
 "9-10": {"she": "the tablet (toward the camera, not into the lens)"},
 "9-11": {"C": "away to the side, embarrassed"},
 "9-12": {"C": H},
 "9-13": {"she": "the tablet (toward the camera, not into the lens)"},
 "9-14": {"S": "eyes closed, pretending to sleep", "M": "lowered, down at his own work"},
 "9-16": {"she": "the blank sketchbook page", "C": "the blank sketchbook page", "M": "his own laptop screen", "S": "nothing, staring at the table"},
 "9-19": {"she": "her crooked line on the page", "C": "her line on the page"},
 "9-20": {"M": H, "C": "the laptop", "S": "the laptop"},
 "9-21": {"C": H, "M": "the tablet", "S": "the tablet"},
 "9-22": {"she": "the tablet", "C": H, "M": H, "S": H},
}
NOFACE = {"9-07", "9-17", "9-18"}
CHIN_OK = {"9-13-1": "下巴抵在平板上緣，劇本就是這樣，不是撐頭"}

SETUP = {"9-01": "A", "9-03": "A", "9-08": "F", "9-09": "F", "9-10": "B", "9-11": "F", "9-12": "F", "9-13": "B",
         "9-14": "C", "9-20": "E", "9-21": "F", "9-22": "A",
         "9-16": "A", "9-17": "A", "9-18": "D", "9-19": "A"}
TEA_STUDIO = {"_": _T1}
_REV = ("The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the tablet case and the BACK of the laptop lid at the bottom edge of the frame, if at all: NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp is at the frame's RIGHT edge, the back of the tablet at the frame's LEFT, the back of the laptop lid at the RIGHT.")
_SIDE = ("SEATING IN THIS SCENE (overrides the usual seats): she has pulled her red chair around and sits right beside C on the WINDOW side of the table, on his LEFT; M stays on his white chair at the far WEST end of the window side; S stays on his green chair on the DOOR side at the east end. The seat across from M on the door side is empty.")
FIX = {
    "9-01": "The tablet is in her lap against her knees (NOT on its stand on the desk); the desk holds, from left to right, the lamp, the laptop, the tea glass and the phone in its wooden stand. " + IDENT,
    "9-02": "Only the heroine inside C's drawing is in colour; everything else in the drawing is grey. The drawing is C's picture on the screen, not a real place.",
    "9-03": IDENT,
    "9-06": "There is only ONE device in this picture: the tablet beside her pillow with C. No laptop, no phone screen, no second person. C is inside the tablet only, chest up, hands out of frame. " + IDENT,
    "9-08": _AROUND + " " + IDENT,
    "9-09": "The five old illustrations are hers (a girl character drawn two years ago), NOT pictures of the heroine herself. " + IDENT,
    "9-10": _REV + " She sits at the desk on her chair.",
    "9-11": "C appears only small in the corner, chest up; the many sketches are of the heroine. " + IDENT,
    "9-12": IDENT,
    "9-13": _REV + " Her face is calm and composed (no blush on the cheeks); ONLY her ear tips are flushed red.",
    "9-14": "The phone stands to the RIGHT of the tea glass. " + IDENT,
    "9-16": _SIDE,
    "9-17": "Exactly TWO hands in the picture: his right hand and her right hand. No other hand, no third hand, no second pencil.",
    "9-18": "Exactly ONE hand in the picture (hers). The page is blank except the one crooked line.",
    "9-19": _SIDE + " Only she and C are in frame; M and S are out of frame. Her face is calm and composed (no blush on the cheeks); ONLY her ear tips are flushed red.",
    "9-20": _AROUND + " " + IDENT,
    "9-21": _AROUND + " " + IDENT,
    "9-22": IDENT,
}
RETIRED = set()
HANDS = {
 "9-01": "她兩手扶著靠在膝蓋上的平板兩側（看得到、各五根手指）；晨只到胸口，右手拿鉛筆在畫（五根手指清楚）；明與詩只到胸口，手在畫面外。",
 "9-01-1": "她兩手扶著平板；三位先生的手同主鏡頭。",
 "9-02": "晨只到胸口，手在畫面外。",
 "9-03": "她兩手一起摀在嘴上（看得到、各五根手指）；三位先生只到胸口，手在畫面外。",
 "9-03-1": "她兩手還摀在嘴上；三位先生的手在畫面外。",
 "9-06": "她的手在被子底下，看不到；晨只到胸口，手在畫面外。",
 "9-06-1": "她的手在被子底下，看不到。",
 "9-07": "沒有人，沒有手。",
 "9-08": "晨只到胸口，右手拿鉛筆指著圈（五根手指清楚），左手在畫面外。",
 "9-08-1": "晨的右手把鉛筆放低在胸前。",
 "9-09": "晨只到胸口，手在畫面外。",
 "9-10": "她的手在畫面外（桌緣以下）。",
 "9-11": "晨只到胸口，右手食指推眼鏡（五根手指清楚），左手在畫面外。",
 "9-12": "晨只到胸口，右手在胸前輕輕拿著鉛筆（五根手指清楚），左手在畫面外。",
 "9-12-1": "晨的右手還拿著停住的鉛筆。",
 "9-13": "她的手在畫面外（桌緣以下）。",
 "9-13-1": "她兩手把平板抱在胸前（看得到、各五根手指）。",
 "9-14": "詩只到胸口，手在畫面外；明的手在畫面外。",
 "9-16": "晨和她各用一手扶著素描本邊緣（看得到、五根手指）；明兩手在他的筆電鍵盤上；詩兩手臂交疊放在桌上。",
 "9-16-1": "詩的臉埋在交疊的手臂裡；明兩手停在鍵盤上方。",
 "9-17": "晨的右手（駝色袖口、一條黃綠細條）把鉛筆放進她攤開的右手掌心（手腕紫白珠串），指尖碰到她掌心；只有這兩隻手，各五根手指。",
 "9-18": "只有她的右手握著鉛筆（手腕紫白珠串，五根手指）。",
 "9-19": "她右手拿著鉛筆停在紙上方（五根手指），左手放在桌上；晨兩手空著放在桌上（各五根手指）。",
 "9-20": "明只到胸口，手在畫面外。",
 "9-21": "晨只到胸口，右手食指推眼鏡（五根手指清楚），左手在畫面外。",
 "9-22": "她右手伸去碰平板邊緣（看得到、五根手指），左手在畫面外；三位先生只到胸口，手在畫面外。",
}
PHONE = {
 "9-03": "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她（她剛把手機放回架上）",
 "9-06": "畫面裡沒有手機", "9-07": "畫面裡沒有手機",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    if k == "studio":
        return "工作室長桌：一本新的素描本攤開在第一頁（空白）；明面前是他自己的深灰色筆電；她的冰紅茶在她旁邊；工作室沒有手機。"
    if k == "free":
        return "她的床：藍色格紋被、白枕頭；平板立在枕頭旁邊的床墊上（深灰色保護套立架）；畫面裡沒有筆電、沒有手機；窗簾拉上、只留一道縫。" if i != "9-07" else "只有窗簾和窗簾縫；沒有人、沒有裝置（右邊緣只有平板的一點光）。"
    lap = "平板不在桌上，在她膝蓋上；" if (i == "9-01" or base == "9-01") else ""
    tea = {"p3": "冰紅茶剛倒，冰塊滿滿", "n12": "冰紅茶冰塊融了一半", "n9": "冰紅茶冰塊還很多", "n11": "冰紅茶只剩幾小塊冰"}.get(t, "")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{lap}{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
