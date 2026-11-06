# 從 art/cg/ch1_shots.py 組提示詞並產圖（.11 codex-image；送圖排隊在 tools/gen.py，走全機共用的 ~/.cache/cg_jobs）。
#   python3 tools/shots.py prompts            # 只寫 art/cg/ch1/<id>.prompt.txt
#   python3 tools/shots.py run masters [id…]  # 產非差分格（主鏡頭、單格）
#   python3 tools/shots.py run vars [id…]     # 產差分（主鏡頭的定稿要先在 art/cg/<base>.jpg）
# 產出在 art/gen/ch1/<id>.png；驗收過的才轉成 art/cg/<id>.jpg。
import json, os, subprocess, sys, pathlib, concurrent.futures as cf
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "art/cg")); from ch1_shots import S, GAZE, SETUP, SETUP_DESC, SEATING, TEA_STUDIO, HANDS, props
OUT, PR = ROOT / "art/gen/ch1", ROOT / "art/cg/ch1"
REF = "canon/refs/"
SHEET = {"t": REF + "tea.jpg", "c": REF + "c.jpg", "m": REF + "m.jpg", "s": REF + "s.jpg"}
NAME = {"t": "heroine (茶語) sheet", "c": "C sheet", "m": "M sheet", "s": "S sheet"}

