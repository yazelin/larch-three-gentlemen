# 第六章分鏡規格（劇本/第六章.md 的產圖版）。CH=6 python3 tools/shots.py … 讀這份。格式與規矩同 ch1、ch2、ch4_shots.py。
# id 一律「6-」開頭，定稿放 art/cg/ch6/<id>.jpg。全章在現實層（書桌、床），沒有工作室。三人已取名，分鏡描述一律用 M／C／S 字母。
# time：t3＝凌晨三點（冰早化光）／d5＝清晨五點（天開始變淺）／e730＝晚上七點半（剛倒的紅茶）／c1＝凌晨一點（冰半融）
#       ／a239＝凌晨兩點（房間燈全關，只有手機與書桌上三台裝置的光）／c25＝凌晨兩點多（冰化光）／t4＝三點五十一分
from ch1_shots import SETUP_DESC, SEATING, H, _T1
from ch4_shots import IDENT, _ALLON
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "d5": "TIME: 5 a.m., the very first dawn: the sky outside the window has turned a pale grey-blue with a thin warm line low over the rooftops, almost every city window dark; the desk lamp is still on but now looks weak against the cool light. The tea glass has NO ice at all, water droplets running down the glass.",
    "e730": "TIME: 7:30 p.m. The warm desk lamp is on and the ceiling light is off; the room is soft blue dusk-dark; the city outside has many lit windows. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
}
_CAL = ("art/cg/06-1.jpg", "COMPOSITION REFERENCE: an earlier frame of this exact shot (the open laptop seen straight on, the calendar window on its screen with one day circled); paint a NEW picture with the same camera, framing and layout, not a copy: the differences are described below. Its rendering (transparent watercolour) is the style to match")
SETREF = {"6-11": _CAL}

_MAP = "a top-down pixel-art RPG map of a red-lit angry kingdom: a glowing pink crystal on a small stone plinth in the centre, three stone paths branching from it to the top, left and right, lava cracks, flat game-map colours, NO text"
_SCR = 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.'

# ── 一、五點的回覆（凌晨三點→清晨五點，書桌）──
shot("6-01", "desk", "t3", f"""SHOT (MASTER for the 3 a.m. release; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): she has just sent a post and is shaking out her right hand in the air, fingers spread, wrist loose, worn out from days of fighting monsters in her own game. Beyond her the three devices are lined up on the desk: the open laptop at the LEFT shows a pixel game map (a red angry kingdom with a glowing crystal) on its left two thirds and M chest up in his deep blue interface space in a rounded window on its right third; in the MIDDLE the tea glass (no ice) and the phone standing in its small wooden stand showing S; at the RIGHT the tablet on its stand showing C. S grins at her hand-shaking; C smiles; M looks at the map. {_ALLON}""")
shot("6-01-1", "var", "t3", "A small plain notification bubble (no text) has popped up at the top of the laptop screen; she has stopped shaking her hand and leans toward the laptop, frowning in confusion ('huh?'); M has turned to look at the bubble; S and C look at her.", base="6-01")
shot("6-02", "insert", "t3", f"""SHOT (close insert of the laptop screen): {_MAP}; a tiny pixel knight who walked up the RIGHT path is being yanked away by a pink teleport sparkle and dropped onto the LEFT path, a small dotted arrow showing the wrong jump (no text). In a small rounded window at the lower right corner of the screen M chest up looks at the map with a slight frown.""")
shot("6-03", "desk", "d5", f"""SHOT (MASTER for the dawn wait; close over-the-shoulder shot from just behind her LEFT shoulder): she has laid her head down sideways on her folded arms on the desk, cheek on her forearm, eyes OPEN and tired, waiting; beyond her head the open laptop at the LEFT glows with M in his window looking down at her; the tea glass and the phone in its stand with S in the MIDDLE; the tablet with C at the RIGHT. The window behind the devices has turned the pale grey-blue of first dawn. {_ALLON}""")
shot("6-03-1", "var", "d5", "She has jerked upright off her arms, eyes wide at a new plain reply bubble on the laptop screen (no text) ('he's still awake at five?!'); S has burst out laughing inside the phone, fang showing; C smiles sleepily; M looks at the reply.", base="6-03")
shot("6-04", "insert", "d5", """SHOT (close insert of the laptop screen): a simple game-editor card fills the screen: a small pink crystal icon and a single large toggle switch that has just slid from a glowing gold ON position back to a soft grey OFF position, a little spark where it moved; beside it a tiny pixel knight standing in front of a small pixel stone church, and the crystal next to him now dim and grey. No text, no numbers. In a small rounded window at the lower right corner M chest up gives one small satisfied nod.""")
shot("6-05", "desk", "d5", f"""SHOT (wide establishing shot from the corner by the door, exactly the EMPTY SET image's camera D): the whole room at the first dawn: the window behind the desk pale grey-blue with a thin warm line over the dark rooftops; she sits at the desk typing on the laptop, back to us in three-quarter, shoulders loose with relief; on the desk the three devices are lit (laptop with M at the LEFT, phone in its stand with S in the MIDDLE beside the tea glass, tablet with C at the RIGHT), small at this distance. The bed with its blue plaid duvet and the wardrobe exactly where the EMPTY SET image shows them. {_ALLON}""")

