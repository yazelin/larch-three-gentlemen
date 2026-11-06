# 運鏡：把劇本裡【CG id｜運鏡 X】用到的 CG 做成短片，上傳 Larch 媒體庫（Cloudflare Stream）。
#   python3 tools/motion.py            # 只做本機影片
#   python3 tools/motion.py --upload   # 做完上傳，寫 art/video/media.json
# 影片結束停在最後一格，所以同時輸出最後一格的 jpg，建置時拿它當那一句的背景，影片播完不會跳回原圖。
import hashlib, json, re, subprocess, sys, pathlib, base64
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import larch_build as lb

ROOT = lb.ROOT
OUT = ROOT / "art/video"
MAP = OUT / "media.json"
W, H, FPS, SEC = 1536, 1024, 30, 7
N = FPS * SEC
E = f"(on/{N})*(on/{N})*(3-2*(on/{N}))"   # smoothstep，起步與停下都慢
# 每種運鏡：zoom、x、y 的 ffmpeg 運算式（iw/ih 是放大後的原圖）
MOVES = {
    "推近": (f"1+0.14*{E}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
    "拉遠": (f"1.16-0.16*{E}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
    "左搖": ("1.14", f"(iw-iw/zoom)*(1-{E})", "ih/2-(ih/zoom/2)"),
    "右搖": ("1.14", f"(iw-iw/zoom)*{E}", "ih/2-(ih/zoom/2)"),
    "下搖": ("1.18", "iw/2-(iw/zoom/2)", f"(ih-ih/zoom)*{E}"),
    "呼吸": (f"1+0.035*{E}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),
    "逼近": (f"1+0.32*{E}", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"),   # 心跳時刻：慢慢推到他臉上
}

def keys():
    md = (ROOT / "劇本/第一章.md").read_text(encoding="utf-8")
    return sorted(k for k in set(re.findall(r"【CG ([^｜\s】]+)｜運鏡 (\S+?)[】｜]", md)) if k[1] != "定")   # 定＝不動，不做影片

def make(cid, move):
    src = ROOT / f"art/cg_paper/{cid}.jpg"   # 運鏡也用紙紋版，影片播完接回背景才不會跳
    z, x, y = MOVES[move]
    stem = f"{cid}_{ {'推近':'in','拉遠':'out','左搖':'panl','右搖':'panr','下搖':'tiltd','呼吸':'breath','逼近':'close'}[move] }"
    mp4, end = OUT / f"{stem}.mp4", OUT / f"{stem}_end.jpg"
    vf = f"scale={W*2}:{H*2}:flags=lanczos,zoompan=z='{z}':x='{x}':y='{y}':d={N}:s={W}x{H}:fps={FPS},format=yuv420p"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(src), "-vf", vf, "-t", str(SEC),
                    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-movflags", "+faststart", str(mp4)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.1", "-i", str(mp4), "-frames:v", "1", "-q:v", "2", str(end)], check=True)
    return mp4, end, hashlib.sha1(src.read_bytes()).hexdigest()[:12]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    m = json.loads(MAP.read_text()) if MAP.exists() else {}
    pid = json.loads(lb.STATE.read_text())["id"]
    for cid, move in keys():
        if not (ROOT / f"art/cg/{cid}.jpg").exists(): print("略過（圖還沒好）", cid); continue
        k = f"{cid}|{move}"
        mp4, end, h = make(cid, move)
        print("做好", k, mp4.name, mp4.stat().st_size // 1024, "KB")
        if "--upload" in sys.argv and m.get(k, {}).get("src") != h:
            r, _ = lb.call("POST", f"/projects/{pid}/media", {"name": mp4.name, "mimeType": "video/mp4", "category": "scene",
                                                              "base64": base64.b64encode(mp4.read_bytes()).decode()})
            a = r["asset"]
            m[k] = {"mediaId": a["id"], "url": a["url"], "src": h, "end": f"art/video/{end.name}"}
            MAP.write_text(json.dumps(m, ensure_ascii=False, indent=1))
            print("  上傳", a["url"])
        elif k in m:
            m[k]["end"] = f"art/video/{end.name}"; MAP.write_text(json.dumps(m, ensure_ascii=False, indent=1))
