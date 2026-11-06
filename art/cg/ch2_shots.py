# 第二章分鏡規格（劇本/第二章.md 的產圖版）。CH=2 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py。
# id 一律「2-」開頭，定稿放 art/cg/ch2/<id>.jpg。
# time：n9＝第一晚九點（剛倒的冰紅茶、冰塊滿）／n11＝第二晚十一點（冰塊半融）／a239＝凌晨兩點三十九分（燈全關，只有手機的光）／day＝工作室白天
from ch1_shots import SETUP_DESC, SEATING, H, _T1, _T2, _T3
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

# ── 一、天亮前的聲音（第一晚九點，書桌）──
shot("2-01", "desk", "n9", """SHOT (establishing wide shot from the corner by the door, exactly the EMPTY SET image's camera D): 9 p.m., she has just come home from class: she stands beside her desk chair, a canvas tote bag still on her shoulder, bending slightly to slide her phone into the small wooden phone stand on the desk. The room is lit by the warm desk lamp and the ceiling light is OFF; the city outside the window is full of lit windows. On the desk the laptop shows M and the tablet shows C (small, chest up, both glancing at her); the phone screen shows S (tiny). The bed with the blue plaid duvet on the left, the wardrobe on the right, exactly as in the EMPTY SET.""")
shot("2-01A", "desk", "n9", """SHOT (MASTER for the first-night talk; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): beyond her the three devices are lined up on the desk, all screens lit: the laptop (M), the tea glass with plenty of ice, the phone standing in its wooden stand (S), the tablet on its stand (C). She is talking to them, a little tired after class, her shoulders relaxed. M looks down at something on his own side (not up); C twirls a pencil and looks at her; S leans toward the phone glass, curious.""")
shot("2-01A-1", "var", "n9", "She sighs and her shoulders drop, the back of her head tilting slightly — 'I didn't hear a word in that class'. S grins; C's pencil stops for a beat; M still looks down.", base="2-01A")
shot("2-01A-2", "var", "n9", "M now looks straight at her with calm, unreadable eyes; she has gone still, head lowered a little, caught by his question. C and S both look at her quietly.", base="2-01A")
shot("2-02", "insert", "n9", """SHOT (her point of view, close insert): her phone is in her right hand, held low over the desk; the screen fills most of the frame, slim lavender frame at the edges. On the screen: a travel photo taken from a hotel window before dawn — a deep blue sky, the silhouette of a distant mosque dome and minaret over old rooftops, a thin line of light at the horizon, a few lit windows. In the top corner of the screen a small rounded window with S (tiny, chest up, wine-red interface) looking down at the photo. No readable text anywhere.""")
shot("2-03", "desk", "n9", """SHOT (MASTER for her face while she scrolls the album; close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders, she holds the phone low in front of her chest (the phone itself is below the frame), scrolling with her thumb; the phone's cool white light falls on her face from below, the warm lamp rims her hair from the frame's RIGHT. Behind her, soft and dark: the wardrobe on the left, the door, the bed with the plaid duvet on the right, as in the EMPTY SET image. Neutral, remembering, a little amused.""")
shot("2-03-1", "var", "n9", "She makes an exaggerated face of horror at the idea of getting up early: eyes squeezed half shut, mouth pulled into a grimace — 'I'd rather sleep to death'.", base="2-03")
shot("2-03-2", "var", "n9", "Caught out: her eyes slide away to the side, lips pressed together in a small stubborn line, the tips of her ears turning faintly red; her face tries to stay calm.", base="2-03")
shot("2-03-3", "var", "n9", "She has stopped scrolling; she looks down at the photo with soft, far-away eyes, lips slightly parted, very still, remembering a sound.", base="2-03")
shot("2-03-4", "var", "n9", "She lifts her eyes from the phone with a quiet, decided look, a small breath in — 'faith. I'll use faith.'", base="2-03")
shot("2-04", "insert", "n9", """SHOT (extreme close-up insert of the phone in her hand, her thumb at the lower edge of the screen): the dawn photo still fills the screen; in the small rounded window at the top corner, S has hung his wine-red headphones back around his neck and looks down, tapping something on his own side, no smile, not asking anything more. No readable text.""")

