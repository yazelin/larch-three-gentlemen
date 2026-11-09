# 島上工作室的房子本體：用 Larch 3D 模型卡的黏土形狀（clay prims）拼，寫進指定專案的指定模型卡。
#   python3 tools/studio_house.py <projectId> <boardId> <nodeId>
# 座標：公尺，y 往上；大窗在 -z 面（放上島時朝北），門在 +z 面（朝南）。
# 形狀照 larch.ink 前端 modelDoc：op add／subtract／intersect／paint，box 的 s 是半邊長，r 是弧度，blend 0 是硬邊，最多 96 個。
import sys, json, math, urllib.request, pathlib

W, D, H = 3.0, 2.0, 1.3          # 房子半長（x）、半深（z）、牆半高
RIDGE = 1.0                       # 屋脊比牆頂高多少
WALL, TRIM, ROOF, FRAME, DOOR = "#d9a46c", "#f4efe6", "#5b5560", "#3d3f48", "#9a5f35"
LEAF = ["#7fae4a", "#9cc35a", "#6f9e3e"]

n = [0]
def prim(shape, op, p, s, color=WALL, r=(0, 0, 0), blend=0.0, rnd=0.0):
    n[0] += 1
    d = {"id": f"h{n[0]:02d}", "shape": shape, "op": op, "p": [round(v, 3) for v in p], "r": [round(v, 4) for v in r],
         "s": [round(v, 3) for v in s], "blend": blend, "color": color}
    if rnd: d["round"] = rnd
    return d

def house():
    P = []
    top = 2 * H
    P.append(prim("box", "add", (0, H, 0), (W, H, D), WALL, rnd=0.02))                    # 外殼
    P.append(prim("box", "add", (0, top + RIDGE / 2, 0), (W - 0.05, RIDGE / 2, D)))      # 山牆的填塊
    th = math.atan2(RIDGE, D)                                                             # 屋頂斜度
    L = math.hypot(D, RIDGE)
    for sgn in (-1, 1):                                                                   # 削掉屋頂斜面以上
        nz, ny = sgn * math.sin(th), math.cos(th)                                         # 斜面朝外的法線
        cz, cy = sgn * D / 2 + nz * 1.0, top + RIDGE / 2 + ny * 1.0
        P.append(prim("box", "subtract", (0, cy, cz), (W + 0.5, 1.0, L), WALL, r=(sgn * th, 0, 0)))
    for sgn in (-1, 1):                                                                   # 屋頂板，出簷 0.3
        nz, ny = sgn * math.sin(th), math.cos(th)
        cz, cy = sgn * (D / 2 + 0.12) + nz * 0.09, top + RIDGE / 2 - 0.06 + ny * 0.09
        P.append(prim("box", "add", (0, cy, cz), (W + 0.3, 0.08, L / 2 + 0.3), ROOF, r=(sgn * th, 0, 0)))
    P.append(prim("box", "subtract", (0, H + 0.12, 0), (W - 0.16, H - 0.08, D - 0.16)))  # 挖出室內（地板留 0.2，太薄網格會破洞）
    P.append(prim("box", "subtract", (0, H + 0.05, -D), (W - 0.45, H - 0.3, 0.3)))       # 北面大窗的洞
    P.append(prim("box", "subtract", (0, 1.05, D), (0.48, 1.05, 0.3)))                    # 南面門洞
    P.append(prim("box", "add", (0, 1.04, D - 0.04), (0.45, 1.0, 0.035), DOOR))          # 門板
    P.append(prim("sphere", "add", (0.3, 1.0, D + 0.01), (0.045, 0.045, 0.045), "#d8b24a"))   # 門把
    # 窗框格子（嵌在洞裡，靠外側）
    x0, x1, y0, y1 = -(W - 0.45), W - 0.45, 0.35, 2 * H - 0.25
    for i in range(9):
        x = x0 + (x1 - x0) * i / 8
        P.append(prim("box", "add", (x, (y0 + y1) / 2, -D + 0.04), (0.06, (y1 - y0) / 2, 0.06), FRAME))
    for j in range(5):
        y = y0 + (y1 - y0) * j / 4
        P.append(prim("box", "add", (0, y, -D + 0.04), ((x1 - x0) / 2, 0.06, 0.06), FRAME))
    for sx in (-1, 1):                                                                    # 四角白色柱
        for sz in (-1, 1):
            P.append(prim("box", "add", (sx * (W + 0.02), H, sz * (D + 0.02)), (0.08, H, 0.08), TRIM))
    for sx in (-1, 1):                                                                    # 兩面山牆的圓窗（白框＋淡藍玻璃色）
        P.append(prim("cylinder", "add", (sx * (W + 0.01), top + 0.38, 0), (0.32, 0.03, 0.32), TRIM, r=(0, 0, math.pi / 2)))
        P.append(prim("cylinder", "add", (sx * (W + 0.03), top + 0.38, 0), (0.25, 0.03, 0.25), "#cfe3ef", r=(0, 0, math.pi / 2)))
    # 藤蔓先不做：黏土球看起來像一顆顆綠球，之後另做
    return P

def call(method, path, body=None, etag=None):
    key = (pathlib.Path.home() / ".config/larch/key").read_text().strip()
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    if etag: h["If-Match"] = etag
    r = urllib.request.urlopen(urllib.request.Request("https://larch.ink/api/agent" + path, method=method, headers=h,
                               data=json.dumps(body).encode() if body is not None else None), timeout=200)
    return json.loads(r.read() or b"{}"), r.headers.get("ETag")

if __name__ == "__main__":
    pid, bid, nid = sys.argv[1:4]
    P = house(); assert len(P) <= 96, len(P)
    b, etag = call("GET", f"/projects/{pid}/boards/{bid}"); b = b.get("board", b)
    node = next(x for x in b["nodes"] if x["id"] == nid)
    m = json.loads(node["data"]["pluginValues"]["model"])
    assert m.get("source") == "clay", "只改黏土模型卡"
    m.update({"name": "工作室", "clay": {"prims": P}, "material": {"preset": "standard"}, "physics": {"wobble": 0, "mass": 1, "bounce": 0}})
    m.pop("thumb", None)
    node["data"]["pluginValues"]["model"] = json.dumps(m, ensure_ascii=False)
    node["data"]["title"] = "工作室"
    call("PUT", f"/projects/{pid}/boards/{bid}", {"name": b.get("name"), "nodes": b["nodes"], "edges": b.get("edges", [])}, etag)
    print("寫入", len(P), "個形狀")
