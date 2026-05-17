# 贡献指南

感谢参与 Entroly。提交变更前，请先按实际影响范围完成验证，并在 PR 或提交说明中写清楚已运行的命令。

## 构建指南

完整本地开发、测试、Wasm、PyO3 wheel、Docker 与发布前构建流程见：

- [docs/build-guide.md](docs/build-guide.md)

本仓库是 Python + Rust + Roslyn + Wasm 混合项目。不要只跑单一语言的测试后就推送跨边界改动。

## 提交前要求

1. 从 `main` 创建分支。
2. 只修改完成目标所需的文件。
3. 按 [构建指南](docs/build-guide.md) 选择最小充分验证。
4. 确认 `git status --short --branch --untracked-files=all` 中没有误加入的产物或本地配置。
5. 打开 PR 时写明变更摘要、验证命令和未验证项。

## 代码质量

- Python 目标版本为 3.10+，行宽 120。
- Rust 使用 stable toolchain，提交前通过 `cargo fmt`、`cargo test` 和 `cargo clippy --all-targets -- -D warnings`。
- 新行为需要自动化测试；无法自动化时，在 PR 中说明人工验证依据。
- 不提交 `.entroly/`、`dist/`、`target/`、`entroly-wasm/pkg/`、`.pytest_cache/`、本地密钥或临时产物。

## 行为准则

讨论保持具体、尊重和可验证。技术争议以代码、测试、日志和官方文档为依据。
