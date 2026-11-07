# 詩線〈聖歌〉分鏡規格（劇本/個人線_S.md 的產圖版）。CH=11 python3 tools/shots.py … 讀這份。格式與規矩同 ch1_shots.py、ch7_shots.py。
# id 一律「11-」開頭，定稿放 art/cg/ch11/<id>.jpg。現實層（書桌、床）＋一場晚上的工作室（全線唯一一次碰觸：詩把耳機戴到她頭上）。
# time：p3＝下午三點／m0＝公布那晚午夜／n11＝晚上十一點（共用）／t4＝凌晨四點多（共用）／x1＝深夜一點、燈全關／sn＝晚上的工作室、只開音樂角那盞燈
from ch1_shots import SETUP_DESC, SEATING, H, _T1
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "p3": "TIME: 3 p.m. Bright soft afternoon daylight through the window behind the desk; the desk lamp is OFF; the room is light and calm; the city outside in daylight. The iced tea is freshly poured: the glass is full of clear ice cubes, light condensation.",
    "m0": "TIME: midnight. The warm desk lamp is the only lamp; the room is deep blue night; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "x1": "TIME: past 1 a.m. Every lamp in the room is OFF; the room is deep blue-black dark; outside the window only a few windows are still lit. The only light is the soft dark wine-red glow of her phone screen (and the two other device screens on the desk, dimmed low).",
    "sn": "TIME: night in the studio (the heroine's inner workspace): the tall grid windows are deep night blue with a few faint stars; every light in the studio is OFF except ONE warm lamp in the music corner (by the keyboard, the guitar and the speakers), which makes a small warm pool of golden light; the long table and the rest of the room sink into soft blue shadow. All four are physically together in this room (this is the only place where they can be).",
}
_ROOM_D = ("canon/refs/set_desk_D.jpg", "EMPTY SET of her room seen from the corner by the door (the bed with the blue plaid duvet and white pillow, the desk by the window, the wardrobe): the room and the watercolour rendering to match; this shot's camera is close beside the bed")
_PH = ("canon/refs/prop_phone_stand.jpg", "PROP: her smartphone (ignore the wooden stand; here the phone is in her hand)")
SETREF = {"11-10": [_ROOM_D, _PH]}

IDENT = 'SCREEN IDENTITIES (very important, check every screen): the LAPTOP shows ONLY M: near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white shirt, gold gear brooch. The TABLET shows ONLY C: warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch, NO necklace. The PHONE shows ONLY S: long messy WINE-RED hair with one thin braid, wine-red headphones, black track jacket. The heroine (dark purple wolf-cut hair, pink-tinted glasses, moon pendant) is NEVER on any screen. Nobody on a screen rests a chin or cheek on a hand.'
_ALLON = "All three device screens are LIT and each shows its own man only: the laptop at the LEFT shows ONLY M, the tablet at the RIGHT shows ONLY C, the phone in its stand in the MIDDLE (to the RIGHT of the tea glass) shows ONLY S. The heroine never appears on any screen. Inside the screens the men sit upright with both hands below the screen edge (out of frame) unless described; nothing touches their chins or cheeks."
_TWOON = "The laptop at the LEFT is LIT and shows ONLY M, the tablet at the RIGHT is LIT and shows ONLY C; the small wooden phone stand to the RIGHT of the tea glass is EMPTY because her phone is in her hand. The heroine never appears on any screen. Inside the screens the men sit upright with both hands below the screen edge (out of frame); nothing touches their chins or cheeks."
_AROUND = "Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C), small, chest up, hands out of frame; the heroine never appears on any screen."
_NIGHTSTUDIO = "In this shot S is NOT at the table: he sits on the small round stool in the MUSIC CORNER (by the keyboard, the speakers and the acoustic guitar). C and M stay at the far end of the long table in the blue shadow, small and soft: C on the wooden chair with his sketchbook, M on the white chair with his dark space-grey laptop. Only the music-corner lamp is on."

