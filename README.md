# RankHub - 排行榜中心

一个支持Markdown自动转换为HTML的排行榜网站，可通过GitHub Pages自动部署。

## 功能特性

- 📊 支持B站、抖音、微信公众号、小红书排行榜
- 🌍 支持全球AI网站和中国AI应用排行榜
- ✍️ 使用Markdown编写内容，自动转换为HTML
- 🎨 现代化UI设计，带有渐变色彩
- 🚀 GitHub Actions自动构建和部署

## 快速开始

### 本地开发

1. 安装Python 3.8+
2. 安装依赖：
   ```bash
   pip install markdown
   ```
3. 运行构建脚本：
   ```bash
   python build.py
   ```
4. 在浏览器中打开 `docs/index.html` 预览

### GitHub Pages部署

1. 将代码推送到GitHub仓库
2. 在仓库设置中启用GitHub Pages
3. 选择 `main` 分支作为源
4. 每次推送到 `main` 分支会自动触发构建和部署

## 目录结构

```
.
├── .github/workflows/    # GitHub Actions配置
│   └── deploy.yml
├── content/              # Markdown内容文件
│   ├── bilibili.md
│   ├── douyin.md
│   ├── wechat.md
│   ├── xiaohongshu.md
│   ├── ai-global.md
│   └── ai-china.md
├── templates/            # HTML模板
│   └── base.html
├── build.py             # 构建脚本
└── docs/                # 生成的HTML文件（部署目录）
```

## 添加新内容

1. 在 `content/` 目录下创建新的 `.md` 文件
2. 运行 `python build.py` 生成HTML
3. 提交并推送到GitHub

## Markdown格式示例

```markdown
# 页面标题

## 二级标题

| 列1 | 列2 | 列3 |
|-----|-----|-----|
| 数据1 | 数据2 | 数据3 |

- 列表项1
- 列表项2
```

## 自定义

### 修改颜色主题

编辑 `content/css/styles.css` 中的CSS变量：

```css
:root {
    --primary: #6366f1;
    --secondary: #ec4899;
    --accent: #06b6d4;
    /* ... */
}
```

### 添加新的排行榜

1. 在 `content/` 目录创建新的Markdown文件
2. 在 `build.py` 的 `generate_index()` 函数中添加对应的HTML代码
3. 在导航栏中添加链接

## 许可证

MIT License
# rankhub
