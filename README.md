<!--
  aiyangdie · GitHub Profile
  产品化交付 · 自动化工具 · 游戏与价格情报
-->

<div align="center">

<img src="./assets/profile-header.svg" alt="艾阳 · 产品与工程开发者" width="100%"/>

<img src="./assets/typing.svg" alt="ship useful products · build reliable tools · keep learning" width="85%"/>

<br/>

[![Email](https://img.shields.io/badge/aike1015%40qq.com-07C160?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aike1015@qq.com)
[![Website](https://img.shields.io/badge/aike.ink-1F6FEB?style=for-the-badge&logo=googlechrome&logoColor=white)](https://aike.ink/)
[![GitHub](https://img.shields.io/badge/@aiyangdie-181717?style=for-the-badge&logo=github)](https://github.com/aiyangdie)
[![Views](https://komarev.com/ghpvc/?username=aiyangdie&label=Profile%20views&color=238636&style=for-the-badge)](https://github.com/aiyangdie)

</div>

---

## 我在做什么

我是艾阳，关注 **能真正上线、能持续维护、对用户有帮助的产品**。目前的工作与开源探索主要集中在：

| 方向 | 我关心的问题 |
|:---|:---|
| 支付与商户合规 | 申诉、工单、支付接入、OAuth 与运营后台如何稳定协作 |
| 微信生态 | 小程序、H5、知识付费与轻量工具如何形成完整体验 |
| 游戏与价格情报 | 怎样把 Steam 价格、折扣、史低与提醒做得更可信 |
| 工程工具 | 图片处理、局域网通信、自动化脚本与开发效率 |

```ts
type ProductPrinciples = {
  ship: '线上可用'
  trust: '来源清楚 · 密钥不上库'
  design: '先把用户流程做顺'
  openSource: '能公开的工具尽量公开'
}
```

## 当前项目 · Steam 新史低

正在完善一个面向 Steam 玩家和折扣信息用户的价格情报小站：

- 搜索中文名、英文名、AppID 或 Steam 商店链接
- 展示 Steam 中国区当前价格与折扣
- 通过 CheapShark 查询 Steam 历史价格；可选接入 ITAD 获取地区历史低价
- 关注游戏、目标价提醒、本地账号、评论与点赞
- 明确区分当前价格、第三方历史价格和本机采样数据，不把不确定的数据包装成“真正史低”

项目当前以 `Python + SQLite` 验证产品链路，长期规划为 `Laravel API + Vue 3 + PostgreSQL + Redis`，并持续补齐测试、权限边界和数据来源说明。

## 主业产品 · 可点开

<div align="center">

<a href="https://appeal.aikex.ink/chat/"><img src="./assets/card-appeal.svg" width="90%" alt="申诉 AI"/></a>

<a href="https://open.aikex.ink/docs"><img src="./assets/card-oauth.svg" width="90%" alt="OAuth 中控"/></a>

<a href="https://aike.ink/"><img src="./assets/card-pay.svg" width="90%" alt="aike.ink 支付门户"/></a>

</div>

## 微信小程序与生态

| 项目 | 说明 | 状态 |
|:-----|:-----|:-----|
| [**KnowledgeLinkerX**](https://github.com/aiyangdie/KnowledgeLinkerX) | 小程序导航聚合、二维码收录与分类检索 | 开源 |
| [**sms-verify-kit**](https://github.com/aiyangdie/sms-verify-kit) | 号码认证 SDK，登录与设备绑定工具 | 开源 |
| [**WexOpen**](https://github.com/aiyangdie/WexOpen) | Windows 微信多开助手，CI 自动出包 | 开源 |
| 知识付费 H5 | 小程序与 H5 共用后端的产品形态 | 线上 |

## 小游戏与互动项目

<div align="center">

<a href="https://github.com/aiyangdie/mc-aikex-ink"><img src="https://opengraph.githubassets.com/1/aiyangdie/mc-aikex-ink" width="46%" alt="mc-aikex-ink"/></a>&nbsp;
<a href="https://github.com/aiyangdie/wechat-whack-a-mole"><img src="https://opengraph.githubassets.com/1/aiyangdie/wechat-whack-a-mole" width="46%" alt="wechat-whack-a-mole"/></a>

<a href="https://github.com/aiyangdie/retro-games-hub"><img src="https://opengraph.githubassets.com/1/aiyangdie/retro-games-hub" width="46%" alt="retro-games-hub"/></a>&nbsp;
<a href="https://github.com/aiyangdie/feiji"><img src="https://opengraph.githubassets.com/1/aiyangdie/feiji" width="46%" alt="feiji"/></a>

</div>

| 项目 | 玩法 | 入口 |
|:-----|:-----|:-----|
| [**mc-aikex-ink**](https://github.com/aiyangdie/mc-aikex-ink) | 体素沙盒、服务器权威联机 | [在线玩](https://mc.aikex.ink/) |
| [**wechat-whack-a-mole**](https://github.com/aiyangdie/wechat-whack-a-mole) | 微信打地鼠、动画音效与计分排行 | 仓库 |
| [**retro-games-hub**](https://github.com/aiyangdie/retro-games-hub) | HTML5 Canvas 复古游戏合集 | 仓库 |
| [**feiji**](https://github.com/aiyangdie/feiji) · [**cf-game**](https://github.com/aiyangdie/cf-game) | 射击与街机小品 | 仓库 |

## 开源工具

| 仓库 | 一句话 |
|:-----|:-------|
| [**ictupian**](https://github.com/aiyangdie/ictupian) | 浏览器端图片压缩，支持 WebP / PNG / JPEG |
| [**internal-chat**](https://github.com/aiyangdie/internal-chat) | 局域网 P2P 聊天与文件传输，免登录、零配置 |
| [**-ContractAI**](https://github.com/aiyangdie/-ContractAI) | AI 合同生成与法务材料辅助 |
| [**cursor-boost**](https://github.com/aiyangdie/cursor-boost) | Cursor 常见问题的一键排障工具 |

## 技术栈

<div align="center">

![Stack](https://skillicons.dev/icons?i=react,vue,nodejs,ts,php,python,mysql,redis,docker,githubactions,linux,nginx&perline=6)

</div>

`React / Vue` · `Node.js / TypeScript` · `PHP / Python` · `微信小程序` · `MySQL / Redis` · `Docker / Nginx / GitHub Actions`

## 活跃度

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=aiyangdie&theme=github_dark" height="168" alt="GitHub stats"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=aiyangdie&theme=github_dark" height="168" alt="Top languages"/>

<img src="https://streak-stats.demolab.com?user=aiyangdie&theme=github-dark-blue&hide_border=true&background=0D1117&ring=07C160&fire=3FB950&currStreakLabel=07C160" alt="GitHub streak"/>

</div>

---

<div align="center">

## 合作

**商户申诉 / 合规系统** · **微信支付与 OAuth** · **小程序与小游戏** · **Steam 工具与价格情报**

[邮箱](mailto:aike1015@qq.com) · [官网 aike.ink](https://aike.ink/) · [申诉 AI](https://appeal.aikex.ink/chat/) · [OAuth 文档](https://open.aikex.ink/docs)

<sub>Production first · Private for clients · Open source for leverage</sub>

</div>
