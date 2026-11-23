---
title: Windows Forms 是什麼
sources: [S04, S07]
related: [csharp-basics, first-app, event-handling]
---
# Windows Forms 是什麼

## 定義
- Windows Forms 是用來建立 **Windows 桌面應用程式**的 UI 架構，提供控制項、繪圖、資料繫結與使用者輸入處理。〔S04〕
- Visual Studio 提供**拖放式設計工具**：選控制項、放到表單上，還有對齊輔助線。〔S04〕

## 兩個核心名詞
| 名詞 | 意思 | 例子 |
|---|---|---|
| 表單 Form | 顯示資訊給使用者的視窗 | `Form1` |
| 控制項 Control | 顯示資料或接受輸入的 UI 元素 | 按鈕、文字方塊、下拉清單 |
〔S04〕

## 事件讓程式「動起來」
使用者點滑鼠、按鍵盤時會引發**事件**，程式再用程式碼處理這些事件。〔S04〕詳見 [[event-handling]]。

## 其他常見工具
- 版面配置：FlowLayoutPanel、TableLayoutPanel、SplitContainer。〔S04〕
- 表格資料：DataGridView。〔S04〕

## 版本
- Windows Forms for .NET 是開放原始碼；另有 .NET Framework 4 版本。〔S04〕
- 新專案建議使用 .NET 版本範本（見 [[first-app]]）。〔S07〕

## 相關條目
- [[first-app]]：動手做第一個視窗程式
- [[event-handling]]
- [[csharp-basics]]