# ── 二、一直問（工作室，白天）──
shot("2-05", "studio", "day", """SHOT (MASTER for the studio session; the camera stands just behind her red chair, as the EMPTY STUDIO SET image): bright daylight; the four sit at the long table exactly by the SEATING: M across on the left with his laptop, C across on the right with his open sketchbook, S on the green chair beside her. She is seen from behind her right shoulder, leaning forward with both forearms on the table, thinking out loud. All three men look at her: M calm, C with his pencil ready, S lounging back on his chair.""")
shot("2-05-1", "var", "day", "She waves one hand in a little dismissive flick ('so old-fashioned'), a wry smile in her profile; S laughs; M nods slightly; C smiles.", base="2-05")
shot("2-05-2", "var", "day", "C has bent over his sketchbook and is already drawing fast, eyes on the page; she watches him; M and S glance at C's sketch.", base="2-05")
shot("2-05-3", "var", "day", "She has leaned back against her chair and stares up at the ceiling, stuck, both hands resting in her lap; the three men look at her, waiting.", base="2-05")
shot("2-05-4", "var", "day", "M has turned his laptop around toward her and slid it to the middle of the table, then sits back with his hands off the keyboard; she leans in to read the screen; C and S look at the laptop. The laptop screen shows only lines of grey blur, nothing readable.", base="2-05")
shot("2-05-5", "var", "day", "Silence at the table: all three men look at her, serious and a little startled; S's grin has gone; she sits very straight, both hands flat on the table.", base="2-05")
shot("2-06C", "studio", "day", """SHOT (close-up from beside C, over his right shoulder onto his sketchbook): a pencil sketch of a knight's gloved hand trembling slightly, half-open, a holy medallion slipping from the fingers; real pencil strokes, unfinished. C's own right hand holds the pencil at the edge of the page; his soft, serious profile is at the frame's left edge, eyes on the drawing. Sunlight across the paper.""")
shot("2-06M", "studio", "day", """SHOT (close-up of M at the head of his side of the table): M looks up from his laptop at her (just past the camera), calm, a faint half-smile, as if saying 'you decide'; the laptop glow on one side of his face; window light behind him. His hands rest on the keyboard.""")
shot("2-06S", "studio", "day", """SHOT (close-up of S in profile): S has closed his eyes and lifts one hand slightly off the table, fingers spread a little, as if holding a sudden silence in the air; his wine-red headphones hang around his neck; a shaft of window light falls across half his face. Background soft.""")
shot("2-08", "studio", "day", """SHOT (medium-long shot, the camera on the door side looking north toward the tall grid windows, as the EMPTY STUDIO SET image): she stands alone at the window, small against the bright glass, her back half turned, one hand resting on the window frame, saying something very quietly to herself. At the table in the soft foreground: M and C on the window side are seen small, and C's pencil has stopped; S on his green chair looks over his shoulder at her.""")

