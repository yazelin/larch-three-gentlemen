# 第一章分鏡規格（劇本/第一章_分鏡.md 的產圖版）。tools/shots.py 讀這份組提示詞。
# kind：room＝人形介面啟動前的房間（螢幕關著、沒有三位先生）／desk＝書桌（現實層，三人在螢幕裡）／insert＝特寫插入（可無人）／studio＝工作室（四人同處）／var＝從主鏡頭改表演／free＝不套共用段落
# time：t1＝23:40（冰塊融一半）／t3＝凌晨三點（沒冰塊）／t4＝凌晨四點多（杯子快空）／day＝工作室白天
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

# ── 一、題目 ──
shot("01-0", "room", "t1", """SHOT (establishing long shot): HIGH ANGLE: the camera is in the same corner as the EMPTY SET image (camera D, the corner by the door, looking across the room toward the window) but raised up to the CEILING, looking DOWN at about 45 degrees, so the whole small student bedroom is seen from above and she looks small. Keep the room layout of the EMPTY SET exactly; only the camera height changes. The room layout is exactly the set: the bed along the LEFT wall, the desk under the window, the wardrobe at the RIGHT edge; to the LEFT of the bed there is only the wall with the shelf, picture frames and plants, NO wardrobe and NO cupboard there. The door is behind the camera, not in the picture. The room is VERY DARK, much darker than the EMPTY SET (the set is lit only to show the layout; do not copy its brightness): the walls, the bed, the wardrobe and the floor sink into deep blue shadow, nearly black toward the edges and corners of the picture; the ONLY light is a small warm pool of the desk lamp on the desk and on her. She sits on the desk chair, small in the frame, head bowed over her phone held in both hands, waiting; the olive jacket hangs on the chair back. On the desk from left to right: the lamp, the laptop, the tea glass on its coaster, the tablet on its stand; their screens are DARK and OFF (the humanoid interface does not exist yet). A lot of dark negative space. Window: the city at night with many lit windows.""")

shot("01-1", "insert", "t1", """SHOT (extreme close-up insert at desk height, lens almost touching the tall iced tea glass): beads of condensation and half-melted ice cubes in sharp focus in the foreground; behind it, out of focus, her phone lying on the desk has just lit up with a notification, its white light blooming into soft bokeh. No person in frame. Warm lamp rim light on the glass.""")
shot("01-2", "desk", "t1", """SHOT (close-up, slightly low, from in front of her): she has pulled her chair close and holds the phone near her face; the phone is in the lower foreground, out of focus, seen from its back. The phone's white light lights her face from below; the lamp rims her hair in gold. Her eyes have just widened, her breath held, one corner of her mouth starting to rise — restrained excitement. Only the fingertips of one hand show at the phone's edge. Behind her: the dark room exactly as the EMPTY SET image (bed on the right, wardrobe and door further back); the desk and its devices are on the camera's side, out of frame.""")
shot("01-2b", "insert", "t1", """SHOT (her point of view: the phone screen fills the frame, slim silver bezel at the edges): the challenge web page as an illustration with NO readable text: a sea of clouds at dusk, four clouds bound in the sky by iron chains, and in the centre one large ornate padlock hanging from the chains. Painted like a film poster. Her thumb is not visible.""")
shot("01-2c", "var", "t1", """Change ONLY this: the large central padlock has just sprung open; the chains are breaking apart into hundreds of glowing golden motes of light, and one cloud is drifting free toward the upper right. The motes are the brightest thing in the frame.""", base="01-2b")
shot("01A", "desk", "t1", """SHOT (MASTER for her reading scene; medium close-up, three-quarter front): she sits at the desk reading the challenge page on her phone held at chest height; we see her from mid-chest up; the phone is a dark shape at the lower edge, her hands below the frame. Behind her, soft out-of-focus: the dark room exactly as the EMPTY SET image (bed on the right, wardrobe and door behind). The lamp lights her from the frame's right. The laptop and tablet are on the camera's side, out of frame. Expression: neutral, absorbed, reading.""")
shot("01A-1", "var", "t1", "She has just read the theme; her brow draws together very slightly and she goes completely still, lips just parted.", base="01A")
shot("01A-2", "var", "t1", "She narrows her eyes a little and the corners of her mouth turn down — mildly fed up with how abstract it sounds.", base="01A")
shot("01A-3", "var", "t1", "A small breath of a laugh through her nose; only one corner of her mouth lifts.", base="01A")
shot("01A-4", "var", "t1", "She goes quiet; her eyes soften and she gives a very small nod, as if the sentence touched her.", base="01A")
shot("01A-5a", "var", "t1", "She lowers her eyes, remembering a comment that hurt; a little wistful.", base="01A")
shot("01A-5b", "var", "t1", "She lifts her eyes again, chin set, a quiet decision in her face.", base="01A")
shot("01A-5c", "var", "t1", "She leans back against her chair with a self-mocking little smile, eyes up at the ceiling.", base="01A")

# ── 二、就這個月 ──
shot("02A", "insert", "t1", """SHOT (top-down shot straight above the desk): her phone lies flat showing three plain app tiles side by side (a brush icon, a code-brackets icon, a music-note icon — faceless tools, no text), each with a small glowing upgrade button; next to it a calculator and the tall iced tea glass on its cork coaster, half-melted ice. Only her right index finger hovers above the calculator, the rest of her hand out of frame; the finger has a natural nail and joints. DESK ORDER seen from above, left to right along the window: the lamp and books, the laptop, the tea glass on its coaster, the tablet on its stand; the phone lies in front of the laptop, the calculator beside it.""")
shot("02B", "room", "t1", """SHOT (close-up): she leans back in her chair, the phone resting against her chest, staring up at the ceiling and letting out a long breath — the student wallet is crying. Only her face, shoulders and the top of the phone in frame; hands out of frame. Lamp light from the side, the rest dark. The sigh is shown only by her face and shoulders (lips slightly parted, shoulders dropped); NO visible breath, NO smoke, NO vapour anywhere. TIGHT CLOSE-UP: only her head, shoulders and the top of the phone on her chest fill the frame; the laptop, tablet, tea glass and desk are all OUT OF FRAME (they are behind the camera). Behind her, soft blur of the dark room: the door and wardrobe, part of the bed at the frame's right.""")
shot("02B-1", "var", "t1", "She has sat upright; her eyes have settled and turned bright with resolve — 'just this month'.", base="02B")
shot("02-1", "insert", "t1", """SHOT (extreme close-up insert): her index fingertip pressing a glowing confirm button on the phone screen (no text on the button), the moment of contact; only the one finger is visible, with a natural nail and knuckle. Shallow depth of field.""")
shot("01-3", "insert", "t1", """SHOT (close-up, camera slightly above the desk looking down at about 35 degrees, the phone lying flat in the dark): the WHOLE phone is in frame and keeps its true shape: one straight rectangle with four equal rounded corners and parallel long edges, ordinary proportions exactly like the phone prop image, no warping, no bent or angled edges, no fish-eye. The laptop and tablet screens behind are switched OFF (dark glass), because the interface appears on the phone first. The room is dark except the desk lamp; on the phone screen three small rounded windows have just lit up side by side, each glowing a different colour — pale yellow-green, deep blue, dark wine red — with a faint human silhouette forming inside each, not yet clear. Their light spills across the desk and the glass. No readable text.""")

