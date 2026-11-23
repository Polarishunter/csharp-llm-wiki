// 以 jsdom 載入簡報，模擬鍵盤／按鈕／網址 hash 操作，檢查切換是否正確
const { JSDOM } = require("jsdom");
const fs = require("fs");
const path = process.argv[2];
const html = fs.readFileSync(path, "utf8");
let pass = 0, fail = 0;
function check(name, cond) { if (cond) { pass++; console.log("  ✓", name); } else { fail++; console.log("  ✗", name); } }
function load(hash) {
  const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/slides/index.html" + (hash || "") });
  return dom.window;
}
let w = load();
const d = w.document;
const total = d.querySelectorAll(".slide").length;
const active = () => [...d.querySelectorAll(".slide")].findIndex(s => s.classList.contains("active"));
const key = k => d.dispatchEvent(new w.KeyboardEvent("keydown", { key: k, bubbles: true }));
check(`共 ${total} 張投影片，初始顯示第 1 張`, active() === 0 && d.querySelectorAll(".slide.active").length === 1);
key("ArrowRight"); check("→ 切到第 2 張", active() === 1);
key(" "); check("空白鍵切到第 3 張", active() === 2);
key("ArrowLeft"); check("← 回到第 2 張", active() === 1);
d.getElementById("next").click(); check("▶ 按鈕切到第 3 張", active() === 2);
d.getElementById("prev").click(); check("◀ 按鈕回到第 2 張", active() === 1);
key("End"); check("End 跳到最後一張", active() === total - 1);
key("ArrowRight"); check("最後一張再按 → 不會超出範圍", active() === total - 1);
key("Home"); key("ArrowLeft"); check("第一張再按 ← 不會小於 1", active() === 0);
check("頁碼顯示正確", d.getElementById("count").textContent === `1 / ${total}`);
w = load("#16"); 
check("網址 #16 直接開啟第 16 張", [...w.document.querySelectorAll(".slide")].findIndex(s => s.classList.contains("active")) === 15);
check("每張都有 Wiki 對應標示", [...d.querySelectorAll(".slide")].every(s => s.querySelector(".meta a")));
const codes = [...d.querySelectorAll("pre code")];
check(`程式碼上色後文字不變（${codes.length} 個區塊）`, codes.every(c => !c.textContent.includes("&lt;") && !c.textContent.includes("<span")));
check("第 8 頁 '<' 正確顯示", d.querySelectorAll(".slide")[7].querySelector("pre").textContent.includes("tempInCelsius < 20.0"));
console.log(`\n結果：${pass} 通過，${fail} 失敗`);
process.exit(fail ? 1 : 0);
