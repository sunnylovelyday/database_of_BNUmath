# BNU_math 网站

首次发布：在 Settings → Pages → Build and deployment 中将 Source 设为 GitHub Actions，合并网站 PR 到 main 后等待工作流完成。也可手动运行 workflow_dispatch。

网址：https://sunnylovelyday.github.io/database_of_BNUmath/

网站按原始文件夹层级浏览，支持关键词搜索、分类和课程筛选，搜索时自动展开匹配目录。

PDF 会随页面一起部署到 GitHub Pages，链接使用站点相对路径，例如 `./考试题目/数学分析1/文件.pdf`。文件由 github.io 提供，使用 PDF 内容类型，让支持 PDF 的浏览器直接阅读。其他格式仍使用 GitHub raw 地址下载，不复制到 Pages。

目录通过 `python scripts/build_catalog.py` 从跟踪文件生成。工作流获取 LFS 原文件，校验 PDF 文件头，并保留嵌套路径复制 PDF；不发布 Git 元数据。当前目录中 PDF 总计约 677 MB。构建超过 950 MB 会报错，预留 GitHub Pages 1 GB 大小限制的余量。增加大量资料时需关注构建包大小。

站点无需登录或个人访问令牌。main 更新后会重新生成目录并部署。部署前本地运行目录生成脚本，可用 `python -m http.server 8000` 预览。
