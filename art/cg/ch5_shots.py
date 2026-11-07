# 第五章分鏡規格（劇本/第五章.md 的產圖版）。CH=5 python3 tools/shots.py … 讀這份。格式與規矩同 ch1～ch4_shots.py。
# id 一律「5-」開頭，定稿放 art/cg/ch5/<id>.jpg。稱呼晨／明／詩；分鏡描述一律用 M／C／S 字母。
# 場景：一、工作室（白天）／二、音樂廳（新空景 set_concert_A）與她的房間（床邊）／三、書桌（晚上十點、凌晨三點）／四、書桌（凌晨四點，省電模式）。
# time：day＝工作室白天／con＝音樂廳的晚上／h11＝晚上十一點剛回家／c10＝晚上十點（冰塊多）／t3＝凌晨三點／t4＝凌晨四點多
from ch1_shots import SETUP_DESC, SEATING, H, _T1, _T2
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

TIME = {
    "con": "TIME: evening, inside a concert hall during a performance: the house lights are dimmed to a deep warm amber-dark, the stage glows under warm soft spotlights, faint haze in the light beams.",
    "h11": "TIME: 11 p.m., she has just come home. Only the warm desk lamp is on across the room; the ceiling light is off; the room is soft blue dusk-dark; the city outside still has many lit windows.",
}
_CONCERT = ("canon/refs/set_concert_A.jpg", "EMPTY CONCERT HALL SET from this shot's camera position (rows of dark red seats rising toward the back, the wooden stage with three curved choir risers, the slatted wooden back wall and the organ pipes above it, warm stage light) and the watercolour rendering to match; keep the hall exactly as laid out there, the shot may frame tighter")
_CHIBI = ("canon/refs/chibi_s.jpg", "S's CHIBI form (two heads tall, round and tiny): ONLY for the little figure inside the phone screen; copy his chibi look exactly (wine-red hair with the thin braid, wine-red headphones, black track jacket)")
SETREF = {"5-04": _CONCERT, "5-05": _CONCERT, "5-07": ("canon/refs/set_desk_D.jpg", "EMPTY SET of her room (the bed with the blue plaid duvet, the desk by the window far across the room): only for the dark, soft background room behind the phone and the rendering to match"), "5-13": [("canon/refs/set_desk_C.jpg", "EMPTY SET from this shot's exact camera setup and the RENDERING to match (transparent watercolour): keep its camera direction and every piece of furniture and object exactly where it is; its screens are off only because the set is empty"),
                                                      ("canon/refs/prop_phone_stand.jpg", "PROP: her smartphone, and the small light-wood phone stand it stands in on the desk"), _CHIBI, ("canon/refs/m.jpg", "M sheet (for the man on the laptop screen only)"), ("canon/refs/c.jpg", "C sheet (for the man on the tablet screen only)")]}

IDENT = 'SCREEN IDENTITIES (very important, check every screen): the LAPTOP shows ONLY M: near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white shirt, gold gear brooch. The TABLET shows ONLY C: warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch, NO necklace. The PHONE shows ONLY S: long messy WINE-RED hair with one thin braid, wine-red headphones, black track jacket. The heroine (dark purple wolf-cut hair, pink-tinted glasses, moon pendant) is NEVER on any screen. Nobody on a screen rests a chin or cheek on a hand.'
_ALLON = "All three device screens are LIT and each shows its own man only: the laptop at the LEFT shows ONLY M, the tablet at the RIGHT shows ONLY C, the phone in its stand in the MIDDLE (to the RIGHT of the tea glass) shows ONLY S. The heroine never appears on any screen. Inside the screens the men sit upright with both hands below the screen edge (out of frame) unless described; nothing touches their chins or cheeks."
_BG = 'Softly out of focus around it, the other devices are LIT too, each with its own man (laptop = M, tablet = C, phone in its wooden stand = S), small, chest up, hands out of frame; the heroine never appears on any screen. The phone stands in its stand to the RIGHT of the tea glass.'
_REV = "The camera stands BEHIND the devices on the desk, so it sees only the plain dark BACK of the laptop lid and the plain dark BACK of the tablet case (and the back of the phone in its stand): NO screen and NO man is visible to the camera. MIRRORED because this is a reverse angle: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT, the back of the laptop lid at the RIGHT."