# ── 二、聽完整（同一天晚上七點半，書桌）──
shot("6-06", "desk", "e730", f"""SHOT (MASTER for the player talk; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): she has turned her head toward the phone in the MIDDLE, talking to S. Inside the phone in its small wooden stand beside the tea glass, S sits chest up in his wine-red interface space with an acoustic guitar across his chest, his right hand resting on the strings (five clear fingers), looking at her with an easy grin. The laptop at the LEFT shows M in his window; the tablet at the RIGHT shows C. {_ALLON}""")
shot("6-06-1", "var", "e730", "S grins wider with his fang showing, teasing her ('you? aren't you a programming idiot?'); she has turned to him with a puffed cheek and narrowed eyes; M glances at the phone with the faintest smile; C laughs quietly.", base="6-06")
shot("6-07", "insert", "e730", """SHOT (close insert of the laptop screen): a full-screen music player she built fills the laptop screen: a large round glowing play button in the centre, a vertical list of song blocks on the left (plain coloured bars, no text), a thin wine-red waveform running along the bottom, the play button just pressed with a soft ripple. In a small rounded window at the lower right corner M chest up looks out at her. No text, no numbers.""")
shot("6-08", "insert", "e730", f"""SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, in his dark wine-red interface space, S has turned his head AWAY to one side, eyes lowered, NOT smiling, quiet and moved, the guitar still across his chest, his hands still. Faint wine-red music notes of light drift in his space. {_SCR}""")
shot("6-08-1", "var", "e730", "S has turned back and pouts toward the tablet on the right (out of focus), one eyebrow raised in protest ('that's my home, don't draw on it'); in the out-of-focus tablet C smiles at him.", base="6-08")