# ── 三、三位先生 ──
shot("03-T", "free", "t1", """A three-panel SPLIT-SCREEN composition (triptych, three tall panels side by side with thin dark gaps), cinematic, watercolour. Left panel: C appears for the first time inside a soft pale yellow-green glowing interface space with drifting motes, opening his eyes, gentle. Middle panel: M inside a deep blue glowing interface space, calm, looking up. Right panel: S inside a dark wine-red glowing interface space, a sudden bright grin. Each man is drawn exactly as his canon sheet (Images 2, 3, 4). Chest-up, each looking out of his panel toward the viewer's lower centre (toward her). No rooms, no text.""", who="cms")
shot("03-0", "desk", "t1", """SHOT (medium shot, dynamic): three streaks of light — yellow-green, deep blue and wine red — leap out of the phone in her hands: the blue one arcs into the laptop, the yellow-green one into the tablet, the red one curls back into the phone. Motion-blurred light trails across the dark room. She sits in the chair in the lower-left foreground, seen from behind her right shoulder as in the EMPTY SET image, startled, hair lifting slightly. The screens are just lighting up, and each man has just landed in his screen and turned his head to look at HER, his first sight of her: M in the laptop and C in the tablet turn their faces toward her at the left edge of the frame (eyes clearly on her, not up, not at the viewer), S in the phone in her hands looks up at her face, grinning.""")
shot("01-4", "desk", "t1", """SHOT (medium shot, REVERSE ANGLE: the camera stands behind the devices on the desk, looking at her): in the out-of-focus foreground we see only the BACKS of the devices as dark silhouettes: MIRRORED ORDER because the camera is behind the devices: from the frame's LEFT to RIGHT: the back of the TABLET on its folio stand at the LEFT, the back of the phone standing in its small wooden phone stand beside the tea glass in the middle, the back of the LAPTOP lid at the RIGHT. All three screens face HER, so no screen and no man is visible to the camera. In the middle ground she has jerked back in her chair, eyes wide, startled; the three coloured lights from the screens (pale yellow-green from the left, wine red from the centre, deep blue from the right) spill around the edges of the devices and hit her face at once; tiny reflections of three glowing screens shine in her glasses. The desk lamp and the stack of books are at the frame's RIGHT, behind the laptop (mirrored too); the wardrobe and door behind her, the bed at the frame's right.""")
shot("03S", "desk", "t1", """SHOT (frame within a frame, MASTER for S): the camera is close to the phone standing in its small wooden phone stand beside the tea glass; the phone's bezel frames S, who fills the screen from chest up inside his wine-red interface space, leaning close to the screen glass, curious, eyebrows up. She is not in frame. Behind and around the phone, softly out of focus: to the LEFT the OPEN laptop with M on its lit screen, to the RIGHT the tablet on its stand with C on its lit screen; the tea glass and the phone stand in the MIDDLE between them. Desk lamp bokeh.""")
shot("03S-1", "var", "t1", "S grins wide with his fang showing and points at himself with one hand (the hand inside the screen, drawn with five clear fingers).", base="03S")
shot("03S-2", "var", "t1", "S's eyes light up, remembering; a warm, almost proud smile, hands out of the screen.", base="03S")
shot("03A", "desk", "t1", """SHOT (MASTER for the introductions; medium shot from behind her LEFT shoulder, three-quarter back view of her at the lower RIGHT of the frame, chest up): beyond her, the three devices are lined up on the desk and clearly visible, from the frame LEFT to RIGHT: the open laptop with M, then the tea glass with the phone standing in its small wooden stand right beside it showing S (both in the MIDDLE, between the laptop and the tablet), then the tablet on its folio stand with C. The same positions in every frame of this scene. Each man inside his own coloured interface space, and ALL THREE look at HER (toward the lower RIGHT of the frame, where she sits; heads turned to the right): M has turned from his side monitor to her, C looks at her over his pencil, S leans toward her. Nobody looks up or away into the distance. Her hands are below the frame. Lamp light.""")
shot("03A-1", "var", "t1", "She turns her face a little toward the phone; we see her cheek and eyelashes soften. S looks at her expectantly; C and M watch quietly.", base="03A")
shot("03A-2", "var", "t1", "S frowns and raises an eyebrow, unconvinced; M in the laptop stays expressionless; C hides a smile.", base="03A")
shot("03A-3a", "var", "t1", "S leans toward the glass protesting; M only lifts his eyes toward S without moving his head.", base="03A")
shot("03A-4", "var", "t1", "She bows her head and laughs, her shoulders giving one small shake. S is stunned speechless; C laughs softly; M's mouth twitches.", base="03A")
shot("03A-5", "var", "t1", "She lowers her eyes to the desk, quiet, remembering; all three men fall silent and watch her.", base="03A")
shot("03A-6", "var", "t1", "She explains very seriously, a little sheepish in the eyes; M listens with a calm, patient look; S hides a grin.", base="03A")
shot("03A-7", "var", "t1", "Her shoulders drop; a resigned 'okay then' in her posture. M watches her with a faint, almost apologetic softness.", base="03A")
shot("03C", "desk", "t1", """SHOT (frame within a frame, MASTER for C): the tablet on its stand fills the frame; inside the screen, in his soft yellow-green interface space, C sits chest up holding a pencil between his fingers, a warm shy smile, looking out at her. She is not in frame. DEVICES: exactly ONE phone in the picture, S's phone standing in its small wooden phone stand beside the tea glass, lit, showing S looking at her; the laptop shows M and the tablet shows C, both lit and looking at her; nothing else lies on the desk with a screen.""")
shot("03C-1", "var", "t1", "C tilts his head slightly, a little embarrassed, explaining a quirk of his.", base="03C")
shot("03C-2", "var", "t1", "C's smile opens up and he sits straighter, eager, the pencil ready — 'tell me, I'll draw it right away'.", base="03C")
shot("03M", "desk", "t1", """SHOT (frame within a frame, MASTER for M): the open laptop fills the frame; inside the screen, in his deep blue interface space, M sits chest up, calm, a faint smile, looking out at her; a soft glow of another monitor to his side. She is not in frame. DEVICES: exactly ONE phone in the picture, S's phone standing in its small wooden phone stand beside the tea glass, lit, showing S looking at her; the laptop shows M and the tablet shows C, both lit and looking at her; nothing else lies on the desk with a screen. DEVICE ORDER on the desk from the frame's LEFT to RIGHT (camera faces the window): laptop, then the tall tea glass with the phone standing in its small wooden stand, then the tablet on its stand at the far right. The phone is never to the left of the laptop.""")
shot("03M-1", "var", "t1", "M lowers his eyes for a moment — the first hint of regret: there is one thing he cannot do for her.", base="03M")
shot("03M-2", "var", "t1", "M looks straight at her (toward the camera's left, not into the lens), steady and serious.", base="03M")
shot("03-F", "free", "t1", """A FLASHBACK image, two years ago: the same student desk at night, a younger her (same face and hair, slightly rounder cheeks) drawing alone on paper under the desk lamp, surrounded by crumpled sketches, five finished CG pages pinned to the wall. Desaturated, faded colours, the edges of the image dissolving into soft white watercolour bloom like a memory. No devices glowing, nobody else. Draw her face as the EMPTY SET image.""", who="t")
shot("03-F2", "var", "t1", "Change ONLY this: a soft pale yellow-green light now enters from the right edge of the frame and falls gently across her drawing paper, as if someone is keeping her company.", base="03-F")

