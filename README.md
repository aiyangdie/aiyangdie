<p align="center"><img src="assets/banner.jpg" alt="艾阳 · aiyangdie" width="100%"></p>

<h1 align="center">艾阳 · aiyangdie</h1>

<p align="center">
<b>商户合规</b> ｜ 支付与微信生态 ｜ 全栈开发 ｜ Windows 工具 ｜ AI 应用
</p>

<p align="center">
<a href="#主线商户合规">商户合规</a> ·
<a href="#发展历程">发展历程</a> ·
<a href="#代表项目">代表项目</a> ·
<a href="#全部公开项目">全部公开项目</a> ·
<a href="#在线体验">在线体验</a> ·
<a href="mailto:aike1015@qq.com">邮箱</a>
</p>

<p align="center">
<sub>84 个仓库（52 公开 / 32 私有）· 74 ★ · 13 个在线站点 · 自 2025 年 4 月起</sub>
</p>

---

## 主线 · 商户合规

我做的是**商户侧的合规与技术落地**：商家在平台上遇到处罚、申诉、资质、收款问题时，把散乱的材料整理成能提交的东西，把流程做成能复用的系统。

| 能力 | 具体做什么 | 对应实现 |
|---|---|---|
| **申诉材料梳理** | 按平台要求拆解违规类型，把对话记录、订单凭证、整改说明归成结构化材料与说明文 | [merchant-appeal](https://github.com/aiyangdie/merchant-appeal)（公开）＋ 私有工单台 |
| **平台规则对照** | 把微信、支付机构、电商平台的规则条款整理成可检索的知识库，遇到具体问题能定位到条款 | 私有合规知识库 |
| **问题排查** | 针对交易、投诉、扣款等具体异常做链路排查，定位是资质、通道还是操作环节的问题 | 私有投诉排查工具 |
| **资质与支付接入** | 商户资质材料整理、号码认证、收单通道对接与联调 | [sms-verify-kit](https://github.com/aiyangdie/sms-verify-kit)、[ds_shop](https://github.com/aiyangdie/ds_shop)、[independent-mall](https://github.com/aiyangdie/independent-mall) |
| **流程系统化** | 把一次次的材料整理做成可复用的后台：工单流转、模板生成、规则沉淀 | [merchant-appeal](https://github.com/aiyangdie/merchant-appeal) 的对话收集与规则库 |

**边界说明**：我提供的是材料整理、规则梳理与技术实现，材料由商户自行提交，处理结果由平台判定，不对申诉结果作承诺。

---

## 发展历程

按仓库真实创建时间归纳，不是事后编的年表：

| 时间 | 阶段 | 做了什么 |
|---|---|---|
| **2025.04** | 起步 | 建号第一周上线微信小程序打地鼠、书签死链检测、贪吃蛇、图片压缩；同期起了一批私有项目打底 |
| **2025.05–06** | 前端工具铺开 | 小程序导航页、手机比价、太空战机、星座展示、心情驿站、装机工具、二维码、DropIt 规则集 |
| **2025.08–09** | 转头啃底层 | Fork minimind 系列，从预训练、SFT、LoRA 读到 MoE 与 RoPE，自己写 12 篇源码精读笔记；同期做端到端文件传输 |
| **2025.12** | AI 应用落地 | 多语言合同生成器，6 类模板 × 11 种语言，接 Gemini 走完整闭环 |
| **2026.01–02** | 转向商户侧 | 先把规范驱动开发流程引进来；**2 月 11 日 merchant-appeal 上线**，商户申诉正式成为主线 |
| **2026.03–04** | 合规体系铺开 | 私有线密集建设：工单工作台、投诉排查工具、商户知识库、申诉系统多个版本并行迭代 |
| **2026.05–07** | 工具与运维期 | SysPulse 硬件监控、微信多开、网页版 CF、荒野生存、Cursor 修复、短信验证套件、局域网互传、Flutter 工具箱 |
| **2026.09–11** | 系统级项目 | 体素沙盒联机版、霓虹卡丁车、紫微排盘引擎、云栈商城、独立商城、仿抖音 App、ESP32 小智板工具包 |

一条看得出来的线：**先做小工具练手 → 补底层原理 → 回到自己真正面对的商户问题 → 越做越重。**

---

## 怎么合作

| 环节 | 内容 |
|---|---|
| **确认范围** | 明确功能、对接条件、验收标准；能做的说能做，做不了的直说 |
| **开发与验证** | 按约定开发，接口联调与测试，过程留待确认清单 |
| **部署与交接** | 交付部署说明、验收清单与维护记录，代码可交接 |

合作方向：商户合规材料与系统、小程序与公众号、Web 系统与后台、支付与接口对接、桌面工具与内部效率工具。

---

## 代表项目

<table>
<tr>
<td width="33%" align="center">
<a href="https://github.com/aiyangdie/merchant-appeal"><img src="https://raw.githubusercontent.com/aiyangdie/merchant-appeal/main/assets/covers/01-merchant-appeal.jpg" width="100%"></a>
<br><b>商户申诉平台</b><br><sub>对话收集信息，生成申诉文案与材料清单</sub>
</td>
<td width="33%" align="center">
<a href="https://github.com/aiyangdie/lan-share"><img src="https://raw.githubusercontent.com/aiyangdie/lan-share/main/assets/covers/17-lan-share.jpg" width="100%"></a>
<br><b>LanShare 局域网互传</b><br><sub>手机电脑双向传，数据不出本地网络</sub>
</td>
<td width="33%" align="center">
<a href="https://github.com/aiyangdie/mc-aikex-ink"><img src="https://raw.githubusercontent.com/aiyangdie/mc-aikex-ink/main/assets/covers/10-mc-aikex-ink.jpg" width="100%"></a>
<br><b>像素方块世界</b><br><sub>Three.js 体素沙盒，支持联机与末地</sub>
</td>
</tr>
<tr>
<td align="center">
<a href="https://github.com/aiyangdie/ds_shop"><img src="https://raw.githubusercontent.com/aiyangdie/ds_shop/main/assets/covers/03-ds_shop.jpg" width="100%"></a>
<br><b>云栈商城</b><br><sub>自助下单、卡密发货、分站与会员</sub>
</td>
<td align="center">
<a href="https://github.com/aiyangdie/ziwei-chat"><img src="https://raw.githubusercontent.com/aiyangdie/ziwei-chat/main/assets/covers/23-ziwei-chat.jpg" width="100%"></a>
<br><b>紫微斗数排盘</b><br><sub>真太阳时校正、夏令时、十二神煞</sub>
</td>
<td align="center">
<a href="https://github.com/aiyangdie/cursor-boost"><img src="https://raw.githubusercontent.com/aiyangdie/cursor-boost/main/assets/covers/27-cursor-boost.jpg" width="100%"></a>
<br><b>Cursor 故障修复</b><br><sub>编辑器挂了也能独立运行，一键修</sub>
</td>
</tr>
<tr>
<td align="center">
<a href="https://github.com/aiyangdie/WexOpen"><img src="https://raw.githubusercontent.com/aiyangdie/WexOpen/main/assets/covers/05-WexOpen.jpg" width="100%"></a>
<br><b>微信多开助手</b><br><sub>免 Python 单文件，CI 自动发布</sub>
</td>
<td align="center">
<a href="https://github.com/aiyangdie/douyin-app"><img src="https://raw.githubusercontent.com/aiyangdie/douyin-app/main/assets/covers/16-douyin-app.jpg" width="100%"></a>
<br><b>仿抖音短视频</b><br><sub>Expo + RN，离线可用，零网络依赖</sub>
</td>
<td align="center">
<a href="https://github.com/aiyangdie/sms-verify-kit"><img src="https://raw.githubusercontent.com/aiyangdie/sms-verify-kit/main/assets/covers/04-sms-verify-kit.jpg" width="100%"></a>
<br><b>短信验证码套件</b><br><sub>阿里云号码认证，PHP SDK + 网关</sub>
</td>
</tr>
</table>

---

## 全部公开项目

### 支付 · 商户 · 微信生态

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [merchant-appeal](https://github.com/aiyangdie/merchant-appeal) | 商户申诉与投诉管理平台，含规则库进化与 AI 中枢 | React · Node · MySQL | — |
| [sms-verify-kit](https://github.com/aiyangdie/sms-verify-kit) | 阿里云号码认证短信验证码套件，CLI + SDK + HTTP 网关 | PHP | — |
| [ds_shop](https://github.com/aiyangdie/ds_shop) | 云栈商城：自助下单、卡密发货、分站、会员 | PHP · MySQL | — |
| [independent-mall](https://github.com/aiyangdie/independent-mall) | 通用商城社区版，console 命令体系，默认本地支付通道 | PHP 8.2+ | — |
| [WexOpen](https://github.com/aiyangdie/WexOpen) | Windows 微信多开，免 Python 运行，含安装版与便携版 | Python · PyInstaller | — |
| [wechat-dual-open](https://github.com/aiyangdie/wechat-dual-open) | 微信双开启动器，纯 Win32 C 实现，单文件约 155KB | C | — |
| [wechat-whack-a-mole](https://github.com/aiyangdie/wechat-whack-a-mole) | 微信小程序打地鼠，3×3 洞、难度曲线、本地最高分 | 小程序原生 | [玩一局](https://mole.aikex.ink) |
| [KnowledgeLinkerX](https://github.com/aiyangdie/KnowledgeLinkerX) | 小程序与公众号导航聚合页，扫码直达 | HTML · CSS | [打开](https://knowledge.aikex.ink) |

### AI 与大模型应用

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [-ContractAI](https://github.com/aiyangdie/-ContractAI) | 多语言合同生成器，6 类模板 × 11 种语言 | React 19 · TS · Gemini | — |
| [CodeCraft-AI-](https://github.com/aiyangdie/CodeCraft-AI-) | AI 助手展示页，粒子背景与工具集，零框架零构建 | HTML · CSS · JS | [打开](https://codecraft.aikex.ink) |
| [ziwei-chat](https://github.com/aiyangdie/ziwei-chat) | 紫微斗数排盘引擎，含真太阳时、夏令时与回归测试 | TS | — |
| [ziwei-ai](https://github.com/aiyangdie/ziwei-ai) | 星言紫微 AI 助手，AI 不通时降级为本地速读 | TS · Cloudflare | [打开](https://aiyangdie.github.io/ziwei-ai/) |
| [xiaozhi-kit](https://github.com/aiyangdie/xiaozhi-kit) | ESP32 小智板工具包：JSON CLI + Web 控制台 + Skill | Python | — |

### 游戏与互动娱乐

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [mc-aikex-ink](https://github.com/aiyangdie/mc-aikex-ink) | 开源体素沙盒：存档、联机房间、末地、管理面板 | Three.js · Node · ws | [进入](https://mc.aikex.ink) |
| [cf-game](https://github.com/aiyangdie/cf-game) | 网页第一人称射击，波次敌人、三把武器、军械库 | Three.js | [开打](https://aiyangdie.github.io/cf-game/) |
| [neon-kart](https://github.com/aiyangdie/neon-kart) | 霓虹卡丁车，网页版 + Windows 安装包，支持联机对战 | HTML · JS | [开跑](https://aiyangdie.github.io/neon-kart/) |
| [wilderness-survival](https://github.com/aiyangdie/wilderness-survival) | 荒野生存，2D 稳定版与 3D 版并存 | JS · Canvas | [进入](https://aiyangdie.github.io/wilderness-survival/) |
| [feiji](https://github.com/aiyangdie/feiji) | 太空战机，4 类敌机、程序化音效、动态难度 | Canvas | [开玩](https://feiji.aikex.ink) |
| [retro-games-hub](https://github.com/aiyangdie/retro-games-hub) | 复古贪吃蛇，面向对象封装，移动端虚拟方向键 | Canvas | [开玩](https://games.aikex.ink) |

### Windows 工具与 IT 运维

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [lan-share](https://github.com/aiyangdie/lan-share) | 局域网互传：Windows 客户端 + Android APK + iPhone PWA | Node · WebView | [试用](https://aiyangdie.github.io/lan-share/) |
| [SysPulse](https://github.com/aiyangdie/SysPulse) | 终端硬件监控，6 大面板、0–100 综合评分 | Python · Rich | — |
| [cursor-boost](https://github.com/aiyangdie/cursor-boost) | Cursor 故障诊断与一键修复，独立于编辑器运行 | Python · PowerShell | — |
| [train-monitor](https://github.com/aiyangdie/train-monitor) | 训练实时监控，零依赖 Tkinter，GPU 指标与 checkpoint 扫描 | Python | — |
| [Computer-Auto-Installation-Tools](https://github.com/aiyangdie/Computer-Auto-Installation-Tools) | 四合一装机工具：BAT 合并、WinGet、静默安装、下载管理 | Batch · Python | — |
| [DropIt-Advanced-Profiles](https://github.com/aiyangdie/DropIt-Advanced-Profiles) | DropIt 分类规则集，100+ 条规则覆盖 15 大类文件 | INI · HTML | [下载](https://dropit.aikex.ink) |
| [wifi-speed-test](https://github.com/aiyangdie/wifi-speed-test) | WiFi 名称、信号、IP 与网关，一键测延迟上下行 | Python · Tkinter | — |
| [yourusername-pony-swf-player](https://github.com/aiyangdie/yourusername-pony-swf-player) | SWF 播放器，系统播放器失败时自动切 Ruffle | Python | — |
| [honor-zone](https://github.com/aiyangdie/honor-zone) | 王者战力查询与战区排行榜演示，主备数据源自动切换 | Flask · MySQL · Redis | — |

### 效率工具与展示页

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [QuickCompress](https://github.com/aiyangdie/QuickCompress) | 纯前端批量图片压缩，图片不上传服务器 | browser-image-compression | [使用](https://compress.aikex.ink) |
| [ictupian](https://github.com/aiyangdie/ictupian) | 智能压缩，WebWorker 独立线程 + 压缩报告 | WebWorker | [使用](https://img.aikex.ink) |
| [qrcode](https://github.com/aiyangdie/qrcode) | 纯前端二维码生成，纠错等级 H，可下载 PNG | QRCode.js | [使用](https://qr.aikex.ink) |
| [Bookmark-Validator](https://github.com/aiyangdie/Bookmark-Validator) | 书签批量死链检测，可一键清理并导出 | DOMParser · Fetch | [使用](https://bookmark.aikex.ink) |
| [Dynamic-Background-Navigator](https://github.com/aiyangdie/Dynamic-Background-Navigator) | 网址导航双版本：动态背景版与拟态版 | HTML · CSS | — |
| [Zodiac-Showcase](https://github.com/aiyangdie/Zodiac-Showcase) | 十二星座互动展示页，四元素分类与三层动态背景 | HTML · CSS · JS | [打开](https://zodiac.aikex.ink) |
| [PhonePriceVista](https://github.com/aiyangdie/PhonePriceVista) | 手机比价全栈应用，参数与价格筛选、爬虫同步 | React · TS · Express · MySQL | [打开](https://aiyangdie.github.io/PhonePriceVista/) |
| [student-course-system](https://github.com/aiyangdie/student-course-system) | 选课管理系统，适合课程设计与毕业设计演示 | Spring Boot · Vue 2 | — |

### 局域网与 P2P 通信

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [internal-chat](https://github.com/aiyangdie/internal-chat) | 局域网 P2P 聊天与文件传输，数据点对点直连 | WebRTC · WebSocket | — |
| [file-transfer-go](https://github.com/aiyangdie/file-transfer-go) | 端到端文件传输，多文件、屏幕共享、断点续传（Fork） | Next.js · Go · WebRTC | — |

### 移动端 App

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [douyin-app](https://github.com/aiyangdie/douyin-app) | 仿抖音短视频 App，离线优先、全本地素材，附内容后台 | Expo · React Native | — |
| [ai_toolkit](https://github.com/aiyangdie/ai_toolkit) | 轻量工具箱 App，计算、换算、倒计时、密码、笔记等 | Flutter · Hive | — |

### 心理健康轻工具

| 项目 | 说明 | 技术 | 在线 |
|---|---|---|---|
| [-Xin-Qing-Yi-Zhan](https://github.com/aiyangdie/-Xin-Qing-Yi-Zhan) | 心情驿站 React 版，5 套主题、正能量语录、心情记录 | React · Tailwind | [打开](https://xinqing.aikex.ink) |
| [Mood-Station-H5-Version](https://github.com/aiyangdie/Mood-Station-H5-Version) | 心情驿站 H5 版，纯静态零依赖，主题记忆持久化 | HTML · CSS · JS | [打开](https://mood.aikex.ink) |

### 学习与参考（Fork）

| 项目 | 说明 | 技术 |
|---|---|---|
| [minimind](https://github.com/aiyangdie/minimind) | 超小语言模型从零训练，覆盖预训练到 RLHF 全链路 | Python |
| [minimind-v](https://github.com/aiyangdie/minimind-v) | MiniMind 的多模态视觉语言扩展 | Python |
| [MiniMind-in-Depth](https://github.com/aiyangdie/MiniMind-in-Depth) | MiniMind 源码逐行精读笔记，12 篇教程 | Markdown |
| [spec-kit](https://github.com/aiyangdie/spec-kit) | 规范驱动开发工具集，为 AI 编码 Agent 提供流程与模板 | Python |
| [tubatoolsPlugin](https://github.com/aiyangdie/tubatoolsPlugin) | 图吧工具箱社区插件库，含插件审核与病毒扫描 | Python · YARA |

### 占位仓库

| 项目 | 说明 |
|---|---|
| [env-installer](https://github.com/aiyangdie/env-installer) | 环境安装器概念位，同类能力已由 Computer-Auto-Installation-Tools 落地 |
| [NovaBrowser](https://github.com/aiyangdie/NovaBrowser) | 隐私浏览器概念位，暂无实现 |
| [aiyangtongxue](https://github.com/aiyangdie/aiyangtongxue) | 旧账号名留下的 Profile 位 |

> 另有 32 个私有仓库在维护，涉及商户工单台、投诉排查、合规知识库、ERP 与量化等方向，不对外公开。

---

## 在线体验

不用装环境，点开就能用：

| 站点 | 项目 |
|---|---|
| [mole.aikex.ink](https://mole.aikex.ink) | 微信打地鼠 |
| [knowledge.aikex.ink](https://knowledge.aikex.ink) | 小程序导航页 |
| [compress.aikex.ink](https://compress.aikex.ink) | 批量图片压缩 |
| [img.aikex.ink](https://img.aikex.ink) | 智能图片压缩 |
| [qr.aikex.ink](https://qr.aikex.ink) | 二维码生成 |
| [bookmark.aikex.ink](https://bookmark.aikex.ink) | 书签死链检测 |
| [zodiac.aikex.ink](https://zodiac.aikex.ink) | 星座展示 |
| [mood.aikex.ink](https://mood.aikex.ink) | 心情驿站 H5 |
| [xinqing.aikex.ink](https://xinqing.aikex.ink) | 心情驿站 React |
| [codecraft.aikex.ink](https://codecraft.aikex.ink) | AI 助手展示页 |
| [dropit.aikex.ink](https://dropit.aikex.ink) | DropIt 规则包下载 |
| [mc.aikex.ink](https://mc.aikex.ink) | 体素沙盒 |
| [feiji.aikex.ink](https://feiji.aikex.ink) | 太空战机 |
| [games.aikex.ink](https://games.aikex.ink) | 复古游戏合集 |

另有 8 个托管在 GitHub Pages：[cf-game](https://aiyangdie.github.io/cf-game/)、[neon-kart](https://aiyangdie.github.io/neon-kart/)、[wilderness-survival](https://aiyangdie.github.io/wilderness-survival/)、[lan-share](https://aiyangdie.github.io/lan-share/)、[PhonePriceVista](https://aiyangdie.github.io/PhonePriceVista/)、[ziwei-ai](https://aiyangdie.github.io/ziwei-ai/)、[mc-aikex-ink](https://aiyangdie.github.io/mc-aikex-ink/)。

---

## 技术栈

**前端** React · Vue · TypeScript · Next.js · Tailwind ｜ **后端** Node.js · Python · PHP · Go ｜ **移动端** Expo + React Native · Flutter ｜ **图形** Three.js · Canvas · WebRTC ｜ **数据** MySQL · Redis · SQLite ｜ **部署** GitHub Pages · Actions · Docker · Nginx

---

## 说明

- 标 **Fork** 的项目来自上游，内容与文档归原作者，我只做本地化与链接维护。
- 部分仓库 README 声明 MIT，但仓库内暂无 LICENSE 文件，二次使用前请先确认授权。
- `WeFlow` 仓库因 GitHub 侧访问受限（HTTP 451）已无法打开，此处不再列出。
- 三个占位仓库只有说明页，没有代码实现。

---

<p align="center">
<a href="mailto:aike1015@qq.com">aike1015@qq.com</a> ·
<a href="https://github.com/aiyangdie?tab=repositories">全部仓库</a>
</p>
