#!/usr/bin/env python3
"""LLM Wiki 健康檢查（依 AGENTS.md §7）。用法：python3 tools/lint.py"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SLIDES = ROOT / "slides" / "index.html"
EXAMPLES = ROOT / "tools" / "examples"

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


# ---------- 讀取 raw ----------
raw_status = {}
for f in sorted(RAW.glob("*.md")):
    fm = frontmatter(f.read_text(encoding="utf-8"))
    if not fm or "id" not in fm:
        err(f"[raw] {f.name}: 缺少 frontmatter 或 id")
        continue
    for key in ("title", "url", "fetched", "page_updated", "status"):
        if key not in fm:
            err(f"[raw] {f.name}: 缺少欄位 {key}")
    raw_status[fm["id"]] = fm.get("status", "")

ok_sources = [k for k, v in raw_status.items() if v == "ok"]
print(f"raw 來源：{len(raw_status)} 篇（可用 {len(ok_sources)}，rejected {len(raw_status) - len(ok_sources)}）")
if len(ok_sources) < 5:
    err(f"[raw] 可用來源只有 {len(ok_sources)} 篇，作業要求至少 5 篇")

# ---------- 讀取 wiki ----------
pages = {p.stem: p for p in WIKI.rglob("*.md")}
inbound = {name: set() for name in pages}
for name, path in pages.items():
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if not fm:
        err(f"[wiki] {name}: 缺少 frontmatter")
        continue
    for key in ("title", "sources", "related"):
        if key not in fm:
            err(f"[wiki] {name}: frontmatter 缺少 {key}")
    body = text.split("---", 2)[2]
    # 1) 連結
    for link in set(re.findall(r"\[\[([^\]]+)\]\]", body)):
        if link not in pages:
            err(f"[wiki] {name}: 斷鏈 [[{link}]]")
        elif link != name:
            inbound[link].add(name)
    for rel in re.findall(r"[\w-]+", fm.get("related", "")):
        if rel not in pages:
            err(f"[wiki] {name}: related 指向不存在的條目 {rel}")
    # 2) 來源標註
    cited = set(re.findall(r"〔(S\d+)〕", body))
    declared = set(re.findall(r"S\d+", fm.get("sources", "")))
    for c in cited | declared:
        if c not in raw_status:
            err(f"[wiki] {name}: 引用不存在的來源 {c}")
        elif raw_status[c] != "ok":
            err(f"[wiki] {name}: 引用了狀態為 {raw_status[c]} 的來源 {c}")
    for c in cited - declared:
        err(f"[wiki] {name}: 內文引用 {c} 但 frontmatter sources 未列出")
    # index、sources 與 queries/ 下的查詢結果以表格列出來源 ID，只要求 frontmatter 宣告
    is_meta = name in ("index", "sources") or path.parent.name == "queries"
    if is_meta and name != "index" and not declared:
        err(f"[wiki] {name}: frontmatter 未宣告任何來源")
    if not is_meta and not cited:
        err(f"[wiki] {name}: 內文沒有任何〔Sxx〕來源標註")

# 3) 孤兒頁
for name, src in inbound.items():
    if name != "index" and not src:
        err(f"[wiki] {name}: 孤兒條目（沒有任何條目連入）")

# 4) index 是否列出全部條目
index_text = pages["index"].read_text(encoding="utf-8")
for name in pages:
    if name != "index" and f"[[{name}]]" not in index_text:
        err(f"[index] 未列出條目 {name}")

print(f"wiki 條目：{len(pages)} 個")

# ---------- 簡報 ----------
s = SLIDES.read_text(encoding="utf-8")
slides = re.findall(r'<section class="slide[^"]*" data-wiki="([^"]+)">(.*?)</section>', s, re.S)
print(f"投影片：{len(slides)} 張")


def norm(code):
    # 去除每行前後空白再比對：範例檔中的方法位於 class 內，縮排深度與簡報不同
    return "\n".join(line.strip() for line in code.strip("\n").splitlines())


code_count = 0
for idx, (w, body) in enumerate(slides, 1):
    if w not in pages:
        err(f"[slides] 第 {idx} 頁 data-wiki=\"{w}\" 不存在於 wiki")
        continue
    wiki_text = pages[w].read_text(encoding="utf-8")
    for ex, code in re.findall(r'<pre data-example="([^"]+)"><code>(.*?)</code></pre>', body, re.S):
        code_count += 1
        code = norm(html.unescape(code))
        exfile = EXAMPLES / ex
        if not exfile.exists():
            err(f"[slides] 第 {idx} 頁：範例檔 {ex} 不存在")
        elif code not in norm(exfile.read_text(encoding="utf-8")):
            err(f"[slides] 第 {idx} 頁：程式碼與 {ex} 不一致")
        if code not in norm(wiki_text):
            err(f"[slides] 第 {idx} 頁：程式碼不在對應條目 {w}.md 中（簡報內容超出 Wiki）")
    if "<pre" in body and "data-example" not in body:
        err(f"[slides] 第 {idx} 頁：有程式碼區塊但未標 data-example")
print(f"簡報程式碼區塊：{code_count} 個")

# ---------- 結果 ----------
print()
if errors:
    print(f"發現 {len(errors)} 個問題：")
    for e in errors:
        print("  ✗", e)
    sys.exit(1)
print("✓ Lint 全部通過")
