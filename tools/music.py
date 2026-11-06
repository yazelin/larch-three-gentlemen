# 配樂：走 gemini-web /api/music（網址讀 ~/larch-eleven-minutes/art/music.py 的 URL，金鑰讀 ~/.bashrc 的 GEMINI_IMAGE_KEY，都不進 repo）
#   python3 tools/music.py 名字…   → art/music_raw/<名字>.mp3，再正規化到 art/bgm/<名字>.mp3（-16 LUFS）
import base64, json, os, re, ssl, subprocess, sys, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKS = {
    "main_theme": "Main title theme for a romantic otome visual novel: a tender, heart-fluttering melody on warm felt piano carried by soft strings, a delicate music box and a gentle celesta, "
                  "the night sky slowly turning to dawn, a young woman and three men who quietly fell for her, sweet and a little bittersweet, hopeful, cinematic but intimate, "
                  "built on the same tender rising four-note motif, 76 BPM, major key with a wistful minor turn, instrumental, no vocals, no choir, no organ, no drums, seamless loop",
    "night_desk": "A single soft felt piano alone in a quiet room at midnight, sparse gentle notes with long pauses, a tender rising four-note motif, "
                  "a young woman alone at her desk waiting for something to begin, lonely but quietly hopeful, intimate, 66 BPM, instrumental, no vocals, no drums, loopable",
    "studio_day": "Warm felt piano and soft fingerpicked acoustic guitar with light pizzicato strings and a gentle glockenspiel, a bright sunlit studio where four friends brainstorm, "
                  "playful curiosity and a little flutter of the heart, the same tender four-note motif, 92 BPM, major key, instrumental, no vocals, loopable",
}
def key():
    for l in open(os.path.expanduser("~/.bashrc"), encoding="utf-8"):
        if l.startswith("export GEMINI_IMAGE_KEY="): return l.split("=", 1)[1].strip().strip('"')
URL = re.search(r"^URL = '([^']+)'", open(os.path.expanduser("~/larch-eleven-minutes/art/music.py"), encoding="utf-8").read(), re.M)[1]
for name in sys.argv[1:]:
    raw, out = f"{ROOT}/art/music_raw/{name}.mp3", f"{ROOT}/art/bgm/{name}.mp3"
    os.makedirs(os.path.dirname(raw), exist_ok=True)
    for n in range(4):
        try:
            r = urllib.request.Request(URL, method="POST", data=json.dumps({"prompt": TRACKS[name], "timeout": 720}).encode(),
                                       headers={"Content-Type": "application/json", "x-goog-api-key": key()})
            d = json.load(urllib.request.urlopen(r, timeout=900, context=ssl._create_unverified_context()))
        except Exception as e: print(name, "例外", repr(e)[:120], flush=True); continue
        if d.get("success"):
            open(raw, "wb").write(base64.b64decode(d["audio"])); break
        print(name, "失敗", (d.get("message") or d.get("error") or "")[:80], flush=True)
    else: print(name, "四次都失敗"); continue
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-b:a", "192k", out], check=True)
    print(name, "好了", out, flush=True)
