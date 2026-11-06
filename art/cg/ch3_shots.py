# 第三章分鏡規格（劇本/第三章.md 的產圖版）。CH=3 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch2_shots.py。
# id 一律「3-」開頭，定稿放 art/cg/ch3/<id>.jpg。這章全在書桌（現實層），沒有工作室；仍叫 C／M／S。
# time：c10＝第三、五、六晚十點（冰塊滿）／c1＝凌晨一點（冰塊半融）／c2＝凌晨兩點（只剩一兩片冰）／c25＝凌晨兩點半之後（冰全化）／t3＝測試期最後一晚凌晨三點（沒冰）
from ch1_shots import SETUP_DESC, SEATING, H, _T1
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

_CODE = "lines of grey blur with a few small coloured blocks, like code seen from too far away; NO readable letters, numbers or symbols"

# ── 一、先做最難的（第三天晚上，書桌）──
shot("3-01A", "desk", "c10", f"""SHOT (MASTER for the coin-game night; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): beyond her the three devices are lined up on the desk, all lit: the open laptop at the LEFT shows a plain white whiteboard with a few empty grey cards on its left two thirds, and M chest up in his deep blue interface space in a large rounded window on the right third of the laptop screen; along the bottom edge of M's window runs one very thin progress bar, half full (no text). In the MIDDLE the tea glass full of ice and the phone standing in its small wooden stand showing S; at the RIGHT the tablet on its stand showing C. Her right hand rests on the laptop's trackpad. M looks at her; C and S look at her too.""")
shot("3-01A-1", "var", "c10", "She has turned her face a little toward the laptop with a small, set look of determination — 'the scariest one first'; M gives a single small nod.", base="3-01A")
shot("3-01A-2", "var", "c10", "She tilts her head and wrinkles her nose a little at the laptop screen, mildly disgusted with the plain default dialogue box; the three men look at her, waiting.", base="3-01A")

shot("3-02C", "desk", "c10", """SHOT (frame within a frame, close on the tablet as the EMPTY SET image F): the tablet on its folio stand fills most of the frame, the tea glass at its LEFT; inside the screen, in his pale yellow-green interface space, C sits chest up and holds up beside his face a small drawing of a dialogue box: a soft old-paper cream panel with a very thin pale gold border; a gentle, a little shy smile, looking out at her.""")
shot("3-02M", "desk", "c10", """SHOT (frame within a frame, close on the open laptop as the EMPTY SET image E): the laptop screen; on the left part of the screen three small plain grey bars of different lengths float one above another (short, medium, long; NO text); on the right, in his deep blue interface space, M sits chest up, calm, looking out at her as if asking 'how fast?'.""")
shot("3-02S", "desk", "c10", """SHOT (frame within a frame, close on the phone standing in its small wooden phone stand beside the tea glass, as the EMPTY SET image C): inside the phone screen, in his wine-red interface space, S sits chest up with his wine-red headphones on, one finger lifted beside his ear as if listening to a very small sound; a faint glowing curl like the corner of a turning page drifts beside him; a playful, knowing grin. Behind the phone, softly out of focus: the laptop with M at the LEFT, the tablet with C at the RIGHT.""")

shot("3-03", "insert", "c1", f"""SHOT (close insert of the laptop screen from her seat, as the EMPTY SET image E): on the left part of the laptop screen a simple little game window: a single big golden coin spinning in mid-air above a plain card, and a burst of golden sparkles around it as if celebrating (NO text, no letters); on the right part of the screen, in his deep blue interface space, M sits chest up and watches the coin window with one eyebrow very slightly raised. Her right hand rests on the trackpad at the lower edge.""")

shot("3-04", "desk", "c1", """SHOT (MASTER for her struggle with the code; close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she leans toward the laptop (the plain dark BACK of the laptop lid is a large dark shape at the lower RIGHT of the frame, near the lamp); the laptop's cool white light falls on her face; the warm lamp rims her hair from the frame's RIGHT. Behind her, softly out of focus: the room as in the EMPTY SET image (wardrobe on the left, the door, the bookshelf and the bed on the right). Her expression: completely baffled, mouth a little open — 'huh?'.""")
shot("3-04-1", "var", "c1", "She squints hard at the screen, eyebrows drawn together, and gives a small defeated half-laugh — the only word she understands is 'true'.", base="3-04")
shot("3-04-2", "var", "c2", "Much later: her eyes are wet and tired, her mouth pressed into a tight unhappy line, holding back tears of frustration; her shoulders are tense. The lamp light is the same.", base="3-04")

