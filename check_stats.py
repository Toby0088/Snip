#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
查询 GitHub Releases 下载量（无需安装任何库，Python 3 自带 urllib）

用法：
    python check_stats.py            # 使用仓库名 toby0088/Snip
    python check_stats.py 你的名字/Snip

提示：公开仓库无需 Token 也能查，但有次数限制；查询多了可用 GitHub Token 提升额度。
"""
import json
import sys
import urllib.request

repo = sys.argv[1] if len(sys.argv) > 1 else "toby0088/Snip"
url = "https://api.github.com/repos/%s/releases" % repo

try:
    req = urllib.request.Request(url, headers={"User-Agent": "Snip-stats"})
    data = json.load(urllib.request.urlopen(req, timeout=15))
except Exception as e:
    print("查询失败：", e)
    print("请确认：1) 仓库已公开  2) 仓库名写对（用户名/仓库名）  3) 已发布过 Release")
    sys.exit(1)

total = 0
for rel in data:
    n = sum(a.get("download_count", 0) for a in rel.get("assets", []))
    total += n
    print("%-12s %s  下载 %d 次" % (rel.get("tag_name", "?"), rel.get("published_at", "?"), n))
print("-" * 40)
print("全部版本累计下载：%d 次" % total)