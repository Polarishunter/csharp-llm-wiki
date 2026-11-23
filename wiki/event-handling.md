---
title: 事件處理
sources: [S05, S06, S07]
related: [windows-forms, first-app, conditions]
---
# 事件處理

## 什麼是事件
- 事件是程式可以回應的「動作」，通常由使用者觸發（例如按鍵、點擊），也可能由程式或系統引發。〔S05〕
- Windows Forms 是**事件驅動**：事件發生時，如果有附加的處理常式，就執行它。〔S05〕
- 每個表單和控制項都有預先定義好的事件，例如 Click。〔S05〕

## 事件處理常式長什麼樣子
```csharp
private void button1_Click(object sender, System.EventArgs e)
{

}
```
〔S05〕
- `sender`：是**誰**引發了這個事件（例如被按的那顆按鈕）。〔S05〕
- `e`：事件附帶的資料（例如滑鼠位置）。〔S05〕
- 處理常式回傳型別是 `void`。〔S05〕

## 怎麼把事件接上處理常式
- 在設計工具的屬性視窗，選控制項的事件並雙擊，Visual Studio 會自動產生處理常式。〔S07〕
- 事件是透過**委派（delegate）**與處理方法連結的；一個事件可以掛多個處理常式。〔S05〕

## 一個動作，可能觸發多個事件
- 雙擊滑鼠也會引發 MouseDown、MouseUp、Click。〔S05〕
- 一個處理常式也可以同時處理多個控制項的事件。〔S05〕

## 表單的事件順序
啟動時：HandleCreated → BindingContextChanged → **Load** → VisibleChanged → Activated → **Shown**〔S06〕

關閉時：Closing → **FormClosing** → Closed → **FormClosed** → Deactivate〔S06〕

初學者只要先記住：`Load` 適合做初始化，`FormClosing` 可以在關閉前做確認。

## 相關條目
- [[windows-forms]]
- [[first-app]]
- [[conditions]]
