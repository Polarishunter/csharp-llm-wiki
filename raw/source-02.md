---
id: S02
title: C# 類型系統
url: https://learn.microsoft.com/zh-tw/dotnet/csharp/fundamentals/types/
fetched: 2026-11-23
page_updated: 2026-03-26（頁面顯示）
status: ok
---
# 頁面重點（擷取紀錄）
- C# 是強型別語言：每個變數、常數、運算式都有型別；編譯器檢查每個運算對其型別是否合法（型別安全）。
- 與 C/C++ 不同，C# 的 `bool` 不能轉成 `int`。
- 型別錯誤在編譯時期就會被抓到；型別資訊也以 metadata 存在執行檔中，供 CLR 在執行時做額外檢查。
- 宣告變數可明確寫出型別，或用 `var` 讓編譯器依指派值推斷。
- 變數宣告後不能改變型別，也不能指派不相容的值；隱含轉換不會遺失資料，明確轉換（cast）必須寫在程式中。
- 內建型別包含整數、浮點數、`bool`、`char`、`string`。
- 每個型別不是實值型別（value type）就是參考型別（reference type）。實值型別直接保存資料，指派時複製；參考型別保存對物件的參考，指派後兩個變數指向同一物件。`string`、類別、陣列屬參考型別；內建數值型別、struct、enum 屬實值型別。

## 程式範例（頁面所示）
```csharp
int a = 5;
int b = a + 2; // OK

bool test = true;

// Error. Operator '+' cannot be applied to operands of type 'int' and 'bool'.
// int c = a + test;
```
```csharp
// Explicit type:
int count = 10;
double temperature = 36.6;

// Compiler-inferred type:
var name = "C#";
```

## 非頁面內容（不可引用）
擷取工具補充「`decimal` 也是內建型別」，頁面此處未提及，Wiki 不引用。
