// 簡報第 4、6、7、8、9、10 頁的程式碼（依 wiki/csharp-basics、variables、conditions）

// This line prints "Hello, World"
Console.WriteLine("Hello, World");

// 明確寫出型別
int count = 10;
double temperature = 36.6;

// 用 var 讓編譯器推斷型別
var name = "C#";
Console.WriteLine($"{count} {temperature} {name}");

int a = 5;
int b = a + 2; // OK

bool test = true;

// Error. Operator '+' cannot be applied to operands of type 'int' and 'bool'.
// int c = a + test;
Console.WriteLine($"{b} {test}");

DisplayWeatherReport(15.0);
DisplayWeatherReport(25.0);

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