# ── 三、圈（凌晨一點，書桌）──
shot("6-09", "desk", "c1", f"""SHOT (MASTER for the variable list; close over-the-shoulder shot from just behind her LEFT shoulder, her cheek and glasses in lost profile at the frame's lower right): she leans very close to the laptop, her face almost at the screen, frowning in concentration at a long list of small coloured rows (no text) on the left of the laptop screen; M chest up in his rounded window on the right of the laptop screen, and beside M a second small window showing a monthly calendar grid. The tea glass and the phone in its stand with S, and the tablet with C, softly out of focus at the right. {_ALLON}""")
shot("6-11", "free", "c1", """SHOT (extreme close-up insert, the same framing as the COMPOSITION REFERENCE): the camera looks straight at the open laptop screen; inside the screen, in M's deep blue interface space, a small floating calendar window shows a simple monthly grid with NO numbers or text, one day circled in a single thin red ring. M's shoulder and the gold gear brooch on his charcoal lapel are at the right edge of the screen. NEW in this frame: faintly REFLECTED on the dark glass over the calendar, the ghost of HER face — her dark purple hair, the gold rim of her glasses, her widening eyes — overlapping the circled day, as if she is seeing it for the first time. The desk lamp at the upper left; dark window behind the laptop. No text anywhere.""", who="m")
shot("6-12C", "insert", "c1", f"""SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up, his pencil stopped still in his fingers, looking out at her with a careful, quiet face, no smile. {_SCR}""")
shot("6-12S", "insert", "c1", f"""SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, in his dark wine-red interface space, S has taken his wine-red headphones off his neck and holds them in his lap (out of frame below the screen edge), and looks out at her, NOT smiling for once, serious. {_SCR}""")
shot("6-12M", "insert", "c1", """SHOT (frame within a frame, close): the open laptop fills the frame; inside the screen, in his deep blue interface space, M sits chest up and looks straight out at her, calm and honest, a little sorry; the small calendar window floats beside him with its one circled day. Softly out of focus around the laptop, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S); the heroine never appears on any screen.""")
shot("6-13", "desk", "c1", """SHOT (MASTER for her breaking; close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she has bowed her head and pressed her face into both open palms, fingers over her eyes and glasses pushed up a little (her face is covered by her hands, NOT resting on them: her elbows are off the desk, her back curved); the three coloured glows (yellow-green, blue, wine red) from the devices below the frame fall on her hands and hair. Behind her, dark and soft: the wardrobe, the door, the bed with the plaid duvet, as in the EMPTY SET image.""")
shot("6-13-1", "var", "c1", "She has lowered her hands into her lap and lifted her face: her eyes are wet behind her glasses, her mouth pressed into a small tired line, looking at the devices below the frame, resigned ('we can only wait').", base="6-13")

