---
id: S03
title: if 和 switch 語句 - 選取要執行的程式碼路徑
url: https://learn.microsoft.com/zh-tw/dotnet/csharp/language-reference/statements/selection-statements
fetched: 2026-11-23
page_updated: 2026-01-22（頁面顯示）
status: ok
---
# 頁面重點（擷取紀錄）
- `if` 依照布林運算式決定是否執行；有 `if-else`（二選一）與只有 `if`（條件為 true 才執行）兩種形式。
- 可以巢狀／串接 `if` 檢查多個條件（頁面以 `char.IsUpper`、`char.IsLower`、`char.IsDigit` 示範 `if / else if / else`）。
- `switch` 以「模式」比對運算式，由上而下評估，執行第一個符合的區段；無法到達的 case 會造成編譯錯誤。
- `default` 在沒有其他 case 符合時執行；沒有符合且沒有 default 時，直接離開 switch。
- 一個區段可以有多個 case 標籤。
- 每個 switch 區段必須以 `break`、`goto`、`return` 或 `throw` 結束；落到下一個區段（fall-through）是編譯錯誤。

## 程式範例（頁面所示）
```csharp
void DisplayWeatherReport(double tempInCelsius)
{
    if (tempInCelsius < 20.0)
    {
        Console.WriteLine("Cold.");
    }
    else
    {
        Console.WriteLine("Perfect!");
    }
}
```
```csharp
case < 0:
case > 100:
    Console.WriteLine("Out of an acceptable range.");
    break;
```