# ── 四、三道鎖 ──
shot("04-0", "desk", "t1", """SHOT (extreme close-up): her profile, eyelashes lowered, she leans close over the desk reading the challenge page on her phone, which stands in its small wooden phone stand beside the tea glass on the desk in front of her (S is shown small in the corner of the phone screen); the screen light on her face, lamp light rimming her hair. The tea glass and the phone stand ON THE SAME single flat desk top, in the middle between the laptop and the tablet; there is no second level, shelf or step in the desk. Beyond her, in soft blur, the desk exactly as the EMPTY SET image (laptop, tea glass with the phone, tablet in that order).""")
shot("04-0b", "var", "day", "Change ONLY this: her eyes are now OPEN and the light has completely changed to bright white daylight from a tall window; the dark room behind her has become a soft, sunlit blur.", base="04-0")
shot("04-1", "studio", "day", """SHOT (medium-wide over-the-shoulder shot from just behind her right shoulder as she stands at the threshold of the studio, camera at her eye height): only the back of her head and her right shoulder at the lower left edge; beyond her, the sunlit studio with the tall grid windows, plants and the long wooden table, shafts of light with floating dust. FRAMING: tight enough that the three men at the table are seen from the waist up and their FACES ARE LARGE AND CLEAR (each face at least a tenth of the frame height); the room is the background, not the subject. The three men have each just paused what they were doing and turned their heads to look at her, natural and unposed, a little surprised and warm: C looks up from his sketchbook, M looks up from his laptop, S turns around on his chair; nobody poses, nobody smiles at the camera, nobody raises a hand to his face or headphones. S sits normally ON his chair, both feet on the floor.""")
shot("04A", "studio", "day", """SHOT (MASTER for the studio conversation; medium shot at eye level from one side of the long table): all four sit around the table: she sits nearest the camera on the left; C opposite her with his sketchbook; M at the head with his laptop; S sits relaxed but properly on his chair (back against the backrest, both feet on the floor, not slumping or sliding down), headphones around his neck. Above the middle of the table float three faint lines of light (no text). Sunlight from the tall windows. Everyone relaxed.""")
shot("04A-1", "var", "day", "She looks doubtful, eyebrows slightly raised; M answers her with a calm, level look; C and S glance at her.", base="04A")
shot("04A-2", "var", "day", "The three floating lines of light above the table glow brighter; everyone looks at them.", base="04A")
shot("04A-3a", "var", "day", "M leans forward slightly as he speaks; the others look at him.", base="04A")
shot("04A-3b", "var", "day", "C leans forward over his sketchbook as he speaks, thoughtful; the others look at him.", base="04A")
shot("04A-3c", "var", "day", "S leans forward with a half smile as he speaks; the others look at him.", base="04A")
shot("04A-4", "var", "day", "She leans back in her chair with a helpless little smile. ALL THREE MEN turn their heads to the LEFT of the frame and look at HER (she sits at the left): C and S amused, M calm. Nobody looks at the camera or upward.", base="04A")
shot("04A-5", "var", "day", "She closes her eyes and sighs. ALL THREE MEN look to the LEFT of the frame at HER: S and C holding back laughter, M calm and kind. Nobody looks at the camera or upward.", base="04A")
shot("04B", "studio", "day", """SHOT (close-up of her alone; S is a soft blurred shape beside her on her left side of the frame; behind her the studio's south wall with the wooden door, as in the EMPTY SET image): she bites her lip, uneasy — afraid of choosing wrong. Sunlight on her hair. HANDS: both her hands rest together on the table in front of her, fingers loosely laced; her chin and cheeks touch nothing.""")
shot("04B-1", "var", "day", "She gives a small self-mocking smile, eyes lowered.", base="04B")
shot("04-PC", "studio", "day", """SHOT (her POINT OF VIEW from her own seat, the red chair at the south-west corner of the table, at her seated eye height, looking DIAGONALLY across the table toward the north-east, where C sits at the window side; close-up): C across the table looks up from his sketchbook STRAIGHT INTO THE CAMERA — at her — his pencil stopped on the paper, a gentle, open look. Sunlight behind him, the background soft. At the lower edge, out of focus, the corner of her own sketchbook; her iced tea stands ON the table top in front of her, close to the near edge, its coaster flat on the wood, fully on the table. HANDS: M sits upright with both forearms resting on the table; S sits upright with both hands in his lap; nobody touches his own face, chin or cheek. SEATING FROM HER SEAT (very important): across the table M sits on the LEFT and C on the RIGHT; S is on HER side of the table beside her, so at most his shoulder shows at the near right edge of the frame; S is NEVER across the table.""", who="c")
shot("04-PM", "studio", "day", """SHOT (her POINT OF VIEW, the camera is her eyes; close-up): M at the head of the table looks STRAIGHT INTO THE CAMERA — at her — calm, quietly waiting for her to speak first, the glow of his laptop on one side of his face. Background soft. LEFT-RIGHT (very important): seen from her seat looking across the table toward the windows, M sits on the LEFT (with his laptop) and C sits on the RIGHT (with his sketchbook); S is on her own side of the table, to her right. M is in the centre-left, looking into the lens; C at the right looks at M; S's shoulder may show at the far right edge. Nobody touches his chin, cheek or face; hands rest on the table, the laptop keys, the sketchbook or the headphones as described. M has lifted his eyes from the laptop and looks DIRECTLY INTO THE LENS (at her), face turned to the camera, both eyes visible; his hands rest still on the table beside the laptop, not typing.""", who="m")
shot("04-PS", "studio", "day", """SHOT (her POINT OF VIEW, the camera is her eyes; close-up): S slips one ear of his wine-red headphones off and looks STRAIGHT INTO THE CAMERA — at her — a soft, curious half smile. One hand at the headphones, five clear fingers. Background soft. LEFT-RIGHT (very important): seen from her seat looking across the table toward the windows, M sits on the LEFT (with his laptop) and C sits on the RIGHT (with his sketchbook); S is on her own side of the table, to her right. S is in the foreground on the right, close to the camera, looking into the lens; across the table M (left) and C (right) look at S. Nobody touches his chin, cheek or face; hands rest on the table, the laptop keys, the sketchbook or the headphones as described.""", who="s")
shot("04C-1", "studio", "day", """SHOT (close-up from above the sketchbook, slightly angled): C's right hand holds a pencil and is drawing on a sketchbook page: only the outline of a tall city gate seen from inside, a doorframe of light, still unfinished; real pencil strokes. Only his one hand and cardigan cuff (with its thin yellow-green stripe) are visible.""", who="c")
shot("04C-2", "studio", "day", """SHOT (two-shot, medium close-up): she leans over to look at the sketch; C turns his head toward her and smiles; their faces are close, the sketchbook between them. Sunlight between them. Her hands out of frame; his hand holds the pencil. C's head is turned toward HER, his eyes on her face (not on the sketch), smiling.""", who="c")
shot("04C-3", "var", "day", "She has pulled back half a step, her ears turning pink; C watches her and smiles; on the sketchbook a second sketch now shows the gate from outside.", base="04C-2")
shot("04C-4", "studio", "day", """SHOT (insert, top-down): two pencil sketches side by side on the table — the tall gate seen from inside and the same gate seen from outside — and the tip of her index finger hovering between them, not choosing. Only the one finger visible. Strictly TOP-DOWN insert of the table surface only: the two sketches and the tip of her index finger entering from the bottom edge; NO faces, NO people in the frame except that one fingertip and hand.""", who="")
shot("04-afterC", "studio", "day", """SHOT (medium shot of the other two at the table): M has turned his eyes back to his laptop; S puts his headphones back on and does not look at her. Quiet; the sunlight a little cooler.""", who="ms")
shot("04M-1", "studio", "day", """SHOT (over M's shoulder): over M's shoulder we see his open laptop showing a simple grid practice map (coloured tiles, no text); across the table she sits listening; M turns his face toward her, profile visible.""", who="m")
shot("04M-2", "studio", "day", """SHOT (close-up of M): M explains seriously, leaning forward a little, voice low; laptop glow on one side of his face; sunlight behind.""", who="m")
shot("04M-3", "studio", "day", """SHOT (close-up of her): TIGHT close-up on HER face and shoulders only (from the chest up, she fills most of the frame); she watches M quietly, her hands under the table and out of frame, a hidden smile at the corner of her mouth, reassured. M is only a soft out-of-focus shoulder at the frame edge; C and S are NOT in this frame. Nobody rests a chin or cheek on a hand.""")
shot("04-afterM", "studio", "day", """SHOT (medium shot of the other two at the table): C lowers his head and goes back to his sketch; S's grin pauses for a beat before he smiles again. Quiet.""", who="cs")
shot("04S-1", "studio", "day", """SHOT (close-up, profile): S with his wine-red headphones on, eyes closed, tapping a rhythm on the table edge with two fingers, humming; a shaft of window light falls across half of his face. Behind him, out of focus, she watches. HANDS: she sits upright with both hands resting flat on the table in front of her; M stands with his hands at his sides; C's hands rest on his sketchbook; nobody touches his or her face, chin or cheek.""", who="s")
shot("04S-2", "studio", "day", """SHOT (two-shot, medium): S has pulled his headphones down to his neck and turned toward her, drawing one slow line in the air with one hand as he describes the sound; she listens, leaning in.""", who="s")
shot("04S-3", "var", "day", "She looks away with a slight pout of doubt held back; S shrugs with a grin.", base="04S-2")
shot("04S-4a", "studio", "day", """SHOT (close-up of S): S freezes for a second, then laughs, caught off guard by how picky she is.""", who="s")
shot("04S-4b", "studio", "day", """SHOT (close-up of her): she sips her iced tea as if nothing happened, a calm, slightly smug look, eyes on S. One hand holds the tall glass naturally (five fingers around the glass). TIGHT close-up of HER ONLY from the chest up; nobody else is in the frame.""")
shot("04S-5", "studio", "day", """SHOT (extreme close-up): her eyes closed, listening to a sound inside her head; window light on her eyelashes. EXTREME close-up of HER face only (eyes, eyelashes, cheek), nobody else in the frame, her hands out of frame.""")
shot("04-afterS", "studio", "day", """SHOT (medium shot of the other two at the table): C's pencil stops for a moment; M looks at her, then at S, then back to his laptop. LEFT-RIGHT (very important): seen from her seat looking across the table toward the windows, M sits on the LEFT (with his laptop) and C sits on the RIGHT (with his sketchbook); S is on her own side of the table, to her right. Only M (left) and C (right) are in the frame, across the table. Nobody touches his chin, cheek or face; hands rest on the table, the laptop keys, the sketchbook or the headphones as described.""", who="cm")

