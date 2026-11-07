# 間章〈筆電裡的事〉分鏡規格（劇本/間章.md 的產圖版）。CH=8 python3 tools/shots.py … 讀這份。
# id 一律「8-」開頭，定稿放 art/cg/ch8/<id>.jpg。四格漫畫加收尾一格，kind＝comic（tools/shots.py 專給這種格的提示詞）：
# 參考圖全由 SETREF 給（畫風錨＋筆電道具＋該格的人：一般設定圖或 Q 版單人圖），畫風照 COMIC_STYLE（這一章允許 Q 版）。
# 8-P 是 2×2 合頁（tools/comic_page.py 用 8-01～8-04 排版拼成，不重畫），只進 CG 收藏。
from ch1_shots import SETUP_DESC, SEATING, H, _T1
S = {}
def shot(i, kind, time, body, base=None, who=""):
    S[i] = dict(kind=kind, time=time, body=body.strip(), base=base, who=who)

R = "canon/refs/"
_ANCHOR = (R + "style_anchor.jpg", "STYLE ANCHOR: the watercolour rendering and the look of her desk at night (rendering only; never copy its composition)")
_LT = (R + "prop_laptop_tablet.jpg", "PROP: her laptop (left) and tablet on its folio stand (right)")
_PH = (R + "prop_phone_stand.jpg", "PROP: her smartphone standing in its small light-wood phone stand")
_CM = (R + "chibi_m.jpg", "CHIBI M: the two-head-tall chibi version of M (draw chibi M exactly like this)")
_CC = (R + "chibi_c.jpg", "CHIBI C: the two-head-tall chibi version of C (draw chibi C exactly like this)")
_CS = (R + "chibi_s.jpg", "CHIBI S: the two-head-tall chibi version of S (draw chibi S exactly like this)")
_P1 = ("art/cg/ch8/8-01.jpg", "PANEL 1 of this same strip: keep the same laptop, desk, lamp, tea glass, framing, comic panel border and rendering (a new moment; redraw, do not copy the characters' poses)")
SETREF = {
    "8-01": [_ANCHOR, _LT],
    "8-02": [_P1, _ANCHOR, _LT],
    "8-03": [_P1, _ANCHOR, _LT, _CM, _CC, _CS],
    "8-04": [_P1, _ANCHOR, _LT, _CM, _CC, _CS],
    "8-05": [_P1, _ANCHOR, _LT, _PH, _CM],
}

COMIC_STYLE = """STYLE: ONE PANEL of a gentle four-panel comic strip (yonkoma) about the same characters, drawn in the same TRANSPARENT WATERCOLOUR as the style anchor (cold-press paper grain, soft pigment blooms, wet-in-wet edges, delicate thin line art, slightly muted palette). The whole picture is ONE landscape panel framed by a thin hand-inked dark brown comic panel border with slightly rounded corners and a narrow cream paper margin outside the border. Light, funny, warm. Inside the laptop screen there is M's deep blue interface space with faint drifting motes of light (pale yellow-green where C is, dark wine red where S is). Small comic sound-effect marks drawn as simple shapes are allowed (puff clouds, motion lines, a little sparkle), but NO letters, NO numbers, NO speech balloons with text, NO logos anywhere. The heroine is never drawn on any screen. Nobody rests a chin or cheek on a hand."""

CAST3 = "M (near-black short swept-back hair with a cool blue sheen, NO glasses, charcoal suit jacket over a white open-collar shirt, gold gear brooch), C (warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch), S (long messy WINE-RED hair with one thin braid, wine-red over-ear headphones, black track jacket with white stripes and a gold treble clef)"

# ── 第一格：擠進明的筆電 ──
shot("8-01", "comic", "", f"""PANEL 1. Close shot of her open pale starlight laptop on her desk at night (the warm desk lamp at the left edge, the tall iced tea glass beside it); the laptop SCREEN fills most of the panel. Inside the screen, in M's deep blue interface space, all THREE men in their normal look (not chibi) are squeezed together into this one screen, chest up, shoulders pressed together: M in the middle, arms folded, unamused, glancing sideways at the other two; C squeezed in at the LEFT edge of the screen, leaning in, gently insistent; S squeezed in at the RIGHT edge, leaning forward with his finger raised as if making a point, grinning. The three are exactly {CAST3}. Nobody else in the picture; the heroine is not in the room (she has gone to pour tea).""", who="cms")

# ── 第二格：越吵越兇，電量掉到紅色 ──
shot("8-02", "comic", "", f"""PANEL 2. Same laptop, same framing as panel 1, a little closer. Inside the screen the three men (normal look, chest up) are now arguing all at once, crowded and jostling: S jabs a thumb at his own chest, mouth open mid-shout; C holds up a pencil like evidence, flustered; M has unfolded his arms and is raising one flat hand to stop them, lips pressed, annoyed. Small comic motion lines and a few puffs of steam between them. In the TOP-RIGHT corner of the laptop screen a small battery icon (a plain rounded rectangle) has drained to one short bar glowing RED. The three are exactly {CAST3}.""", who="cms")

