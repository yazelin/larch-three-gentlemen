# 第四章分鏡規格（劇本/第四章.md 的產圖版）。CH=4 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch2_shots.py。
# id 一律「4-」開頭，定稿放 art/cg/ch4/<id>.jpg。全章在現實層（書桌、通識課教室），沒有工作室。
# 取名在第四節：之前稱 C／M／S，之後稱晨／明／詩；分鏡描述一律用 M／C／S 字母。
# time：w10＝第一週目第一晚十點（冰塊滿）／w2＝第三晚凌晨兩點（只剩一兩片冰）／w5＝第五晚十一點（冰塊半融）／cls＝第六天下午的通識課／w9＝第六天晚上九點（剛倒的紅茶）／w830＝第七天晚上八點半（冰塊滿）
from ch1_shots import SETUP_DESC, SEATING, H, _T1
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "w10": "TIME: 10 p.m. The warm desk lamp is the only lamp; the room is soft blue night; the city outside has many lit windows. The iced tea is fairly fresh: plenty of clear ice cubes, light condensation.",
    "w2": "TIME: 2 a.m. The desk lamp is the only light; deep blue shadow; only a few windows still lit outside. The iced tea has only one or two thin slivers of ice left.",
    "w5": "TIME: 11 p.m. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "cls": "TIME: a weekday mid-afternoon in a university classroom: warm low sunlight from the tall windows on the left, long diagonal light shafts with dust motes, the projector screen softly glowing.",
    "w9": "TIME: 9 p.m. The warm desk lamp is on and the ceiling light is off; the room is soft blue dusk-dark; the city outside has many lit windows. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
    "w830": "TIME: 8:30 p.m. The warm desk lamp is on and the ceiling light is off; the room is soft blue dusk-dark; the city outside has many lit windows. The iced tea is fresh with plenty of ice.",
}
_CLASS = ("canon/refs/set_class_A.jpg", "EMPTY CLASSROOM SET: the university lecture classroom from this shot's camera position (rows of light-wood desks, the projector screen at the front, tall windows on the LEFT wall, the afternoon light) and the watercolour rendering to match; keep the room exactly as laid out there, the shot may frame tighter")
SETREF = {"4-10": _CLASS, "4-11": _CLASS, "4-12": _CLASS}

_MAP = "a top-down pixel-art RPG map tile of a lazy medieval town: grey stone stairs at the lower right, one long horizontal stone wall across the upper middle, a small round blue pond at the upper right, cobbled paths and grass; flat game-map colours, NO text"
IDENT = 'SCREEN IDENTITIES (very important, check every screen): the LAPTOP shows ONLY M: near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white shirt, gold gear brooch. The TABLET shows ONLY C: warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch, NO necklace. The PHONE shows ONLY S: long messy WINE-RED hair with one thin braid, wine-red headphones, black track jacket. The heroine (dark purple wolf-cut hair, pink-tinted glasses, moon pendant) is NEVER on any screen. Nobody on a screen rests a chin or cheek on a hand.'
_ALLON = "All three device screens are LIT and each shows its own man only: the laptop at the LEFT shows ONLY M, the tablet at the RIGHT shows ONLY C, the phone in its stand in the MIDDLE shows ONLY S. The heroine never appears on any screen. Inside the screens the men sit upright with both hands below the screen edge (out of frame) unless described; nothing touches their chins or cheeks."

