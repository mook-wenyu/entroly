# Entroly 构建指南

本文档是 Entroly 仓库的本地开发、验证和发布前构建指南。命令以 Windows PowerShell 为主；Linux/macOS 可按同一顺序替换路径和 shell 语法。

## 构建边界

Entroly 由四个构建面组成：

- Python 包：根目录 `pyproject.toml`，使用 `hatchling` 构建 `entroly`。
- Rust / PyO3 核心：`entroly-core/`，使用 `maturin` 构建 `entroly-core` wheel。
- Roslyn C# 分析器：`entroly/roslyn/`，使用 .NET 8 构建和运行 xUnit 测试。
- Wasm / Node 包：`entroly-wasm/`，使用 `wasm-pack` 生成 `pkg/`，再由 npm 脚本测试。

不要把 `.entroly/`、`dist/`、`target/`、`entroly-wasm/pkg/`、`.pytest_cache/` 或本地密钥提交进仓库。

## 前置条件

必需工具：

- Python 3.10+。CI 覆盖 3.10、3.11、3.12、3.13、3.14；本机开发默认使用 Python 3.13。
- Rust stable toolchain，包含 `cargo` 和 `clippy`。
- .NET 8 SDK，用于 Roslyn 分析器。
- `maturin`，用于 PyO3 wheel。
- `ruff`、`pytest`、`pytest-timeout`、`psutil`。

条件性工具：

- Node.js 16+。发布 workflow 使用 Node.js 20。
- `wasm-pack`，只在构建或测试 `entroly-wasm/` 时需要。
- Docker / Buildx，只在验证 `Dockerfile.entroly` 或镜像发布路径时需要。

本机 Windows 推荐先定义 Python 路径：

```powershell
$py = "C:\Users\WenYu\AppData\Local\Programs\Python\Python313\python.exe"
$env:PYO3_PYTHON = $py
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
```

`PYTHONUTF8` 和 `PYTHONIOENCODING` 用于避免 Windows GBK 控制台无法打印测试脚本中的 Unicode 符号。

## 本机开发安装

本仓库本机开发默认不创建 venv。CI 可以使用 venv 作为隔离策略，但本机指南保持一条固定解释器路径，减少 PyO3 和 Python 包解析差异。

先安装开发工具：

```powershell
& $py -m pip install --upgrade pip
& $py -m pip install maturin build pytest pytest-cov pytest-timeout ruff psutil
```

如果要安装根包的 `.[full]` extra，先安装相邻的 `ebbiforge` 项目；否则 `ebbiforge` / `ebbiforge_core` 可能无法从本地解析：

```powershell
cd D:\PyProjects\ebbiforge
& $py -m pip install .
```

再安装 Rust 核心和根 Python 包：

```powershell
cd D:\PyProjects\entroly\entroly-core
& $py -m pip install .

cd D:\PyProjects\entroly
& $py -m pip install -e ".[full]"
```

## 日常验证

Python 代码或代理路径变更后运行：

```powershell
cd D:\PyProjects\entroly
& $py -m ruff check entroly/
& $py -m pytest tests/ -v --tb=short
& $py tests/functional_test.py
```

Rust 核心变更后运行：

```powershell
cd D:\PyProjects\entroly\entroly-core
$env:PYO3_PYTHON = $py
cargo test --lib
cargo clippy --all-targets -- -D warnings
cd ..
```

PyO3 边界变更后补跑：

```powershell
cd D:\PyProjects\entroly
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
& $py entroly-core/tests/test_integration.py
& $py entroly-core/tests/test_brutal.py
```

Roslyn / Unity C# 语义分析路径变更后运行：

```powershell
cd D:\PyProjects\entroly
dotnet build entroly/roslyn/Entroly.CSharpAnalyzer/Entroly.CSharpAnalyzer.csproj -nologo
dotnet test entroly/roslyn/Entroly.CSharpAnalyzer.Tests/Entroly.CSharpAnalyzer.Tests.csproj -nologo -v:minimal
```

