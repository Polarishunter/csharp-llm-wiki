#!/usr/bin/env bash
# 編譯簡報中所有 C# 範例（AGENTS.md §6）。
# 1) ConsoleDemo / HelloClassic：用 .NET 8 SDK 編譯並執行。
# 2) NamesApp（WinForms）：在 Windows 上可直接 dotnet build；
#    在 Linux 沙箱中因無法下載 WindowsDesktop 參考套件，改用 .NET SDK 內建的 Roslyn 編譯器
#    搭配 Mono 的 System.Windows.Forms 參考組件，編譯 Form1.cs（檢查語法與型別）。
set -u
export DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
cd "$(dirname "$0")/examples"
OUT=/tmp/csharp-wiki-build
fail=0
for p in ConsoleDemo HelloClassic; do
  echo "=== dotnet build $p ==="
  if dotnet build "$p" -nologo -v q -o "$OUT/$p" > "$OUT-$p.log" 2>&1; then
    grep -E "Warning\(s\)|Error\(s\)" "$OUT-$p.log"
    echo "--- run $p ---"; dotnet "$OUT/$p/$p.dll" || fail=1
  else
    grep -E "error" "$OUT-$p.log"; fail=1
  fi
done
echo "=== compile NamesApp/Form1.cs ==="
if [ "$(uname)" != "Linux" ]; then
  dotnet build NamesApp -nologo -v q || fail=1
else
  CSC=$(ls /usr/lib/dotnet/sdk/*/Roslyn/bincore/csc.dll | head -1)
  M=${MONO_REF:-/usr/lib/mono/4.5}
  cat > "$OUT-stub.cs" <<'CS'
global using System;
global using System.Drawing;
global using System.Windows.Forms;
namespace Names { static class Stub { static void Main() { Application.Run(new Form1()); } } }
CS
  if dotnet "$CSC" -nologo -langversion:latest -nostdlib -noconfig -target:winexe -out:"$OUT/NamesApp.exe" \
      -r:$M/mscorlib.dll -r:$M/System.dll -r:$M/System.Drawing.dll -r:$M/System.Windows.Forms.dll \
      "$OUT-stub.cs" NamesApp/Form1.cs; then
    echo "Form1.cs 編譯成功"
  else
    fail=1
  fi
fi
exit $fail
