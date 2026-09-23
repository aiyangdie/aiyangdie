<!--
  aiyangdie · 艾阳
  本页人工维护。项目介绍基于仓库 README 与现有产品资料。
  保留 update_github_profile.py 的 HANDCRAFTED_README 保护开关。
-->

<div align="center">

<sub>MERCHANT SERVICES · PAYMENTS · WECHAT</sub>

<h1>你好，我是艾阳 👋</h1>

<p><strong>做商户业务，也把业务里的问题做成产品。</strong></p>

<p>商户申诉与合规 · 支付接入 · 授权登录 · AI 应用<br/>
接下来，也想继续做微信小程序。</p>

<a href="mailto:aike1015@qq.com"><img src="https://img.shields.io/badge/Email-aike1015%40qq.com-0969da?style=flat-square" alt="邮箱 aike1015@qq.com"/></a>
<a href="https://aike.ink/"><img src="https://img.shields.io/badge/Website-aike.ink-16803c?style=flat-square" alt="个人站点 aike.ink"/></a>
<a href="https://github.com/aiyangdie"><img src="https://img.shields.io/badge/GitHub-aiyangdie-24292f?style=flat-square&amp;logo=github" alt="GitHub aiyangdie"/></a>

<p>
<a href="#商户服务与产品">商户服务</a> ·
<a href="#微信小程序与-h5">微信生态</a> ·
<a href="#开源作品">开源作品</a> ·
<a href="#技术与工程">技术与工程</a> ·
<a href="#联系与合作">联系我</a>
</p>

</div>

---

我主要做**商户相关业务与系统开发**，关注商户申诉、投诉与工单运营、微信支付对接，以及多域名授权登录。围绕这些实际需求，我把 AI 辅助、业务后台和前端页面连接起来，做能够使用、维护和继续迭代的产品。

微信小程序是我想继续投入的方向。目前已经有小程序导航、微信小游戏和 H5 的项目实践，后续希望把这些经验用于商户服务。业余也会做浏览器游戏、局域网工具和自动化脚本，把有用的部分整理成开源项目。

## 商户服务与产品

<table>
<tr>
<td width="50%" valign="top">
<h3>🟢 商户申诉 AI</h3>
<p>围绕微信商户号申诉提供对话入口，结合知识库检索、材料整理与 AI 辅助，衔接申诉处理流程。</p>
<p><sub>申诉对话 · 知识库 / RAG · 多模型 · 材料辅助</sub></p>
<p><a href="https://appeal.aikex.ink/chat/"><strong>打开申诉助手 →</strong></a></p>
</td>
<td width="50%" valign="top">
<h3>🔵 OAuth 授权中控</h3>
<p>面向微信 / 支付宝授权接入，整理多域名回调、白名单与令牌处理，让业务系统复用授权能力。</p>
<p><sub>授权登录 · 多域名回调 · 白名单 · Token</sub></p>
<p><a href="https://open.aikex.ink/docs"><strong>查看接入文档 →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3>🟠 支付与商户后台</h3>
<p>项目经历包括微信支付、易支付、多通道接入，以及商城、工单运营和申诉全链路后台。</p>
<p><sub>商业项目 · 私有化交付 · 按业务需求协作</sub></p>
<p><a href="mailto:aike1015@qq.com"><strong>沟通业务需求 →</strong></a></p>
</td>
<td width="50%" valign="top">
<h3>🟣 SmsVerifyKit</h3>
<p>基于阿里云号码认证的开源短信验证码工具包，用于手机号登录、注册与绑手机，提供 PHP SDK、CLI 和 HTTP 网关。</p>
<p><sub>开源工具 · 多语言接入 · 配置与诊断脚本</sub></p>
<p><a href="https://github.com/aiyangdie/sms-verify-kit"><strong>查看源码</strong></a> · <a href="https://smsverify.aike.ink/"><strong>使用文档 →</strong></a></p>
</td>
</tr>
</table>

**业务里沉淀的能力：**申诉处理与投诉管理、知识库检索、AI 材料草稿、商户状态校验、工单流转、支付接入，以及 Agent Skills 和材料自动化。商业项目按约定私有交付，公开仓库沉淀可复用的工具与实践。

