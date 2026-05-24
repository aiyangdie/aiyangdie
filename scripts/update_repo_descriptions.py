#!/usr/bin/env python3
"""批量更新 GitHub 公开仓库 description 与用户 bio。"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request

USER = "aiyangdie"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESC_FILE = os.path.join(ROOT, "repo_descriptions.json")

BIO = (
    "全栈工程师 · AI 应用开发 · 45+ 开源项目 | "
    "WebRTC · LLM · React/Go/Python | 独立产品 0→1"
)


def api(method: str, url: str, token: str, data: dict | None = None) -> tuple[int, str]:
    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print("请设置环境变量 GITHUB_TOKEN")
        return 1

    descriptions = json.loads(open(DESC_FILE, encoding="utf-8").read())
    ok, fail = 0, 0

    # 更新 bio
    code, body = api("PATCH", "https://api.github.com/user", token, {"bio": BIO})
    if code == 200:
        print("OK  user bio")
    else:
        print(f"FAIL bio {code}: {body[:200]}")

    # 获取所有公开仓库
    repos: list[dict] = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=public"
        code, body = api("GET", url, token)
        if code != 200:
            print(f"FAIL list repos {code}")
            return 1
        batch = json.loads(body)
        if not batch:
            break
        repos.extend(batch)
        page += 1
        if len(batch) < 100:
            break

    for repo in repos:
        name = repo["name"]
        if name not in descriptions:
            continue
        desc = descriptions[name]
        if len(desc) > 350:
            desc = desc[:347] + "..."
        url = f"https://api.github.com/repos/{USER}/{name}"
        code, resp = api("PATCH", url, token, {"description": desc})
        if code == 200:
            ok += 1
            print(f"OK  {name}")
        else:
            fail += 1
            print(f"FAIL {name} {code}: {resp[:120]}")
        time.sleep(0.3)

    print(f"\n完成: {ok} 成功, {fail} 失败, 共 {len(repos)} 个公开仓库")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