TEA = "茶語 (the heroine, about 20): petite, narrow shoulders, about 158 cm; dark purple wolf-cut hair, shoulder length at the back with flicked ends; thin gold round glasses with pale pink-tinted lenses, always visible; EYES: soft light brown with a hint of reddish-brown (the lightest, warmest eyes of the four); gold crescent-moon pendant that hangs at the FRONT of her chest (seen from behind, only the thin gold chain shows at the nape of her neck, never a pendant on her back); dangling gold ear chains on both ears; oversized off-white short-sleeve T-shirt, wide charcoal cargo work pants with pockets and drawstrings, white sneakers; on BOTH wrists two strands of beaded bracelets each (deep purple beads and pearl-white beads), left and right alike. NOT: black short hair, male shoulders, skirt, heavy makeup."
CAST = """THE THREE MEN (draw exactly as their sheets; neutral clothes, each has only ONE small signature colour):
- M (about 26, the tallest): near-black short tousled hair swept back with a faint cool blue sheen; calm narrow GREY-BROWN eyes (cool, almost grey); charcoal suit jacket open with sleeves rolled up, crisp white shirt with open collar, no tie; gold gear brooch with a short chain on the left lapel; a small DEEP BLUE pocket square (his only blue); brown leather-strap watch on his LEFT wrist only (never on the right).
- C (about 24): warm chestnut-brown fluffy curly hair; thin gold round glasses; gentle droopy WARM-BROWN eyes (a little darker than hers); warm CAMEL-brown open knit cardigan with tiny paint speckles; a small gold leaf brooch enamelled YELLOW-GREEN on the left chest and one thin yellow-green stripe at each cuff (his only yellow-green); white shirt.
- S (about 21, the youngest): deep WINE-RED long messy hair with one thin braid at the front left tied with a wine-red cord; bright AMBER-GOLD eyes (the brightest of the four), a small fang when he grins; silver ear cuffs; WINE-RED over-ear headphones (his only wine red besides his hair); black track jacket with thin white sleeve stripes and ONE small gold treble-clef emblem on the left chest, open over a heather-grey T-shirt.
EYE COLOURS are fixed and never swapped: heroine light reddish-brown, M grey-brown, C warm brown, S amber-gold. Never swap accessories: the gear is only M's, the leaf only C's, the treble clef only S's."""
AI = """THEY ARE AIs (very important): in this real-world scene the three men exist ONLY inside the screens, as humanoid interfaces. Behind each man there is NO room, NO bookshelf, NO window, NO furniture: only a soft abstract glowing space in his own colour with faint drifting motes of light (deep blue for M, pale yellow-green for C, dark wine red for S), and a very faint thin luminous outline along the inner edge of each screen. It must NOT look like a video call with a person at home. GAZE: unless the shot says otherwise, every man visible on a screen looks at HER (wherever she is, in or out of frame) or at whoever is speaking; nobody gazes up and away into the distance. Inside the screens the men do NOT pose: nobody rests his chin or cheek on his hand, nobody smiles at the camera.
RESIDENCE (exclusive): the laptop shows ONLY M, the tablet ONLY C, the phone ONLY S. A lit screen is never blank.
FRAMING INSIDE THE SCREENS (very important): every man inside a screen is shown only from the chest up (at most from the waist up), filling his screen like a video portrait; NEVER a full-body figure, never standing small inside the screen, never legs or feet."""
PROPS = """PROPS: the iced tea is a TALL straight-sided clear drinking glass (no handle, never a mug, never coffee) of amber black tea, the thin white string of a tea bag over the rim on the right with a small cream paper tag, standing on a round light-brown cork coaster. Her phone (when it is on the desk it stands upright in a small light-wood phone stand, never leaning on the glass): industrial design of a recent iPhone in soft pale LAVENDER (flat lavender aluminium frame, rounded corners, flat front glass with a small pill-shaped cut-out at the top; on the back a square camera module at the TOP LEFT with two diagonal lenses), real proportions about 7 x 15 cm. Her laptop: a recent 13-inch MacBook Air design in pale STARLIGHT (very thin, thin black bezel with a small notch). Her tablet: a recent 11-inch iPad Air design in pale starlight, held in landscape on a dark charcoal folio stand. NO logos on any device. Match Images of the props exactly."""
TIME = {
    "t1": "TIME: 11:40 p.m. The warm desk lamp is the only lamp; the room is deep blue shadow; the city outside still has many lit windows. The iced tea is half melted: a few small ice cubes left, condensation on the glass.",
    "t3": "TIME: 3 a.m. The desk lamp is the only light; deep blue shadow; only a few windows still lit outside. The tea glass contains NO ice at all (melted hours ago), condensation running down the glass.",
    "t4": "TIME: past 4 a.m. The desk lamp is the only light; deep blue night; outside almost every window is dark. The tea glass is nearly empty, no ice, a ring of water on the coaster.",
    "day": "TIME: daytime in the studio (the heroine's inner workspace): bright soft white daylight from tall grid windows, plants, warm wood, floating dust in the light shafts. All four are physically together in this room (this is the only place where they can be).",
}
STYLE = """STYLE: the rendering of the first reference image (TRANSPARENT WATERCOLOUR anime illustration: clearly visible cold-press paper grain everywhere, soft pigment blooms and granulation, wet-in-wet edges, gentle colour bleeding, delicate thin line art, slightly muted watercolour palette; NOT clean digital cel shading, NOT glossy, NOT airbrushed), finished to the level of a cinematic FILM STILL for an ADULT audience: realistic adult proportions, restrained acting, rich light with clear contrast, carefully rendered materials (wood grain, glass, condensation, knit, wool, brushed metal), a detailed believable background where it is in focus, a clear focal point, deliberate colour grade. Watercolour is the medium, never an excuse for vagueness. No chibi, no manga symbols, no sweat drops, no exaggerated cartoon faces.
OBJECTS: there are NO mugs, coffee cups or teacups anywhere; the only drink in any scene is her tall iced tea glass. There is exactly ONE phone (hers) in the scene, never a second phone.
BODY LANGUAGE: nobody rests a chin or cheek on a hand and nobody props the head on a hand or arm (unless asleep); hands do only what the shot describes, otherwise they rest naturally or stay out of frame. SOLIDITY: every person is a complete, solid body in believable space: sitting ON a chair or standing on the floor, never sunk into, merged with or cut by a table, chair or wall. FRAMING: only the people this shot names are in frame; if it says "the other two", the heroine is NOT in the picture.
HANDS: any visible hand has five clearly separated fingers with natural joints and nails; hands not described are out of frame or hidden.
No text, letters, numbers or logos anywhere. Nobody looks into the lens unless the shot says POINT OF VIEW."""

