# 遊戲素材走孤兒 tag 給 jsDelivr（yazelin 2026-11-06）：repo 整包超過 jsDelivr 的 50 MB 上限，新版本的檔案一律回 403。
# 每一組素材各做一個沒有父節點的 commit（只含那組檔案）、打 tag 推上去；jsDelivr 只算那個 commit 的大小。
# tag 名稱帶樹的雜湊：內容沒變就沿用，換圖才會出新 tag。
#   python3 tools/assets.py          # 發佈全部組，印出各組 tag
import json, os, pathlib, subprocess, tempfile
ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "yazelin/larch-three-gentlemen"
LIMIT = 48 * 1024 * 1024   # jsDelivr 上限 50 MB，留一點餘裕
# 分組：每章一組。第一章的圖放在資料夾根層，第二章起放 ch2/、ch3/… 子資料夾，自動各成一組（cg-ch2、bgm-ch2…）。
# 每組各自一個孤兒 tag、各自要在 50 MB 以內；超過就再拆（例如 ch2a/、ch2b/）。
BASES = {"cg": "art/web/cg/", "bgm": "art/bgm/", "end": "art/web/end/", "ui": "art/web/ui/"}
WEB = [("art/cg_paper/", "art/web/cg/"), ("art/video/", "art/web/end/"), ("art/ui/challenge/", "art/web/ui/")]   # 原圖資料夾 → WebP 資料夾
QUALITY = 88

def web_path(path):
    """repo 裡的原圖路徑 → 上 CDN 的路徑（圖換成 WebP，音樂不變）。"""
    for src, dst in WEB:
        if path.startswith(src) and path.endswith((".jpg", ".png")):
            return dst + path[len(src):].rsplit(".", 1)[0] + ".webp"
    return path

def prepare():
    from PIL import Image
    n = 0
    for src, dst in WEB:
        for f in sorted((ROOT / src).rglob("*")):   # rglob：章節子資料夾一起轉
            if f.suffix not in (".jpg", ".png"): continue
            out = ROOT / web_path(str(f.relative_to(ROOT)))
            if out.exists() and out.stat().st_mtime >= f.stat().st_mtime: continue
            out.parent.mkdir(parents=True, exist_ok=True)
            Image.open(f).convert("RGB").save(out, "WEBP", quality=QUALITY, method=6); n += 1
    return n
STATE = ROOT / "assets_tags.json"

def group_of(path):
    for kind, base in BASES.items():
        if path.startswith(base):
            rest = path[len(base):]
            return f"{kind}-{rest.split('/')[0]}" if "/" in rest else f"{kind}-ch1"
    raise SystemExit(f"{path} 不屬於任何素材組，先加進 tools/assets.py 的 BASES")

def groups():
    gs = set()
    for base in BASES.values():
        for f in (ROOT / base).rglob("*"):
            if f.is_file() and f.suffix != ".mp4": gs.add(group_of(str(f.relative_to(ROOT))))
    return sorted(gs)

def files(g):
    out = []
    for base in BASES.values():
        for f in sorted((ROOT / base).rglob("*")):
            if not f.is_file() or f.suffix == ".mp4": continue   # mp4 走 Larch 媒體庫，不上 CDN
            r = str(f.relative_to(ROOT))
            if group_of(r) == g: out.append(r)
    return out

def git(*a, env=None, inp=None):
    return subprocess.run(["git", "-C", str(ROOT), *a], check=True, capture_output=True, text=True, env=env, input=inp).stdout.strip()

def publish(g):
    fs = files(g); size = sum((ROOT / f).stat().st_size for f in fs)
    if size > LIMIT: raise SystemExit(f"素材組 {g} 有 {size/1e6:.1f} MB，超過 jsDelivr 上限，拆成兩組")
    with tempfile.TemporaryDirectory() as d:
        env = {**os.environ, "GIT_INDEX_FILE": os.path.join(d, "index")}
        git("read-tree", "--empty", env=env)
        for i in range(0, len(fs), 200): git("add", "-f", "--", *fs[i:i + 200], env=env)
        tree = git("write-tree", env=env)
    tag = f"assets-{g}-{tree[:10]}"
    if not git("ls-remote", "--tags", "origin", tag):
        commit = git("commit-tree", tree, "-m", f"遊戲素材 {g}（{len(fs)} 個檔、{size/1e6:.1f} MB）")   # 沒有 -p：孤兒 commit
        git("tag", "-f", tag, commit); git("push", "-q", "origin", f"refs/tags/{tag}")
    return tag

def tags(refresh=False):
    prepare()
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    if refresh or set(st) != set(groups()):
        st = {g: publish(g) for g in groups()}; STATE.write_text(json.dumps(st, indent=1))
    return st

def url(path, st):
    w = web_path(path)
    return f"https://cdn.jsdelivr.net/gh/{REPO}@{st[group_of(w)]}/{w}"

if __name__ == "__main__":
    print(json.dumps(tags(refresh=True), indent=1))

def _selfcheck():
    assert group_of("art/web/cg/01-0.webp") == "cg-ch1"
    assert group_of("art/web/cg/ch2/07-1.webp") == "cg-ch2"
    assert group_of("art/bgm/main_theme.mp3") == "bgm-ch1"
    assert web_path("art/cg_paper/ch2/07-1.jpg") == "art/web/cg/ch2/07-1.webp"
    assert web_path("art/bgm/x.mp3") == "art/bgm/x.mp3"
_selfcheck()