# ── 三、明天一定寫（第二晚，書桌）──
shot("2-09", "desk", "n11", """SHOT (frame within a frame, MASTER for C's two faces): the tablet on its folio stand fills the frame, the tea glass at its left; inside the screen, in his pale yellow-green interface space, C sits chest up beside two small drawings floating in the space next to him, side by side: on the left a villager drawn as a grey-skinned horned demon, on the right the SAME villager as an ordinary middle-aged baker with flour on his apron — the same face, the same expression. C looks out at her, a little shy, waiting for her reaction. No text.""")
shot("2-09-1", "var", "n11", "C scratches his cheek with one finger and looks a little to the side, an embarrassed small smile — 'I think I drew until almost dawn'.", base="2-09")
shot("2-10", "insert", "n11", """SHOT (close insert of the laptop screen from her seat): a blank white document window fills most of the laptop screen, a heading bar with grey blur (no readable letters) and an empty page with a single blinking cursor; M has shrunk his own window to a small rounded window at the lower right corner, chest up, watching her with a patient look. Her right hand rests on the trackpad. No readable text.""")
shot("2-11", "desk", "n11", """SHOT (frame within a frame, S conducting): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, in his wine-red interface space, S has his headphones on and conducts with one hand with a perfectly serious, solemn face, like a choirmaster; faint golden motes of light rise like organ pipes behind him. Out of focus around the phone: the laptop with M on the left, the tablet with C on the right, both looking at the phone.""")
shot("2-11-1", "var", "n11", "S has stopped conducting; he taps 'save' on his side with one finger and gives a smug little grin with his fang showing.", base="2-11")
shot("2-12", "desk", "n11", """SHOT (MASTER: medium close-up, REVERSE ANGLE from the desk side, eye level): she has doubled over forward in her chair laughing, her face bowed toward the desk edge (not touching it), both arms wrapped around her stomach, shoulders shaking, eyes squeezed shut in laughter; we see her bowed head and her laughing cheek. The phone light (wine red) and the lamp light from the frame's RIGHT. Behind her, dark and soft: the wardrobe, the door, the bed with the plaid duvet, as in the EMPTY SET image.""")
shot("2-12-1", "var", "n11", "She has turned her chair a little toward the phone (off frame right), still wiping a laughing tear at the corner of one eye with a knuckle, a wide grin — 'it's terrible. I love it.'", base="2-12")
shot("2-13", "insert", "n11", """SHOT (close insert of the laptop from just beside her empty seat; she is turned away toward the phone, only her blurred shoulder at the frame's right edge): on the laptop screen, in his deep blue interface space, M glances sideways at a small floating calendar window beside him: a simple monthly grid with NO numbers or text, one day next month circled in a thin red line. His face is unreadable, quiet. No readable text.""")
shot("2-13-1", "var", "n11", "The calendar window has been shrunk away to a tiny tab; M now looks straight out at her with a calm, gentle face, as if promising to keep track of her deadline.", base="2-13")

# ── 四、打了又刪（凌晨兩點三十九分，床上）──
shot("2-15", "bed", "a239", """SHOT (MASTER for the bed scene; HIGH ANGLE from above the head of the bed, looking down): she lies on her back on the bed with the blue plaid duvet pulled up to her chest, her purple hair spread on the white pillow, glasses still on; she holds her phone up above her face with both hands, the phone's cool light on her face. The room around is almost black; the ceiling light and the desk lamp are OFF; far at the frame's edge the desk by the window is only a dark shape (devices dark or very dim). Quiet, sleepless.""")
shot("2-15-1", "var", "a239", "She has pulled the duvet up over her mouth, only her eyes and glasses showing above it, eyes narrowed in a smile — 'ugh, you even keep track of that'.", base="2-15")
shot("2-15-2", "var", "a239", "She has rolled onto her side and buried her face in the pillow, shoulders shaking with laughter; the phone lies glowing on the duvet beside her face.", base="2-15")
shot("2-15-3", "var", "a239", "She has lowered the phone and laid it face-down on her chest, both hands resting on it; her eyes are closed, a small quiet smile.", base="2-15")
shot("2-16", "insert", "a239", """SHOT (her point of view, phone held above her face in the dark): the phone screen fills the frame against black: a chat window with three small round avatar icons at the top in their colours (yellow-green, deep blue, wine red); at the bottom a typed line in the input box shown only as grey blur with a blinking cursor; a soft ellipsis 'typing' bubble. No readable letters anywhere.""")
shot("2-17", "insert", "a239", """SHOT (wide insert of the desk in the dark, from behind her empty chair, as the EMPTY SET image camera A): the desk lamp is OFF; the only light is the laptop screen showing the blank white document with a single blinking cursor, M's tiny window dark in its corner; the tablet and the phone stand dark; the window shows the city with only a few lit windows. Nobody in frame.""")

