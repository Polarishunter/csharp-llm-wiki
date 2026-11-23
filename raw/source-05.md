---
id: S05
title: 事件概觀 - Windows Forms
url: https://learn.microsoft.com/zh-tw/dotnet/desktop/winforms/forms/events
fetched: 2026-11-23
page_updated: 2026-02-18（頁面顯示）
status: ok
---
# 頁面重點（擷取紀錄）
- 事件是程式可以回應的動作，通常由使用者動作（例如按鍵）觸發，也可由程式或系統引發。
- 事件驅動應用程式：事件發生時，若有附加處理常式（handler），就執行該處理常式。每個表單與控制項都有預先定義的事件。
- 事件透過委派（delegate）繫結到處理方法；多播委派可以保存多個處理常式。
- 標準處理常式有兩個參數：`sender`（引發事件的物件）與 `e`（事件相關資料，例如滑鼠位置）。
- 一個處理常式可以服務多個事件，例如多個 RadioButton 的 Click。
- 一個使用者動作可能引發多個事件：雙擊也會引發 MouseDown、MouseUp、Click。
- 處理常式必須回傳 void；非同步處理常式使用 `async void` 並以 try-catch 包住。不要用 `.Wait()`、`.Result` 阻塞 UI 執行緒。

## 程式範例（頁面所示）
```csharp
private void button1_Click(object sender, System.EventArgs e)
{

}
```

## 非頁面內容（不可引用）
擷取工具另外補充了「在設計工具中用閃電圖示連接事件」、「`+=` / `-=` 訂閱語法」與「表單生命週期事件順序」，並註明這些不是本頁內容。
- 事件順序改由 S06 取得。
- 設計工具雙擊產生處理常式的步驟改由 S07 取得。
- `+=` 語法本頁未示範，Wiki 若使用必須另找來源或標為「補充」。