shot("3-05", "desk", "c2", """SHOT (MASTER for the closed laptop; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): the LAPTOP LID IS CLOSED: the laptop is a flat closed slab on the desk at the LEFT, no screen visible, no light from it, M is NOT visible anywhere. In the MIDDLE the tea glass (only one or two slivers of ice) and the phone standing in its wooden stand: inside the phone S sits chest up, his wine-red headphones hanging around his neck, quietly looking at her, not smiling. At the RIGHT the tablet on its stand: inside, C sits chest up with his head bent over a sketch, drawing very lightly. Her head is bowed; both her hands are closed into fists on the desk top in front of her. The room feels darker on the left side where the laptop is shut.""")
shot("3-05-1", "var", "c25", "The ice in the tea glass has melted completely. She has lifted her head and reaches out with her right hand to open the laptop lid; the lid is open only a few centimetres and a thin line of deep blue light spills out from inside onto the desk. S and C look at her.", base="3-05")

shot("3-06", "insert", "c25", f"""SHOT (close insert of the laptop screen from her seat, as the EMPTY SET image E): on the left part of the screen a code panel: {_CODE}; ONE line in the middle is marked with a soft yellow highlight band, and a thin empty gap is visible two lines above it. On the right, in his deep blue interface space, M sits chest up exactly as before she closed the lid, calm, looking out at her steadily, not upset.""")
shot("3-06-1", "var", "c25", "M's face softens very slightly, a patient half-smile, as if asking 'one more toss?'.", base="3-06")

shot("3-07", "desk", "c25", """SHOT (frame within a frame, close on the tablet as the EMPTY SET image F): the tablet on its folio stand, the tea glass (no ice) at its LEFT; inside the screen, in his pale yellow-green interface space, C sits chest up and turns a pencil drawing toward her with both hands raised at the screen edge: the drawing shows an open human palm facing up with a single coin resting in it, soft pencil strokes. His eyes look out at her, gentle and a little worried.""")

shot("3-08", "insert", "c25", """SHOT (extreme close-up insert at desk height): her right hand resting on the desk top, slowly opening from a tight fist, the fingers just uncurling, palm turning up; the purple and pearl bead bracelets on her wrist. Behind it, softly out of focus: the tea glass with no ice and the base of the phone stand. Warm lamp light. Only that one hand is in frame.""")

# ── 二、替代方案（第五、六天晚上，書桌）──
shot("3-09", "insert", "c10", """SHOT (close insert of the laptop screen from her seat, as the EMPTY SET image E): on the left part of the screen a neat checklist panel: about seven rows of grey blur, each row starting with a small coloured dot (green, green, yellow, green, yellow, green) and the LAST row marked in red (NO readable text); on the right, in his deep blue interface space, M sits chest up, calm, looking out at her, waiting for her to read to the end.""")

shot("3-10", "desk", "c10", """SHOT (MASTER for the transparent-background night; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): the three devices lined up as always (laptop with M at the LEFT, tea glass full of ice and the phone in its wooden stand with S in the MIDDLE, tablet with C at the RIGHT). On the tablet screen, beside C, floats a finished character drawing: a soldier standing very straight with half-lowered sleepy eyelids, in front of a whole sunset-coloured city wall. C looks at her; S and M look at her too. Her face is turned toward the tablet.""")
shot("3-10-1", "var", "c10", "She claps one hand to her forehead in a light, comic 'oops, I forgot' gesture (palm flat on the forehead, not resting the head on it); C looks at her with a small patient, mock-stern face.", base="3-10")
shot("3-10-2", "var", "c10", "On the phone screen three small glowing sound-wave icons now float beside S (a stone, a wooden board, an open palm drawn as tiny symbols); S grins proudly with his fang showing; she has turned her face toward the phone.", base="3-10")