def present(i):
    """這一格真的入鏡的人（視線表的人＋描述裡寫到的人）。不在畫面裡的人不送設定圖，免得稀釋空景。"""
    g = GAZE.get(i, {}); d = S[i]; who = []
    h = HANDS.get(i, "")
    if "she" in g and "out of frame" not in g.get("she", "") and "not in frame" not in g.get("she", "") or ("她" in h and "她不在畫面" not in h and "她的手不在畫面裡（主觀" not in h): who.append("t")
    for k, w in (("C", "c"), ("M", "m"), ("S", "s")):
        if k in g or w in (d["who"] or ""): who.append(w)
    return who

def refs_for(i):
    d = S[i]; k = d["kind"]
    if k == "var":
        base = ROOT / f"art/cg/{d['base']}.jpg"
        who = d["who"] or ("tcms" if S[d["base"]]["kind"] in ("desk",) else "t" + (S[d["base"]]["who"] or "cms"))
        files = [str(base)] + [SHEET[w] for w in dict.fromkeys(who) if w in SHEET]
        names = ["the MASTER FRAME of this shot (reproduce it)"] + [NAME[w] for w in dict.fromkeys(who) if w in SHEET]
        return files, names
    if k in ("desk", "insert", "room", "studio"):
        # 2026-11-06 yazelin：背景東西位置都錯。原因是第一張送了畫風參考（封面，本身是一張有書桌和裝置的完整場景），模型照它擺背景。
        # 空景本身已是透明水彩，兼當畫風參考、排第一張；只送真的入鏡的人。
        if k == "studio": setref, setname = REF + f"set_studio_{SETUP.get(i, 'A')}.jpg", "EMPTY STUDIO SET from this shot's camera setup (direction, furniture, seats and the watercolour rendering to match; the shot may frame tighter)"
        else: setref, setname = REF + f"set_desk_{SETUP.get(i, 'A')}.jpg", "EMPTY SET from this shot's exact camera setup and the RENDERING to match (transparent watercolour): keep its camera direction and every piece of furniture and object exactly where it is; its screens are off only because the set is empty"
        files, names = [setref], [setname]
        files += [REF + "prop_tea.jpg"]; names += ["PROP: her iced black tea"]
        if k != "studio":
            files += [REF + "prop_phone_stand.jpg", REF + "prop_laptop_tablet.jpg"]; names += ["PROP: her smartphone, and the small light-wood phone stand it stands in on the desk", "PROP: her laptop (left) and tablet on its folio stand (right)"]
        for w in present(i):
            files.append(SHEET[w]); names.append(NAME[w])
        return files, names
    who = d["who"] or "t"
    files = [REF + "style_anchor.jpg"] + [SHEET[w] for w in who]
    names = ["STYLE ANCHOR (rendering only; never copy its composition or its room)"] + [NAME[w] for w in who]
    return files, names

NAMES = {"she": "the heroine", "M": "M", "C": "C", "S": "S"}
def gaze(i):
    # ponytail: 只管主鏡頭與單格；差分照主鏡頭的視線，差分自己的描述會覆寫
    return "GAZE, who looks at whom (draw exactly, eyes OPEN unless stated; HER = toward the heroine wherever she is; nobody gazes up and away into the distance): " + "; ".join(f"{NAMES[k]} looks at {v}" for k, v in GAZE[i].items()) + "."

def board(i):
    # 分鏡表兩欄（中文）：露出來的手、道具狀態。差分沒寫手就沿用主鏡頭
    h = HANDS.get(i) or HANDS.get(S[i]["base"] or "", "")
    out = []
    if h: out.append("HANDS (storyboard, must be followed exactly; every visible hand has exactly five fingers and is attached to an arm; hands written as out of frame must not appear): " + h)
    p = props(i)
    if p: out.append("PROPS STATE (storyboard, must be followed exactly): " + p)
    return out