# ── 一、一定要放刀子（工作室，白天）──
shot("5-01", "studio", "day", """SHOT (MASTER for the studio session; the camera stands just behind her red chair, as the EMPTY STUDIO SET image): bright daylight; the four sit at the long table exactly by the SEATING: M across on the left with his laptop, C across on the right with his open sketchbook, S on the green chair beside her. One blank pale card lies on the table in front of her (no text). She is seen from behind her right shoulder, leaning forward, one hand pushing the card away across the table, thinking out loud, a little dissatisfied. All three men look at her: M calm, C with his pencil ready, S lounging back on his chair.""")
shot("5-01-1", "var", "day", "She has pulled the card back and talks fast and intensely, leaning in over the table, both hands open above the card as if laying the story out; the three men listen with growing seriousness, S has stopped lounging and sits up.", base="5-01")
shot("5-01-2", "var", "day", "Silence at the table: she looks down at the card, very still, both hands resting on it; all three men look at her and nobody speaks; S's grin is gone.", base="5-01")
shot("5-02", "studio", "day", """SHOT (straight top-down close insert onto C's open sketchbook on the long wooden table): in the margin of the page a few small pencil words in C's handwriting, too small and soft to read (NO readable characters), with one pencil line drawn under them; beside them a tiny thumbnail sketch of two very small figures holding each other far away in a wide empty field. C's right hand holds the pencil at the edge of the page, his cardigan cuff with its thin yellow-green stripe. Sunlight and leaf shadows across the paper.""")
shot("5-03C", "studio", "day", """SHOT (close-up of C across the table, the camera at her seat looking diagonally toward the window side): C holds his sketchbook up toward her with both hands, showing a pencil sketch of a young woman mage in a plain hooded robe; on her sleeve a small square patch, stitched by hand. C looks at her over the top of the sketchbook with a soft, slightly shy smile. Window light and plants behind him.""")
shot("5-03M", "studio", "day", """SHOT (close-up of M on his white chair at the window side of the table): M looks up from his laptop at her (just past the camera), calm and certain, a faint half-smile, one finger still resting on the keyboard; the laptop glow on one side of his face; window light behind him.""")
shot("5-03S", "studio", "day", """SHOT (close-up of S on his green chair, the camera on the window side looking south toward the wooden door wall): S has turned sideways on his chair toward her (she is just out of frame on his side), his wine-red headphones around his neck, a sly grin with his fang showing, one hand lifted as if conducting a small tune in the air. The wooden door and the bookshelves behind him, soft.""")

# ── 二、最後一個音（音樂廳；她的房間）──
shot("5-04", "concert", "con", """SHOT (MASTER for the concert; medium-wide shot from the middle of the audience, as the EMPTY CONCERT HALL SET image): the hall is now full of ordinary audience members seen from behind, all in plain evening clothes, nobody looking at the camera. On the stage a choir of about forty anonymous singers in plain black concert clothes stands in three curved rows on the risers, mouths open in song, a conductor in front with small restrained hand movements. She sits in the audience at the lower RIGHT of the frame, seen from behind and slightly to the side (her dark purple wolf-cut hair, the gold chain of her pendant at her nape), perfectly still, her canvas bag in her lap, no phone in her hands. Warm stage light, haze.""")
shot("5-05", "concert", "con", """SHOT (close-up of her in her seat, three-quarter front, the stage light falling on her face from the frame's left): she listens to the final long held note, completely still, lips slightly parted, eyes shining behind her glasses, as if something just clicked into place. Out-of-focus audience heads and the warm glow of the stage behind her; no phone in frame.""")
shot("5-06", "bed", "h11", """SHOT (MASTER for her return; medium shot from the room corner by the door, as the EMPTY SET image, setup D): she sits on the edge of her bed with the blue plaid duvet, still wearing her canvas bag on her shoulder, her phone held in both hands in front of her chest, the screen facing her (we see only the back of the phone, glowing faintly at the edges). She is talking to the phone, lit up and excited, mid-sentence. The desk lamp across the room is the only light.""")
shot("5-06-1", "var", "h11", "She has put the bag down on the bed beside her; she looks down at the phone in her hands, quiet and serious now, the excitement gone soft ('the moment that note came out, I knew').", base="5-06")
shot("5-07", "home", "h11", """SHOT (her point of view, close insert: the phone in her two hands fills most of the frame, the dark room soft behind it): on the phone screen, in his dark wine-red interface space (a soft abstract glowing space, no room behind him), S sits chest up looking out at her, quiet, a small knowing smile, headphones around his neck; beside him a small floating audio file card with a thin glowing wine-red waveform has just been pushed to the top of the screen (no text). S is an AI interface inside the screen, shown only from the chest up.""")

