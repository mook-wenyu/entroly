# Repository Guidelines

## 项目结构与模块组织

Entroly 是 Python + Rust 混合项目：

- `entroly/`：Python CLI、HTTP 代理、MCP 集成、索引与压缩逻辑
- `entroly-core/`：PyO3 Rust 扩展，承载性能敏感逻辑
- `entroly-wasm/`：JavaScript/Wasm 入口
- `tests/`：Python 测试；`entroly-core/tests/`：Rust/Python 集成测试
- `docs/`、`bench/`、`examples/`、`scripts/`：文档、基准、示例、维护脚本

## 构建、测试与开发命令

```powershell
$py = "C:\Users\WenYu\AppData\Local\Programs\Python\Python313\python.exe"
$env:PYO3_PYTHON = $py
& $py -m pip install maturin pytest pytest-cov pytest-timeout ruff psutil
cd D:\PyProjects\ebbiforge; & $py -m pip install .; cd D:\PyProjects\entroly
cd entroly-core; & $py -m pip install .; cd ..
& $py -m pip install -e ".[full]"
```

约束：

- 不要使用 venv；默认使用本机 Python 3.13
- 先安装 `D:\PyProjects\ebbiforge`，否则 `.[full]` 无法解析 `ebbiforge` / `ebbiforge_core`
- 先构建安装 `entroly-core`，再执行 `pip install -e ".[full]"`

常用验证：

```powershell
& $py -m ruff check entroly/
& $py -m pytest tests/ -v --tb=short
& $py tests/functional_test.py
$env:PYO3_PYTHON = $py
cd entroly-core; cargo test --lib; cargo clippy --all-targets -- -D warnings; cd ..
```

如果修改 `bench/` 或 `BENCHMARKS.md`，补跑：

```powershell
python bench/compare.py --markdown bench_section.md --check-regression
```

## 编码风格与命名约定

- Python 目标版本 `3.10+`，行宽 `120`
- 4 空格缩进；模块、函数、变量用 `snake_case`；类用 `PascalCase`
- Rust 使用 2021 edition，遵循 `cargo fmt` 与 Clippy
- 不要新增依赖，除非现有依赖无法完成目标
- 修改代理、provider、压缩策略时，优先复用 `entroly/` 现有工具函数和配置入口

## 测试规范

- 新增 Python 行为补到 `tests/test_*.py`，测试名使用 `test_<behavior>`
- 核心逻辑先跑相关单测，再跑 `pytest tests/ -v --tb=short`
- 触及 Rust 核心必须跑 `cargo test --lib`
- 触及 PyO3 边界还要跑 `python entroly-core/tests/test_integration.py`
- 代理路径变更必须覆盖 provider、鉴权、URL 转换测试

## 提交与 Pull Request 规范

- 提交信息使用简短意图句，并说明为什么改
- 复杂变更按 Lore trailer 记录 `Constraint:`、`Rejected:`、`Tested:`、`Not-tested:`
- PR 需包含变更摘要、验证命令结果、关联 issue
- 涉及 CLI、HTTP 代理或文档页面时附示例命令或截图

## 安全与配置提示

- 不要提交 `.venv/`、`dist/`、`target/`、`.omx/`、`.verify-artifacts/`、`.tmp/` 或本地密钥
- 代理配置和 token 只通过环境变量或本地未跟踪文件传递
- 修改默认 `base_url`、provider 路由或认证逻辑时，必须验证不会泄露上游凭据
