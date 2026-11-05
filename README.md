# 慕詩客，邀明月，對朝霞

三位先生，都讓我心動

Larch 創作者挑戰「自由與限制」那三個禮拜，大學生茶語在高雄的書桌前做一部聖騎士與信仰的 RPG。這部乙女向視覺小說寫的是那三個禮拜：她，還有她的三個 AI 夥伴，負責美術設計與校稿的 C 先生、技術總監 M 先生、音樂創作的 S 先生。

茶語的人設與製作經過取材自 Larch 創作者茶葉飲料，經她本人同意。她的作品《最後的聖戰》：https://zuihoudeshengzhan.larch.games

公開站：https://yazelin.github.io/larch-three-gentlemen/ （角色、名字的由來、線上閱讀、取材對照）

製作中，還沒有可以玩的版本。Larch 專案目前是私人專案，等整部驗過品質才會上架。


## 這個 repo 放什麼

| 路徑 | 內容 |
|---|---|
| `設計.md` | 企劃、鐵則、角色與場景規格、每一項取材的出處（直播逐字稿行號、茶館貼文時間、作品版本記錄） |
| `canon/cast.json` | 角色、場景、機位的唯一事實來源。每張 CG 都從這裡組提示詞，也照這裡驗收 |
| `canon/refs/` | 定稿圖：四位角色、身高對照、工作室、書桌。`xx.jpg` 是送模型的縮圖，`xx_full.jpg` 是原尺寸 |
| `canon/plans/` | 平面配置圖，每個機位一張，由 `tools/plans.py` 畫出來 |
| `art/ref/` | 朋友提供的原始設定圖與海報，只算草稿，CG 不拿它們當參考 |
| `sources/` | 取材用的公開資料：茶葉飲料的茶館貼文、市集留言、個人頁 |
| `tools/` | 產圖、平面圖、確認頁、公開站的小工具 |
| `docs/` | 公開站（由 `tools/build_site.py` 產生，不手改） |

## 工具

```bash
# 產圖（呼叫自架的 codex-image 服務，網址取環境變數 CODEX_IMAGE_BASE 或 ~/.config/codex-image/base，金鑰取 CODEX_IMAGE_KEY）
python3 tools/gen.py <輸出.png> <提示詞檔> [參考圖...]

# 重畫平面配置圖
python3 tools/plans.py

# 產生定稿確認頁
python3 tools/review_page.py <輸出.html> <id>=<圖檔> ...

# 重產公開站（字幕檔用來把逐字稿行號換成錄影時間；沒有也能跑）
python3 tools/build_site.py [逐字稿字幕.srt]
```

## 授權

劇本、設定與正典圖採 CC BY-NC 4.0，`tools/` 採 MIT，例外見 [LICENSE.md](LICENSE.md)。