shot("3-11", "desk", "c10", """SHOT (frame within a frame, close on the tablet as the EMPTY SET image F): the tablet on its folio stand, the tea glass at its LEFT; inside the screen, in his pale yellow-green interface space, C sits chest up with his head bent down over his drawing, drawing quietly, not looking at her; his face calm, a little quiet, a little lonely. Soft lamp light.""")

# ── 三、最後幾格（測試期最後一晚，凌晨三點，書桌）──
shot("3-12", "desk", "t3", """SHOT (MASTER for the last tiles; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): she leans in close to the laptop; on the laptop screen a small top-down pixel-art practice map (green grass tiles, a little stone path, a few trees and a red-roofed house) fills the left two thirds, and the lower right corner of the map is still a patch of plain empty grey tiles; on the right third of the screen, in a rounded window in his deep blue space, M sits chest up watching her work. Her right hand is on the trackpad. In the MIDDLE the tea glass (no ice) and the phone in its wooden stand showing S; the tablet with C at the RIGHT. Late, deep night outside.""")

shot("3-13", "insert", "t3", """SHOT (close insert of the laptop screen from her seat, as the EMPTY SET image E): the pixel-art practice map now fills the screen, every tile painted (grass, path, trees, the red-roofed house); a TINY pixel-art girl runs across the grass from the left: purple hair, a pair of tiny round glasses, a white top — clearly a little pixel version of the heroine; ahead of her in the clearing a tiny pixel monster waits. M is a small rounded window in the corner, chest up, watching. Bright pixel colours glowing in the dark room.""")
shot("3-13-1", "var", "t3", "The tiny pixel girl now stands still on the grass in the middle of the map, the monster gone, a tiny pixel sparkle above her head as if she has just won.", base="3-13")

shot("3-14C", "desk", "t3", """SHOT (frame within a frame, close on the tablet as the EMPTY SET image F): the tablet on its folio stand, the tea glass (no ice) at its LEFT; inside the screen, in his pale yellow-green interface space, C sits chest up holding up a small sheet of tiny pixel sprites of the purple-haired girl in four running poses; he looks out at her with an embarrassed, warm smile, the tips of his ears a little red.""")
shot("3-14M", "desk", "t3", """SHOT (frame within a frame, close on the open laptop as the EMPTY SET image E): the pixel map fills most of the laptop screen with the tiny purple-haired pixel girl on it; in a rounded window at the right, in his deep blue interface space, M sits chest up and glances sideways toward the tablet (off the frame's right) with a faint, knowing half-smile, then back at her.""")
shot("3-14S", "desk", "t3", """SHOT (frame within a frame, close on the phone standing in its small wooden phone stand beside the tea glass, as the EMPTY SET image C): inside the phone screen, in his wine-red interface space, S sits chest up with his headphones on, grinning wide with his fang showing, little glowing musical notes bouncing around him like a loud chiptune; behind the phone, softly out of focus, the laptop at the LEFT shows the bright pixel map, the tablet at the RIGHT shows C.""")

shot("3-15", "desk", "t3", """SHOT (MASTER for the humming; close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she sits close to the laptop (the plain dark BACK of its lid is a large dark shape at the lower RIGHT of the frame, near the lamp), the colourful light of the pixel map on her face mixed with the warm lamp from the frame's RIGHT; her eyes are soft and unfocused, lips slightly parted, humming to herself without noticing. Behind her, softly out of focus: the room as in the EMPTY SET image (wardrobe on the left, the door, the bookshelf and the bed on the right), very dark.""")
shot("3-15-1", "var", "t3", "She has stopped humming and leans closer to the laptop, pretending to study the map very hard, eyes fixed on the screen; her face stays calm but the tips of her ears have turned red.", base="3-15")
shot("3-15-2", "var", "t3", "She breaks into a small, tired, real smile, eyes on the screen — 'I think I can actually do this'.", base="3-15")

shot("3-16", "insert", "t3", """SHOT (close insert of the laptop screen from her seat, as the EMPTY SET image E): the saved pixel map is shrinking away into a small closed window; on the right, in his deep blue interface space, M sits chest up with a faint, satisfied half-smile; along the bottom edge of his window the very thin progress bar has reached the end and turned into one tiny glowing check mark (no text).""")