H_ = H
GAZE = {
 "2-01": {"she": "the phone she is placing into the stand", "M": H, "C": H, "S": H},
 "2-01A": {"she": "the three devices", "M": "down at something on his own side", "C": "HER at the lower RIGHT of the frame", "S": "HER at the lower RIGHT of the frame"},
 "2-03": {"she": "down at the phone in her hands, below the frame"},
 "2-02": {"S": "down at the photo"},
 "2-04": {"S": "down, at his own side"},
 "2-05": {"she": "M and C across the table", "M": H, "C": H, "S": H},
 "2-06C": {"C": "his sketch"},
 "2-06M": {"M": "just past the camera (her), eyes level"},
 "2-06S": {"S": "eyes closed"},
 "2-08": {"she": "out of the window", "C": H, "S": H, "M": H},
 "2-09": {"C": H},
 "2-10": {"M": H},
 "2-11": {"S": "eyes half closed, conducting", "M": "the phone", "C": "the phone"},
 "2-12": {"she": "down, laughing"},
 "2-13": {"M": "sideways at the calendar window"},
 "2-15": {"she": "her phone above her face"},
}
NOFACE = {"2-16", "2-17"}
CHIN_OK = {}

SETUP = {"2-01": "D", "2-01A": "A", "2-02": "C", "2-04": "C", "2-03": "B", "2-12": "B", "2-09": "F", "2-10": "E", "2-13": "E",
         "2-11": "C", "2-17": "A", "2-15": "D", "2-16": "D",
         "2-05": "C", "2-06C": "C", "2-06M": "A", "2-06S": "B", "2-08": "A"}