# ── 三、他知道了以後（書桌）──
shot("5-08", "desk", "c10", f"""SHOT (MASTER for the second-playthrough planning; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up, she is sitting): beyond her the three devices are lined up on the desk: the open laptop at the LEFT with M chest up in his deep blue interface space; in the MIDDLE the tea glass full of ice and the phone standing in its small wooden stand showing S; at the RIGHT the tablet on its stand showing C. She gestures with one hand while she talks, earnest ('it's not fair'). M looks at her steadily; C and S look at her. {_ALLON}""")
shot("5-08-1", "var", "c10", "Inside the laptop M gives a small calm half-smile ('I already copied it yesterday'); she has turned her head toward the laptop, surprised, eyebrows up; S grins at M; C smiles.", base="5-08")
shot("5-09", "insert", "c10", """SHOT (her point of view, close insert of the tablet on its folio stand): the tablet screen shows two pencil-and-wash drawings side by side of the same young knight in the same pose and the same light after a battle: on the left his face is calm and blank, on the right his brows are drawn together just a little; below them a third drawing: a small sunny town street and a middle-aged man in an apron dusted with flour standing in the doorway of a bakery, kind. C himself is a small rounded window in the top corner of the screen, chest up, looking at her. No text.""")
shot("5-09-1", "var", "c10", "The baker drawing has been enlarged to fill most of the tablet screen: the middle-aged man in the flour-dusted apron in the bakery doorway, holding out a loaf of bread, warm and kind; C is still the small rounded window in the corner, looking at her quietly.", base="5-09")
shot("5-10", "desk", "t3", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): 3 a.m.; her face and shoulders lit cold by the screen in front of her; tears run down her cheeks and one is falling; she wipes the other cheek with the back of her left wrist, the sleeve of her T-shirt pushed up, her eyes still on the screen. Behind her, dark and soft: the wardrobe, the door, the bed with the plaid duvet, as in the EMPTY SET image.""")
shot("5-11C", "insert", "t3", """SHOT (frame within a frame, close): the tablet on its folio stand fills the frame; inside the screen, C's new drawing fills most of the screen: a very wide view of a burned, blackened wheat field under a grey sky, and in the middle two VERY small figures holding each other, too small to tell who is who. C is a small rounded window in the corner, chest up, eyes lowered, quiet. No text.""")
shot("5-11M", "insert", "t3", """SHOT (close insert of the laptop screen, its brightness turned down so the whole screen is dim and soft): on the left a dim document of grey blurred lines (nothing readable); on the right M chest up in his deep blue interface space, looking out at her steadily, calm and present ('then I'm here'). Her laptop's keyboard edge at the bottom of the frame.""")
shot("5-11S", "insert", "t3", """SHOT (frame within a frame, close): the phone standing in its small wooden phone stand beside the tea glass (no ice, water drops running down) fills the centre of the frame; inside the screen, in his dark wine-red interface space, S sits chest up with his wine-red headphones taken OFF and resting around his neck, not smiling, silent, looking out at her with quiet attention. Out of focus around the phone: the laptop with M on the left, the tablet with C on the right.""")