# ── 五、第一首歌（重產：新定稿＋AI 介面空間）──
shot("05-0", "desk", "t3", """SHOT (medium-long shot, quiet, lonely): wide shot from the room's corner exactly as the EMPTY SET image (setup D). She leans far back in her desk chair, head tilted back, staring up at the dark ceiling, unable to sleep. Both hands rest in her lap below the desk edge. On the desk: the phone standing in its small wooden phone stand beside the tea glass with S small and quiet, the laptop with M, the tablet with C; all three turn their heads to the LEFT and look at HER (eyes clearly on her, not down at the desk, not up, not at the viewer). Lots of dark negative space above her.""")
shot("05A", "desk", "t3", """SHOT (MASTER for the 3 a.m. scene; medium close-up, shallow depth of field): camera on the desk side looking at her, eye level. She sits upright, framed from mid-chest up, turned three-quarter toward the frame's RIGHT and looking down at her phone standing in its small wooden phone stand beside the tea glass in the lower-right foreground; the phone is angled so we clearly see S inside it in three-quarter view, looking back at her, headphones around his neck. Behind her, soft blur: the dark room exactly as the EMPTY SET image (bed on the right, wardrobe and door behind). The laptop and the tablet are completely OUT OF FRAME (beside and behind the camera); no laptop, no tablet and no closed device lies anywhere in the picture. Only the tea glass on its coaster and the phone in its stand stand on the desk in front of her. Her hands below the frame. Expression: tired after midnight, quiet, a little lonely, eyes on S.""")
shot("05A-1", "var", "t3", "She speaks softly toward the phone, lips just parted, eyebrows slightly raised in a small hopeful question. S has burst into an easy laugh.", base="05A")
shot("05A-2", "var", "t3", "She has pulled her knees up onto the chair and rests her chin on her knees, arms wrapped around her shins and hidden behind her knees, eyes still on S, a little shy. S tilts his head, curious.", base="05A")
shot("05A-3", "var", "t3", "She looks away toward the dark window on the left, eyes unfocused, describing something she sees in her mind, serious. S listens intently, no smile.", base="05A")
shot("05A-4", "var", "t3", "She watches the phone, waiting. S has just put his wine-red headphones ON his ears and is closing his eyes, a faint wry half smile; his hands are out of the screen.", base="05A")
shot("05A-5", "var", "t3", "She smiles for the first time tonight, softly, eyes warm and certain, looking at the phone. S has headphones around his neck and gives her a small nod.", base="05A")
shot("05-1", "insert", "t3", """SHOT (extreme close-up insert): the phone screen fills most of the frame, the slim silver bezel framing it; inside, in his dark wine-red interface space with drifting motes, S has his wine-red headphones on and closes his eyes, lips parting to sing, completely absorbed; a thin glowing red waveform rises along the bottom of the screen. Hands out of frame. The screen glow is the main light; amber lamp bokeh around.""", who="s")
shot("05-2", "desk", "t3", """SHOT (close-up, REVERSE ANGLE from the desk side looking at her, eye level): her face and shoulders, turned slightly toward the phone standing in its small wooden phone stand beside the tea glass at the frame's lower right (the phone itself is out of frame); the phone's dark wine-red light falls across her cheek; her eyes are wet and wide, lips slightly parted: she has just understood what the song is. Behind her the dark room exactly as the EMPTY SET image (bed on the right, wardrobe and door further back), out of focus. One small white wireless earbud in her ear.""")
shot("05-3", "insert", "t3", """SHOT (extreme close-up): one of her eyes behind the thin gold rim and pale pink lens of her glasses; reflected on the lens, a thin glowing wine-red sound waveform; her eyelashes and the warm lamp light; goosebumps implied only by her stillness. Only the eye, the lens and part of her cheek in frame.""", who="t")
shot("05-4", "free", "t3", """An IMAGINED picture inside her head (no desk, no devices): an extreme long shot from high up inside a vast, very dark cathedral: stone columns fading into darkness, and one single shaft of pale light falling from a high window onto a tiny kneeling figure in the middle of the stone floor, too small and far to recognise. The only bright thing in the whole picture is the shaft of light. Transparent watercolour, deep blue-black washes, a sacred but slightly wrong feeling.""", who="")
shot("01-6", "desk", "t3", """SHOT (cinematic over-the-shoulder, shallow depth of field): camera just behind her LEFT shoulder, very close, at her eye height. FOREGROUND (strongly out of focus): the back of her dark purple hair, a white wireless earbud, the curve of her cheek and eyelashes in lost profile, the gold rim of her glasses. MIDGROUND (the only sharp area): the phone standing in its small wooden phone stand beside the tea glass; inside S sings with eyes closed, headphones on, a small gentle smile; a glowing red waveform along the bottom; the red glow spills onto the glass and her cheek. BACKGROUND (deep blur): the laptop with M and the tablet with C, both with eyes closed, listening. DEVICE ORDER on the desk from the frame's LEFT to RIGHT: the laptop with M, then the tall tea glass with the phone standing in its small wooden stands front, then the tablet on its stand with C at the right. The phone is between the laptop and the tablet, never to the left of the laptop.""")
shot("05-6", "desk", "t3", """SHOT (her POINT OF VIEW, the camera is her eyes): the phone standing in its small wooden phone stand beside the tea glass fills the centre of the frame, close. Inside the screen S looks STRAIGHT INTO THE CAMERA — at her — with a soft, warm, unguarded smile, headphones around his neck, a small nod. At the top-left corner, the out-of-focus edge of her glasses frame and a few strands of her purple hair. The laptop and tablet are soft blurred glows in the background (M and C small and blurred, looking at S). Hands out of frame.""")

