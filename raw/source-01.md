---
id: S01
title: 概觀 - A tour of C#（C# 語言教學導覽）
url: https://learn.microsoft.com/zh-tw/dotnet/csharp/tour-of-csharp/overview
fetched: 2026-11-23
page_updated: 2026-03-25（頁面顯示）
status: ok
replaces: R01
---
# 頁面重點（擷取紀錄）
- C# 是 .NET 平台上最主要的語言；.NET 是免費、跨平台、開放原始碼的開發環境。
- C# 是跨平台的通用語言，可用於 IoT、雲端、手機、桌面、筆電與伺服器應用。
- C# 是編譯式語言：多數專案用 `dotnet build` 編譯、`dotnet run` 執行。
- C# 是強型別語言，每個變數在編譯時就有已知型別。
- 屬於 C 語言家族：分號結束陳述式、識別字區分大小寫、使用大括號 `{}`。
- C# 程式使用執行階段提供的自動記憶體管理與 .NET SDK 附帶的程式庫。

## 程式範例（頁面所示）
```csharp
// This line prints "Hello, World"
Console.WriteLine("Hello, World");
```
傳統寫法：
```csharp
using System;
namespace TourOfCsharp;

class Program
{
    static void Main()
    {
        // This line prints "Hello, World"
        Console.WriteLine("Hello, World");
    }
}
```

## 頁面解釋
- `WriteLine` 是 `Console` 類別的方法，`Console` 位於 `System` 命名空間。
- 命名空間以階層方式組織程式與程式庫；`System` 內含 `Console`，也含 `IO`、`Collections` 等命名空間。
- `using System;` 讓 `System` 內的型別可以不加前綴使用，所以 `Console.WriteLine` 是 `System.Console.WriteLine` 的簡寫。
- 傳統寫法以 `Program` 類別中的 static `Main` 方法作為進入點；使用最上層陳述式（top-level statements）時，編譯器會自動產生這些元素，兩種寫法編譯結果相同。
- 頁面未提及 CLR 名稱。
