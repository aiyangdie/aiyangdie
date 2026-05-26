"""组装完整 Profile README"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
head = (ROOT / "README.head.md").read_text(encoding="utf-8") if (ROOT / "README.head.md").exists() else None

if head is None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    marker_start = "## 🚀 最近交付"
    marker_end = "## 🛠️ 技术栈"
    head = readme.split(marker_start)[0].rstrip()
    tail = readme.split(marker_end)[1]
else:
    tail = (ROOT / "README.tail.md").read_text(encoding="utf-8")

projects = (ROOT / "projects-section.md").read_text(encoding="utf-8").strip()
tail_part = (ROOT / "README.md").read_text(encoding="utf-8").split("## 🛠️ 技术栈", 1)[1]

out = f"{head.rstrip()}\n\n---\n\n{projects}\n\n---\n\n## 🛠️ 技术栈{tail_part}"
(ROOT / "README.md").write_text(out, encoding="utf-8")
print("README.md updated")