## 微信小程序与 H5

我希望逐步把商户服务延伸到微信端，让查询、提交材料和跟进进度更方便。**商户服务小程序属于后续探索方向**；下面是已有的微信生态项目与相关经历。

| 项目 / 经历 | 内容 | 入口 |
|:---|:---|:---|
| **KnowledgeLinkerX** | 微信 / QQ 小程序与公众号导航，图标、二维码和分类入口集中展示 | [仓库](https://github.com/aiyangdie/KnowledgeLinkerX) |
| **微信打地鼠** | 微信小程序实践：WXML / WXSS、音效、交互动画、计分与本地最高分记录 | [仓库](https://github.com/aiyangdie/wechat-whack-a-mole) |
| **WexOpen** | Windows 微信多开助手，自动识别路径，提供纯净版 / 商业版与自动构建发布 | [仓库](https://github.com/aiyangdie/WexOpen) · [下载](https://github.com/aiyangdie/WexOpen/releases) |
| **wechat-dual-open** | C 编写的 Windows 微信双开启动器 | [仓库](https://github.com/aiyangdie/wechat-dual-open) |
| **知识付费 H5** | 既有项目经历：小程序与 H5 共用后端，复用账号与业务接口 | [历史入口说明](#个人资料与原有入口) |

接下来想继续探索：商户自助服务入口、工单进度查询、业务通知，以及小程序 / H5 之间的会话衔接。具体功能随项目推进更新。

## 开源作品

从业务工具到游戏实验，这些仓库记录了我把想法做成可用程序的过程。

| 项目 | 做什么 | 技术 / 入口 |
|:---|:---|:---|
| **[mc-aikex-ink](https://github.com/aiyangdie/mc-aikex-ink)** | 浏览器体素沙盒：单机存档、联机房间、世界探索与管理面板 | Three.js · Node.js · WebSocket · [在线玩](https://mc.aikex.ink/) |
| **[LanShare](https://github.com/aiyangdie/lan-share)** | 手机与电脑在同一 Wi-Fi 下互传文件，提供 Windows 程序、Android 客户端与浏览器入口 | Node.js · Web UI · [项目主页](https://aiyangdie.github.io/lan-share/) |
| **[internal-chat](https://github.com/aiyangdie/internal-chat)** | 基于 WebRTC 的 P2P 文字聊天与文件传输，浏览器使用，无需注册账号 | Node.js · WebSocket · WebRTC |
| **[ictupian](https://github.com/aiyangdie/ictupian)** / **[QuickCompress](https://github.com/aiyangdie/QuickCompress)** | 浏览器本地图片压缩、批量处理与 ZIP 下载，支持 WebP / PNG / JPEG 等格式 | JavaScript · WebWorker · [在线工具](https://ic.aikex.ink/) |
| **[ContractAI](https://github.com/aiyangdie/-ContractAI)** | AI 辅助生成多语言合同草稿，提供模板表单、预览与导出 | React · TypeScript · Gemini |
| **[cursor-boost](https://github.com/aiyangdie/cursor-boost)** | 面向 Windows 的 Cursor 常见问题排查与修复工具 | Python |

### 小游戏与交互

除了体素沙盒和微信打地鼠，也做一些轻量的游戏与交互实验。

| 项目 | 内容 |
|:---|:---|
| [retro-games-hub](https://github.com/aiyangdie/retro-games-hub) | HTML5 Canvas 复古游戏合集 |
| [feiji](https://github.com/aiyangdie/feiji) | JavaScript / Canvas 太空射击小游戏 |
| [cf-game](https://github.com/aiyangdie/cf-game) | 射击游戏实验 |
| [wilderness-survival](https://github.com/aiyangdie/wilderness-survival) | 2D 荒野生存游戏 |

<details>
<summary><strong>更多工具、应用与学习项目</strong></summary>

| 方向 | 项目 |
|:---|:---|
| 桌面与系统工具 | [SysPulse](https://github.com/aiyangdie/SysPulse) · [ai_toolkit](https://github.com/aiyangdie/ai_toolkit) · [wifi-speed-test](https://github.com/aiyangdie/wifi-speed-test) · [train-monitor](https://github.com/aiyangdie/train-monitor) |
| 自动化与环境配置 | [env-installer](https://github.com/aiyangdie/env-installer) · [Computer-Auto-Installation-Tools](https://github.com/aiyangdie/Computer-Auto-Installation-Tools) · [DropIt-Advanced-Profiles](https://github.com/aiyangdie/DropIt-Advanced-Profiles) |
| 浏览器轻工具 | [Bookmark-Validator](https://github.com/aiyangdie/Bookmark-Validator) · [qrcode](https://github.com/aiyangdie/qrcode) · [Dynamic-Background-Navigator](https://github.com/aiyangdie/Dynamic-Background-Navigator) |
| 业务与数据展示 | [student-course-system](https://github.com/aiyangdie/student-course-system) · [PhonePriceVista](https://github.com/aiyangdie/PhonePriceVista) · [honor-zone](https://github.com/aiyangdie/honor-zone) |
| H5 与界面探索 | [心情驿站](https://github.com/aiyangdie/-Xin-Qing-Yi-Zhan) · [Mood-Station-H5-Version](https://github.com/aiyangdie/Mood-Station-H5-Version) · [CodeCraft-AI-](https://github.com/aiyangdie/CodeCraft-AI-) · [Zodiac-Showcase](https://github.com/aiyangdie/Zodiac-Showcase) · [NovaBrowser](https://github.com/aiyangdie/NovaBrowser) |
| 播放器实验 | [yourusername-pony-swf-player](https://github.com/aiyangdie/yourusername-pony-swf-player) |
| Fork · 学习与探索 | [spec-kit](https://github.com/aiyangdie/spec-kit) · [minimind](https://github.com/aiyangdie/minimind) · [MiniMind-in-Depth](https://github.com/aiyangdie/MiniMind-in-Depth) · [minimind-v](https://github.com/aiyangdie/minimind-v) · [file-transfer-go](https://github.com/aiyangdie/file-transfer-go) · [WeFlow](https://github.com/aiyangdie/WeFlow) · [tubatoolsPlugin](https://github.com/aiyangdie/tubatoolsPlugin) |

Fork 仓库单独标注，用于学习、实验与跟进上游项目。

[浏览当前公开仓库](https://github.com/aiyangdie?tab=repositories) · [原有项目目录存档](./projects-section.md) · [另一份个人主页仓库](https://github.com/aiyangdie/aiyangtongxue)

项目目录存档保留旧项目名称与介绍；其中的仓库数量、星标和可见性是历史记录，以当前仓库页面为准。

</details>

### 近期探索：Steam 新史低

一个正在本地开发的 Steam 价格查询与关注工具，目前用 **Python + SQLite** 验证产品流程：

- 支持中文名、英文名、AppID 和 Steam 商店链接搜索。
- 展示 Steam 当前地区价格；从 CheapShark 获取美元历史价，可选接入 ITAD 查询地区历史价。
- 验证关注游戏、目标价提醒、本地账号、评论和点赞等功能。
- 清楚区分当前价、第三方历史价与本机采样记录，标注来源和币种。

后续规划为 Laravel API、Vue 3 / TypeScript / Vite、PostgreSQL 和 Redis，逐步完善个人关注、社区实时更新、邮件 / 站内提醒、管理后台、测试与迁移。**当前仍是验证版，尚未在这里提供公开仓库或体验地址。**

## 技术与工程

| 场景 | 项目中使用与探索的技术 |
|:---|:---|
| Web 与交互 | React · Vue · TypeScript · JavaScript · HTML / CSS · Tailwind CSS · Material UI |
| 后端与业务接口 | Node.js / Express · PHP / ThinkPHP · Python |
| 微信与实时通信 | 微信小程序 · H5 · WebSocket · WebRTC · OAuth |
| 数据与 AI 应用 | MySQL · SQLite · Redis · 数据采集与可视化 · Gemini API · RAG · Agent Skills |
| 部署与自动化 | Linux · Nginx · PM2 · Docker · Git / GitHub Actions |
| 其他项目实践 | Three.js / Canvas · C 启动器 · Dart 工具应用 · Go / React 项目学习 |

<details>
<summary><strong>项目里的工程思路</strong></summary>

- **商户申诉：**围绕“检索知识库 → 生成材料草稿 → 校验商户状态 → 工单流转”组织业务模块。
- **授权与支付：**关注 OAuth 状态校验、回调白名单、会话边界和支付接入；密钥与商业源码按项目约定管理。
- **小程序与 H5：**由后端处理平台登录凭据并建立业务会话，复用账号和业务接口。
- **联机游戏：**由服务端控制已实现的战斗与房间状态，客户端负责交互与渲染；具体能力和限制见游戏仓库。
- **交付与维护：**关注用户体验、可维护性、组件复用、部署与自动化；商业交付与开源工具分别管理。

</details>

## 个人资料与原有入口

艾阳 / **aiyangdie**。计算机相关专业背景，2024 年 6 月毕业，持续实践全栈开发、AI SaaS、微信与支付生态，以及 Web 应用 / 工具产品从 0 到 1 的开发与部署。

| 信息 | 地址 |
|:---|:---|
| GitHub | [github.com/aiyangdie](https://github.com/aiyangdie) |
| 联系邮箱 | [aike1015@qq.com](mailto:aike1015@qq.com) |
| 个人站点 | [aike.ink](https://aike.ink/) |
| 商户申诉助手 | [appeal.aikex.ink/chat](https://appeal.aikex.ink/chat/) |
| 授权中控文档 | [open.aikex.ink/docs](https://open.aikex.ink/docs) |
| 号码认证工具文档 | [smsverify.aike.ink](https://smsverify.aike.ink/) |
| 图片压缩工具 | [ic.aikex.ink](https://ic.aikex.ink/) |
| 体素沙盒 | [mc.aikex.ink](https://mc.aikex.ink/) |

<details>
<summary><strong>保留的博客、小程序导航与 H5 入口</strong></summary>

- 个人博客：[aiyang.aike.ink](https://aiyang.aike.ink/)。
- 小程序导航旧入口：[keji.aikex.ink](https://keji.aikex.ink/)，项目代码仍可在 [KnowledgeLinkerX](https://github.com/aiyangdie/KnowledgeLinkerX) 查看。
- 知识付费 H5 历史入口：[h5.aikex.ink](https://h5.aikex.ink/)。

2026-09-23 核对：aike.ink 当前展示品牌视觉设计与创意服务；h5.aikex.ink 当前展示学习记录。博客与导航旧域名本次未通过 HTTPS 连通检查。保留上述地址和项目经历，实际页面内容以站点当前展示为准。

</details>

<details>
<summary><strong>GitHub 活跃度与语言分布</strong></summary>

<p align="center">
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=aiyangdie&amp;theme=github_dark" width="48%" alt="aiyangdie 的 GitHub 活跃度统计"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=aiyangdie&amp;theme=github_dark" width="48%" alt="公开仓库的语言分布"/>
</p>
<p align="center">
<img src="https://streak-stats.demolab.com?user=aiyangdie&amp;theme=github-dark-blue&amp;hide_border=true&amp;background=0D1117&amp;ring=07C160&amp;fire=3FB950&amp;currStreakLabel=07C160" width="90%" alt="GitHub 连续贡献记录"/>
</p>
<p align="center">
<img src="https://komarev.com/ghpvc/?username=aiyangdie&amp;label=Profile%20views&amp;color=238636&amp;style=flat-square" alt="主页访问计数"/>
</p>

统计由第三方服务生成，以 GitHub 公开记录为基础。

</details>

---

## 联系与合作

欢迎交流 **商户申诉与合规系统、微信支付 / 易支付接入、OAuth 授权、业务后台、AI 辅助工具**，也欢迎一起讨论微信小程序、H5 和小游戏的实际需求。

最方便的联系方式是 **[aike1015@qq.com](mailto:aike1015@qq.com)**。介绍一下你的业务场景、现在遇到的问题和希望实现的功能，就可以开始沟通。

<p align="center">
<sub>业务里发现问题，项目里积累经验，开源里分享工具。</sub>
</p>
