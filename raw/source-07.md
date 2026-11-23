---
id: S07
title: 教學：使用 .NET 建立 Windows Forms 應用程式
url: https://learn.microsoft.com/zh-tw/dotnet/desktop/winforms/get-started/create-app-visual-studio
fetched: 2026-11-23
page_updated: 2026-03-06（頁面顯示）
status: ok
---
# 頁面重點（擷取紀錄）
- 先決條件：Visual Studio 2026，勾選「.NET 桌面開發」工作負載與 .NET 10 個別元件。
- 建立專案：搜尋 `winforms` → 語言選 C# → 選「Windows Forms App」範本（不要選 .NET Framework 版本）→ 專案名稱 `Names` → Framework 選 .NET 10.0（LTS）→ 建立。
- Visual Studio 會開啟預設表單 `Form1` 的設計工具；從「檢視」功能表開啟工具箱與屬性視窗。
- 從工具箱拖曳 Button、Label、ListBox、TextBox 到表單。
- 屬性設定：Label.Text=`Names`；ListBox.Name=`lstNames`；TextBox.Name=`txtName`；Button.Name=`btnAdd`、Text=`Add Name`；Form.Text=`Names`。
- 在屬性視窗選按鈕的 Click 事件並雙擊，會產生處理常式。
- 按 F5（偵錯 > 開始偵錯）執行。

## 程式範例（頁面所示）
```csharp
private void btnAdd_Click(object sender, EventArgs e)
{
    if (!string.IsNullOrWhiteSpace(txtName.Text) && !lstNames.Items.Contains(txtName.Text))
        lstNames.Items.Add(txtName.Text);
}
```
說明：文字方塊不為空白、且清單中尚未有此名字時，才加入 ListBox。
