---
id: S06
title: Windows Forms 中的事件順序
url: https://learn.microsoft.com/zh-tw/dotnet/desktop/winforms/order-of-events-in-windows-forms
fetched: 2026-11-23
page_updated: 2025-05-07（頁面顯示）
status: ok
---
# 頁面重點（擷取紀錄）
應用程式啟動時，主表單事件依序為：
1. Control.HandleCreated
2. Control.BindingContextChanged
3. Form.Load
4. Control.VisibleChanged
5. Form.Activated
6. Form.Shown

應用程式關閉時，主表單事件依序為：
1. Form.Closing
2. Form.FormClosing
3. Form.Closed
4. Form.FormClosed
5. Form.Deactivate

主表單關閉事件之後才引發 Application.ApplicationExit。

以鍵盤（TAB 等）切換焦點時：Enter → GotFocus → Leave → Validating → Validated → LostFocus。
以滑鼠或 Focus() 切換焦點時：Enter → GotFocus → LostFocus → Leave → Validating → Validated。
