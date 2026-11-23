【學校】○○大學｜【學號】○○○○○○○○｜【系級】資訊管理研究所 ○年級｜【姓名】○○○｜主題：從零開始認識 C# Windows Forms

一、LLM Wiki 主題與簡短介紹
主題：C# Windows Forms 初學者教學。
依 Karpathy〈LLM Wiki〉的三層架構自行實作（未使用付費服務）：
- Raw Sources（raw/）：8 篇 Microsoft Learn 官方文件擷取紀錄，7 篇採用、1 篇導覽頁退回；每篇記錄網址、擷取日期、頁面更新日期與狀態，並把擷取工具混入的「非頁面內容」隔離、不得引用。
- Wiki（wiki/）：6 個知識條目（C# 基礎、變數與型別、條件判斷、Windows Forms、第一個程式、事件處理）＋來源清單＋1 個 Query 結果頁；以 index.md 為索引，條目間用 [[連結]] 交叉引用，每個事實標註〔S01〕〜〔S07〕來源。
- Schema（AGENTS.md）：規定 Ingest／Query／Lint 流程、條目格式、回頭規則。
- log.md：依時間記錄每次 Ingest（含寫入前的討論摘要）、Query、Lint、測試。
讀者為沒有程式基礎的初學者。

二、LLM Wiki 連結
GitHub 儲存庫：https://github.com/<帳號>/csharp-llm-wiki
Wiki 索引：https://github.com/<帳號>/csharp-llm-wiki/blob/main/wiki/index.md

三、教學 HTML 簡報連結
https://<帳號>.github.io/csharp-llm-wiki/slides/
共 19 張，可用方向鍵／空白鍵／按鈕／手機滑動切換，網址 #編號 可直接開啟指定頁。每張左下角標示對應的 Wiki 條目與來源；簡報內 9 段 C# 程式碼皆存於 tools/examples/ 並通過編譯。

四、Loop／Graph 流程
取得資料 → Ingest（寫 raw＋討論摘要）→ 建立 Wiki → Lint-A（結構與來源）→ Query（讀 index→條目→簡報大綱，存回 Wiki）→ 整理教學內容（程式碼從 Wiki 複製）→ 產生 HTML → Lint-B（簡報↔Wiki↔範例檔）→ 編譯與瀏覽器測試 → 部署。
重複執行：Ingest→建立 Wiki→Lint-A 每篇來源跑一次；產生 HTML→Lint-B→測試 每次修改簡報都重跑。
返回規則：
- 來源是導覽頁／內容不足 → 回「取得資料」
- Wiki 引用了非頁面內容 → 回「Ingest」
- 斷鏈、孤兒條目、frontmatter 與內文來源不一致 → 回「建立 Wiki」
- 簡報內容在 Wiki 找不到 → 回「Query」
- 範例編譯失敗 → 先修 Wiki，再重新產生簡報
設計理由：Wiki 是簡報唯一的知識來源，所以在進 Query 前先擋下 Wiki 的錯；Lint-B 確認簡報沒有繞過 Wiki；程式碼用真正的 C# 編譯器驗證，因為文字檢查抓不到語法錯誤。
（流程圖：docs/workflow.md，Mermaid 格式，GitHub 上可直接顯示）

五、實際執行與檢查紀錄（2026-11-23，完整輸出見 docs/run-record.md）
1. Ingest：第 1 篇（C# 文件首頁）只有導覽連結 → 退回，改抓「A tour of C# 概觀」。事件概觀頁的擷取結果混入 3 項工具標示的非頁面內容（設計工具接事件、+= 語法、事件順序）→ 隔離，另抓「事件順序」與「建立 WinForms 應用程式教學」兩篇取代。類型系統頁的「decimal」補充同樣隔離。
2. Query：讀 index.md 及 6 個條目，產出 19 張投影片對應表，存回 wiki/queries/slide-outline.md。
3. Lint 第一次發現 5 個問題：
   (1) windows-forms 內文引用 S07，frontmatter 未列 → 補上；
   (2) 第 6 頁程式碼與 variables 條目不一致：簡報直接抄 raw 的英文註解，沒有照 Wiki 的中文版 → 改用 Wiki 版本；
   (3)(4) 第 15、16 頁誤報：Lint 比對沒去縮排 → 修 lint.py；
   (5) Query 結果頁誤報：規則過嚴 → 修規則。
   修正後第二次 Lint：全部通過。
4. 編譯：第一次 dotnet build 因沙箱網路擋 NuGet（403）全部失敗 → 改離線編譯；WinForms 改用 Roslyn 搭配 Mono 的 WinForms 參考組件檢查 Form1.cs。第二次：3 組範例全部編譯成功，執行輸出與簡報說明一致（Cold.／Perfect!／及格／週末）。再故意放錯字（Items→Item）測試，編譯器正確報 CS1061，證明檢查有效。限制：WinForms 是用 Mono 檢查語法與型別，未在 Windows 以 .NET 10 實際執行。
5. 簡報自動化測試（jsdom）：鍵盤、按鈕、邊界、#頁碼、Wiki 標示、程式碼顯示等 14 項全部通過。

六、反思與檢查流程調整
1. 哪個節點最常出錯？
「取得資料／Ingest」出錯次數最多：8 篇來源中有 1 篇是導覽頁、2 篇的擷取結果混入非頁面內容，共 3 次。但最危險的是「產生 HTML」：第 6 頁直接從 raw 抄程式碼，畫面上看不出問題，若沒有自動比對就會讓簡報和 Wiki 默默不一致。另外 Lint 腳本本身也有 2 次誤報，提醒我檢查工具也需要被檢查。
2. 把檢查往前移到哪個步驟？
(1) 來源檢查移到 Ingest：寫 raw 時就區分「頁面內容」與「非頁面內容」，並以 status 標記退回，不等 Wiki 寫完才發現沒出處。
(2) Lint-A 從流程最後移到「每次更新 Wiki 之後」：這次是全部 Ingest 完才跑 Lint，frontmatter 漏列 S07 拖到簡報做完才被抓到；之後每篇 Ingest 後立即跑。
(3) 「程式碼從 Wiki 複製」的規則移到「整理教學內容」步驟，生成前就約束，而不是生成後才比對。
3. 是否修改 workflow／graph？為什麼？
有。原本 v1 只在最後有一個「檢查正確性」節點；改成 v2：拆成 Lint-A（Wiki）與 Lint-B（簡報↔Wiki），新增「編譯與瀏覽器測試」節點，並在 AGENTS.md 寫入新規則。原因是錯誤越晚發現，要回頭重做的節點越多；而 Wiki 是簡報唯一的知識來源，Wiki 的錯一定要在 Query 之前擋下。