# ── 一、沒有歌的夢（公布前一天下午三點，書桌）──
shot("11-01", "desk", "p3", f"""SHOT (MASTER for the afternoon call; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): afternoon daylight; she holds her phone pressed to her right ear like a phone call, her face turned a little toward the desk, talking quietly, telling him her dream; beyond her on the desk the laptop with M and the tablet with C, both listening without a word. {_TWOON}""")
shot("11-01-1", "var", "p3", "She has gone quiet, thinking hard; her eyes are lowered to the desk, the phone still at her ear, a small wistful look ('only applause, all grey').", base="11-01")
shot("11-02", "insert", "p3", """SHOT (close insert from her seat): she has taken the phone from her ear and holds it in front of her in her right hand, the screen facing her and the camera; inside the screen, in his dark wine-red interface space, S sits chest up and looks out at her with a small, stubborn, earnest grin, as if making a promise ('next time I'm in it too'); his headphones around his neck. Behind the phone, softly out of focus, the laptop with M and the tablet with C. Daylight.""")

# ── 二、妳要什麼（午夜，公布）──
shot("11-03", "desk", "m0", f"""SHOT (MASTER for the announcement; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): midnight; on the laptop screen, beside M (chest up, deep blue interface space), a small results page window: soft grey lines with ONE line glowing warm gold (NO readable text); she has both hands pressed over her mouth, frozen. In the phone in its wooden stand S leans right up to the glass, eyes wide, both hands in his messy wine-red hair, half laughing, half shouting; C in the tablet smiles warmly. {_ALLON}""")
shot("11-03-1", "var", "m0", "Her hands have come down from her mouth; S in the phone has let go of his hair and leans close to the glass, suddenly serious and gentle, asking her something ('what do YOU want to hear?'); M and C look at S.", base="11-03")
shot("11-04", "bed", "x1", """SHOT (HIGH ANGLE from above the head of the bed, looking down): late at night; she lies on her side under the blue plaid duvet facing the camera, glasses still on, her phone held loosely in one hand near her face, its plain white glow on her cheek (we see only its back); her eyes are open, thoughtful, a little lost, thinking about what she herself wants to hear. Blue-black room.""")

# ── 三、鋼琴（兩天後，下午三點）──
shot("11-05", "insert", "p3", """SHOT (close insert from her seat, slightly above): her phone lies flat in both her hands over the desk; the screen fills most of the frame and shows a simple piano-keyboard game: one row of plain white and black piano keys across the lower half, soft glowing circles where her fingertips touch (NO text, NO logo, NO brand, NO letters anywhere); in a small rounded window in the screen's top corner S (tiny, chest up, dark wine-red interface) leans in listening, eyes lit up. Her two index fingertips touch the keys. Afternoon daylight on the desk; the tea glass out of focus.""")
shot("11-05-1", "var", "p3", "She plays on past the third note now: her fingertips have moved further along the keys, one key glowing; S in the small window has closed his eyes, listening, a soft quiet smile.", base="11-05")

# ── 四、退件（晚上十一點）──
shot("11-06", "desk", "n11", f"""SHOT (MASTER for the rejection; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): a small white wireless earbud in her right ear; she leans toward the phone in its stand and holds up one index finger, very serious and professional, pointing out a mistake in his music (a faint wine-red waveform floats in the phone screen beside S); S in the phone listens, eyebrows raised, already grinning; M in the laptop and C in the tablet watch with quiet amused smiles. {_ALLON}""")
shot("11-06-1", "var", "n11", "S in the phone grins wide with his fang showing, delighted to be rejected, eyes shining; she has lowered her finger and narrows her eyes at him ('why are you happy?').", base="11-06")