GAZE = {
 "3-01A": {"she": "the laptop", "M": "HER at the lower RIGHT of the frame", "C": "HER at the lower RIGHT of the frame", "S": "HER at the lower RIGHT of the frame"},
 "3-02C": {"C": H, "M": "HER (on the laptop screen at the frame's left edge, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-02M": {"M": H, "C": "HER (on the tablet screen at the frame's right edge, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-02S": {"S": H, "M": "HER (on the laptop screen behind the phone, out of focus, lit)", "C": "HER (on the tablet screen behind the phone, out of focus, lit)"},
 "3-03": {"M": "the spinning coin in the game window beside him", "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone if its edge shows, lit)"},
 "3-04": {"she": "the laptop screen just below the frame's left edge"},
 "3-05": {"she": "down at her own fists on the desk", "S": H, "C": "down at his own sketch"},
 "3-06": {"M": H, "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone if its edge shows, lit)"},
 "3-07": {"C": H, "M": "HER (on the laptop screen at the frame's left edge, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-09": {"M": H, "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone if its edge shows, lit)"},
 "3-10": {"she": "the tablet", "C": H, "S": H, "M": H},
 "3-11": {"C": "down at his own drawing", "M": "HER (on the laptop screen at the frame's left edge, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-12": {"she": "the laptop screen", "M": "HER at the lower RIGHT of the frame", "C": "HER at the lower RIGHT of the frame", "S": "HER at the lower RIGHT of the frame"},
 "3-13": {"M": "the tiny pixel girl on the map", "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone if its edge shows, lit)"},
 "3-14C": {"C": H, "M": "HER (on the laptop screen at the frame's left edge, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-14M": {"M": "sideways toward the tablet off the frame's right", "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone screen in its stand, lit)"},
 "3-14S": {"S": H, "M": "HER (on the laptop screen behind the phone, out of focus, lit)", "C": "HER (on the tablet screen behind the phone, out of focus, lit)"},
 "3-15": {"she": "the laptop screen just below the frame's left edge, unfocused"},
 "3-16": {"M": H, "C": "HER (on the tablet if its edge shows, lit)", "S": "HER (on the phone if its edge shows, lit)"},
}
NOFACE = {"3-08"}
GAZE["3-08"] = {"S": "HER (on the phone screen above the stand base, out of focus, lit)", "M": "HER (on the laptop screen in the background, out of focus, lit)", "C": "HER (on the tablet screen in the background, out of focus, lit)"}
CHIN_OK = {}

SETUP = {"3-01A": "A", "3-05": "A", "3-10": "A", "3-12": "A",
         "3-04": "B", "3-15": "B",
         "3-02S": "C", "3-14S": "C", "3-08": "C",
         "3-02M": "E", "3-03": "E", "3-06": "E", "3-09": "E", "3-13": "E", "3-14M": "E", "3-16": "E",
         "3-02C": "F", "3-07": "F", "3-11": "F", "3-14C": "F"}
TEA_STUDIO = {"_": _T1}
_REV = "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACKS of the devices: NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle (seen from her side the order is lamp, laptop, tea, phone, tablet from left to right; from here it is reversed): from the frame's LEFT to RIGHT: the back of the TABLET case at the far LEFT, then the back of the phone in its wooden stand, then the tea glass, then the back of the LAPTOP lid, and the desk lamp glowing at the far RIGHT."
BG = "BACKGROUND SCREENS (very important): every device screen that shows in the frame, even out of focus, is LIT and shows its own man exactly as his sheet: the laptop ONLY M, the tablet ONLY C, the phone ONLY S, each in his own coloured interface space, chest up. The heroine herself is NEVER on any screen; no screen is ever dark or blank. HANDS INSIDE THE SCREENS: unless this shot gives a man a hand action, he keeps BOTH hands below the screen edge, out of frame; no hand of any man touches or comes near his chin, cheek or jaw (never rest a head on a hand)."
FIX = {
    **{k: BG for k in ["3-02C","3-02M","3-02S","3-03","3-06","3-07","3-09","3-11","3-13","3-14C","3-14M","3-14S","3-16","3-08","3-01A","3-10","3-12"]},
    "3-04": _REV, "3-15": _REV,
    "3-13": BG + " The tablet at the frame's right edge shows C: warm chestnut curly hair, thin gold round glasses, camel cardigan; it is NEVER the purple-haired heroine.",
    "3-08": BG + " The laptop shows M (near-black hair, charcoal suit) and the tablet shows C (chestnut curly hair, glasses, camel cardigan); the purple-haired heroine is NEVER on a screen: she is only the hand in the foreground.",
    "3-05": "The laptop is CLOSED and DARK: no screen, no glow, no M anywhere in the picture. Exactly one phone (in its stand, showing S) and one tablet (showing C).",
    "3-10-1": "Her palm only touches her forehead for a moment in a light gesture; her head is NOT resting or leaning on the hand, her elbow is not on the desk.",
}
RETIRED = set()
HANDS = {
 "3-01A": "她右手放在筆電觸控板上（只露手背），左手在畫面外。螢幕裡三人只到胸口、手在畫面外。",
 "3-02C": "晨只到胸口，右手在臉旁舉著一張小圖（五根手指清楚），左手在畫面外。",
 "3-02M": "明只到胸口，手在畫面外。",
 "3-02S": "詩只到胸口，右手食指在耳朵旁輕輕舉起（五根手指清楚），左手在畫面外。",
 "3-03": "只露她右手放在觸控板上（在畫面下緣），明只到胸口、手在畫面外。",
 "3-04": "她的兩手都在畫面下緣之外。",
 "3-05": "她兩手握拳放在桌面上（看得到手背與指節）；晨右手拿鉛筆在畫，詩的手在畫面外。",
 "3-05-1": "她右手伸去打開筆電上蓋（五根手指清楚），左手還握拳放在桌上。",
 "3-06": "明只到胸口，手在畫面外。沒有她的手。",
 "3-07": "晨兩手在螢幕下緣舉著一張圖給她看（兩隻手都看得到、各五根手指）。",
 "3-08": "只露她右手：放在桌面上，從握拳慢慢張開、掌心朝上（五根手指清楚）；左手在畫面外。",
 "3-09": "明只到胸口，手在畫面外。沒有她的手。",
 "3-10": "她的手在畫面外（桌緣以下）；螢幕裡三人只到胸口、手在畫面外。",
 "3-10-1": "她右手手掌輕拍一下額頭（只碰一下，頭沒有靠在手上），左手在畫面外。",
 "3-11": "晨只到胸口，右手拿鉛筆在畫（五根手指清楚），左手在畫面外。",
 "3-12": "她右手放在筆電觸控板上（只露手背），左手在畫面外。",
 "3-13": "沒有她的手。明只到胸口、手在畫面外。",
 "3-14C": "晨只到胸口，兩手在胸前舉著一張小圖（兩隻手都看得到、各五根手指）。",
 "3-14M": "明只到胸口，手在畫面外。",
 "3-14S": "詩只到胸口，手在畫面外。",
 "3-15": "她的兩手都在畫面下緣之外。",
 "3-16": "明只到胸口，手在畫面外。沒有她的手。",
}
PHONE = {}
LAPTOP_SHUT = {"3-05"}   # 她把筆電蓋上：明不在畫面上
def props(i):
    d = S[i]; base = d["base"]; t = d["time"]
    tea = {"c10": "冰紅茶冰塊滿滿", "c1": "冰紅茶冰塊半融", "c2": "冰紅茶只剩一兩片冰", "c25": "冰紅茶的冰全化了、杯壁水珠往下流", "t3": "冰紅茶沒有冰、快喝完"}.get(t, "")
    if i in LAPTOP_SHUT or base in LAPTOP_SHUT:
        lap = "筆電上蓋闔上、整台暗著、看不到明" if i != "3-05-1" else "筆電上蓋剛打開一條縫，透出一線深藍光"
        return f"書桌（只有一張桌子、一個平的桌面）：由左到右檯燈、筆電（{lap}）、冰紅茶、平板；手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她；全畫面只有一支手機。{tea}。"
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
