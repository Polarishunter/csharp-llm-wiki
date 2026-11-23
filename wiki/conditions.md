---
title: 條件判斷 if / switch
sources: [S03, S07]
related: [variables, event-handling, first-app]
---
# 條件判斷 if / switch

## if：條件成立才做
- `if` 依照一個**布林運算式**（結果是 `true` 或 `false`，見 [[variables]]）決定要不要執行。〔S03〕
- 只有 `if`：條件為 true 才執行；`if-else`：二選一。〔S03〕

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
〔S03〕

## else if：檢查多個條件
可以串接多個 `if` 來檢查多個條件，依序判斷。〔S03〕
```csharp
int score = 75;
if (score >= 90)
{
    Console.WriteLine("優秀");
}
else if (score >= 60)
{
    Console.WriteLine("及格");
}
else
{
    Console.WriteLine("不及格");
}
```
（本 Wiki 自行撰寫的教學範例，語法依〔S03〕。）

## switch：依值選擇路徑
- `switch` 由上而下比對，執行第一個符合的區段；都不符合時執行 `default`。〔S03〕
- 每個區段必須以 `break`（或 `return` 等）結束，不能「掉到」下一個區段，否則編譯錯誤。〔S03〕
- 一個區段可以有多個 case 標籤。〔S03〕

```csharp
int day = 6;
switch (day)
{
    case 6:
    case 7:
        Console.WriteLine("週末");
        break;
    default:
        Console.WriteLine("平日");
        break;
}
```
（本 Wiki 自行撰寫的教學範例，語法依〔S03〕。）

## 在視窗程式中的 if
官方教學在按鈕事件中用 `if` 檢查輸入：〔S07〕
```csharp
if (!string.IsNullOrWhiteSpace(txtName.Text) && !lstNames.Items.Contains(txtName.Text))
    lstNames.Items.Add(txtName.Text);
```
- `!` 表示「不是」，`&&` 表示「而且」；兩個條件都成立才加入清單。詳見 [[first-app]] 與 [[event-handling]]。

## 相關條目
- [[variables]]
- [[event-handling]]
- [[first-app]]