# ── 六、續訂日 ──
shot("06-0", "desk", "t4", """SHOT (medium shot): past 4 a.m.; she sits at the desk wearing small WHITE WIRELESS earbuds (no cables at all), her head slowly sinking forward, eyelids half closed, about to fall asleep over her open textbook. The three screens still glow softly with M, C and S; all three watch her. Lamp light. Exactly ONE phone: S's phone standing in its small wooden phone stand beside the tea glass showing S; no second phone lying on the desk.""")
shot("01-7", "desk", "t4", """SHOT (close shot, camera at desk height just behind and to the right of her chair, the same direction as the EMPTY SET image, looking toward the window): she has fallen asleep with her cheek on her folded arm on the open textbook, her face turned toward the camera in three-quarter, glasses slightly askew, small WHITE WIRELESS earbuds in her ears (no cables at all); only one forearm is visible under her cheek, her hand tucked out of sight. Beyond her head, slightly out of focus, the desk in its fixed order from LEFT to RIGHT: the laptop with M, the tall tea glass with the phone with S standing in its small wooden stand, the tablet on its stand with C; all three look down at her. Their three colours of light lie over her hair. CHECK THE ORDER: the laptop is the LEFTMOST device; the tea glass and phone stand BETWEEN the laptop and the tablet; the pencil cup and books are at the far left beside the lamp, never between devices.""")
shot("06A", "desk", "t4", """SHOT (MASTER for the three men's whispered talk; from just behind and above her sleeping head): her hair in the lower foreground, out of focus; beyond her the three devices on the desk, sharp: the laptop with M, the tablet with C, the phone with S, each in his own coloured interface space; the men can see each other and talk quietly. Lamp light, deep blue night, the window almost all dark.""")
shot("06A-1", "var", "t4", "S looks down at her tenderly; C turns his head toward S's phone, asking.", base="06A")
shot("06A-2", "var", "t4", "C lowers his eyes; S looks at C, realising.", base="06A")
shot("06A-3", "var", "t4", "All three look down at her sleeping, silent, serious.", base="06A")
shot("06A-4", "var", "t4", "S starts to smile again but it fades almost at once; C and M do not smile; they look at S.", base="06A")
shot("06A-5", "var", "t4", "M looks down at her sleeping face, calm and firm; S and C look at M.", base="06A")
shot("06C", "desk", "t4", """SHOT (frame within a frame, close-up): the tablet screen fills the frame; inside, in his yellow-green interface space, C looks down at her (toward the lower left, not into the lens) with steady, quiet resolve, the pencil held still in his hand. In the background laptop, M also looks down toward her sleeping head (never up and away). Her sleeping head lies on the desk IN FRONT of the tablet, below and in front of its stand, clearly outside the screen; inside the screen there is ONLY C in his yellow-green space; her reflection or head never appears inside the screen.""", who="c")
shot("06-1", "insert", "t4", """SHOT (extreme close-up insert, composed like the challenge page's central padlock): the camera looks straight at the open laptop screen; INSIDE the screen, in M's deep blue interface space, a small floating calendar window shows a simple monthly grid with NO numbers or text, one day circled in a single red ring, dead centre of the frame; only the edge of M's shoulder and his gold gear brooch are visible INSIDE the screen beside it. Frame it tight on the laptop screen so the tablet and phone are OUT OF FRAME (if any edge of them shows, the tablet shows C in his pale yellow-green space and the phone shows S in his wine-red space; never a blank or landscape-wallpaper screen). Nobody is in the room in front of the laptop. Cold blue light. She is ASLEEP with her head down on the desk; she is NOT awake, NOT sitting up, and NO hand of hers appears anywhere; nobody holds any device. Only the top of her sleeping head may show at the lower edge, out of focus.""", who="m")
shot("06M", "desk", "t4", """SHOT (frame within a frame, close-up): the laptop screen; inside, in his deep blue interface space, M looks at no one, eyes lowered to the side, cold blue light on his face, unreadable. Exactly ONE phone in the whole picture: S's phone standing in its small wooden phone stand beside the tea glass, showing S; there is NO second phone lying on the desk. She is ASLEEP with her head down on the desk; she is NOT awake, NOT sitting up, and NO hand of hers appears anywhere; nobody holds any device. Only the top of her sleeping head may show at the lower edge, out of focus.""", who="m")
shot("06-F", "var", "t1", "Change ONLY this: grade the whole image cold blue and slightly faded, the edges dissolving softly into white like a memory; every object, the finger and the layout stay exactly as in Image 1.", base="02A")
shot("06S", "desk", "t4", """SHOT (frame within a frame, close-up): the phone screen; inside, in his wine-red interface space, S, inside the phone screen, holds his wine-red headphones in one hand (five clear fingers), having just taken them off his ears; for the first time he is not smiling; he looks down toward her. The phone stands propped in its wooden stand beside the tea glass on the desk; no real hand holds it. She is ASLEEP with her head down on the desk; she is NOT awake, NOT sitting up, and NO hand of hers appears anywhere; nobody holds any device. Only the top of her sleeping head may show at the lower edge, out of focus.""", who="s")
shot("06-2", "desk", "t4", """SHOT (extreme close-up): strands of her dark purple hair on the textbook page, with the warm lamp light and the three faint coloured glows (yellow-green, blue, wine red) lying across them. Nothing else. Silence.""")
shot("06-3a", "var", "t4", "Change ONLY this: the laptop screen has gone completely DARK (M is gone); the tablet with C and the phone with S are still lit; the blue light no longer falls on her hair.", base="06A")
shot("06-3b", "var", "t4", "Change ONLY this: the laptop AND the tablet screens are completely DARK (M and C are gone); only the phone with S is still lit; only a faint red glow remains on her hair.", base="06A")
shot("06-3c", "var", "t4", "Change ONLY this: all three screens — laptop, tablet and phone — are completely DARK; nobody is visible; only the warm desk lamp light remains on her hair.", base="06A")
shot("06-4", "var", "t4", "Change ONLY this: she is now asleep, her head resting on her folded arms on an open textbook on the desk, small white wireless earbuds still in her ears; her phone lies dark on the desk beside her arm; the laptop, tablet and phone screens are all dark; the window shows the city with almost every window dark; the lamp is the only light; even more stillness.", base="01-0")