# ── 第三格：「噗」，三人一起變 Q 版 ──
shot("8-03", "comic", "", """PANEL 3. Same laptop screen, same framing. With a soft comic "poof" (a round watercolour puff of smoke drawn as a shape, no letters), all three men have suddenly shrunk into tiny two-head-tall CHIBI versions of themselves, drawn exactly like the CHIBI M, CHIBI C and CHIBI S reference images, still tangled in a little scuffle cloud in the middle of the screen; out of the cloud fly their small accessories: a pair of thin gold round glasses (C's), a pair of tiny wine-red headphones (S's), and a little gold gear brooch (M's), with small motion lines. The battery icon in the top-right corner is red and nearly empty. Funny and cute.""")

# ── 第四格：她回來，三個小人站好裝沒事 ──
shot("8-04", "comic", "", """PANEL 4. Same laptop screen, from a slightly lower angle. At the bottom-left corner of the panel only her hand is visible (from the front edge of the frame), holding a freshly filled tall iced tea glass with ice cubes; she is NOT drawn otherwise. Inside the screen the three tiny CHIBI men (exactly like the CHIBI references) stand stiffly in a neat row, trying to look innocent: chibi M in the middle stands straight with a perfectly flat calm face but his eyes slide off to one side; chibi C at the LEFT smiles an awkward little smile, his round glasses sitting crooked on his nose; chibi S at the RIGHT has his wine-red headphones slipped all the way down around his neck, his head turned away, lips pursed as if whistling (a tiny drawn musical note, no letters). One small comic sweat-free sparkle of guilt above them is fine; no sweat drops.""")

# ── 收尾：晨和詩回去變回原樣，只剩明是 Q 版 ──
shot("8-05", "comic", "", f"""PANEL 5 (the punchline, a wider panel). Her desk at night, the three devices side by side: LEFT her open laptop, MIDDLE the tall iced tea glass and to its RIGHT her phone standing in its small wooden phone stand, RIGHT her tablet on its folio stand. On the TABLET, C is back to his normal look (chest up, pale yellow-green interface space), hiding a laugh behind a gentle smile. On the PHONE, S is back to his normal look (chest up, dark wine-red interface space), openly snickering, eyes squeezed, fang showing. On the LAPTOP only M is still a tiny two-head-tall CHIBI (exactly like the CHIBI M reference), alone in the deep blue screen, arms folded, cheeks puffed, sulking, the red low-battery icon in the screen's top-right corner. At the front edge of the panel only her hand is visible plugging a thin white charging cable into the side of the laptop. C and S are exactly as their sheets: C (warm chestnut-brown fluffy curly hair, thin gold round glasses, camel knit cardigan, small yellow-green leaf brooch), S (long messy WINE-RED hair with one thin braid, wine-red over-ear headphones, black track jacket with white stripes).""", who="cs")

GAZE = {
 "8-01": {"M": "sideways at the other two", "C": "at M", "S": "at M"},
 "8-02": {"M": "at the other two", "C": "at S", "S": "at C"},
 "8-05": {"C": "toward the laptop (at chibi M)", "S": "toward the laptop (at chibi M)"},
}
NOFACE = {"8-03", "8-04"}
CHIN_OK = {}
SETUP = {}
TEA_STUDIO = {"_": _T1}
FIX = {
    "8-04": "Her arm is BARE from the elbow down (she wears an oversized off-white SHORT-sleeve T-shirt; no knit sleeve, no cuff), with her two beaded bracelets (deep purple and pearl-white) on the wrist. Chibi C's round glasses are clearly TILTED, one lens higher than the other, sliding down his nose (this is the joke). Chibi S's headphones hang around his neck.",
    "8-05": "Her arm is BARE from the elbow down (she wears an oversized off-white SHORT-sleeve T-shirt; no knit sleeve, no cuff), with her two beaded bracelets (deep purple and pearl-white) on the wrist.",
}
RETIRED = set()
HANDS = {
 "8-01": "她不在畫面裡；三人只到胸口，明雙手抱胸（看得到、各五根手指），詩舉起右手食指（五根手指清楚），晨的手在畫面外。",
 "8-02": "她不在畫面裡；詩右手拇指指著自己胸口，晨右手舉著一支鉛筆，明舉起一隻手掌平擋（每隻手五根手指）。",
 "8-03": "Q 版小人的手短短的、扭成一團，不用畫清楚手指；她不在畫面裡。",
 "8-04": "只露她的右手從畫面左下角拿著冰紅茶杯（五根手指握著杯子）；Q 版小人的手垂在身側。",
 "8-05": "只露她的右手在畫面前緣，把白色充電線插進筆電側邊（五根手指清楚）；Q 版明雙手抱胸；晨和詩只到胸口，手在畫面外。",
}
GALLERY_EXTRA = ["8-P"]   # 2×2 合頁：只進 CG 收藏，演完收尾那張卡時解鎖
def props(i):
    return {"8-05": "書桌：由左到右筆電、冰紅茶、手機直立在淺木色小手機架上（紅茶杯右邊）、平板；只有一支手機。"}.get(i, "她的筆電（淡星光色）放在書桌上，旁邊有檯燈與冰紅茶。")
