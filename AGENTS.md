# AGENTS.md — C# Windows Forms 初學者 LLM Wiki 維護規範

本檔是這個 Wiki 的 schema（依 Karpathy〈LLM Wiki〉的三層架構：Raw Sources / Wiki / Schema）。
任何 AI 代理在維護本 Wiki 前，必須先讀完本檔，並遵守以下規則。

## 1. 目錄結構

| 路徑 | 角色 | 誰可以改 |
|---|---|---|
| `raw/` | 原始來源紀錄（不可變） | 只能新增，不可修改既有檔案內容 |
| `wiki/` | 由 AI 整理的知識條目 | AI 維護，人類審閱 |
| `wiki/index.md` | 全部條目的目錄（內容導向） | 每次 Ingest 必更新 |
| `log.md` | 依時間的操作紀錄（append-only） | 每次 Ingest / Query / Lint 必追加 |
| `slides/index.html` | 由 Wiki 產生的教學簡報 | 只能依 Wiki 內容生成 |
| `tools/lint.py` | 自動檢查腳本 | — |
| `tools/examples/` | 簡報中 C# 範例的可編譯版本 | — |

## 2. 來源規則

1. 優先使用 Microsoft Learn 官方文件（`learn.microsoft.com`）。
2. 每篇 raw 檔必須在開頭的 YAML frontmatter 記錄：`id`、`title`、`url`、`fetched`（擷取日期）、`page_updated`（頁面顯示的更新日期）、`status`。
3. raw 檔只記錄「頁面本身寫了什麼」。擷取工具若補充了頁面以外的一般知識，必須放在 `## 非頁面內容（不可引用）` 區塊，**Wiki 不得引用該區塊**。
4. 若來源頁面只是導覽頁、沒有實質內容，`status` 設為 `rejected`，並寫明原因與替代來源。

## 3. Ingest 流程（一次一篇）

1. 讀取來源 → 寫入 `raw/source-XX.md`。
2. **討論（先討論、後生成）**：在 `log.md` 寫下這篇來源的「重點摘要」與「預計更新哪些條目」，經確認後才動 Wiki。
3. 更新或建立相關 `wiki/*.md` 條目；每一個事實陳述後標註來源，例如 `〔S02〕`。
4. 更新 `wiki/index.md`。
5. 在 `log.md` 追加 `## [YYYY-MM-DD] ingest | 標題`。
6. **立即執行 `python3 tools/lint.py`（Lint-A）**，通過後才處理下一篇。（v2 新增：原本只在最後檢查，見 log 2026-11-23 lint 紀錄）

## 4. Wiki 條目格式

```markdown
---
title: 條目名稱
sources: [S01, S02]
related: [other-page]
---
# 條目名稱
內容……〔S01〕
## 相關條目
- [[other-page]]
```

- 交叉連結一律使用 `[[檔名不含副檔名]]`。
- 每個條目至少有一個來源、至少連到一個其他條目、且至少被一個條目連入（不可為孤兒頁）。
- 程式碼範例若是改寫自來源，要標明「改寫自〔Sxx〕」。

## 5. Query 流程

1. 先讀 `wiki/index.md`，再進入相關條目。
2. 回答必須附來源標註。
3. 有價值的查詢結果（例如簡報大綱）要存回 `wiki/queries/`，並登記到 index 與 log。

## 6. 簡報生成規則

1. 簡報每一張投影片以 `data-wiki="條目名"` 標示對應條目；內容不得超出 Wiki 已有的知識。
   - **程式碼一律從對應的 Wiki 條目複製，不可從 raw 複製**（v2 新增：第一次生成時第 6 頁直接抄了 raw 的英文註解，與 Wiki 不一致）。
2. 簡報中的 C# 程式碼必須同步存放在 `tools/examples/`，並通過編譯檢查。

## 7. Lint（健康檢查）項目

執行 `python3 tools/lint.py`，檢查：

1. 每個 Wiki 條目的 frontmatter 是否完整。
2. `[[連結]]` 是否都指向存在的條目（無斷鏈）。
3. 是否有孤兒條目（沒有任何條目連入，index 除外）。
4. 條目中引用的 `〔Sxx〕` 是否存在於 raw，且該來源不是 `rejected`。
5. index 是否列出全部條目。
6. 簡報每張投影片的 `data-wiki` 是否對應到存在的條目。
7. 簡報中的程式碼是否與 `tools/examples/` 一致。

另外以 C# 編譯器編譯 `tools/examples/` 中的範例（見 `tools/compile.sh`）。

人工檢查：條目間是否矛盾、是否有「非頁面內容」被誤引用、初學者用語是否易懂。

## 8. 回頭規則（Loop）

| 發現的問題 | 退回哪個節點 |
|---|---|
| 來源是導覽頁／內容不足 | 回到「取得資料」 |
| Wiki 引用了非頁面內容或來源不支持的說法 | 回到「Ingest」重新核對 raw |
| 斷鏈、孤兒頁、index 漏列 | 回到「建立 Wiki」 |
| 簡報內容在 Wiki 找不到 | 回到「Query」，必要時先補 Wiki |
| 程式碼編譯失敗 | 先修 Wiki 中的範例，再重新產生簡報 |