# 視線表（yazelin 2026-11-06：「各的人物到底是誰在看誰 要畫清楚」）。shots.py 會把它附在每一格提示詞最後。
# 她＝茶語。「her」在螢幕裡＝轉向她所在的方向；POV 格的「lens」才看鏡頭。沒列到的人不在畫面裡。
H = "HER"
GAZE = {
 "03-T": {"C": "toward the lower centre (her)", "M": "toward the lower centre (her)", "S": "toward the lower centre (her)"},
 "03-0": {"she": "the streaks of light, startled", "M": H, "C": H, "S": "up at her face"},
 "03S": {"S": H + ", eyes open and bright, leaning close to the screen glass", "M": "sideways and down at the monitor beside him, clearly reading it", "C": H, "she": "out of frame"},
 "03A": {"she": "the three devices", "M": "HER at the lower RIGHT of the frame, close to the camera: head turned to the right, eyes down-right", "C": "HER at the lower RIGHT of the frame: head turned to the right, eyes down-right", "S": "HER at the lower RIGHT of the frame: leaning to the right, eyes down-right"},
 "03C": {"C": H, "M": "C on the tablet (head turned toward the tablet beside him, eyes level, NOT up)", "S": "C on the tablet, curious"},
 "03M": {"M": "just past the camera, slightly to the left, eyes level (she sits right beside the camera)", "C": "M on the laptop, smiling a little", "S": "M on the laptop"},
 "04-0": {"she": "her phone, absorbed", "M": H + " (quietly watching her read)", "C": H, "S": H},
 "04-1": {"she": "the room in wonder", "M": H, "C": H, "S": H},
 "04A": {"she": "the floating lines of text above the table", "M": H, "C": H, "S": H},
 "04B": {"she": "down at the table, uneasy", "M": H, "C": H, "S": H},
 "04C-2": {"she": "the sketch", "C": "HER FACE, his head fully turned to her, eyes clearly on her eyes, NOT down at the sketchbook"},
 "04-afterC": {"M": "his laptop screen", "S": "down, eyes half closed, not at her"},
 "04M-1": {"M": "his laptop screen", "she": "M"},
 "04M-2": {"M": H},
 "04M-3": {"she": "M"},
 "04-afterM": {"C": "his sketchbook", "S": "M"},
 "04S-1": {"S": "eyes closed"},
 "04S-2": {"S": H, "she": "S"},
 "04S-4a": {"S": H},
 "04S-4b": {"she": "S"},
 "04-afterS": {"C": "his sketchbook, pencil stopped", "M": "S"},
 "05-0": {"she": "the dark ceiling", "M": H, "C": H, "S": H},
 "05A": {"she": "S", "S": H},
 "01-6": {"S": "eyes closed, singing", "M": "eyes closed, listening", "C": "eyes closed, listening"},
 "05-6": {"S": "lens", "M": "lens (her)", "C": "lens (her)"},
 "06-0": {"she": "eyelids half closed", "M": H, "C": H, "S": H},
 "01-7": {"she": "asleep"},
 "06A": {"she": "asleep", "M": "down at her sleeping head", "C": "down at her sleeping head", "S": "up at her sleeping head"},
 "06C": {"C": "down at her", "M": "down at her", "she": "asleep"},
 "06M": {"M": "lowered to the side, at no one", "C": H, "S": H, "she": "asleep"},
 "06S": {"S": "down toward her", "M": H, "C": H, "she": "asleep"},
}

GAZE.update({
 "04-PC": {"C": "lens (her), eyes raised from the sketchbook straight into the camera", "M": "C", "S": "C"},
 "04-PM": {"M": "lens (her)", "C": "M", "S": "M"},
 "04-PS": {"S": "lens (her)", "M": "S", "C": "S"},
 "04S-1": {"S": "eyes closed", "she": "S", "M": "S", "C": "S"},
})

GAZE.update({
 "01-2": {"she": "her phone, just below the camera"},
 "01A": {"she": "her phone"},
 "01-4": {"she": "the three glowing screens on the desk, coloured light on her face"},
 "05-2": {"she": "the phone at the lower right"},
})

# 書桌機位（yazelin 2026-11-06 第一章回饋：東西亂搬、兩張桌子）。平面圖 canon/refs/desk_plan.jpg，空景 canon/refs/set_desk_<機位>.jpg。
SETUP = {
 "01-0": "D", "05-0": "D",
 "03A": "A", "03-0": "A", "04-0": "A", "06-0": "A", "06A": "A", "01-6": "A",
 "01-2": "B", "01A": "B", "02B": "B", "05A": "B", "01-4": "B", "01-7": "A",
 "01-1": "C", "01-3": "C", "02-1": "C", "03S": "C", "05-1": "C", "05-6": "C", "06S": "C",
 "03M": "E", "06M": "E", "06-1": "E",
 "02A": "A", "05-2": "B", "05-3": "B", "06-2": "A",   # 2026-11-06 補：沒寫會默默套 A
 "03C": "F", "06C": "F",
}
SETUP_DESC = {
 "A": "SETUP A: the camera stands behind her chair, looking at the desk and the window",
 "B": "SETUP B (reverse angle): the camera is on the desk side looking into the room; behind her are the bed (frame right), the wardrobe and the door",
 "C": "SETUP C: close on the right half of the desk: the tea glass on its coaster, the phone in front of it, the tablet on its stand",
 "D": "SETUP D: wide shot of the whole room from the corner near the door",
 "E": "SETUP E: close on the laptop from her seat",
 "F": "SETUP F: close on the tablet on its stand, the tea glass to its left",
}

