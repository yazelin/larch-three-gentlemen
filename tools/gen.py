# 呼叫自架的 codex-image 服務（環境變數 CODEX_IMAGE_BASE、CODEX_IMAGE_KEY）：python3 tools/gen.py <輸出.png> <提示詞檔> [參考圖...]
import sys, os, json, base64, urllib.request
out, pf, refs = sys.argv[1], sys.argv[2], sys.argv[3:]
# ponytail: 檔案鎖讓兩條隊伍不畫同一張；已存在或有人在畫就跳過。要重畫請先刪掉輸出檔與 .lock
if os.path.exists(out) or os.path.exists(out + ".lock"):
    print("skip", out); sys.exit(0)
open(out + ".lock", "w").close()
body = {"prompt": open(pf, encoding="utf-8").read(), "size": os.environ.get("GEN_SIZE", "1536x1024")}   # 直式：GEN_SIZE=1024x1536
if refs: body["reference_images_base64"] = [base64.b64encode(open(r, "rb").read()).decode() for r in refs]
req = urllib.request.Request((os.environ.get("CODEX_IMAGE_BASE") or open(os.path.expanduser("~/.config/codex-image/base")).read().strip()).rstrip("/") + "/v1/images/generate",
    data=json.dumps(body).encode(), headers={"Content-Type": "application/json",
    "Authorization": "Bearer " + os.environ["CODEX_IMAGE_KEY"]})
r = json.load(urllib.request.urlopen(req, timeout=900))
img = r["images"][0]
data = base64.b64decode(img["b64_json"]) if img.get("b64_json") else urllib.request.urlopen(img["url"]).read()
open(out, "wb").write(data); os.remove(out + ".lock"); print("ok", out, len(data))
