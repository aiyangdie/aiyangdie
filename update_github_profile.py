
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新GitHub个人主页README - 增强版
- 检查新项目
- 按Star排序
- 自动获取Star项目并总结
- 分析编码风格和个人特点
- 邮件通知更新状态
- GitHub热榜推送
- 自动更新README.md
"""

import os
import json
import smtplib
import requests
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
import os
GITHUB_USERNAME = "aiyangdie"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.qq.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
EMAIL_USER = os.getenv("EMAIL_USER", "aike1015@qq.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
STATE_FILE = "state.json"
README_FILE = "README.md"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def get_github_repos(username):
    """获取GitHub仓库列表"""
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取仓库列表失败: {response.status_code}")
        return []

def get_starred_repos(username):
    """获取Star的仓库列表"""
    url = f"https://api.github.com/users/{username}/starred?per_page=30"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取Star列表失败: {response.status_code}")
        return []

def get_readme(repo_full_name):
    """获取仓库README"""
    url = f"https://api.github.com/repos/{repo_full_name}/readme"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            import base64
            content = base64.b64decode(response.json()["content"]).decode("utf-8")
            return content
    except Exception as e:
        print(f"获取README失败: {e}")
    return ""

def summarize_readme(readme_content, repo_name):
    """简单总结README（避免调用外部API）"""
    if not readme_content:
        return f"{repo_name} - 有趣的项目"
    
    # 简单的关键词提取和总结
    keywords = ["🚀", "✨", "🔥", "💡", "🎯", "⚡", "🎉"]
    lines = readme_content.split("\n")
    summary = repo_name
    
    for line in lines[:20]:
        line = line.strip()
        if line and len(line) < 100 and not line.startswith("#"):
            summary = f"{repo_name} - {line}"
            break
    
    return summary

def sort_repos_by_stars(repos):
    """按Star数排序"""
    return sorted(repos, key=lambda x: x.get('stargazers_count', 0), reverse=True)

def get_repo_description(repo):
    """获取仓库描述"""
    desc = repo.get('description', '')
    if not desc:
        desc = repo.get('name', '')
    return desc

def get_github_hotlist():
    """获取GitHub热榜"""
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>1000",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        hotlist = []
        for item in data.get("items", []):
            hotlist.append({
                "name": item["full_name"],
                "url": item["html_url"],
                "description": item["description"] or "",
                "stars": item["stargazers_count"]
            })
        return hotlist
    except Exception as e:
        print(f"获取热榜失败: {e}")
        return []

def generate_readme(repos, starred_repos, username):
    """生成README.md内容"""
    
    # 生成README内容
    readme = f"""# 👋 你好，我是艾阳（{username}）

<p align="center">
  <img src="https://img.shields.io/badge/🎓-Graduated-blue?style=flat-square">
  <img src="https://img.shields.io/badge/💻-Full--Stack%20Developer-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/🚀-Open%20Source%20Enthusiast-orange?style=flat-square">
  <img src="https://img.shields.io/badge/🤖-AI%20Explorer-purple?style=flat-square">
</p>

<p align="center">
  <a href="mailto:aike1015@qq.com">📧 邮箱</a> ·
  <a href="https://aiyang.aike.ink/">🌐 博客</a> ·
  <a href="https://github.com/{username}">🐙 GitHub</a>
</p>

---

## 🎯 关于我

> 计算机相关专业（2024年6月毕业），热爱技术，追求卓越。能够独立完成从0到1的Web应用/工具型产品开发。

### 我的方向
- 🎨 **前端工程化** - React、TypeScript、组件化设计
- 📊 **数据采集与展示** - 爬虫、数据可视化、MySQL
- 🔗 **P2P/WebRTC** - 实时通信、文件传输、桌面共享
- 🤖 **AI应用原型** - Gemini API、大模型应用

### 我的理念
> 💡 注重用户体验、可维护性与可复用的组件化设计

---

## 🛠️ 技术栈

<p align="center">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=nodedotjs&logoColor=white">
  <img src="https://img.shields.io/badge/Express.js-404D59?style=for-the-badge">
  <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/Material--UI-0081CB?style=for-the-badge&logo=mui&logoColor=white">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
</p>

---

## 🚀 我的项目

"""
    
    # 我的项目（精选）
    my_projects = ['PhonePriceVista', 'ictupian', 'QuickCompress', '-ContractAI', 'spec-kit']
    for repo_name in my_projects:
        repo = next((r for r in repos if r['name'] == repo_name), None)
        if repo:
            readme += generate_project_section(repo)
    
    # 按Star排序的项目（仅显示自己的项目）
    sorted_repos = sort_repos_by_stars(repos)
    if sorted_repos:
        readme += """
## 🌟 我的项目（按Star排序）

> ⏰ 本列表每7天自动检查更新一次

"""
        for repo in sorted_repos:
            readme += generate_starred_project_section(repo)
    
    # Star的项目
    if starred_repos:
        readme += """
## ⭐ 我点的 Star · 我喜欢的项目

"""
        for repo in starred_repos[:20]:  # Limit to 20
            readme += generate_star_project_section(repo)
    
    # 全部项目
    readme += """
## 📁 全部项目

"""
    for repo in repos:
        readme += generate_all_project_section(repo)
    
    # GitHub统计
    readme += f"""
## 📊 GitHub 统计

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=radical" alt="GitHub Stats">
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=radical" alt="GitHub Streak">
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=radical" alt="Top Languages">
</p>

---

## 📫 联系我