# 工作室機位與座位表（yazelin 2026-11-06：工作室的機位也要用）。空景 canon/refs/set_studio_<機位>.jpg；窗在北。
SETUP.update({
 "04-1": "A", "04-PM": "A", "04C-1": "A", "04M-2": "A", "04-afterS": "A",
 "04B": "B", "04M-1": "B", "04M-3": "B", "04S-2": "B", "04S-4a": "B", "04S-4b": "B", "04S-5": "B",
 "04A": "C", "04-PS": "C", "04-PC": "C", "04C-2": "C", "04-afterC": "C", "04-afterM": "C", "04S-1": "C",
 "04C-4": "D",
})
SETUP_DESC.update({
 "sA": "STUDIO SETUP A: the camera is on the south side (the door side) looking north toward the tall grid windows; M and C face the camera from the window side of the table",
 "sB": "STUDIO SETUP B (reverse): the camera is on the window side looking south toward the wooden door; the heroine and S face the camera from the door side of the table",
 "sC": "STUDIO SETUP C: the camera stands just behind the heroine's red chair at the south-west corner of the table, looking diagonally across the table toward the windows (left) and the music corner (right); S's green chair is beside hers, M and C sit across the table",
 "sD": "STUDIO SETUP D: straight top-down view of the table",
})
SEATING = ("SEATING (fixed, never swap): the long table runs east-west; the windows are on the north. On the WINDOW (north) side: M on the white chair at the west end with his laptop, "
           "C on the wooden chair at the east end with his sketchbook. On the DOOR (south) side: the heroine on the red chair at the west end (across from M), "
           "S on the green chair at the east end beside her (across from C). Her iced tea stands in front of her.")

# 工作室的冰紅茶照會議進度變少（現實時間還在走；yazelin 2026-11-06 選）
_T1 = "Her iced tea in front of her: about 85% full, several clear ice cubes."
_T2 = "Her iced tea in front of her: about 70% full, the ice half melted into small rounded pieces."
_T3 = "Her iced tea in front of her: about half full (she has drunk some), only one or two small slivers of ice left."
TEA_STUDIO = {"_": _T2, "04-1": _T1, "04A": _T1, "04B": _T1,
              "04S-4b": _T2 + " She is drinking from it now.", "04S-5": _T3, "04-afterS": _T3}

# ── 分鏡表（新流程第三層，2026-11-06）──────────────────────────────
# 露出來的手：每一隻看得到的手放哪、拿什麼；看不到的手也寫「畫面外」。差分沿用主鏡頭，只寫有變的。
# 試玩抓到的錯（review/第一章_試玩問題.md）都是「手沒寫死」或「道具沒寫死」：少手指、少一隻手臂、手機出現在工作室。
# 量產驗收（2026-11-07）抓到的錯，重畫時附在該格描述後面。
FIX = {
    "03-0": "INSIDE THE SCREENS: M and C sit upright with both hands below the screen edge, out of frame; their faces are free, nothing touches their chins or cheeks.",
    "03C": "In the background laptop M sits upright, both hands below the screen edge and out of frame; nothing touches his chin or cheek.",
    "04-0": "FRAMING IS AN EXTREME CLOSE-UP: only her face in profile, her lowered eyelashes, the phone in its stand and the edge of the tea glass fill the frame; the laptop and the tablet are out of frame, so no man is visible except the small S on the phone screen.",
    "04-1": "LEFT-RIGHT (very important): she stands at the door (south) looking north toward the windows. Across the table on the WINDOW side: M on the WHITE chair at the LEFT with his laptop, C on the WOODEN chair at the RIGHT with his sketchbook. On the near (door) side: her own red chair at the LEFT is empty, S sits on the GREEN chair at the RIGHT and turns around toward her. Only M has a laptop.",
    "04S-1": "FRAMING: a CLOSE-UP of S alone in profile from the chest up, filling the frame; she is only a soft out-of-focus shape behind him; M and C are out of frame.",
    "04S-2": "LEFT-RIGHT (very important): the camera is on the WINDOW side looking south toward the door. On the far (door) side of the table: S on the GREEN chair at the frame's LEFT, she on the RED chair at the frame's RIGHT. In the near foreground, seen from behind: C on the wooden chair at the LEFT, M on the white chair at the RIGHT with his laptop.",
    "04S-4b": "She sits on HER RED chair. She drinks straight from the rim of the tall glass (no straw); the thin white tea-bag string hangs over the rim with its small cream tag.",
    "05-2": "MIRRORED because this is a reverse angle from behind the desk: the desk lamp glows at the frame's RIGHT edge, the back of the tablet is at the frame's LEFT edge, the back of the laptop lid at the RIGHT; the phone and its stand are out of frame, only their wine-red light reaches her.",
    "06C": "She sleeps with her cheek on her folded arms on the OPEN TEXTBOOK lying on the desk, the same textbook as in the other shots of this scene.",
    "06-1": "The phone stands in its small wooden phone stand to the RIGHT of the tea glass (left to right: laptop, tea glass, phone stand).",
}

