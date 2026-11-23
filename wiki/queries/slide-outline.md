---
title: 簡報大綱（Query 結果）
sources: [S01, S02, S03, S04, S05, S06, S07]
related: [index, csharp-basics, variables, conditions, windows-forms, first-app, event-handling]
---
# 查詢：「要教初學者 C# Windows Forms，簡報該怎麼排？」

## 查詢過程
1. 讀 [[index]]，依「語言基礎 → Windows Forms」兩大類排定順序。
2. 逐一讀取條目，挑出初學者必要的概念與程式範例。
3. 進階內容（實值／參考型別、模式比對 switch、資料繫結、async 事件）不放入簡報，只留在 Wiki。

## 回答：投影片與條目對應表
| # | 投影片 | 對應條目 | 來源 |
|---|---|---|---|
| 1 | 封面：從零開始認識 C# Windows Forms | [[index]] | — |
| 2 | 今天的學習地圖 | [[index]] | — |
| 3 | C# 是什麼 | [[csharp-basics]] | S01 |
| 4 | 第一個程式 Hello, World | [[csharp-basics]] | S01 |
| 5 | 寫 C# 的三個規則 | [[csharp-basics]] | S01 |
| 6 | 變數與常用型別 | [[variables]] | S02 |
| 7 | 型別安全 | [[variables]] | S02 |
| 8 | if / else | [[conditions]] | S03 |
| 9 | else if 多重條件 | [[conditions]] | S03 |
| 10 | switch | [[conditions]] | S03 |
| 11 | Windows Forms 是什麼 | [[windows-forms]] | S04 |
| 12 | 表單與控制項 | [[windows-forms]] | S04 |
| 13 | 建立第一個專案 | [[first-app]] | S07 |
| 14 | 放控制項、設定屬性 | [[first-app]] | S07 |
| 15 | 事件與處理常式 | [[event-handling]] | S05, S07 |
| 16 | 寫按鈕事件 | [[first-app]] | S07 |
| 17 | 表單的事件順序 | [[event-handling]] | S06 |
| 18 | 小結與練習 | [[index]] | — |
| 19 | 資料來源 | [[sources]] | 全部 |

## 程式範例規則
簡報中的程式碼同步存放於 `tools/examples/`，必須通過編譯檢查（見 AGENTS.md §6）。