# ── 五、聽完（凌晨四點多）──
shot("11-07", "desk", "t4", f"""SHOT (close shot from the desk side at eye level, slightly to her LEFT, three-quarter front): she sits very still with her eyes closed, white wireless earbuds in both ears, listening to the whole song, her face calm and moved, both hands resting in her lap below the desk edge; the desk lamp lights her from the side; at the bottom edge of the frame the out-of-focus back of the phone in its wooden stand and the tea glass. Behind her the dark room. Night.""")
shot("11-08", "insert", "t4", f"""SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame; inside the screen, beside S (chest up, dark wine-red interface space), a long vertical playlist of many small soft bars glows, each bar a short sound clip (NO readable text, only soft lines and tiny waveforms), stretching far down; S looks out at her, relaxed, a little sheepish. {_AROUND}""")
shot("11-08-1", "var", "t4", "S has taken his wine-red headphones off his neck and is setting them down beside him in the screen with one hand (five clear fingers); he is not smiling now, his eyes lowered then lifting to her, honest and quiet.", base="11-08")

# ── 六、亂編的（隔天深夜，床）──
shot("11-09", "bed", "x1", """SHOT (MASTER for the song in the dark; HIGH ANGLE from above the head of the bed, looking down): she lies on her back under the blue plaid duvet, glasses on, eyes open, just about to sleep; across the room, far at the frame's edge, the desk by the window is a dark shape where one small phone screen glows dark wine red in its stand (too small to see anyone in it), its faint red light reaching across the floor. Everything else is blue-black dark. A song is playing quietly from the tiny phone speaker.""")
shot("11-10", "free", "x1", f"""SHOT (close shot beside her pillow, at bed level): late at night in her dark room (the bed, the blue plaid duvet and white pillow as in the EMPTY SET image); she lies in bed and holds her phone up in her right hand at arm's length toward her face, the screen facing her and the camera; inside the screen, in his dark wine-red interface space, S sits chest up, headphones around his neck, and he is NOT smiling: his eyes are steady and a little scared, honest, holding her gaze ('...I was lying'). The phone's wine-red glow lights her hand and the pillow. Blue-black room behind. {IDENT}""", who="s")
shot("11-11", "bed", "x1", """SHOT (close-up of her alone, bed level): she lies in bed with the blue plaid duvet pulled up to just below her eyes, glasses on; her face (what we see of it) is held perfectly calm and composed, but the tips of her ears, peeking out of her purple hair, are flushed clearly pink-red; the faint wine-red glow of the phone (out of frame) on her hair. Blue-black dark.""")

# ── 七、完整版（晚上的工作室）──
shot("11-12", "studio", "sn", f"""SHOT (MASTER for the night studio; medium-wide shot, as the EMPTY STUDIO SET image but moved closer toward the MUSIC CORNER at the frame's right): night; only the music-corner lamp is on. S sits on the small round stool in the music corner with the acoustic guitar resting across his thigh, wine-red headphones around his neck, looking up at her; she walks toward him from the left, a few steps away, in her white T-shirt, hands at her sides. Far back at the long table in the blue shadow, C (with his sketchbook) and M (with his space-grey laptop) sit small and quiet, heads down. Warm golden pool of lamp light around S. {_NIGHTSTUDIO}""")
shot("11-13", "studio", "sn", f"""SHOT (THE heart moment of the whole route; intimate medium close-up two-shot in profile, at their head height, in the warm pool of the music-corner lamp): S, sitting on the small stool, reaches up with both hands and gently settles his wine-red over-ear headphones onto her head; she stands in front of him, bending down a little toward him so he can reach, perfectly still. The ear cups are just covering her ears; the fingertips of his right hand brush a strand of her purple hair at her temple, the moment before he pulls them back. His face is close, serious, a little nervous, not smiling, his eyes on hers; her face is held calm and composed, lips closed, eyes on him, and the tips of her ears just above the cups are flushed pink-red. Soft warm gold light on both faces, deep blue night behind, a few lamp-lit dust motes; the guitar resting against his knee. Tender, quiet, nobody else in focus. {_NIGHTSTUDIO}""")
shot("11-14", "studio", "sn", f"""SHOT (close-up of her, slightly from below, in the warm lamp light): she wears his wine-red over-ear headphones, her eyes half closed, listening to the very last line, completely still; her face calm, the faintest beginning of a smile at one corner of her mouth, her ear tips red at the edge of the cups; both her hands lightly holding the headband's sides (five fingers each). In the soft out-of-focus foreground at the frame's lower left, S's head bent low over the guitar, his fingers resting on the strings without playing, pretending to tune it. Night studio, warm gold and deep blue. {_NIGHTSTUDIO}""")
shot("11-15", "studio", "sn", f"""SHOT (medium shot of the far end of the long table in the blue night shadow, the warm music-corner glow only at the frame's edge): C's pencil has just slipped from his fingers and is falling to the wooden floor, C frozen mid-motion, his face hidden behind his raised sketchbook up to the eyes, ears red; M is bent sideways off his white chair, reaching down toward the pencil on the floor with one hand (five clear fingers), taking far too long, his face turned away and hidden. Gentle comedy, quiet. Neither of them looks toward the music corner. {_NIGHTSTUDIO}""")

