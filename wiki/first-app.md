---
title: 第一個 Windows Forms 程式
sources: [S07]
related: [windows-forms, event-handling, conditions]
---
# 第一個 Windows Forms 程式（官方教學「Names」）

## 準備
- Visual Studio 2026，安裝「.NET 桌面開發」工作負載與 .NET 10 元件。〔S07〕

## 建立專案
1. 開啟 Visual Studio → 建立新專案。〔S07〕
2. 搜尋 `winforms`，語言選 C#，選「Windows Forms App」範本（**不要**選 .NET Framework 版）。〔S07〕
3. 專案名稱 `Names`，Framework 選 .NET 10.0（LTS），按建立。〔S07〕
4. 畫面出現 `Form1` 的設計工具；用「檢視」功能表打開工具箱與屬性視窗。〔S07〕

## 放控制項並設定屬性
| 控制項 | 屬性 | 值 |
|---|---|---|
| Label | Text | `Names` |
| ListBox | Name | `lstNames` |
| TextBox | Name | `txtName` |
| Button | Name / Text | `btnAdd` / `Add Name` |
| Form | Text | `Names` |
〔S07〕

`Name` 是程式碼裡稱呼控制項的名字；`Text` 是畫面上顯示的文字。

## 撰寫按鈕事件
在屬性視窗選按鈕的 Click 事件並雙擊，Visual Studio 會產生處理常式；填入：〔S07〕
```csharp
private void btnAdd_Click(object sender, EventArgs e)
{
    if (!string.IsNullOrWhiteSpace(txtName.Text) && !lstNames.Items.Contains(txtName.Text))
        lstNames.Items.Add(txtName.Text);
}
```
- 意思：文字方塊不是空白、而且清單裡還沒有這個名字，才把名字加入清單。〔S07〕
- 條件語法見 [[conditions]]；`sender`、`e` 參數見 [[event-handling]]。

## 執行
按 **F5**（偵錯 > 開始偵錯），輸入名字後按按鈕。〔S07〕

## 相關條目
- [[windows-forms]]
- [[event-handling]]
- [[conditions]]