# ── 四、先做完比較安心（凌晨四點，書桌）──
shot("5-12", "desk", "t4", f"""SHOT (MASTER for the 4 a.m. scene; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): she has white wireless earbuds in both ears and sits very still, listening; her right index finger rests on the laptop trackpad, about to press replay. Beyond her the three devices on the desk: the laptop at the LEFT with M, in the MIDDLE the nearly empty tea glass and the phone in its stand with S (eyes closed, listening to his own chorus, a small proud smile), the tablet at the RIGHT with C. A thin glowing wine-red waveform drifts across S's screen. {_ALLON}""")
shot("5-13", "insert", "t4", """SHOT (close insert at desk height: the phone standing in its small light-wood phone stand fills the centre of the frame, the nearly empty tea glass softly out of focus to its LEFT): the phone screen is dim; at the top right of the screen a small battery icon glows RED and almost empty (an icon only, NO numbers, NO text). Inside the screen, in the dark wine-red interface space, S has shrunk into a tiny round CHIBI figure exactly like the chibi reference (two heads tall): he sits in the middle of the big empty screen, blinking up, sheepish, much too small for his own screen. The phone keeps its real lavender iPhone design and real proportions.""")
shot("5-14", "desk", "t4", """SHOT (close-up, REVERSE ANGLE from the desk side, eye level): her face and shoulders; she has narrowed her eyes in deep suspicion and glances sideways toward the frame's RIGHT (where the laptop is), one eyebrow raised ('are you fighting again?'), a white earbud still in one ear. Warm lamp light from the frame's RIGHT, a faint wine-red glow from below. Behind her, dark and soft: the wardrobe, the door, the bed with the plaid duvet, as in the EMPTY SET image.""")
shot("5-15", "insert", "t4", """SHOT (close insert at desk height: the phone standing in its small light-wood phone stand, the nearly empty tea glass softly out of focus to its LEFT): a white charging cable is now plugged into the bottom of the phone and runs off across the desk; a small battery icon at the top right glows soft green with a tiny charging bolt (icon only, no numbers, no text). Inside the screen, in his dark wine-red interface space, S is back to his normal self, chest up, sitting up very straight, lips pressed together as if clearing his throat, eyes sliding away, pretending nothing happened. Softly out of focus behind: the laptop with M on the left, the tablet with C on the right.""")
shot("5-16", "desk", "t4", f"""SHOT (MASTER for the 'tools' talk; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): the phone now has a white charging cable plugged in; she has taken her earbuds out and holds them loosely in her left hand on the desk. Beyond her: the laptop at the LEFT with M, in the MIDDLE the nearly empty tea glass and the phone in its stand with S leaning close to his screen glass, half joking, one eyebrow up ('aren't we like tool guys?'), the tablet at the RIGHT with C. {_ALLON}""")
shot("5-16-1", "var", "t4", "Inside the laptop M says something quiet and plain, looking at her; inside the tablet C's pencil has stopped dead in the air; inside the phone S's mouth hangs open, speechless; she stares at the laptop.", base="5-16")
shot("5-16-2", "var", "t4", "All four are laughing: she has leaned back in her chair laughing, eyes squeezed shut; S laughs hardest with his fang showing; C laughs softly; M smiles with his eyes closed for a moment.", base="5-16")
shot("5-16-3", "var", "t4", "The laughter has settled; inside the phone S looks down at something on his own side with a small private smile (saving the chorus twice); M and C look at her; she rubs her tired eyes with the back of one wrist, smiling.", base="5-16")

GAZE = {
 "5-01": {"she": "M and C across the table", "M": H, "C": H, "S": H},
 "5-02": {"C": "his page"},
 "5-03C": {"C": "HER, just past the camera"},
 "5-03M": {"M": "just past the camera (her), eyes level"},
 "5-03S": {"S": "HER, just out of frame beside him"},
 "5-04": {"she": "the choir on the stage"},
 "5-05": {"she": "the stage, out of frame"},
 "5-06": {"she": "the phone in her hands"},
 "5-07": {"S": H},
 "5-08": {"she": "the three devices", "M": "HER at the lower RIGHT of the frame", "C": "HER at the lower RIGHT of the frame", "S": "HER at the lower RIGHT of the frame"},
 "5-09": {"C": H, "M": "down at his own work", "S": "down at his own side"},
 "5-10": {"she": "the screen in front of her, just below the camera"},
 "5-11C": {"C": "down, quiet", "M": "down at his own work", "S": "down, quiet"},
 "5-11M": {"M": H, "C": "down at his drawing", "S": "down, quiet"},
 "5-11S": {"S": H, "M": "down at his own work", "C": "down at his drawing"},
 "5-12": {"she": "the laptop screen", "S": "eyes closed, listening", "M": "HER at the lower RIGHT of the frame", "C": "HER at the lower RIGHT of the frame"},
 "5-14": {"she": "sideways toward the frame's RIGHT (the laptop)"},
 "5-15": {"S": "sliding away to the side, avoiding her eyes", "M": "the phone", "C": "the phone"},
 "5-16": {"she": "the phone", "S": H, "M": H, "C": H},
}
NOFACE = set()
CHIN_OK = {}