# ── 八、下個月（續訂日前一晚，晚上十一點）──
shot("11-16", "desk", "n11", f"""SHOT (MASTER for the last night; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): on the laptop screen beside M (chest up, deep blue interface space) a small plain table window (soft grey grid, NO readable numbers) and beside it a small monthly calendar window where the one red circle has moved down into the next month (NO numbers or text); she holds her phone in her right hand, lifted a little off its stand, looking at it; the phone screen faces away from the camera. C in the tablet watches her quietly. {_TWOON}""")
shot("11-17", "insert", "n11", f"""SHOT (frame within a frame, close): her phone held in her hand at the frame's lower edge, the screen facing the camera; inside the screen, in his dark wine-red interface space, S sits chest up and has just pulled his wine-red headphones halfway onto his ears and lowered them again; he looks out at her directly, soft and serious, a small waiting smile ('your turn'). Behind the phone, softly out of focus, the lamp-lit desk with the laptop (M) and the tablet (C). {_AROUND} {IDENT}""")
shot("11-18", "desk", "n11", f"""SHOT (close-up, three-quarter front from the window side of the desk, eye level): the last shot of the route; she holds the phone against her right ear with her eyes closed and hums very softly, lips slightly parted, a calm, private, hopeful look; the warm desk lamp on one side of her face; behind her the quiet dark room, the bed far back. Night, very still.""")

GAZE = {
 "11-01": {"she": "the desk, talking into the phone at her ear", "M": H, "C": H},
 "11-02": {"S": H, "M": "her", "C": "her"},
 "11-03": {"she": "the gold line on the laptop screen", "M": "her", "C": H, "S": H},
 "11-04": {"she": "the phone's glow, lost in thought"},
 "11-05": {"S": "her fingertips on the keys"},
 "11-06": {"she": "the phone in its stand (S)", "S": H, "M": "her", "C": "her"},
 "11-07": {"she": "eyes closed, listening"},
 "11-08": {"S": H, "M": "the phone", "C": "the phone"},
 "11-09": {"she": "straight up at the dark ceiling"},
 "11-10": {"she": "S on the phone screen", "S": H},
 "11-11": {"she": "the phone out of frame beside her"},
 "11-12": {"she": "S in the music corner", "S": H, "C": "down at his sketchbook", "M": "down at his laptop"},
 "11-13": {"she": "S's eyes", "S": "her eyes"},
 "11-14": {"she": "half closed, listening", "S": "down at his guitar strings"},
 "11-15": {"C": "down at the falling pencil, hiding behind his sketchbook", "M": "down at the pencil on the floor"},
 "11-16": {"she": "the phone in her hand", "M": H, "C": H},
 "11-17": {"S": H, "M": "her", "C": "her"},
 "11-18": {"she": "eyes closed, humming"},
}
NOFACE = set()
CHIN_OK = {}