# ── 四、夜班（凌晨兩點，床→書桌）──
shot("6-14", "bed", "a239", """SHOT (MASTER for the bed scene; HIGH ANGLE from above the head of the bed, looking down): she lies on her back on the bed with the blue plaid duvet pulled up to her chest, her purple hair spread on the white pillow, glasses on; she holds her phone up above her face with both hands, scrolling a plain list of rectangular job cards on its screen (no text), its cool light on her face. The ceiling light and desk lamp are OFF; at the frame's far edge the desk by the window is a dark shape where the laptop and the tablet glow softly blue and yellow-green.""")
shot("6-14-1", "var", "a239", "She has lowered the phone and laid it face-down on her chest under both hands; she stares straight up at the ceiling with dry, open eyes, unable to answer.", base="6-14")
shot("6-15", "insert", "c25", """SHOT (close insert at desk height, the moment of the accident): her sleeve has caught the rim of the tall glass and it is tipping over; amber tea with NO ice pours out across the wooden desk in a spreading sheet toward an open lined notebook lying beside the laptop; on the notebook's last page a pagoda-shaped stack of small handwritten lines (too small to read, NO readable characters) is just being reached by the tea, the ink starting to bleed brown. The cork coaster sliding. Her hand and sleeve at the frame's edge (five clear fingers). The desk lamp's warm light; the phone in its wooden stand and the laptop softly out of focus.""")
shot("6-16", "insert", "c25", """SHOT (top-down close insert of the soaked notebook page): the last page of the lined notebook is wet and stained amber-brown; the pagoda-shaped handwritten lines have bled into soft brown blurs, unreadable; her right hand presses a soaked white tissue onto the page (five clear fingers, bead bracelets on the wrist), and where she presses, the brown blur spreads a little more. A puddle of tea on the wooden desk around the notebook.""")
shot("6-17", "desk", "c25", """SHOT (MASTER for her crying; close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she holds a crumpled wet tissue in both hands at chest height (both hands visible, five fingers each), tears running down behind her glasses, one tear falling onto the tissue; her mouth trembles between crying and a broken little laugh ('it's just a cup of tea...'). The warm lamp from the frame's RIGHT and the three coloured device glows from below. Behind her, dark and soft: the wardrobe, the door, the bed, as in the EMPTY SET image.""")
shot("6-17-1", "var", "c25", "She is laughing through her tears now, eyes squeezed, a wet small smile, the tissue pressed under her nose with one hand.", base="6-17")
shot("6-18C", "insert", "c25", f"""SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, in his pale yellow-green interface space, C sits chest up beside a freshly drawn picture floating in his space: a tall straight-sided glass of amber iced tea with the thin white string of a tea bag over the rim and a small cream tag, standing on a round cork coaster, drawn in soft pencil and watercolour. C looks out at her with a gentle, worried smile. {_SCR}""")
shot("6-18M", "insert", "c25", """SHOT (frame within a frame, close): the open laptop fills the frame; inside the screen, in his deep blue interface space, M sits chest up and looks DOWN toward the desk beside the laptop, serious and practical; at the bottom of the frame a thin line of spilled amber tea creeps along the wooden desk toward the laptop's edge. Softly out of focus around the laptop, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S); the heroine never appears on any screen.""")
shot("6-18S", "insert", "c25", f"""SHOT (frame within a frame, close): the phone standing in its small wooden phone stand fills the centre of the frame; inside the screen, in his dark wine-red interface space, S glares sideways down at the fallen glass (out of frame) with an exaggerated scowl, as if scolding it, his wine-red headphones around his neck. {_SCR}""")
shot("6-18S-1", "var", "c25", "S's scowl has melted; he looks out at her softly, putting his headphones back on, faint wine-red music notes of light drifting up in his space (a slow wordless melody).", base="6-18S")
shot("6-19", "insert", "t4", """SHOT (close insert on the window ledge behind the desk): the lined notebook lies open on the window ledge to dry, its last page wrinkled and stained amber-brown, the handwritten lines blurred beyond reading; only at the very top of the pagoda-shaped stack ONE single handwritten character is still clear and dark: 茶. Night outside the window, almost every city window dark. The desk lamp's warm light from below.""")
shot("6-20", "desk", "t4", f"""SHOT (wide closing shot from the corner by the door, exactly the EMPTY SET image's camera D): 3:51 a.m.; the city outside the window is almost completely dark; she sits at the desk again, the laptop pulled back in front of her, typing a short note; the desk is wiped clean, the glass upright and empty on its coaster; the three devices are lit (laptop with M at the LEFT, phone in its stand with S in the MIDDLE, tablet with C at the RIGHT), the only glow in the room with the lamp; the notebook drying on the window ledge. {_ALLON}""")

GAZE = {
 "6-01": {"she": "her own shaking hand", "M": "the map on his screen", "C": H, "S": "her shaking hand, grinning"},
 "6-02": {"M": "the map", "C": "down at his drawing", "S": "the laptop"},
 "6-03": {"she": "the laptop", "M": H, "C": H, "S": H},
 "6-04": {"M": "the toggle", "C": "the laptop", "S": "the laptop"},
 "6-05": {"she": "the laptop", "M": H, "C": H, "S": H},
 "6-06": {"she": "the phone", "S": H, "M": "the phone", "C": "the phone"},
 "6-07": {"M": H, "C": "the laptop", "S": "the laptop"},
 "6-08": {"S": "away to one side, eyes lowered", "M": "the phone", "C": "the phone"},
 "6-09": {"she": "the list on the laptop screen", "M": "his own work", "C": "down at his drawing", "S": "down at his own side"},
 "6-11": {"M": "out at her"},
 "6-12C": {"C": H, "M": H, "S": H},
 "6-12S": {"S": H, "M": H, "C": H},
 "6-12M": {"M": H, "C": H, "S": H},
 "6-13": {"she": "into her own hands"},
 "6-14": {"she": "the phone above her face"},
 "6-15": {"S": "the falling glass"},
 "6-16": {},
 "6-17": {"she": "the tissue in her hands, then the devices below the frame"},
 "6-18C": {"C": H, "M": H, "S": H},
 "6-18M": {"M": "down at the spilled tea by the laptop", "C": H, "S": H},
 "6-18S": {"S": "down at the fallen glass, scowling", "M": "the phone", "C": "the phone"},
 "6-19": {},
 "6-20": {"she": "the laptop", "M": H, "C": H, "S": H},
}
NOFACE = {"6-16", "6-19", "6-15"}
CHIN_OK = {"6-03": "她趴在交疊的手臂上等天亮（休息，不是撐頭）", "6-13": "她把臉埋進手心，是哭，不是托腮撐頭"}

