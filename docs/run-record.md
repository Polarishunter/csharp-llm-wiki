# 實際執行與檢查紀錄（2026-11-23）

以下為本專案第一次完整執行 Loop 的真實紀錄，終端機輸出為原樣貼上。

## 1. 取得資料與 Ingest
| 順序 | 來源 | 結果 |
|---|---|---|
| 1 | R01 C# 文件首頁 | **退回**：擷取結果只有導覽連結；擷取工具另外補了一般知識。→ 回到「取得資料」改抓 S01 |
| 2 | S01 A tour of C# 概觀 | 採用 |
| 3 | S02 C# 類型系統 | 採用；擷取結果補充的「decimal 也是內建型別」不在頁面上 → 隔離不引用 |
| 4 | S03 if 和 switch 語句 | 採用；頁面範例為模式比對，對初學者太難 → Wiki 另寫教學範例並註明 |
| 5 | S04 什麼是 Windows Forms | 採用 |
| 6 | S05 事件概觀 | 採用；擷取結果有 3 項被工具標示為「非本頁內容」（設計工具接事件、+= 語法、生命週期順序）→ 隔離，並補抓 S06、S07 取代 |
| 7 | S06 Windows Forms 中的事件順序 | 採用（取代 S05 中無出處的事件順序） |
| 8 | S07 教學：建立 Windows Forms 應用程式 | 採用 |

每篇在寫入 Wiki 前，先於 `log.md` 記錄討論摘要與預計更新的條目（先討論、後生成）。

## 2. Query
- 查詢問題：「要教初學者 C# Windows Forms，簡報該怎麼排？」
- 讀取順序：`wiki/index.md` → csharp-basics → variables → conditions → windows-forms → first-app → event-handling → sources
- 結果存回 Wiki：`wiki/queries/slide-outline.md`（19 張投影片 ↔ 條目對應表）

## 3. Lint 第一次（簡報生成後）
```
$ python3 tools/lint.py
raw 來源：8 篇（可用 7，rejected 1）
wiki 條目：9 個
投影片：19 張
簡報程式碼區塊：9 個

發現 5 個問題：
  ✗ [wiki] windows-forms: 內文引用 S07 但 frontmatter sources 未列出
  ✗ [wiki] slide-outline: 內文沒有任何〔Sxx〕來源標註
  ✗ [slides] 第 6 頁：程式碼不在對應條目 variables.md 中（簡報內容超出 Wiki）
  ✗ [slides] 第 15 頁：程式碼與 NamesApp/Form1.cs 不一致
  ✗ [slides] 第 16 頁：程式碼與 NamesApp/Form1.cs 不一致
```

### 判斷與修正
| # | 問題 | 原因 | 屬於 | 修正 |
|---|---|---|---|---|
| 1 | windows-forms 引用 S07 但 frontmatter 未列 | Ingest S07 時改了內文，忘了改 frontmatter | 建立 Wiki | frontmatter 改為 `[S04, S07]` |
| 2 | slide-outline 無〔Sxx〕 | Query 頁用表格列來源，規則過嚴（Lint 誤報） | Lint 規則 | index / sources / queries 改為只要求 frontmatter 宣告來源 |
| 3 | 第 6 頁程式碼不在 variables.md | **簡報直接抄 raw（英文註解），沒有照 Wiki（中文註解）** | 產生 HTML | 簡報與範例檔改用 Wiki 的版本；AGENTS.md 新增「程式碼一律從 Wiki 複製」 |
| 4 | 第 15 頁與 Form1.cs 不一致 | 範例檔的方法在 class 內有縮排，比對未去縮排（Lint 本身的 bug） | Lint 腳本 | 比對前去除每行前後空白 |
| 5 | 第 16 頁與 Form1.cs 不一致 | 同 #4 | Lint 腳本 | 同 #4 |

## 4. Lint 第二次（修正後）
```
$ python3 tools/lint.py
raw 來源：8 篇（可用 7，rejected 1）
wiki 條目：9 個
投影片：19 張
簡報程式碼區塊：9 個

✓ Lint 全部通過
```

## 5. 編譯檢查
第一次：`dotnet build` 全部失敗，錯誤為 `Unable to load the service index for source https://api.nuget.org/v3/index.json`（沙箱網路擋下 NuGet，HTTP 403）。屬於環境問題，不是程式碼錯誤。

修正：
- 主控台範例不需要套件 → 加 `tools/examples/NuGet.config` 清空套件來源，離線編譯。
- WinForms 參考套件無法下載 → 改用 .NET SDK 內建的 Roslyn 編譯器，搭配 Ubuntu 套件庫中 Mono 的 System.Windows.Forms 參考組件編譯 `Form1.cs`。
  限制：這是以 Mono（.NET Framework 4.5 API）檢查語法與型別，不是在 Windows 上以 .NET 10 實際執行。

第二次：
```
$ bash tools/compile.sh
=== dotnet build ConsoleDemo ===
    0 Warning(s)
    0 Error(s)
--- run ConsoleDemo ---
Hello, World
10 36.6 C#
7 True
Cold.
Perfect!
及格
週末
=== dotnet build HelloClassic ===
    0 Warning(s)
    0 Error(s)
--- run HelloClassic ---
Hello, World
=== compile NamesApp/Form1.cs ===
Form1.cs 編譯成功
```
執行輸出與簡報說明一致：15°C → Cold.、25°C → Perfect!、score 75 → 及格、day 6 → 週末。

### 編譯檢查有效性測試
在暫存副本中把 `lstNames.Items.Add` 故意改成 `lstNames.Item.Add`：
```
NamesApp/Form1.cs(39,22): error CS1061: 'ListBox' does not contain a definition for 'Item' and no accessible extension method 'Item' accepting a first argument of type 'ListBox' could be found (are you missing a using directive or an assembly reference?)
```
確認編譯檢查會擋下錯誤（原始檔未修改）。

## 6. 簡報切換測試（jsdom 自動化）
```
$ node tools/slidetest.js slides/index.html
  ✓ 共 19 張投影片，初始顯示第 1 張
  ✓ → 切到第 2 張
  ✓ 空白鍵切到第 3 張
  ✓ ← 回到第 2 張
  ✓ ▶ 按鈕切到第 3 張
  ✓ ◀ 按鈕回到第 2 張
  ✓ End 跳到最後一張
  ✓ 最後一張再按 → 不會超出範圍
  ✓ 第一張再按 ← 不會小於 1
  ✓ 頁碼顯示正確
  ✓ 網址 #16 直接開啟第 16 張
  ✓ 每張都有 Wiki 對應標示
  ✓ 程式碼上色後文字不變（9 個區塊）
  ✓ 第 8 頁 '<' 正確顯示

結果：14 通過，0 失敗
```