RETIRED = {"01-2b", "01-2c"}
NOFACE = {"04C-1", "04C-4", "06-2", "02-1", "02A", "06-F"}   # 畫面裡只有手或頭髮，不需要視線表   # 改成敲鎖小遊戲（art/ui/minigame_challenge.html），不再產圖
HANDS = {
 "01-0": "她兩手一起捧著亮著的手機，手很小、在檯燈光裡，不必畫清每根手指。",
 "01-1": "沒有人，沒有手。",
 "01-2": "只露她兩手的指尖扶在手機兩側邊緣（前景、失焦），其餘的手在畫面外。",
 "01A": "她的兩手都在畫面下緣之外，看不到。",
 "02A": "只露她右手：食指伸出、懸在計算機上方，其他四指自然收起，手腕從畫面下緣進來。",
 "02B": "她的兩手都在畫面外，只看得到手機上緣貼在胸口。",
 "02-1": "只露她右手食指的指尖按在發光的確認鈕上，指甲與指節自然。",
 "01-3": "沒有人，沒有手。",
 "03-T": "三人都只到胸口，手都在畫面外。",
 "03-0": "她兩手在胸前一起捧著手機（兩隻手都看得到、各五根手指），三道光從手機射出。",
 "01-4": "她的兩手都在畫面外（桌緣以下）。",
 "03S": "她不在畫面裡；詩只到胸口，手在畫面外。",
 "03A": "她的手在畫面外；三位先生都只到胸口，手在畫面外。",
 "03C": "她不在畫面裡；晨右手在胸前拿著一支鉛筆（五根手指清楚，鉛筆夾在拇指與食指之間），左手在畫面外。",
 "03M": "她不在畫面裡；明只到胸口，手在畫面外。",
 "03-F": "兩年前的她：右手拿鉛筆在紙上畫，左手壓著紙的角落，兩隻手都看得到、各五根手指。",
 "04-0": "她右手輕輕放在桌緣（五根手指自然、看得到），左手在畫面外；手機不在她手上。",
 "04-1": "她站在門口，只露後腦與右肩，手在畫面外。明兩手放在筆電鍵盤上；晨右手拿鉛筆在素描本上、左手扶著本子；詩右手搭在椅背上、左手放在大腿上。",
 "04A": "她兩手交疊放在桌上（兩隻都看得到）。明兩手放在筆電鍵盤上；晨右手拿鉛筆、左手扶素描本；詩右手搭在椅背上、左手放在大腿上。",
 "04B": "她兩手交疊放在桌上、手指輕輕交握；詩在旁邊失焦，手看不清楚也可以。",
 "04-PC": "她的手不在畫面裡（主觀鏡頭）。晨右手拿鉛筆停在素描本上、左手扶著本子；明兩手在筆電上；詩的手在畫面外。",
 "04-PM": "她的手不在畫面裡（主觀鏡頭）。明兩手交疊放在筆電前的桌上；晨與詩的手在畫面外。",
 "04-PS": "她的手不在畫面裡（主觀鏡頭）。詩右手把一邊耳罩從耳朵拉下來（五根手指清楚），左手在畫面外。",
 "04C-1": "只露晨的右手與袖口（袖口有黃綠細線），右手拿鉛筆在素描本上畫。",
 "04C-2": "她的手在畫面外。晨右手拿鉛筆放在素描本上，左手在畫面外。",
 "04C-4": "只露她右手食指的指尖，懸在兩張草圖中間，沒有碰到紙。",
 "04-afterC": "明兩手放在筆電鍵盤上；詩兩手把耳機戴回頭上（兩手扶著耳罩，各五根手指）。她不在畫面裡。",
 "04M-1": "越過明的右肩：明右手放在觸控板上，左手在畫面外；她在桌子對面，兩手交疊放在桌上（遠、小）。",
 "04M-2": "明右手放在筆電鍵盤上，左手在畫面外。",
 "04M-3": "她的兩手都在桌面以下、畫面外。",
 "04-afterM": "晨右手拿鉛筆畫、左手扶著本子；詩兩手放在桌上。她不在畫面裡。",
 "04S-1": "詩右手兩根手指在桌緣打拍子，左手在畫面外；她在後面失焦，兩手平放在桌上。",
 "04S-2": "詩只露右手，在空中畫一條慢慢的線（五根手指清楚），左手在畫面外。她兩手交疊放在膝上，兩隻手都看得到。",
 "04S-4a": "詩的兩手都在畫面外（只到胸口）。",
 "04S-4b": "她右手握著高玻璃杯（五根手指自然圈住杯身），左手在畫面外。",
 "04S-5": "她的手在畫面外（只有臉）。",
 "04-afterS": "晨右手拿鉛筆停在紙上、左手扶著本子；明兩手放在筆電鍵盤上。她不在畫面裡。",
 "05-0": "她兩手放在腿上、桌緣以下。",
 "05A": "她的兩手都在桌緣以下、畫面外。",
 "05-1": "詩只到胸口，手在畫面外。",
 "01-6": "她的手在畫面外；三位先生都只到胸口，手在畫面外。",
 "05-6": "主觀鏡頭，沒有手；詩只到胸口。",
 "06-0": "她右手壓在攤開的課本上，左手垂在腿上（畫面外）。",
 "01-7": "她兩手臂交疊在課本上當枕頭，臉頰枕在上面（兩隻手臂都看得到，手掌半藏在手臂下）。",
 "06A": "她只露頭髮，手在畫面外；三位先生只到胸口，手在畫面外。",
 "06C": "晨右手拿著鉛筆、靜止不動（五根手指清楚），左手在畫面外。",
 "06-1": "沒有人，沒有手。",
 "06M": "明只到胸口，手在畫面外。",
 "06-F": "照 02A：只露她右手食指懸在計算機上方。",
 "06S": "詩右手拿著剛摘下的耳機（五根手指清楚），左手在畫面外。",
 "06-2": "沒有人，沒有手。",
 "05-2": "她的兩手都在畫面外（只到肩膀）。",
 "05-3": "沒有手。",
 "05-4": "想像畫面：跪著的小人影太小，看不出手；沒有其他人。",
}
# 差分格只寫手有變的（沒寫就沿用主鏡頭）
HANDS.update({
 "04S-3": "她兩手交疊放在膝上，兩隻手都看得到；詩只露右手，在胸前輕輕攤開（五根手指清楚），左手在畫面外。",
 "04A-4": "她往後靠在椅背上，兩手放在腿上；三位先生的手照 04A。",
 "04A-5": "她閉眼嘆氣，兩手交疊放在桌上；三位先生的手照 04A。",
})

# 手機在哪：人形介面出現（03S）之前，手機在她手上或平放在桌上；之後詩住在手機裡，手機立著靠在紅茶杯右邊
PHONE = {
 "01-0": "手機在她手上亮著；筆電與平板的螢幕關著", "01-1": "手機平放在紅茶後面、剛亮起通知；筆電與平板的螢幕關著、全黑", "01-2": "手機在她手上；筆電與平板的螢幕關著、全黑",
 "01A": "手機在她手上；筆電與平板的螢幕關著、全黑", "02A": "手機平放在桌上；筆電與平板的螢幕關著、全黑", "02B": "手機貼在她胸口；筆電與平板的螢幕關著、全黑", "02-1": "手機在桌上、她的指尖按著螢幕；筆電與平板的螢幕關著、全黑",
 "01-3": "手機平放在桌上", "03-0": "手機在她手上、射出三道光", "06-F": "（回憶）手機平放在桌上",
 "06-4": "手機暗著平放在她手邊；三台裝置的螢幕都暗了"
}
def props(i):
    """道具狀態：依場景與時間自動帶，不逐格手抄。沒入鏡的道具不用畫。"""
    d = S[i]; k = d["kind"] if d["kind"] != "var" else S[d["base"]]["kind"]; t = d["time"]
    if k == "studio":
        tea = TEA_STUDIO.get(i, TEA_STUDIO["_"])
        return "工作室：桌上沒有任何手機；明用他自己的太空灰素面筆電；她的三台裝置都不在工作室。" + tea
    if k in ("desk", "room", "insert"):
        tea = {"t1": "冰紅茶冰塊半融、剩幾小塊", "t3": "冰紅茶沒有冰塊、杯壁水珠往下流", "t4": "冰紅茶快喝完、杯墊上一圈水痕"}.get(t, "")
        ph = PHONE.get(i) or PHONE.get(d["base"] or "", "手機直立在淺木色小手機架上，放在紅茶杯右邊、螢幕朝她")
        lean = "冰紅茶和手機架都在筆電與平板中間的桌面上；手機架照道具圖：淺木色低座加一片短靠背，沒有任何金屬板或夾子；手機不碰杯子；" if "手機架" in ph else ""
        return f"書桌（只有一張桌子、一個平的桌面，沒有第二層或架子）：由左到右檯燈、筆電、冰紅茶、平板；{ph}；{lean}全畫面只有一支手機；沒入鏡的道具不用畫。{tea}。"
    return ""
