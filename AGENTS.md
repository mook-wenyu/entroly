# Repository Guidelines

## 项目结构与模块组织

Entroly 是 Python 包与 Rust 核心混合项目。`entroly/` 放置 Python CLI、HTTP 代理、MCP 集成、压缩与索引逻辑；`entroly-core/` 是 PyO3 Rust 扩展，包含性能敏感的优化与压缩核心；`entroly-wasm/` 提供 JavaScript/Wasm 入口。测试主要在 `tests/`，Rust/Python 集成测试在 `entroly-core/tests/`。文档与站点资源在 `docs/`，基准测试脚本和数据在 `bench/`，示例在 `examples/`，维护脚本在 `scripts/`。

## 构建、测试与开发命令

```powershell
$py = "C:\Users\WenYu\AppData\Local\Programs\Python\Python313\python.exe"
$env:PYO3_PYTHON = $py
& $py -m pip install maturin pytest pytest-cov pytest-timeout ruff psutil
cd entroly-core; & $py -m pip install .; cd ..
& $py -m pip install -e ".[proxy,native]"
```

不要使用 venv；本仓库默认安装到本机 Python 3.13。`pip install .` 会通过 maturin 构建并安装本地 Rust 扩展。`pip install -e ".[proxy,native]"` 安装 Python 包、本地 Rust 核心和代理相关依赖；避免使用 `.[full]`，因为其中的 `ebbiforge` 依赖不一定在当前 pip 源可用。常用验证命令：

```powershell
& $py -m ruff check entroly/
& $py -m pytest tests/ -v --tb=short
& $py tests/functional_test.py
$env:PYO3_PYTHON = $py
cd entroly-core; cargo test --lib; cargo clippy --all-targets -- -D warnings; cd ..
```

如修改 `bench/` 或 `BENCHMARKS.md`，运行 `python bench/compare.py --markdown bench_section.md --check-regression`。

## 编码风格与命名约定

Python 目标版本为 3.10+，行宽按 Ruff 配置使用 120。保持 4 空格缩进，模块、函数、变量使用 `snake_case`，类使用 `PascalCase`。Rust 使用 2021 edition，遵循 `cargo fmt` 与 Clippy 建议。不要新增依赖，除非变更目标无法用现有依赖实现。修改代理、provider、压缩策略时，优先复用 `entroly/` 内现有工具函数与配置入口。

## 测试规范

新增 Python 行为应补充 `tests/test_*.py`，测试名使用 `test_<behavior>`。核心逻辑变更先跑相关单测，再跑完整 `pytest tests/ -v --tb=short`。触及 Rust 核心时必须运行 `cargo test --lib`；触及 PyO3 边界时还要运行 `python entroly-core/tests/test_integration.py`。代理路径变更需覆盖 provider、鉴权和 URL 转换测试。

## 提交与 Pull Request 规范

近期提交使用简短意图句，例如“统一代理入口真源，避免错误写死 OpenAI 路径前缀”。提交信息应说明为什么修改；复杂变更按 Lore trailer 记录 `Constraint:`、`Rejected:`、`Tested:`、`Not-tested:`。PR 需包含变更摘要、验证命令结果、关联 issue；涉及 CLI、HTTP 代理或文档页面时附示例命令或截图。

## 安全与配置提示

不要提交 `.venv/`、`dist/`、`target/`、`.omx/`、`.verify-artifacts/`、`.tmp/` 或本地密钥。代理相关配置和 token 只通过环境变量或本地未跟踪文件传递。修改默认 base URL、provider 路由或认证逻辑时，必须明确验证不会泄露上游凭据。
