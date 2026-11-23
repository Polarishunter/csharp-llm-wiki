---
title: C# 基礎
sources: [S01]
related: [variables, conditions, windows-forms]
---
# C# 基礎

## C# 是什麼
- C# 是 .NET 平台上最主要的程式語言；.NET 是免費、跨平台、開放原始碼的開發環境。〔S01〕
- C# 是通用語言，可以寫桌面、手機、伺服器、雲端甚至 IoT 裝置上的程式。〔S01〕
- C# 是**編譯式**語言：程式碼先編譯（`dotnet build`），再執行（`dotnet run`）。〔S01〕
- C# 是**強型別**語言：每個變數在編譯時就有確定的型別（詳見 [[variables]]）。〔S01〕

## 寫 C# 的三個基本規則
1. 每個陳述式（一句指令）以分號 `;` 結尾。〔S01〕
2. 大小寫有差別：`Console` 和 `console` 是不同的名字。〔S01〕
3. 用大括號 `{ }` 把程式碼包成一個區塊。〔S01〕

## 第一個程式：Hello, World
最短的寫法（最上層陳述式）：〔S01〕
```csharp
// This line prints "Hello, World"
Console.WriteLine("Hello, World");
```
傳統寫法：〔S01〕
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

## 逐行理解
- `Console.WriteLine(...)`：`WriteLine` 是 `Console` 類別的方法，負責輸出一行文字。〔S01〕
- `using System;`：`Console` 位在 `System` 命名空間；寫了 `using System;` 就能直接用 `Console`，不必寫成 `System.Console`。〔S01〕
- 命名空間：用階層方式整理程式與程式庫，像資料夾一樣。〔S01〕
- `static void Main()`：傳統寫法中程式的進入點。用最上層陳述式時，編譯器會自動產生這些結構，兩種寫法編譯結果相同。〔S01〕

## 相關條目
- [[variables]]：資料怎麼存
- [[conditions]]：程式怎麼做判斷
- [[windows-forms]]：把 C# 用在視窗程式