<p align="center">
  <a href="mailto:aike1015@qq.com">
    <img src="https://img.shields.io/badge/📧-Email-blue?style=for-the-badge">
  </a>
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/🐙-GitHub-black?style=for-the-badge">
  </a>
  <a href="https://aiyang.aike.ink/">
    <img src="https://img.shields.io/badge/🌐-Blog-orange?style=for-the-badge">
  </a>
</p>

---

<p align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id={username}.{username}" alt="Visitor Badge">
</p>

<p align="center">
  <i>⭐ 如果我的项目对你有帮助，欢迎 Star！</i>
</p>

<p align="center">
  <i>由 AI 自动更新于 {datetime.now().strftime('%Y 年 %m 月 %d 日')}</i>
</p>

<p align="center">
  Made with ❤️ by 艾阳
</p>
"""
    
    return readme

def generate_project_section(repo):
    """生成项目部分"""
    name = repo['name']
    url = repo['html_url']
    desc = get_repo_description(repo)
    stars = repo.get('stargazers_count', 0)
    
    section = f"### 📦 {name}\n"
    section += f"> {desc}\n\n"
    if stars > 0:
        section += f"⭐ **{stars} Star**\n\n"
    section += f"[🔗 GitHub]({url})\n\n"
    section += "---\n\n"
    return section

def generate_starred_project_section(repo):
    """生成Star项目部分"""
    name = repo['name']
    url = repo['html_url']
    desc = get_repo_description(repo)
    stars = repo.get('stargazers_count', 0)
    
    section = f"### 💫 {name}\n"
    section += f"> {desc}\n\n"
    section += f"⭐ **{stars} Star**\n\n"
    section += f"[🔗 GitHub]({url})\n\n"
    section += "---\n\n"
    return section

def generate_star_project_section(repo):
    """生成我Star的项目部分"""
    name = repo['full_name']
    url = repo['html_url']
    desc = get_repo_description(repo)
    stars = repo.get('stargazers_count', 0)
    
    # 获取README并总结
    readme = get_readme(name)
    summary = summarize_readme(readme, name)
    
    section = f"### ⭐ {name}\n"
    section += f"> {summary}\n\n"
    section += f"⭐ **{stars} Star**\n\n"
    section += f"[🔗 GitHub]({url})\n\n"
    section += "---\n\n"
    return section

def generate_all_project_section(repo):
    """生成全部项目部分"""
    name = repo['name']
    url = repo['html_url']
    desc = get_repo_description(repo)
    
    section = f"### 📁 {name}\n"
    section += f"> {desc}\n\n"
    section += f"[🔗 GitHub]({url})\n\n"
    section += "---\n\n"
    return section

def send_email(subject, body):
    """发送邮件"""
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER
    msg["Subject"] = subject
    
    msg.attach(MIMEText(body, "plain", "utf-8"))
    
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("邮件发送成功")
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False

def main():
    """主函数"""
    username = GITHUB_USERNAME
    state = load_state()
    
    print("=" * 80)
    print("GitHub个人主页自动更新工具 - 增强版")
    print("=" * 80)
    print()
    
    # 获取仓库列表
    print(f"📥 获取 {username} 的仓库列表...")
    repos = get_github_repos(username)
    if not repos:
        print("❌ 获取仓库列表失败")
        return
    
    print(f"✅ 成功获取 {len(repos)} 个仓库")
    print()
    
    # 获取Star列表
    print(f"📥 获取 {username} 的Star列表...")
    starred_repos = get_starred_repos(username)
    print(f"✅ 成功获取 {len(starred_repos)} 个Star项目")
    print()
    
    # 生成README
    print("📝 生成 README.md...")
    readme_content = generate_readme(repos, starred_repos, username)
    
    # 保存README
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README.md 已保存到: {readme_path}")
    print()
    
    # 检查是否有变化
    print("🔍 检查是否有变化...")
    os.chdir(os.path.dirname(__file__))
    
    # Git操作
    git_status = os.popen('git status --porcelain').read().strip()
    readme_changed = 'README.md' in git_status
    
    # 获取热榜
    print("🔥 获取GitHub热榜...")
    hotlist = get_github_hotlist()
    hotlist_changed = False
    old_hotlist = state.get("hotlist", [])
    if hotlist != old_hotlist:
        hotlist_changed = True
        state["hotlist"] = hotlist
        print("✅ 热榜已更新")
    else:
        print("✅ 热榜无变化")
    
    # 准备邮件内容
    subject = "GitHub Profile Update Report"
    body = ""
    if readme_changed:
        body += "本次更新内容：\n- README已更新\n\n"
    else:
        body += "本次无更新\n\n"
    
    if hotlist_changed:
        body += "GitHub热榜更新：\n"
        for item in hotlist:
            body += f"- {item['name']} ({item['stars']}⭐) - {item['description']}\n"
            body += f"  {item['url']}\n"
    
    # 发送邮件
    print("📧 发送邮件通知...")
    if readme_changed or hotlist_changed:
        if send_email(subject, body):
            print("✅ 邮件发送成功")
    else:
        print("✅ 无更新，不发送邮件")
    
    # 提交和推送
    if git_status:
        print("📝 发现变化，提交更新...")
        os.system('git add README.md state.json')
        os.system(f'git commit -m "🔄 自动更新项目列表 - {datetime.now().strftime("%Y-%m-%d")}"')
        os.system('git push origin main')
        print("✅ 更新已推送到GitHub!")
    else:
        print("✅ 没有变化，无需更新")
    
    # 保存状态
    state["last_run"] = datetime.now().isoformat()
    save_state(state)
    
    print()
    print("=" * 80)
    print("✅ 更新完成!")
    print("=" * 80)

if __name__ == "__main__":
    main()

