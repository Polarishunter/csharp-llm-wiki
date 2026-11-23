# log.md — 操作紀錄（append-only）

格式：`## [日期] 操作 | 標題`。查最近紀錄：`grep "^## \[" log.md | tail -5`

## [2026-11-23] setup | 建立專案與 AGENTS.md
- 依 Karpathy LLM Wiki 原文確認三層架構（raw / wiki / schema）與 ingest / query / lint 三種操作。
- 建立 `AGENTS.md`，規定來源格式、條目格式、Lint 項目與回頭規則。

## [2026-11-23] ingest | R01 C# 文件首頁 → 判定 rejected
- 討論：擷取結果只有導覽連結，沒有說明或範例；擷取工具另外補了一般知識。
- 決策：不採用，改抓頁面中連到的「A tour of C#」概觀頁（S01）。
- **回頭**：Ingest → 取得資料。

## [2026-11-23] ingest | S01 A tour of C# 概觀
- 討論重點：C# 是 .NET 主要語言、編譯式、強型別；三個語法規則（分號、大小寫、大括號）；Hello World 兩種寫法。
- 預計更新：新建 [[csharp-basics]]。
- 已完成：csharp-basics。

## [2026-11-23] ingest | S02 C# 類型系統
- 討論重點：變數／型別定義、明確型別與 var、型別安全在編譯時期檢查、bool 不能轉 int。實值／參考型別對初學者偏難，只放「進階預告」。
- 注意：擷取結果補充的 `decimal` 不在頁面內容，排除。
- 預計更新：新建 [[variables]]；在 [[csharp-basics]] 連到 variables。

## [2026-11-23] ingest | S03 if 和 switch 語句
- 討論重點：if / if-else / else if、switch 由上而下比對、不可 fall-through、多個 case 標籤。頁面範例使用模式比對（`case < 0.0`），對初學者太進階 → 另寫整數 switch 教學範例並註明。
- 預計更新：新建 [[conditions]]。

## [2026-11-23] ingest | S04 什麼是 Windows Forms
- 討論重點：表單與控制項的定義、拖放設計工具、事件的概念。資料繫結相關內容只簡述。
- 預計更新：新建 [[windows-forms]]。

## [2026-11-23] ingest | S05 事件概觀
- 討論重點：事件驅動、sender 與 e、一個動作可觸發多事件。
- 注意：擷取結果中「設計工具接事件」「+= 語法」「生命週期順序」被標示為非頁面內容 → 不引用，事件順序另找 S06、設計工具步驟由 S07 提供。
- 預計更新：新建 [[event-handling]]。

## [2026-11-23] ingest | S06 Windows Forms 中的事件順序
- 討論重點：啟動與關閉時的事件順序（官方列表）。
- 預計更新：[[event-handling]] 的「表單的事件順序」段落。

## [2026-11-23] ingest | S07 教學：建立 Windows Forms 應用程式
- 討論重點：建立專案步驟、Names 範例的控制項與屬性、btnAdd_Click 程式碼。這是簡報中「動手做」的核心。
- 預計更新：新建 [[first-app]]；[[conditions]] 加入「在視窗程式中的 if」；[[event-handling]] 加入設計工具雙擊產生處理常式。

## [2026-11-23] index | 建立 wiki/index.md 與 wiki/sources.md

## [2026-11-23] query | 簡報該怎麼排？
- 讀 index → 6 個條目，產出 [[slide-outline]]，存回 wiki/queries/ 並登記到 index。

## [2026-11-23] generate | 產生 slides/index.html（19 張）

## [2026-11-23] lint | 第一次：5 個問題
- windows-forms frontmatter 缺 S07（建立 Wiki 疏漏）→ 修正。
- 第 6 頁程式碼抄自 raw 而非 Wiki → 改用 Wiki 版本。**回頭：產生 HTML → Query**。
- 第 15、16 頁誤報（Lint 未處理縮排）、slide-outline 誤報（規則過嚴）→ 修正 lint.py。
- 第二次 Lint：全部通過。

## [2026-11-23] test | 編譯與簡報測試
- 第一次編譯：NuGet 被沙箱擋下（403），改離線編譯與 Mono 參考組件。
- 第二次編譯：3 組範例全部通過；故意放錯字的副本會被擋下。
- 簡報切換測試：14 項通過。

## [2026-11-23] schema | AGENTS.md v2
- Ingest 每篇後立即執行 Lint-A（原本只在最後檢查）。
- 簡報程式碼一律從 Wiki 條目複製。
- 詳見 docs/workflow.md「v1 → v2 的修改」。
