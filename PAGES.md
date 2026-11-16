# BNU_math 网站

首次发布：

1. 在仓库 Settings → Pages → Build and deployment 中，将 Source 设为 GitHub Actions。
2. 合并网站 PR 到 main；Actions 中的 Deploy BNU_math to GitHub Pages 会构建并发布。也可手动运行 workflow_dispatch。
3. 等部署成功后访问 https://sunnylovelyday.github.io/database_of_BNUmath/ 。此地址是预期地址，实际结果以 Actions 的 deployment URL 为准。

网站支持关键词搜索、三类资料筛选和考试课程筛选，按仓库原始嵌套目录逐层展开浏览。搜索时自动展开匹配文件所在文件夹。点击文件直接访问原文件地址，不经过 GitHub 文件展示页；PDF 是否在浏览器内预览取决于浏览器设置及文件服务响应头，部分文件可能直接下载。目录从三类资料文件夹中的 Git 跟踪文件自动生成，不包含隐藏文件。添加资料并推送 main 后，部署时自动更新索引，无需修改 HTML。生成索引：`python scripts/build_catalog.py`。本地查看：先生成目录，再运行 `python -m http.server 8000`。

发布包仅包含 index.html 与 catalog.json；资料保留在原仓库。站点无登录、令牌或浏览器端 GitHub API 请求。GitHub Actions 使用 GitHub 自动提供的短期令牌和 Pages OIDC，不需要配置个人访问令牌。

如使用 Git LFS，工作流不会拉取大文件；目录中的大小可能显示 LFS 指针大小。文件通过 GitHub raw 文件地址访问，由 GitHub 处理原文件重定向。
