# Profile README 维护脚本

当前主页使用人工编排的商户业务介绍与项目导航，直接编辑根目录 `README.md`。
`update_github_profile.py` 中的 `HANDCRAFTED_README = True` 会跳过旧版自动生成流程，请保留。
`build_readme.py` 依赖旧版标题结构，不适用于当前主页，不要用它覆盖新版 README。
下方命令保留作旧项目目录的维护参考；目录中的数量、星标和可见性须以实际查询时间为准。

1. 拉取最新仓库列表（PowerShell）：

```powershell
# 在 aiyangdie-profile 目录执行，需 GITHUB_TOKEN 可选
$headers = @{ "User-Agent" = "aiyangdie-profile"; "Accept" = "application/vnd.github+json" }
if ($env:GITHUB_TOKEN) { $headers["Authorization"] = "Bearer $env:GITHUB_TOKEN" }
$all = @(); $page = 1
do {
  $batch = Invoke-RestMethod -Uri "https://api.github.com/users/aiyangdie/repos?per_page=100&page=$page&type=owner&sort=name" -Headers $headers
  if ($batch.Count -eq 0) { break }; $all += $batch; $page++
} while ($batch.Count -eq 100)
$all | Sort-Object name | ForEach-Object {
  [PSCustomObject]@{ name=$_.name; desc=($_.description -replace "`r`n"," "); lang=$_.language; stars=$_.stargazers_count; fork=$_.fork; url=$_.html_url }
} | ConvertTo-Json -Depth 3 | Out-File -Encoding utf8 repos-all.json
```

2. 仅重新生成 `projects-section.md` 项目目录（不会改写主页）：

```bash
python scripts/generate_projects.py
```