def prompt(i):
    d = S[i]; files, names = refs_for(i)
    ref = "REFERENCE IMAGES: " + " ".join(f"Image {n+1} = {x}." for n, x in enumerate(names))
    if d["kind"] == "var":
        return "\n".join([ref,
            "Reproduce Image 1 EXACTLY: same camera position, framing, lens, lighting, colour grade, room, background, devices and what each screen shows, props, clothing, hair, glasses and accessories, same watercolour rendering and level of detail.",
            "Change ONLY what is described here, nothing else in the picture: " + d["body"],
            *board(i),
            "Keep every face identical to Image 1 and to the character sheets. Restrained adult acting; no manga symbols. Hands not mentioned stay as in Image 1 or out of frame. No text."])
    parts = [ref, TEA]
    if d["kind"] in ("desk", "studio", "free") and (d["kind"] != "free" or d["who"] not in ("", "t")): parts.append(CAST)
    if d["kind"] in ("desk", "insert", "room"): parts.append(PROPS)
    if d["kind"] == "room": parts.append("SCREENS OFF (very important): the humanoid interface does not exist yet. The laptop and tablet screens are switched OFF — solid black glass with only a faint reflection of the lamp — and NOBODY appears on any device. The three men are NOT in this picture at all.")
    if d["kind"] == "studio":
        parts.append("NO PHONE anywhere in the studio (this is her imagined workspace; S is physically present). M works on HIS OWN laptop: a thin dark SPACE-GREY laptop with a completely plain lid (no sticker, no logo, no marks of any kind), clearly NOT her pale starlight laptop; her devices never appear in the studio. " + TEA_STUDIO.get(i, TEA_STUDIO["_"]))
        parts.append(SETUP_DESC["s" + SETUP.get(i, "A")] + ". The EMPTY STUDIO SET image is this setup: keep its camera DIRECTION and every piece of furniture where it is (one long table, four chairs); the FRAMING is this shot's own, move closer along the same direction as the shot describes. " + SEATING)
    if d["kind"] in ("desk", "insert", "room"):
        parts.append((SETUP_DESC[SETUP[i]] if i in SETUP else SETUP_DESC["A"]) + ". The EMPTY SET image is the room seen from this camera setup. Keep its camera DIRECTION and the room exactly as laid out there: the same ONE desk, every object in the same place (left to right on the desk: lamp and books, laptop, tea glass on its coaster, tablet on its stand; the phone in front of the tea glass or standing in its small wooden stand). Never add a second desk, never move or duplicate an object. The FRAMING is this shot's own (close-up, extreme close-up, low angle, over-the-shoulder): move the camera closer or lower along the same direction as the shot describes; do not widen it back to the empty set's framing.")
    parts.append(d["body"])
    if d["kind"] == "desk": parts.append(AI)
    if d["kind"] != "free": parts.append(TIME[d["time"]])
    if i in GAZE: parts.append(gaze(i))
    parts += board(i)
    parts.append(STYLE)
    return "\n".join(parts)

def job(i):
    out = OUT / f"{i}.png"
    files, _ = refs_for(i)
    r = subprocess.run(["python3", str(ROOT / "tools/gen.py"), str(out), str(PR / f"{i}.prompt.txt")] + [str(ROOT / f) if not f.startswith("/") else f for f in files],
                       capture_output=True, text=True, cwd=ROOT)
    return i, (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True); PR.mkdir(parents=True, exist_ok=True)
    for i in S: (PR / f"{i}.prompt.txt").write_text(prompt(i), encoding="utf-8")
    if sys.argv[1:2] == ["prompts"]: print(len(S), "份提示詞"); sys.exit()
    which = sys.argv[2]; ids = sys.argv[3:] or [i for i in S if (S[i]["kind"] == "var") == (which == "vars")]
    ids = [i for i in ids if not (OUT / f"{i}.png").exists()]
    if which == "vars":
        miss = [i for i in ids if not (ROOT / f"art/cg/{S[i]['base']}.jpg").exists()]
        if miss: print("主鏡頭還沒定稿，先略過：", miss); ids = [i for i in ids if i not in miss]
    print("要產", len(ids), "張", flush=True)
    with cf.ThreadPoolExecutor(3) as ex:
        for i, msg in ex.map(job, ids): print(i, msg[0] if msg else "", flush=True)
