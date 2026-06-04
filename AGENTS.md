# RankHub 项目规则

## 构建流程

每次修改源代码后，必须运行构建命令：

```bash
python build.py
```

源文件目录：
- `content/*.md` — 页面内容（Markdown）
- `templates/base.html` — HTML 模板
- `content/css/` — 样式文件
- `content/js/` — JavaScript 文件
- `build.py` — 构建脚本

构建产物输出到 `docs/` 目录，该目录由 GitHub Pages 部署。

## 密码保护

`content/draft/` 下的 Markdown 文件会被自动注入密码保护。
默认密码在 `content/js/password.js` 的 `PASSWORD` 变量中。

## 部署流程

部署通过 GitHub Actions 自动完成。推送 `main` 分支后触发：
`.github/workflows/deploy.yml`

手动部署：
```bash
git add -A
git commit -m "描述"
git push origin main
```

## 新增页面

1. 在 `content/` 下创建 `.md` 文件
2. 在 `build.py` 的 `SECTIONS` 和 `MONTHLY_RANKS` 中添加条目
3. 在 `templates/base.html` 的导航栏中添加链接
4. 运行 `python build.py`

## 新增待发布页面

1. 在 `content/draft/` 下创建 `.md` 文件
2. 在 `build.py` 的 `MONTHLY_RANKS['draft']` 中添加条目
3. 运行 `python build.py`
