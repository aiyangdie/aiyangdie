"""从 repos-all.json 生成 Profile README 精选项目区块"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "repos-all.json").read_text(encoding="utf-8-sig"))

DESC_OVERRIDE = {
    "cf-game": "穿越火线风格小游戏 · GitHub Pages 在线游玩",
    "ecommerce-platform": "电商平台全栈 · Spring Boot + Vue3 + uni-app",
    "honor-zone": "王者荣耀战力查询 + 战区排行榜演示 · Flask + MySQL + Redis",
    "wilderness-survival": "2D 荒野生存游戏 · JavaScript Canvas",
    "file-transfer-go": "端到端 WebRTC 传文件 / 聊天 / 投屏 · Go + React",
    "get_jobs": "AI 求职自动投递 · Java · Selenium",
    "minimind": "26M 参数大语言模型 · 从零训练",
    "minimind-v": "26M 多模态 VLM · 从零训练",
    "MiniMind-in-Depth": "MiniMind 深度解析与实验",
    "InfiniteTalk": "无限时长数字人视频生成",
    "xiaohongshu-mcp": "小红书 MCP 自动化服务",
    "WeixinBot": "微信机器人框架",
    "openhanako": "个人 AI Agent 助手",
    "WeFlow": "微信聊天记录导出与年度报告",
    "spec-kit": "规范驱动开发工具集 · GitHub 官方 Fork",
}


def clean_desc(repo: dict) -> str:
    name = repo["name"]
    raw = (repo.get("desc") or "").strip()
    if name in DESC_OVERRIDE:
        return DESC_OVERRIDE[name]
    if not raw or raw.count("?") > 4:
        return DESC_OVERRIDE.get(name, "开源项目 · 持续维护中")
    # 取描述第一片段，去掉 emoji 后过长截断
    part = raw.split("|")[0].strip()
    if len(part) > 56:
        part = part[:53] + "…"
    return part


def lang(repo: dict) -> str:
    return repo.get("lang") or "—"


def link(repo: dict) -> str:
    name = repo["name"]
    return f"[**{name}**]({repo['url']})"


def star_badge(n: int) -> str:
    return f" ⭐{n}" if n else ""


def table_rows(repos: list[dict]) -> str:
    lines = [
        "| 项目 | 简介 | 技术 |",
        "|------|------|------|",
    ]
    for r in repos:
        fork = " `fork`" if r.get("fork") else ""
        lines.append(
            f"| {link(r)}{star_badge(r.get('stars', 0))}{fork} | {clean_desc(r)} | `{lang(r)}` |"
        )
    return "\n".join(lines)


original = [r for r in DATA if not r["fork"]]
forks = [r for r in DATA if r["fork"]]

# 原创：星标优先，其次名称
original.sort(key=lambda r: (-r.get("stars", 0), r["name"].lower()))
forks.sort(key=lambda r: r["name"].lower())

section = f"""## 🔥 精选项目

> 共 **{len(DATA)}** 个公开仓库 · 原创 **{len(original)}** · Fork **{len(forks)}** · 持续更新中

### 🏆 原创开源（{len(original)}）

{table_rows(original)}

### 🔗 Fork · 学习共建（{len(forks)}）

{table_rows(forks)}
"""

(ROOT / "projects-section.md").write_text(section, encoding="utf-8")
print("OK", len(DATA), len(original), len(forks))