# ── 一、什麼都不要做（第一週目第一晚，書桌）──
shot("4-01", "desk", "w10", f"""SHOT (MASTER for the first-week planning night; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): beyond her the three devices are lined up on the desk: the open laptop at the LEFT shows a plain white whiteboard with ONE grey card in its centre (no text) on its left two thirds, and M chest up in his deep blue interface space in a large rounded window on the right third of the laptop screen; in the MIDDLE the tea glass full of ice and the phone standing in its small wooden stand showing S; at the RIGHT the tablet on its stand showing C. She is talking to them, thinking out loud, her head tilted a little. S leans toward the phone glass grinning; M looks at her; C looks at her with his pencil still. {_ALLON}""")
shot("4-01-1", "var", "w10", "S has burst out laughing inside the phone, fang showing, pointing at her through the glass ('this level is literally you'); she has turned her head sharply toward the phone, cheek puffed in mock annoyance ('shut up'); M's mouth twitches; C hides a smile.", base="4-01")
shot("4-02C", "insert", "w10", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up beside a small floating pencil drawing of an inviting unmade bed: the duvet turned back halfway, a pillow with a soft dent in it, as if someone just got up. C looks out at her with a soft, slightly sleepy smile. No text.""")
shot("4-02M", "insert", "w10", """SHOT (frame within a frame, close): the open laptop fills the frame; inside the screen, beside M (chest up, deep blue interface space, calm, looking out at her with a faint dry smile), a small floating window shows a simple top-down pixel game map with a little bed tile and a tiny pixel character standing still next to it, a small round progress ring filling up above the character's head (no numbers, no text).""")
shot("4-02S", "insert", "w10", """SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, in his dark wine-red interface space, S has his wine-red headphones on and his eyes closed, listening, a lazy small smile; faint thin slanted lines of soft rain drift across his interface space like a sound. Out of focus around the phone: the laptop with M on the left, the tablet with C on the right, both watching the phone.""")
shot("4-03", "var", "w10", "She has slumped back against her chair with a rueful laugh, eyes up at the ceiling for a second ('then I'm done for, I'll get stuck on this level'); S grins; C smiles; M looks at her with quiet amusement.", base="4-01")

# ── 二、找不同（第三晚凌晨兩點，書桌）──
shot("4-04", "desk", "w2", f"""SHOT (MASTER for the map night; close over-the-shoulder shot from just behind her LEFT shoulder, her cheek and glasses in lost profile at the frame's lower right): the open laptop fills most of the frame: on its screen two map tiles side by side, LEFT the original, RIGHT the enlarged copy — each is {_MAP} — they look almost the same but the right one is subtly off. In a small rounded window at the lower right of the laptop screen, M chest up looks at the maps. Beside the laptop, softly out of focus: the tea glass and the phone in its stand showing S, the tablet showing C. She leans close to the screen, frowning a little. {_ALLON}""")
shot("4-04-1", "var", "w2", "She has leaned back against her chair, silent, hands in her lap, staring at the screen with a tired, hurt stillness; inside the phone S has lowered his eyes and is tapping something off on his own side (turning his music off); C and M look at her.", base="4-04")
shot("4-06C", "insert", "w2", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up with his eyes lowered, sincere and a little ashamed, not making excuses; beside him a small floating copy of the original map tile. No text.""")
shot("4-06C-1", "var", "w2", "C has bent over his own drawing inside the screen, pencil moving fast and careful, eyes on the work; the floating original map tile is beside him.", base="4-06C")
shot("4-06M", "insert", "w2", """SHOT (close insert of the laptop screen): a simple grid table of small map-tile thumbnails fills the laptop screen, most framed in soft green, exactly FOUR framed in red (no numbers, no text); in a small rounded window at the lower right corner M chest up looks out at her steadily, calm. Her laptop's keyboard edge at the bottom of the frame.""")
shot("4-06S", "desk", "w2", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she has put white wireless earbuds in both ears and closed her eyes, listening, very still, tired; the warm lamp from the frame's RIGHT, and a faint wine-red glow from the phone below the frame on her chin. Behind her, dark and soft: the wardrobe, the door, the bed with the plaid duvet, as in the EMPTY SET image.""")
shot("4-07", "insert", "w2", f"""SHOT (close insert of the laptop screen): the two map tiles, original and the new enlarged copy, are now laid exactly on top of each other at half transparency and line up perfectly: the stairs, the horizontal wall and the pond all match; a faint soft glow along the matching edges. Each is {_MAP}. Nothing else on the screen except a small rounded window at the lower right with M chest up.""")
shot("4-08", "insert", "w2", """SHOT (her point of view, close insert of the tablet): the tablet screen shows C's folder as a grid of image thumbnails; under every thumbnail there is a second, slightly different version: a standing guard portrait and below it the same guard with a sunset city wall behind him; a map tile and below it the same map with one extra little path; and so on. C himself is a small rounded window at the top corner, chest up, looking shyly at her. No text, no file names.""")
shot("4-09", "var", "w5", "Another night (the tea now half melted): she has frozen in panic, eyes wide, both hands flat on the desk, staring at the whiteboard ('wait — is the deadline today?'); M looks at her calmly; S and C look surprised.", base="4-01")
shot("4-09-1", "var", "w5", "She has sagged with relief, one hand on her chest, letting out a breath; M looks at her with a small patient smile; S laughs; C smiles.", base="4-01")

# ── 三、茶（第六天下午，通識課教室）──
shot("4-10", "classroom", "cls", """SHOT (MASTER for the class; medium-wide shot from the side aisle, as the EMPTY CLASSROOM SET image): the classroom is now about half full of ordinary students seen from behind and the side, all in plain everyday clothes, faces turned to the screen, nobody looking at the camera; she sits in a middle row near the aisle in profile, her notebook open on the desk, a pen in her hand, slouched a little, half listening. At the front, the projector screen shows the pagoda-shaped poem as soft blurred grey strokes (no readable characters); the teacher is a small figure beside the lectern. Afternoon light shafts from the left windows.""")
shot("4-11", "classroom", "cls", """SHOT (close-up of her in her seat, three-quarter front from the aisle side, the projector glow on her face): she has suddenly sat up straight, eyes wide behind her glasses, lips slightly parted, looking at the screen at the front (out of frame). Afternoon light on her hair; out-of-focus students and desks behind her.""")
shot("4-12", "classroom", "cls", """SHOT (top-down close insert of her open notebook on a light-wood classroom desk): the LAST page of a lined notebook; her right hand holds a pen and is copying a poem laid out as a pagoda-shaped stack of handwritten lines (one tiny line at the top, each line below longer), written in neat dark ink but too small and soft to read: NO readable characters. Her bead bracelets on the wrist. Afternoon light across the page.""")

# ── 四、名字（第六天晚上，書桌；第七天晚上上架）──
shot("4-13", "desk", "w9", f"""SHOT (MASTER for the naming; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame): she holds her open notebook up in both hands toward the laptop's camera, showing the last page (the handwritten page is turned away from us; we see only the back cover and her fingers). Beyond her the three devices are lined up on the desk, all lit: the laptop at the LEFT with M, the tea glass and the phone in its stand with S in the MIDDLE, the tablet at the RIGHT with C. All three men look at the notebook, then at her, attentive and quiet. {_ALLON}""")
shot("4-13-1", "var", "w9", "She has lowered the notebook to her lap and looks down at it, the tips of her ears faintly red; inside the phone S looks down with a small shy smile, saying his new name quietly to himself; C and M look at S.", base="4-13")
shot("4-13-2", "var", "w9", "Inside the laptop M gives one small calm nod with the faintest smile; S leans toward his phone glass, squinting suspiciously at the laptop ('did you type that in advance?'); C watches, amused; she glances from one to the other.", base="4-13")
shot("4-14", "insert", "w9", """SHOT (close insert of the laptop screen): M's rounded window, M chest up in his deep blue interface space looking out at her calm and pleased; at the top edge of his window a small name tab has JUST changed: a soft gold shimmer runs along it, as if a new name had been written there an instant ago (the tab shows only a soft glow, no readable character).""")
shot("4-15", "insert", "w9", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C has opened his sketchbook to a fresh page and is writing the SAME single handwritten character over and over in neat rows with his pencil, half the page already filled, each one neater than the last; the strokes are small and soft, NOT readable. His face is bent toward the page, serious, his ears a little red.""")
shot("4-15-1", "var", "w9", "C has stopped writing and looks up at her over the page with a shy, warm small smile, the pencil still in his hand.", base="4-15")
shot("4-16", "desk", "w830", f"""SHOT (MASTER for the release; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame): the next evening; the laptop at the LEFT shows a game store page as a simple layout of soft blocks with a cover image of a knight in a stone hall and a small glowing check badge (no text), and M in a small rounded window on the right of the laptop screen; the phone in its stand with S in the MIDDLE beside the tea glass full of ice; the tablet at the RIGHT with C. She sits up a little, both hands lifted from the keyboard, a breath of disbelief and joy. {_ALLON}""")
shot("4-16-1", "var", "w830", "All three men smile at her: S grins wide with his fang showing ('first time you called all three of us together'); C nods with a soft smile; M looks at her with a calm, pleased half smile; she has already leaned back toward the laptop to fix something, a small guilty grin.", base="4-16")

GAZE = {
 "4-01": {"she": "the three devices", "M": "HER at the lower RIGHT of the frame", "C": "HER at the lower RIGHT of the frame", "S": "HER at the lower RIGHT of the frame"},
 "4-02C": {"C": H, "M": "down at his own work", "S": "down at his own side"},
 "4-02M": {"M": H, "C": "down at his drawing", "S": "down at his own side"},
 "4-02S": {"S": "eyes closed, listening", "M": "the phone", "C": "the phone"},
 "4-04": {"she": "the two maps on the laptop screen", "M": "the maps", "S": H, "C": H},
 "4-06C": {"C": "down, ashamed", "M": "down at his own work", "S": "down, quiet"},
 "4-06M": {"M": H, "C": "down at his drawing", "S": "down, quiet"},
 "4-06S": {"she": "eyes closed"},
 "4-07": {"M": "the matched maps", "C": "down at his drawing", "S": "the laptop"},
 "4-08": {"C": H, "M": "down at his own work", "S": "down at his own side"},
 "4-10": {"she": "the projector screen at the front"},
 "4-11": {"she": "the projector screen at the front, out of frame"},
 "4-13": {"she": "the laptop", "M": "the notebook in her hands", "C": "the notebook in her hands", "S": "the notebook in her hands"},
 "4-14": {"M": H, "S": "the laptop", "C": "the laptop"},
 "4-15": {"C": "down at his sketchbook page", "M": "down at his own work", "S": "the tablet"},
 "4-16": {"she": "the laptop screen", "M": H, "C": H, "S": H},
}
NOFACE = {"4-12"}
CHIN_OK = {"4-06S": "手機的光照在她下巴上，不是撐頭"}

SETUP = {"4-01": "A", "4-04": "A", "4-07": "E", "4-06M": "E", "4-02M": "E", "4-02C": "F", "4-06C": "F", "4-08": "F", "4-15": "F",
         "4-02S": "C", "4-06S": "B", "4-13": "A", "4-14": "E", "4-16": "A"}
TEA_STUDIO = {"_": _T1}
FIX = {
    "4-15-1": "C has LIFTED his head: his face is raised and turned out toward the viewer (her), eyes looking straight out of the screen at her, NOT down at the page; his pencil rests still on the paper.",
    "4-02M": IDENT,
    "4-02C": 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.' + " " + IDENT,
    "4-06C": 'Inside the tablet is ONLY C exactly as his sheet: a young MAN with warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan with a small yellow-green leaf brooch. The heroine (purple hair) is NEVER on this screen. Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.',
    "4-06M": 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.',
    "4-07": 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.',
    "4-08": 'The laptop screen is not blank: it shows M small, chest up, in his deep blue interface space. Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.' + " " + IDENT,
    "4-14": 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.' + " " + IDENT,
    "4-15": 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.',
    "4-02S": 'The phone in its wooden stand stands to the RIGHT of the tea glass (left to right on the desk: laptop, tea glass, phone in its stand, tablet).' + " " + IDENT,
    "4-06S": "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the plain dark BACK of the tablet case (and the back of the phone in its stand): NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT, the back of the laptop lid at the RIGHT.",
    "4-10": "Every student is an ordinary background extra seen from behind or in far profile, small and soft; NONE of them has purple hair, gold glasses or her clothes: the heroine appears exactly ONCE in the picture. No laptop, tablet or phone of hers on the desk; only her notebook and pen.",
    "4-11": "Only the heroine is in focus; no device of hers in frame. No readable text anywhere.",
    "4-13": "The handwritten side of the notebook faces the laptop (away from the camera); we see only the plain back cover. Nothing touches anyone's chin.",
}
RETIRED = set()
HANDS = {
 "4-01": "她的手在畫面外（桌緣以下）；三位先生只到胸口，晨右手在胸前拿一支鉛筆，其他人的手在畫面外。",
 "4-01-1": "詩右手食指在螢幕內側指著她（五根手指清楚），其他人的手在畫面外；她的手在畫面外。",
 "4-02C": "晨只到胸口，手在畫面外。",
 "4-02M": "明只到胸口，手在畫面外。",
 "4-02S": "詩只到胸口，手在畫面外。",
 "4-03": "她的手在畫面外。",
 "4-04": "她的右手放在筆電觸控板上（五根手指自然），左手在畫面外；三位先生的手在畫面外。",
 "4-04-1": "她兩手放在腿上（畫面外）；詩右手食指在他那一側點了一下，其他人的手在畫面外。",
 "4-06C": "晨只到胸口，手在畫面外。",
 "4-06C-1": "晨右手拿鉛筆在畫（五根手指清楚），左手在畫面外。",
 "4-06M": "明只到胸口，手在畫面外；她的手不在畫面裡。",
 "4-06S": "她的兩手都在畫面下緣之外。",
 "4-07": "明只到胸口，手在畫面外；沒有別人的手。",
 "4-08": "晨只到胸口，手在畫面外；她的手不在畫面裡（主觀鏡頭）。",
 "4-09": "她兩手平放在桌上（看得到、各五根手指）；三位先生的手在畫面外。",
 "4-09-1": "她右手按在胸口（五根手指清楚），左手放在桌上。",
 "4-10": "她右手拿筆，左手壓著筆記本；其他學生的手小而模糊。",
 "4-11": "她的手在畫面外。",
 "4-12": "只露她右手拿著筆在寫（五根手指清楚，手腕有串珠手環），左手在畫面外。",
 "4-13": "她兩手把筆記本舉在胸前（兩隻手都看得到、各五根手指）；三位先生只到胸口，手在畫面外。",
 "4-13-1": "她兩手把筆記本放在腿上（畫面外）；三位先生的手在畫面外。",
 "4-14": "明只到胸口，手在畫面外。",
 "4-15": "晨右手拿鉛筆在素描本上寫（五根手指清楚），左手扶著本子。",
 "4-15-1": "晨右手拿著鉛筆停在紙上，左手扶著本子。",
 "4-16": "她兩手剛從鍵盤上抬起來，懸在鍵盤上方（看得到、各五根手指）；三位先生只到胸口，手在畫面外。",
 "4-16-1": "她右手放在觸控板上，左手在畫面外；三位先生的手在畫面外。",
}
PHONE = {}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    if k == "classroom":
        return "通識課教室：她桌上只有攤開的筆記本和一支筆；她的筆電、平板、手機都不在畫面裡；沒有紅茶。"
    tea = {"w10": "冰紅茶冰塊滿滿", "w2": "冰紅茶只剩一兩片冰", "w5": "冰紅茶冰塊半融、剩幾小塊", "w9": "冰紅茶剛倒，冰塊滿滿", "w830": "冰紅茶冰塊滿滿"}.get(t, "")
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