TEA_STUDIO = {"_": _T1, "2-05-4": _T2, "2-05-5": _T2, "2-08": _T2}
FIX = {
    "2-03": "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the plain dark BACK of the tablet case (and the back of the phone in its stand): NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT, the back of the laptop lid at the RIGHT.",
    "2-12": "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the plain dark BACK of the tablet case (and the back of the phone in its stand): NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT, the back of the laptop lid at the RIGHT.",
    "2-04": "The photo on the phone screen is EXACTLY the same as in shot 2-02: a deep blue pre-dawn sky over old rooftops with the silhouette of a mosque dome and a thin minaret, a thin line of light at the horizon. NOT a seaside town, NOT white houses, NOT a sunset.",
    "2-06C": "The camera is over C's right shoulder on the WINDOW (north) side of the table, looking SOUTH toward the wooden door: so the background is the door wall with the wooden door, NOT the windows. Across the table, facing the camera: the heroine on the red chair and S on the green chair beside her. M sits on the SAME side as C (window side, at the far right of the frame or out of frame), never across the table.",
    "2-08": "There is only ONE heroine in this picture: she stands at the window. Her red chair at the table is EMPTY. At the table only M (white chair, window side, with his laptop), C (wooden chair, window side) and S (green chair, near side) are sitting.",
    "2-09": "IDENTITIES (very important): the laptop at the left edge shows ONLY M exactly as his sheet: near-black short hair with a cool blue sheen, charcoal suit jacket, gold gear brooch (NOT silver or white hair). The phone in its stand shows ONLY S exactly as his sheet: long messy WINE-RED hair with one thin braid, wine-red headphones around his neck, black track jacket (NOT dark brown short hair).",
    "2-10": "The phone stands in its wooden stand with its SCREEN facing her (toward the camera). On that phone screen is S ONLY, exactly as his sheet: a young MAN with long messy WINE-RED hair and one thin braid, wine-red headphones around his neck, black track jacket, small, chest up, in his dark wine-red interface space. The heroine herself is NEVER on any screen.",
    "2-11": "INSIDE THE SCREENS: M and C sit upright with both hands below the screen edge and out of frame; nothing touches their chins or cheeks; they simply watch the phone.",
}
RETIRED = set()
HANDS = {
 "2-01": "她右手把手機插進手機架（五根手指清楚），左手扶著肩上的帆布袋背帶。螢幕裡三人只到胸口、手在畫面外。",
 "2-01A": "她的手在畫面外（桌緣以下）；三位先生只到胸口，晨右手在胸前轉一支鉛筆，其他人的手在畫面外。",
 "2-02": "只露她右手：拿著手機，拇指在螢幕下緣，其他四指在手機背後；左手在畫面外。",
 "2-03": "她的兩手都在畫面下緣之外（拿著手機）。",
 "2-03-1": "她的兩手都在畫面下緣之外。",
 "2-04": "只露她右手拇指在螢幕下緣，其他手指在手機背後。詩只到胸口，手在畫面外。",
 "2-05": "她兩前臂平放在桌上、兩手輕輕交握（看得到）。明兩手放在筆電鍵盤上；晨右手拿鉛筆、左手扶素描本；詩右手搭在椅背上、左手放在大腿上。",
 "2-05-1": "她只抬起右手在空中輕輕一揮（五根手指清楚），左前臂還平放在桌上；三位先生的手照 2-05。",
 "2-05-3": "她兩手放在腿上（畫面外）；三位先生的手照 2-05。",
 "2-05-4": "明兩手離開鍵盤，放在桌上；她兩手扶著桌緣；晨、詩的手照 2-05。",
 "2-05-5": "她兩手平放在桌上（看得到）；三位先生的手照 2-05。",
 "2-06C": "只露晨的右手拿鉛筆（五根手指清楚，袖口有黃綠細線）；畫裡的騎士手套是畫的，不是真的手。",
 "2-06M": "明兩手放在筆電鍵盤上，只露手背。",
 "2-06S": "詩右手微微抬離桌面、五指稍微張開（五根手指清楚），左手在畫面外。",
 "2-08": "她右手輕扶窗框（小、遠），左手垂在身側。桌邊三人的手看不清楚也可以。",
 "2-09": "晨只到胸口，右手在胸前輕拿一支鉛筆（五根手指清楚），左手在畫面外。",
 "2-09-1": "晨右手食指輕搔臉頰（不是撐著臉，手指只碰一下），左手在畫面外。",
 "2-10": "只露她右手放在觸控板上，五根手指自然。明只到胸口，手在畫面外。",
 "2-11": "詩只到胸口，右手在胸前像指揮那樣舉起（五根手指清楚），左手在畫面外。",
 "2-11-1": "詩右手食指點在螢幕內側一下，左手在畫面外。",
 "2-12": "她兩手臂環抱在肚子前（兩隻手都看得到、各五根手指），頭和手都沒有碰到桌子。",
 "2-12-1": "她右手指節輕擦眼角，左手放在桌上。",
 "2-13": "明只到胸口，手在畫面外。",
 "2-15": "她兩手一起把手機舉在臉上方（兩隻手都看得到、各五根手指）。",
 "2-15-1": "她兩手把被子拉到嘴巴上（手指從被緣露出一點）。",
 "2-15-2": "她的手藏在枕頭和被子下面，看不到。",
 "2-15-3": "她兩手交疊壓在胸口的手機上。",
 "2-16": "沒有手（主觀鏡頭，手機在畫面外的手上）。",
 "2-17": "沒有人，沒有手。",
}
PHONE = {
 "2-01": "她正把手機插進手機架",
 "2-02": "手機在她右手上，螢幕是一張旅行照片，角落一個小視窗裡是詩",
 "2-03": "手機在她手上（畫面外）",
 "2-04": "手機在她右手上，螢幕是同一張旅行照片，角落小視窗裡是詩",
 "2-15": "手機在她手上，舉在臉的上方",
 "2-16": "手機在她手上，舉在臉的上方",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    if k == "studio":
        return "工作室：桌上沒有任何手機；明用他自己的太空灰素面筆電；她的三台裝置都不在工作室。" + TEA_STUDIO.get(i, TEA_STUDIO["_"])
    tea = {"n9": "冰紅茶剛倒，冰塊滿滿", "n11": "冰紅茶冰塊半融、剩幾小塊", "a239": "冰紅茶在黑暗的書桌上看不清楚"}.get(t, "")
    if k == "bed":
        return "床：藍色格紋被、白枕頭（照空景）；她躺在床上；書桌在畫面邊緣、只是一團暗影，檯燈與房間的燈都關著；全畫面只有一支手機（在她手上）。"
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；" if "手機架" in ph else ""
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