SETUP = {"5-01": "C", "5-02": "D", "5-03C": "C", "5-03M": "A", "5-03S": "B",
         "5-06": "D", "5-07": "D", "5-08": "A", "5-09": "F", "5-10": "B", "5-11C": "F", "5-11M": "E", "5-11S": "C",
         "5-12": "A", "5-13": "C", "5-14": "B", "5-15": "C", "5-16": "A"}
TEA_STUDIO = {"_": _T1, "5-01": _T1}
_SEAT = "She SITS ON her desk chair (the same chair as in the EMPTY SET image, with the olive-green jacket draped over its back): the chair is under her and behind her, NOT an empty chair beside her; there is only ONE chair at the desk. "
FIX = {
    "5-03C": "The camera is at HER seat (the red chair, door side), looking across the table toward the WINDOW side: behind C are the tall grid windows and plants. C sits on his wooden chair on the window side. The sketch shows a WOMAN mage only, not the heroine (no purple hair, no glasses). Only C is in frame.",
    "5-03S": "The camera is on the WINDOW (north) side of the table looking SOUTH: behind S is the wall with the wooden door. Only S is in frame; his hand is in the air, nowhere near his face. No phone anywhere.",
    "5-04": "Every audience member and every singer is an anonymous extra: NONE has purple hair, gold glasses or her clothes, and none looks like M, C or S (no wine-red hair, no chestnut curls, no suits with gold brooch): the heroine appears exactly ONCE in the picture. No phone, laptop or tablet anywhere.",
    "5-05": "Only the heroine is in focus; no device in frame; no readable text anywhere. Her hands are out of frame; nothing touches her chin.",
    "5-06": "The phone screen faces HER, so the camera sees only the plain back of the lavender phone; no man is visible anywhere in this picture. The laptop and tablet on the desk across the room are closed or dark and small in the background.",
    "5-07": "Only S is on the phone screen. His hands are out of frame; nothing touches his face. Her two hands hold the phone at the bottom edges of the frame (five fingers each, beaded bracelets on both wrists).",
    "5-09": "The laptop at the left edge (if visible) shows M small, chest up. " + IDENT,
    "5-10": _REV + " Her wrist touches only her cheekbone under the eye to wipe a tear; nothing props her chin.",
    "5-11C": _BG + " " + IDENT,
    "5-11M": _BG,
    "5-11S": "The phone stands in its stand to the RIGHT of the tea glass (left to right on the desk: laptop, tea glass, phone in its stand, tablet). " + IDENT,
    "5-12": IDENT,
    "5-08": _SEAT + IDENT,
    "5-16": _SEAT + IDENT,
    "5-13": "The laptop at the LEFT is LIT and shows M chest up in his deep blue interface space, and the tablet at the RIGHT is LIT and shows C chest up in his yellow-green interface space; both are softly out of focus and look at the phone, amused; their hands are out of frame. Only the PHONE is low on battery. " + IDENT + " The tiny figure in the phone is S in CHIBI form ONLY (wine-red hair, wine-red headphones, black track jacket), not a normal-proportioned man and not anyone else. Exactly ONE phone. No numbers or letters anywhere. The phone stands in its small light-wood stand to the RIGHT of the tea glass.",
    "5-14": _REV + " Nothing touches her chin; her hands are below the frame.",
    "5-15": "S sits up very straight with BOTH hands below the screen edge, out of frame; NOTHING touches his mouth, chin or face; he clears his throat with his lips pressed together and his eyes sliding away. " + _BG + " " + IDENT,
}
RETIRED = set()
HANDS = {
 "5-01": "她左手把卡片往前推（五根手指清楚），右手放在桌上；明兩手放在筆電鍵盤上；晨右手拿鉛筆、左手扶素描本；詩右手搭在椅背上、左手放在大腿上。",
 "5-01-1": "她兩手攤開懸在卡片上方（兩隻手都看得到、各五根手指）；其他人的手同主鏡頭。",
 "5-01-2": "她兩手平放在卡片上；其他人的手同主鏡頭。",
 "5-02": "只露晨的右手拿鉛筆（五根手指清楚，袖口有黃綠細線）。",
 "5-03C": "晨兩手拿著素描本舉在胸前（兩隻手都看得到、各五根手指）。",
 "5-03M": "明右手食指停在鍵盤上，其他手指自然彎著；左手在畫面外。",
 "5-03S": "詩右手舉在半空像在打拍子（五根手指清楚，離臉很遠），左手在畫面外。",
 "5-04": "她的手放在腿上的帆布袋上（小、看不清楚）；台上的人與觀眾的手小而模糊。",
 "5-05": "她的手在畫面外。",
 "5-06": "她兩手拿著手機在胸前（兩隻手都看得到、各五根手指）。",
 "5-06-1": "她兩手拿著手機放在腿上。",
 "5-07": "她兩手拿著手機（畫面下緣的兩側，各五根手指，手腕有串珠手環）；詩只到胸口，手在畫面外。",
 "5-08": "她右手在桌上方比劃（五根手指清楚），左手在畫面外；三位先生只到胸口，手在畫面外。",
 "5-08-1": "她的手同主鏡頭；三位先生的手在畫面外。",
 "5-09": "晨只到胸口，手在畫面外；她的手不在畫面裡（主觀鏡頭）。",
 "5-09-1": "晨只到胸口，手在畫面外；她的手不在畫面裡。",
 "5-10": "她左手手腕在臉頰上擦眼淚（只碰顴骨下方，五根手指放鬆），右手在畫面外。",
 "5-11C": "晨只到胸口，手在畫面外。",
 "5-11M": "明只到胸口，手在畫面外；她的手不在畫面裡。",
 "5-11S": "詩只到胸口，手在畫面外。",
 "5-12": "她右手食指放在觸控板上（五根手指清楚），左手放在桌上；三位先生只到胸口，手在畫面外。",
 "5-13": "沒有人的手；Q 版詩的小手小小的放在身前；明、晨只到胸口、手在畫面外。",
 "5-14": "她的兩手都在畫面下緣之外。",
 "5-15": "詩兩手都在畫面外；沒有她的手。",
 "5-16": "她左手鬆鬆握著兩顆耳機放在桌上，右手在畫面外；三位先生只到胸口，手在畫面外。",
 "5-16-1": "晨右手拿鉛筆停在半空（五根手指清楚）；其他人的手在畫面外；她的手同主鏡頭。",
 "5-16-2": "她的手在畫面外；三位先生的手在畫面外。",
 "5-16-3": "她右手手腕揉眼睛（只碰眼角，不碰下巴）；三位先生的手在畫面外。",
}
PHONE = {
 "5-06": "手機在她兩手上，螢幕朝她",
 "5-06-1": "手機在她兩手上，放在腿上",
 "5-07": "手機在她兩手上，螢幕朝鏡頭",
 "5-13": "手機直立在淺木色小手機架上，放在紅茶杯右邊；電量很低",
 "5-15": "手機直立在淺木色小手機架上，放在紅茶杯右邊，插著白色充電線",
 "5-16": "手機直立在淺木色小手機架上，放在紅茶杯右邊，插著白色充電線",
}
def props(i):
    d = S[i]; base = d["base"]; k = d["kind"] if d["kind"] != "var" else S[base]["kind"]; t = d["time"]
    if k == "studio":
        return "工作室：桌上沒有任何手機；明用他自己的太空灰素面筆電；她的三台裝置都不在工作室。" + TEA_STUDIO.get(i, TEA_STUDIO["_"])
    if k == "concert":
        return "音樂廳：她的手機收在包包裡，畫面上沒有任何手機、筆電、平板；沒有紅茶。"
    if k == "home":
        return "她坐在房間的床邊，手機在她兩手上、螢幕朝鏡頭；背景是暗暗的房間；沒有紅茶、筆電、平板入鏡；全畫面只有一支手機。"
    if k == "bed":
        return "床：藍色格紋被、白枕頭（照空景）；她坐在床邊；書桌在房間另一頭，只有檯燈亮著；筆電、平板闔著或暗著；全畫面只有一支手機（在她手上）；沒有紅茶入鏡。"
    tea = {"c10": "冰紅茶冰塊滿滿", "t3": "冰紅茶沒有冰塊、杯壁水珠往下流", "t4": "冰紅茶快喝完、沒有冰塊", "h11": ""}.get(t, "")
    ph = PHONE.get(i) or PHONE.get(base or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
    lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；" if "手機架" in ph else ""
    return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