全仓语义编译验证：

```powershell
cd D:\PyProjects\entroly
& $py -m entroly.cli compile . --max-files 0
```

这个命令必须在修复 `compile`、Roslyn analyzer、文件筛选、语言识别、vault 写入或 C# 项目解析后运行。成功输出至少应包含 `Files processed`、`Entities extracted` 和 `Beliefs written`。

## Wasm / Node 构建

只有修改 `entroly-wasm/` 或 npm 发布路径时才需要运行。

安装缺失工具：

```powershell
npm install -g wasm-pack@0.15.0
```

构建和测试：

```powershell
cd D:\PyProjects\entroly\entroly-wasm
cargo test
npm test
```

`npm test` 会先执行：

```powershell
wasm-pack build --target nodejs --out-dir pkg
```

`pkg/` 是生成产物，默认不要提交。

## 发布前本地构建

构建根 Python sdist 和 wheel：

```powershell
cd D:\PyProjects\entroly
& $py -m build
```

构建 PyO3 release wheel：

```powershell
cd D:\PyProjects\entroly\entroly-core
$env:PYO3_PYTHON = $py
maturin build --release --out ..\dist
cd ..
```

如果本机安装了 Docker，验证容器镜像：

```powershell
cd D:\PyProjects\entroly
docker build -f Dockerfile.entroly -t entroly:local .
```

当前命令只验证本机单架构镜像。GitHub Actions 发布路径使用 Buildx / BuildKit 构建并推送镜像。

## 条件性验证

修改 `bench/` 或 `BENCHMARKS.md` 后运行：

```powershell
cd D:\PyProjects\entroly
python bench/compare.py --markdown bench_section.md --check-regression
```

修改 provider、代理转发、鉴权、URL 转换或真实上游行为后，可以在配置真实密钥后运行 live provider 测试：

```powershell
cd D:\PyProjects\entroly
& $py -m pytest tests/ -m live_provider -v --tb=short
```

不要把真实 token 写入仓库。只通过环境变量或本地未跟踪配置传递。

## 推送前检查

推送前至少检查：

```powershell
cd D:\PyProjects\entroly
git status --short --branch --untracked-files=all
git diff --check HEAD -- . ':(exclude)bench/tuning_config.json'
```

如果存在无关未提交改动，不要把它们加入提交。普通 `git push origin main` 只推送已提交对象，不会推送工作区未提交文件。

## 常见问题

### `wasm-pack` 不存在

现象：

```text
'wasm-pack' is not recognized as an internal or external command
```

处理：

```powershell
npm install -g wasm-pack@0.15.0
```

然后重新运行 `npm test`。

### PyO3 脚本在 Windows 上 UnicodeEncodeError

现象：

```text
UnicodeEncodeError: 'gbk' codec can't encode character
```

处理：

```powershell
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
```

然后重跑对应 Python 脚本。

### Docker 命令不存在

现象：

```text
The term 'docker' is not recognized
```

这是本机工具链缺口，不代表 Python、Rust、Roslyn 或 Wasm 构建失败。需要验证容器镜像时，先安装 Docker Desktop 或在有 Docker / Buildx 的 CI 环境运行镜像构建。

## 参考真源

- PyPA `build`：`python -m build` 默认构建 sdist，再从 sdist 构建 wheel，输出到 `dist/`。
- maturin：`maturin build` 构建 PyO3 wheel；`--out` 指定 wheel 输出目录。
- wasm-pack：`wasm-pack build --target nodejs` 生成 Node.js 可用的 Wasm npm 包到 `pkg/`。
- Docker：`docker build` / `docker buildx build` 使用 BuildKit 构建镜像；最后一个路径参数是 build context。

官方文档：

- https://build.pypa.io/en/latest/how-to/basic-usage.html
- https://www.maturin.rs/distribution.html
- https://rustwasm.github.io/docs/wasm-pack/tutorials/npm-browser-packages/building-your-project.html
- https://docs.docker.com/build/
