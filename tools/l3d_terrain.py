# Larch 3D 地形編解碼（照 larch.ink 前端 modelDoc 的 On/qn：每列差分 int16、×100、zlib、base64）
import zlib, base64, array
def dec(s, n, scale=100, nan=None):
    c = array.array('H', zlib.decompress(base64.b64decode(s))); out = []
    for row in range(len(c)//n):
        h = 0
        for f in range(n):
            h = (h + c[row*n+f]) & 65535; u = h-65536 if h >= 32768 else h
            out.append(float('nan') if nan is not None and u == nan else u/scale)
    return out
def enc(vals, n, scale=100, nan=None):
    s = array.array('H', [0]*len(vals))
    for row in range(len(vals)//n):
        prev = 0
        for f in range(n):
            v = vals[row*n+f]
            l = nan if v != v else max(-32000, min(32000, round(v*scale)))
            s[row*n+f] = (l-prev) & 65535; prev = l
    return base64.b64encode(zlib.compress(s.tobytes())).decode()
def enc_u8(b): return base64.b64encode(zlib.compress(bytes(b))).decode()
def dec_u8(s): return zlib.decompress(base64.b64decode(s))
if __name__ == "__main__":
    import json, sys
    p = json.load(open(sys.argv[1])); p = p.get("project", p)
    d = [n["data"] for n in p["boards"][0]["nodes"] if n["data"]["type"] == "plugin"][0]
    s = json.loads(d["pluginValues"]["scene"]); t = s["terrain"]; N = t["res"]+1
    H = dec(t["heights"], N)
    assert enc(H, N) and dec(enc(H, N), N) == H
    for o in s["objects"]:
        if o["type"] in ("asset", "model", "spawn"):
            x, y, z = o["p"]; i = round((x+t["size"]/2)/t["size"]*t["res"]); j = round((z+t["size"]/2)/t["size"]*t["res"])
            print(o["name"], round(y, 2), "地形", H[i+j*N])