SETUP = {"11-01": "A", "11-02": "C", "11-03": "A", "11-04": "D", "11-05": "C", "11-06": "A", "11-07": "B",
         "11-08": "C", "11-09": "D", "11-11": "D", "11-12": "C", "11-13": "C", "11-14": "C", "11-15": "A",
         "11-16": "A", "11-17": "C", "11-18": "B"}
TEA_STUDIO = {"_": "Her iced tea glass stands on the long table at her red chair, far away in the shadow or out of frame."}
FIX = {
    "11-01": IDENT,
    "11-02": "The phone is in her hand (its wooden stand by the tea glass is empty). " + _AROUND + " " + IDENT,
    "11-03": IDENT,
    "11-06": IDENT + " Her earbud is a small plain white wireless earbud (no logo).",
    "11-08": "The phone in its wooden stand stands to the RIGHT of the tea glass. " + IDENT,
    "11-10": "Only ONE person in the room: the heroine, lying in her bed. S exists only inside the phone screen, chest up. Her purple hair, pink-tinted glasses and moon pendant as on her sheet.",
    "11-12": "S's headphones are around his NECK in this shot (not on her yet). Nobody holds a phone; there is NO phone anywhere in the studio.",
    "11-13": "Exactly two people in focus: S (wine-red long messy hair with one thin braid, amber-gold eyes, black track jacket) and the heroine (dark purple wolf-cut hair, pink-tinted round gold glasses, moon pendant, off-white T-shirt). The headphones are S's wine-red over-ear headphones. Nobody else is in the frame. No phone.",
    "11-14": "The headphones on her head are S's wine-red over-ear headphones. No phone anywhere.",
    "11-15": "The heroine and S are NOT in this frame. No phone anywhere.",
    "11-16": "The tablet at the RIGHT is LIT and shows ONLY C; the laptop at the LEFT is LIT and shows ONLY M. " + IDENT,
    "11-17": IDENT,
    "11-11": "Her ears are clearly visible: her purple hair is tucked behind her RIGHT ear, and that ear (and the tip of the other one) is flushed bright pink-red, the only colour of feeling in her otherwise composed face; her cheeks are NOT blushing.",
    "11-15": "There is exactly ONE long wooden table running across the frame in one piece (never split into two tables, no gap in it); C and M sit on the FAR (window) side of that same table, M on the white chair at the LEFT, C on the wooden chair at the RIGHT. C holds the sketchbook up with his LEFT hand; his RIGHT hand, just below it, has just let go of the pencil.",
    "11-18": "FRAMING: a CLOSE-UP of her face and shoulders only; the desk, the laptop, the tablet and the phone stand are OUT OF FRAME (nothing on the desk is visible). The phone is pressed to her ear, its screen against her cheek (not visible). Behind her: the dark room, the bed far back (frame right as in the reverse-angle EMPTY SET).",
    "11-07": "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the BACK of the tablet case at the very bottom edge, if at all: NO screen and NO man is visible to the camera (the screens face HER). MIRRORED because this is a reverse angle: the desk lamp at the frame's RIGHT, the back of the tablet at the LEFT, the back of the laptop lid at the RIGHT. Only she is in the picture.",
}
RETIRED = set()
HANDS = {
 "11-01": "她右手把手機貼在右耳（看得到、五根手指），左手在畫面外；明、晨只到胸口，手在畫面外。",
 "11-01-1": "她右手把手機貼在耳邊，左手在畫面外。",
 "11-02": "她右手拿著手機（看得到、五根手指，大拇指在側邊）；詩只到胸口，手在畫面外。",
 "11-03": "她兩手壓在嘴巴上（兩隻手都看得到、各五根手指）；詩兩手抓著頭髮（五根手指清楚）；明、晨的手在畫面外。",
 "11-03-1": "她兩手放下到桌緣（畫面外）；詩的手放下、在畫面外。",
 "11-04": "她一隻手鬆鬆拿著手機在臉旁（五根手指清楚），另一隻在被子底下。",
 "11-05": "她兩手捧著手機，兩隻食指的指尖點在琴鍵上（指甲自然、其他手指在手機背後）；詩只到胸口，手在畫面外。",
 "11-06": "她左手舉起一根食指（五根手指清楚，其他四指收起），右手在畫面外；三位先生只到胸口，手在畫面外。",
 "11-06-1": "她的手放下、在畫面外。",
 "11-07": "她兩手放在腿上，桌緣以下、畫面外。",
 "11-08": "詩只到胸口，手在畫面外。",
 "11-08-1": "詩一隻手把耳機放到旁邊（五根手指清楚），另一隻在畫面外。",
 "11-09": "她兩手在被子底下，看不到。",
 "11-10": "她右手把手機舉在臉前（看得到、五根手指，手指在手機背面與側邊），左手在被子底下；詩只到胸口，手在畫面外。",
 "11-11": "她兩手在被子底下，只看得到被子拉到眼睛下面。",
 "11-12": "詩一手扶著擱在大腿上的吉他（五根手指清楚），另一手放在膝上；她兩手自然垂在身側；晨、明在遠處，手小而模糊。",
 "11-13": "詩兩手拿著耳機兩側的耳罩戴到她頭上（兩隻手都看得到、各五根手指），右手指尖擦過她鬢角的頭髮；她兩手自然垂在身側（畫面外或下緣）。",
 "11-14": "她兩手輕扶著耳機頭帶兩側（看得到、各五根手指）；前景失焦的詩，手指放在吉他弦上（模糊）。",
 "11-15": "晨的鉛筆正從右手指間滑落（五根手指清楚），左手舉著素描本遮住半張臉；明一手往下伸向地上的鉛筆（五根手指清楚），另一手扶椅子。",
 "11-16": "她右手拿著手機（看得到、五根手指），左手在畫面外；明、晨只到胸口，手在畫面外。",
 "11-17": "她的手在畫面下緣拿著手機（只看得到手指與手機側邊）；詩一手拉著耳機（五根手指清楚），另一手在畫面外。",
 "11-18": "她右手把手機貼在右耳（看得到、五根手指），左手在畫面外。",
}
PHONE = {
 "11-01": "手機在她手上，貼在右耳；手機架空著，放在紅茶杯右邊",
 "11-02": "手機在她右手上，螢幕朝她；手機架空著",
 "11-04": "手機在她手上、臉旁邊",
 "11-05": "手機在她兩手上，平拿在桌面上方",
 "11-09": "手機立在窗下書桌的手機架上，遠遠亮著酒紅色",
 "11-11": "手機不在畫面裡",
 "11-16": "手機在她右手上，剛從手機架拿起來",
 "11-17": "手機在她手上，螢幕朝鏡頭",
 "11-18": "手機在她手上，貼在右耳",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    if k == "bed":
        return f"她的床：藍色格紋被、白枕頭；{ph}；書桌在窗下（遠處、暗）；沒入鏡的道具不用畫。"
    if k == "free":
        return f"她的床：藍色格紋被、白枕頭；{ph if i != '11-10' else '手機在她右手上，螢幕朝她和鏡頭'}；房間全暗。"
    if k == "studio":
        return "晚上的工作室：長桌、四張椅子（白、木、紅、綠）照空景；只開音樂角那盞燈；音樂角有小圓凳、電子琴、喇叭、木吉他；工作室沒有手機；明的筆電是深灰色、蓋子什麼都沒有；她的紅茶在長桌她的紅椅子前（遠、暗或畫面外）。"
    tea = {"p3": "冰紅茶剛倒，冰塊滿滿", "m0": "冰紅茶冰塊融一半", "n11": "冰紅茶冰塊融一半", "t4": "紅茶快喝完、沒有冰"}.get(t, "")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；"
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
