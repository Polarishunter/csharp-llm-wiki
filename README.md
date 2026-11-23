# C# Windows Forms 初學者 LLM Wiki

依 [Karpathy〈LLM Wiki〉](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 的三層架構建立：

| 層 | 位置 | 說明 |
|---|---|---|
| Raw Sources | [`raw/`](raw/) | 7 篇 Microsoft Learn 來源紀錄（另 1 篇導覽頁被退回） |
| Wiki | [`wiki/`](wiki/index.md) | 6 個知識條目 + 來源清單 + 1 個 Query 結果，從 [`wiki/index.md`](wiki/index.md) 開始讀 |
| Schema | [`AGENTS.md`](AGENTS.md) | AI 維護規則、Ingest / Query / Lint 流程、回頭規則 |

- 操作紀錄：[`log.md`](log.md)
- 教學簡報：[`slides/index.html`](slides/index.html)
- 工作流程（Loop / Graph）：[`docs/workflow.md`](docs/workflow.md)
- 實際執行與檢查紀錄：[`docs/run-record.md`](docs/run-record.md)

## 檢查工具
```bash
python3 tools/lint.py          # Wiki 結構、來源、簡報對應檢查
bash tools/compile.sh          # 編譯並執行主控台範例（需 .NET 8 SDK）
node tools/slidetest.js slides/index.html   # 簡報切換測試（需 npm i jsdom）
```