SETUP = {"6-01": "A", "6-02": "E", "6-03": "A", "6-04": "E", "6-05": "D", "6-06": "A", "6-07": "E", "6-08": "C",
         "6-09": "A", "6-11": "E", "6-12C": "F", "6-12S": "C", "6-12M": "E", "6-13": "B", "6-14": "D",
         "6-15": "C", "6-16": "A", "6-17": "B", "6-18C": "F", "6-18M": "E", "6-18S": "C", "6-19": "A", "6-20": "D"}
TEA_STUDIO = {"_": _T1}
_REV = "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the plain dark BACK of the tablet case (and the back of the phone in its stand): NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT, the back of the laptop lid at the RIGHT."
FIX = {
    "6-08-1": "Inside the out-of-focus tablet there is exactly ONE man, C (chestnut curly hair, gold round glasses, camel cardigan), alone; never two people on one screen.",
    "6-01": IDENT, "6-03": IDENT, "6-05": IDENT, "6-06": IDENT, "6-09": IDENT, "6-20": IDENT,
    "6-02": _SCR + " " + IDENT, "6-07": _SCR + " " + IDENT, "6-08": IDENT,
    "6-04": _SCR + " " + IDENT + " DESK ORDER (very important): from LEFT to RIGHT exactly: desk lamp, the laptop (filling the centre), the tea glass on its coaster, the phone in its wooden stand, the tablet on its stand. Nothing stands to the LEFT of the laptop except the lamp.",
    "6-11": "The reflection is faint and ghostly, only on the dark glass; she is NOT inside the screen as a person; M is the only man on this screen. Nothing touches anyone's chin.",
    "6-12C": IDENT, "6-12S": IDENT, "6-12M": IDENT, "6-18C": IDENT, "6-18M": IDENT, "6-18S": IDENT,
    "6-13": _REV, "6-17": _REV,
    "6-15": "Exactly ONE tall glass (hers), tipping; NO mug. Only the phone in its stand and the laptop are softly visible; no extra device.",
    "6-19": "The single clear character is 茶 written by hand in dark ink; every other mark on the page is an unreadable brown blur. No other text anywhere.",
}
RETIRED = set()
HANDS = {
 "6-01": "她右手舉在半空甩一甩（五根手指張開、清楚），左手在畫面外；三位先生只到胸口，手在畫面外。",
 "6-01-1": "她兩手在畫面外（桌緣以下）；三位先生的手在畫面外。",
 "6-02": "明只到胸口，手在畫面外；沒有別人的手。",
 "6-03": "她兩手交疊在桌上當枕頭（看得到前臂和手背，手指自然收著）；三位先生只到胸口，手在畫面外。",
 "6-03-1": "她兩手撐在桌緣把自己推起來（看得到、各五根手指）；三位先生的手在畫面外。",
 "6-04": "明只到胸口，手在畫面外；沒有別人的手。",
 "6-05": "她兩手在鍵盤上（遠景，小而自然）；三位先生的手在畫面外。",
 "6-06": "詩右手搭在吉他弦上（五根手指清楚），左手在畫面外；她的手在畫面外；明和晨的手在畫面外。",
 "6-06-1": "詩右手還搭在吉他上；她的手在畫面外。",
 "6-07": "明只到胸口，手在畫面外；沒有別人的手。",
 "6-08": "詩的手停在吉他上不動（看得到右手、五根手指）；別人的手在畫面外。",
 "6-09": "她右手放在觸控板上（五根手指自然），左手在畫面外；三位先生的手在畫面外。",
 "6-11": "沒有人的手。",
 "6-12C": "晨右手拿著鉛筆停住（五根手指清楚），左手在畫面外。",
 "6-12S": "詩只到胸口，兩手在畫面下緣之外。",
 "6-12M": "明只到胸口，手在畫面外。",
 "6-13": "她兩手攤開蓋住臉（兩隻手都看得到、各五根手指，手肘離開桌面）。",
 "6-13-1": "她兩手放在腿上（畫面外）。",
 "6-14": "她兩手舉著手機在臉上方（兩隻手都看得到、各五根手指）。",
 "6-14-1": "她兩手把手機蓋在胸口（兩隻手都看得到）。",
 "6-15": "只露她右手的手背和袖口在畫面邊緣（五根手指自然），左手在畫面外。",
 "6-16": "只露她右手壓著濕衛生紙（五根手指清楚，手腕有串珠手環），左手在畫面外。",
 "6-17": "她兩手在胸前捏著濕衛生紙（兩隻手都看得到、各五根手指）。",
 "6-17-1": "她右手拿衛生紙按在鼻子下，左手在畫面外。",
 "6-18C": "晨只到胸口，手在畫面外。",
 "6-18M": "明只到胸口，手在畫面外。",
 "6-18S": "詩只到胸口，手在畫面外。",
 "6-18S-1": "詩兩手把耳機戴回耳朵上（看得到、各五根手指）。",
 "6-19": "沒有人的手。",
 "6-20": "她兩手在鍵盤上（遠景，小而自然）；三位先生的手在畫面外。",
}
PHONE = {}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    if k == "bed":
        return "床：藍色格紋被、白枕頭（照空景）；她躺在床上；書桌在畫面邊緣、只是一團暗影，上面筆電和平板的螢幕亮著微光；檯燈與房間的燈都關著；全畫面只有一支手機（在她手上）。"
    if i == "6-19":
        return "窗台：攤開晾乾的筆記本，最後一頁被紅茶泡皺、字糊成褐色；沒有其他道具。"
    if t == "c25" and i not in ("6-15", "6-16"):   # 打翻之後：杯子倒在桌上、空的（試畫把杯子畫回直立裝滿，不連戲）
        return "書桌：打翻之後，玻璃杯橫倒在桌面上、裡面是空的，桌面一攤紅茶漫到攤開的筆記本；軟木杯墊滑開；由左到右檯燈、筆電、倒下的杯子、手機在淺木色手機架上、平板；全畫面只有一支手機、只有一個杯子，沒有任何直立裝滿的杯子。"
    if i in ("6-15", "6-16"):
        return "書桌：玻璃杯倒下、冰早就化光的紅茶在桌面漫開，漫到攤開的筆記本最後一頁；軟木杯墊滑開；手機在手機架上、筆電在旁邊；全畫面只有一支手機、只有一個杯子。"
    tea = {"t3": "冰紅茶冰塊全部化光、杯壁水珠往下流", "d5": "冰紅茶冰塊全部化光、杯壁水珠往下流", "e730": "冰紅茶剛倒，冰塊滿滿",
           "c1": "冰紅茶冰塊半融、剩幾小塊", "c25": "冰紅茶冰塊全部化光", "t4": "玻璃杯空的、直立在杯墊上，桌面已經擦乾"}.get(t, "")
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
