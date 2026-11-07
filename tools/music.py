# 配樂：走 .11 的 gemini-web /api/music（Lyria）。不用 suno-web（yazelin 2026-11-03）。
#   python3 tools/music.py <名字>   → art/music_raw/<名字>.mp3（原始）→ art/bgm/<名字>.mp3（-16 LUFS、尾巴淡出）
# 服務網址從 ~/larch-eleven-minutes/art/music.py 讀（同 ~/larch-handoff/tools/run_local.sh），金鑰讀 ~/.bashrc 的 GEMINI_IMAGE_KEY，都不進 repo。
import base64, json, os, re, ssl, subprocess, sys, urllib.request, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
TRACKS = {
    "ch6/tea_leaves_soft": dict(vocals="instrumental", prompt=(
        "A very soft, slow, wordless instrumental lullaby played on a single warm nylon-string acoustic guitar with a little felt piano, "
        "intimate and close like it is playing quietly from a phone speaker at 3 a.m. to comfort someone who just cried; 64 BPM, gentle, "
        "a simple tender melody that repeats, no drums, no vocals, a little room reverb, ends softly.")),
    "ch2/tomorrow_i_write": dict(vocals="vocals", prompt=(
        "A solemn sacred hymn for a mixed SATB church choir with a grand pipe organ, cathedral reverb, slow and majestic, 66 BPM, "
        "sung completely seriously in Mandarin Chinese — but the lyrics are a student's confession of procrastination, so it is comically over-dramatic. "
        "Organ introduction, then the choir enters in full harmony; the last line repeats 'míngtiān' three times with a long held final chord. "
        "Lyrics (Mandarin, sing exactly): 白紙攤在桌上，題目寫得清清楚楚／主啊，我知道我該寫／可是今晚，請讓我再拉一條線／明天，明天，明天我一定寫。")),
    "ch5/concert_hymn": dict(vocals="vocals", prompt=(
        "A live performance of a sacred choral hymn by a large mixed SATB amateur choir in a warm concert hall, three rows of singers, "
        "very rich deep bass section, staggered breathing so the sound never breaks, a clear pure soprano line soaring up to a high note, "
        "soft pipe organ underneath, slow and reverent, 60 BPM, natural hall reverb. Sung on open vowels and Latin-like syllables (no clear words). "
        "It ends with one final chord held for a very long time, slowly dying away into the hall's silence.")),
    "ch5/last_note": dict(vocals="vocals", prompt=(
        "An original sacred chorale for a dark fantasy game: a deep pipe organ introduction, then three choir parts entering one by one and layering "
        "(low men, then women, then a high soprano), solemn, holy but faintly bittersweet, slow 62 BPM, cathedral reverb, thick warm bass. "
        "Wordless: sung only on open vowels 'ah' and 'oh', no lyrics. It builds to a full chord and ends on one single final note held very long, fading into silence.")),
    "ch11/s_song": dict(vocals="vocals", prompt=(
        "An intimate, very quiet love song: one young man (about 21, soft gentle tenor, a little shy, breathy, close to the microphone) singing alone "
        "with a single warm acoustic guitar, fingerpicked, slow 70 BPM, about two minutes, no drums, no strings, almost no reverb, like he is singing "
        "to one person sitting right next to him at night. The complete opposite of a grand church hymn: small, close, tender. "
        "The lyrics are in an invented, made-up language (soft open syllables, not any real language) EXCEPT the very last line, which is spoken-sung "
        "clearly and slowly in Mandarin Chinese after a short pause, almost a whisper but every word clearly audible. "
        "Lyrics (sing exactly): Sae lumi, ta veneri / nao siel, ae noria / Ilsa ven, mi tolae / ta siel, ta siel / "
        "Ro lianne, ve astra / mira tol, ae venei / Sae lumi, ta veneri / nao siel… / (pause) / 我喜歡妳啦。聽到沒。")),
    "ch11/flute_hymn": dict(vocals="vocals", prompt=(
        "A slow original sacred hymn built from a simple, slightly melancholy flute melody: it opens with a solo concert flute alone, very slow and "
        "breathing naturally between phrases, then a mixed choir enters softly layer by layer (men, then sopranos, the altos last), wordless on open "
        "vowels 'ah' and 'oh', gentle pipe organ underneath, 60 BPM, warm church reverb, holy and tender rather than cold; "
        "ends on one long held final note that fades into silence.")),
}

def cfg():
    url = re.search(r"^URL = '([^']+)'", (pathlib.Path.home() / "larch-eleven-minutes/art/music.py").read_text(), re.M)[1]
    key = next(l.split("=", 1)[1].strip().strip('"') for l in open(os.path.expanduser("~/.bashrc"), encoding="utf-8") if l.startswith("export GEMINI_IMAGE_KEY="))
    return url, key

def gen(name, tries=4):
    url, key = cfg(); t = TRACKS[name]
    raw = ROOT / f"art/music_raw/{name}.mp3"; raw.parent.mkdir(parents=True, exist_ok=True)
    for n in range(tries):
        body = {"prompt": t["prompt"], "timeout": 720, "vocals": t["vocals"]}
        req = urllib.request.Request(url, method="POST", data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
        try: d = json.load(urllib.request.urlopen(req, timeout=900, context=ssl._create_unverified_context()))
        except Exception as e: print(f"{name} 第{n+1}次 例外 {e!r}", flush=True); continue
        if d.get("success"):
            raw.write_bytes(base64.b64decode(d["audio"])); print(f"{name} 好了", flush=True); return raw
        print(f"{name} 第{n+1}次 失敗 {d.get('message') or d.get('error')}", flush=True)
    raise SystemExit(f"{name} 失敗")

def master(name):
    raw, out = ROOT / f"art/music_raw/{name}.mp3", ROOT / f"art/bgm/{name}.mp3"; out.parent.mkdir(parents=True, exist_ok=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw)], capture_output=True, text=True).stdout)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-af", f"loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st={max(0, dur - 3):.2f}:d=3",
                    "-ar", "44100", "-b:a", "160k", str(out)], check=True)
    print("→", out.relative_to(ROOT), f"{dur:.0f} 秒")

if __name__ == "__main__":
    for n in sys.argv[1:] or TRACKS: gen(n); master(n)
