# Profile README 维护脚本

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

2. 生成并写入 README：

```bash
python scripts/generate_projects.py
python scripts/build_readme.py
```
