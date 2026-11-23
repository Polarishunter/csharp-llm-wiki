---
title: 變數與型別
sources: [S02, S01]
related: [csharp-basics, conditions]
---
# 變數與型別

## 觀念
- **變數**：一個有名字的儲存位置，用來放值。〔S02〕
- **型別**：決定變數能放什麼資料、能做哪些運算。〔S02〕
- C# 是強型別語言，每個變數、常數、運算式都有型別；編譯器會檢查運算是否合法。〔S02〕

## 宣告變數
```csharp
// 明確寫出型別
int count = 10;
double temperature = 36.6;

// 用 var 讓編譯器推斷型別
var name = "C#";
```
〔S02〕

## 初學者常用的內建型別
| 型別 | 用途 | 例子 |
|---|---|---|
| `int` | 整數 | `int age = 20;` |
| `double` | 有小數的數字 | `double score = 85.5;` |
| `bool` | 真或假 | `bool passed = true;` |
| `char` | 單一字元 | `char grade = 'A';` |
| `string` | 文字 | `string name = "小明";` |

C# 內建整數、浮點數、`bool`、`char`、`string` 等型別，任何 C# 程式都能直接使用。〔S02〕（表中例子為本 Wiki 自行撰寫的教學範例。）

## 型別安全：錯誤在編譯時就被抓到
```csharp
int a = 5;
int b = a + 2; // OK

bool test = true;

// Error. Operator '+' cannot be applied to operands of type 'int' and 'bool'.
// int c = a + test;
```
- 型別不符的錯誤在**編譯時期**就會被發現，不必等到執行。〔S02〕
- C# 的 `bool` 不能轉成 `int`（這點和 C/C++ 不同）。〔S02〕
- 變數宣告後不能改變型別；需要轉型時，必須明確寫出轉換。〔S02〕

## 進階預告：實值型別與參考型別
- 實值型別（如 `int`、`double`）直接保存資料，指派時會複製一份。〔S02〕
- 參考型別（如 `string`、類別、陣列）保存的是物件的參考。〔S02〕

## 相關條目
- [[csharp-basics]]：強型別的由來
- [[conditions]]：`bool` 用在條件判斷
