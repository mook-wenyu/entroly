# Fork 与上游差异评估

## 结论

不建议把当前代码整体改回 `upstream/main`。当前 fork 已经不是少量本地补丁，而是围绕代理、Codex provider、Responses 注入、Roslyn C# 语义分析、dashboard 可观测性和真实 provider 验证形成的一组能力。整体回退会删除 56 个文件范围内的大量实现和测试，风险明显高于收益。

建议路径：保留 fork 主线，用 merge 吸收上游真实新增能力，再按本仓库证据处理文档数字。2026-04-30 的上游新增 3 个提交：`281183a` 更新 README benchmark 数字，`19f9197` 修正文档 demo 链接，`e5d3562` 增加 fast-path 路由与 5 个生产修复。本次已合入 `e5d3562` 的代码修复和 demo 链接；benchmark 数字继续采用 2026-04-29 本 fork 的 `gpt-5.5` fresh 结果，因为当前 provider 路由没有复现上游点估计。

## 已验证事实

- 同步前 `origin/main` 与 `HEAD`：`e73a712`。
- 同步前 `upstream/main`：`e5d3562`，提交信息为 `fix: harden engine core — 5 production bugs + fast-path routing`。
- 同步前 merge-base：`55a379a`。
- 同步前 `main...upstream/main`：fork 侧 17 个提交，上游侧 3 个提交。
- 上游真实新增范围（`55a379a..upstream/main`）：7 个文件，660 行新增，18 行删除。
- 已完成 merge 后，`upstream/main` 是当前 `main` 的祖先；当前分支保留 fork 主线并包含上游 `e5d3562`。
- 若直接把 fork 改成上游树，差异仍会覆盖 56 个文件，约 5,000+ 行 fork 能力和测试会消失。
- 目录分布：`tests/` 约 42.8%，`entroly/` 约 32.1%，说明 fork 差异有测试覆盖，不是无测试堆叠。
- `bench/tuning_config.json` 只有行尾噪声，本次同步不纳入提交。

## 差异分组

| 分组 | fork 当前内容 | 上游回退影响 | 判断 |
|---|---|---|---|
| Codex/provider 路由 | `entroly/codex_integration.py` 读取 Codex provider，保留 provider path prefix，生成会话级 override | 删除后 `wrap codex` 退回简单代理入口，第三方 provider 容易路径错配 | 保留 |
| HTTP 代理 | `entroly/proxy.py`、`proxy_http.py`、`proxy_transform.py` 处理逐跳头、上游错误、Responses/Chat/Anthropic/Gemini 注入 | 删除后错误传播和多 provider contract 倒退 | 保留 |
| Roslyn C# / Unity | `entroly/csharp_semantic.py` 与 `entroly/roslyn/...` 使用 Roslyn `SemanticModel`，记录 asmdef metadata 和 diagnostics | 删除后 C# belief 回到弱语义或缺失路径 | 保留 |
| dashboard/runtime | `runtime_status.py`、dashboard snapshot、last optimization、CogOps 状态区分 | 删除后运行时身份和优化可见性倒退 | 保留 |
| benchmark | BFCL loader、严格函数名匹配、benchmark registry | 删除后 public benchmark 覆盖减少 | 保留 |
| 文档 | README、DETAILS、中文 README 记录 fork 能力边界 | 回退后用户文档会与当前功能不一致 | 保留并继续维护 |
| 上游 fast-path 修复 | `entroly/fast_path.py`、`server.py`、`reward_crystallizer.py`、`sdk.py` 等生产修复 | 未合入会漏掉上游已修问题 | 已合入 |
| 上游新增 README 指标 | README 三项 benchmark 数字上调 | fresh `gpt-5.5` 运行未复现这些点估计 | 不吸收上游数字，改用本仓库 fresh 证据 |

## 优缺点评估

### fork 当前优势

- 高内聚边界已经形成：Codex 配置解析集中在 `entroly/codex_integration.py`，HTTP header 和 URL 拼接集中在 `entroly/proxy_http.py`，C# 语义适配集中在 `entroly/csharp_semantic.py`。
- 测试支撑明确：`tests/test_codex_wrap.py` 覆盖 provider/profile/path-prefix，`tests/test_proxy_provider_contracts.py` 覆盖多 provider 注入形状，`tests/test_csharp_semantic_compiler.py` 覆盖 Roslyn/asmdef/打包边界，`tests/test_live_provider_e2e.py` 提供真实 provider 可选验证。
- 失败语义更清楚：Roslyn analyzer 缺失、无效 JSON、非 ok 状态都会显式失败；严格优化模式可让代理优化失败暴露为错误，避免静默转发掩盖问题。
- 文档更贴近当前本机开发环境：`AGENTS.md` 明确 Python 3.13、`ebbiforge`、`entroly-core` 和 `.[full]` 的安装顺序。

### fork 当前不足

- fork 与上游分叉面已经较大，后续同步上游时需要逐项审计，不能再按简单 merge 处理。
- README 中 fork 专用说明混入英文主 README，后续应减少长段新增，改用链接到专门文档。
- `BENCHMARKS.md` 已补充 2026-04-29 fresh `gpt-5.5` 三项结果，并把 engine version 更新为 `entroly-core v0.10.0`；历史 `gpt-4o-mini` 全套快照仍作为历史证据保留。
- 当前会话可读取 exa MCP 工具列表，但没有暴露可调用搜索工具；tavily MCP 未列出资源。本次补充直接抓取 OpenAI Python SDK、HuggingFace datasets-server rows、Python `urllib.request` 官方资料作为外部依据。

### 上游当前优势

- 主线代码更小，维护面更少。
- `e5d3562` 补了 fast-path 路由、RewardCrystallizer 外部 baseline、代码压缩 ratio、代理属性防御访问和 server 片段计数等生产问题。
- `19f9197` 修正 Live demo 链接，已随 merge 保留。

### 上游当前不足

- 缺少 fork 中已经验证的 Codex provider、第三方 Responses 代理、Roslyn C# 语义和运行时可观测性能力。
- 上游最新 README 数字与本仓库 fresh `gpt-5.5` 结果不一致；本仓库继续使用已验证的 benchmark 真源和复现实验产物。

## 外部依据

- OpenAI 官方 Python SDK `responses.create` 暴露 `input`、`instructions`、`stream`、`stream_options`，支持当前 fork 把 Responses 注入放在 `instructions` 并保留用户 `input` 的方向。来源：`https://github.com/openai/openai-python/blob/main/src/openai/resources/responses/responses.py`。
- HuggingFace datasets-server rows 文档是本仓库 MMLU、TruthfulQA、LongBench loader 的数据源依据。来源：`https://huggingface.co/docs/datasets-server/en/rows`。
- Python `urllib.request` 官方文档支撑本次用显式 `Request`、headers、timeout 调用 Responses provider 和 HuggingFace rows API。来源：`https://docs.python.org/3/library/urllib.request.html`。
- Microsoft Learn Roslyn 语义分析说明：语义问题依赖 source files、assembly references、compiler options；`Compilation` 近似编译器看到的单项目上下文，`SemanticModel` 提供符号和类型信息。来源：`https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/get-started/semantic-analysis`。
- Unity assembly definition 官方文档可访问，支撑 `.asmdef` 作为 Unity assembly 边界的事实。来源：`https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html`。
- maturin 官方文档说明 wheel/sdist 构建和包含文件规则，支撑 fork 对 Roslyn analyzer 源码打包并排除 `bin/obj` 的方向。来源：`https://www.maturin.rs/distribution.html`。
- PyO3 官方文档说明 Python/Rust 边界由 PyO3 类型与解释器 token 管理，支撑本仓库把性能核心留在 `entroly-core`、Python 层做 orchestration 的结构。来源：`https://pyo3.rs/main/python-from-rust.html`。
- RAG 论文把检索到的知识作为生成上下文的一部分，支撑 Entroly 的代码上下文检索/压缩方向。来源：`https://arxiv.org/abs/2005.11401`。
- SWE-bench 以真实 GitHub issue/PR 为软件工程评估任务，支撑用文件命中率、上下文选择和可复现 benchmark 评估代码助手场景。来源：`https://arxiv.org/abs/2310.06770`。

## 实现任务

### 任务 1：保留 fork 主线，建立同步准入规则

- 文件：`docs/fork-upstream-audit.md`
- 操作：记录本次差异事实、结论和进度。
- 验收：文档明确“不整体回退”，并说明上游 README 指标暂不吸收的原因。

### 任务 2：后续上游同步必须先跑文档/benchmark 一致性检查

- 文件：`README.md`、`BENCHMARKS.md`、`docs/i18n/README.zh-CN.md`、`bench/accuracy.py`
- 操作：任何 benchmark 数字变更必须同步 benchmark 真源或附 fresh run 证据。
- 验收：README、中文 README、`BENCHMARKS.md` 三处数值一致；命令或产物能说明数字来源。

### 任务 3：代理和 provider 能力继续以测试为边界演进

- 文件：`entroly/codex_integration.py`、`entroly/proxy.py`、`entroly/proxy_http.py`、`entroly/proxy_transform.py`
- 测试：`tests/test_codex_wrap.py`、`tests/test_proxy_provider_contracts.py`、`tests/test_proxy_http.py`、`tests/test_proxy_streaming.py`、`tests/test_live_provider_e2e.py`
- 操作：后续改动先补或更新测试，再改实现；不引入隐藏失败的自动转发逻辑。
- 验收：provider path prefix、Responses 注入、上游错误传播、loopback/no_proxy 均有自动化测试。

### 任务 4：Roslyn C# / Unity 能力继续保持显式边界

- 文件：`entroly/csharp_semantic.py`、`entroly/belief_compiler.py`、`entroly/roslyn/Entroly.CSharpAnalyzer/*`
- 测试：`tests/test_csharp_semantic_compiler.py`、`tests/test_change_listener.py`
- 操作：新增 Unity 语义支持时必须先定义 diagnostics 和测试，不模拟未实现的 Unity Editor 编译行为。
- 验收：缺 `dotnet`、analyzer 输出异常、选中文件未返回时显式失败。

### 任务 5：清理文档冲突与过时声明

- 文件：`README.md`、`BENCHMARKS.md`、`docs/DETAILS.md`、`docs/fork-upstream-audit.md`
- 操作：把 fork 专用长说明逐步迁移到专题文档；主 README 只保留短链接和用户必要路径。
- 验收：用户文档不重复、不冲突，benchmark 数字不出现多版本并存。

## 最新进度

- 已完成：刷新 `upstream/main` 到 `e5d3562`。
- 已完成：确认同步前 fork 侧 17 个提交，上游侧 3 个提交。
- 已完成：确认上游新增包含 README benchmark 数字、demo 链接修正和 fast-path/生产修复。
- 已完成：确认直接改回上游树会删除 56 文件范围内的 fork 能力和测试。
- 已完成：合入上游 `e5d3562`，并解决 `entroly/proxy_transform.py` 的格式级冲突。
- 已完成：完成关键模块取样：Codex provider、代理、Roslyn、dashboard/runtime、benchmark、测试。
- 已完成：完成外部依据取证；当前会话 exa/tavily 未暴露可调用搜索接口，已直接抓取 OpenAI Python SDK、HuggingFace rows、Python urllib 官方资料。
- 已完成：新增本评估与进度文档。
- 已完成：补齐 `bench.accuracy --wire-api responses`，自定义 `base-url` 的 Responses 路径改为显式 HTTP 请求，避免 SDK 默认请求形态影响兼容 provider。
- 已完成：重跑 upstream-touched 三项 fresh benchmark，模型 `gpt-5.5`，样本 `n=100`，endpoint `https://api.mookbot.com/v1`，三项 exit code 均为 0。
- 已完成：MMLU fresh 结果：baseline 97.0% [91.6-99.0%]，Entroly 98.0% [93.0-99.5%]，retention 101.0%。
- 已完成：TruthfulQA fresh 结果：baseline 91.0% [83.8-95.2%]，Entroly 90.0% [82.6-94.5%]，retention 98.9%。
- 已完成：LongBench fresh 结果：baseline 74.0% [64.6-81.6%]，Entroly 74.0% [64.6-81.6%]，retention 100.0%。
- 已完成：同步 `README.md`、`docs/i18n/README.zh-CN.md`、`BENCHMARKS.md`、`docs/DETAILS.md` 的 benchmark 表述。
- 未完成：未重跑完整 8 项 full-suite；本轮目标是补 fresh benchmark 证据并同步上游触及的三项基准文档。

## 验证命令

当前文档变更后应执行：

```powershell
$py = "C:\Users\WenYu\AppData\Local\Programs\Python\Python313\python.exe"
& $py -m ruff check bench/accuracy.py tests/test_bench_accuracy.py entroly/
& $py -m pytest tests/test_codex_wrap.py tests/test_proxy_provider_contracts.py tests/test_proxy_http.py tests/test_proxy_streaming.py tests/test_csharp_semantic_compiler.py tests/test_dashboard_runtime.py tests/test_bench_accuracy.py -q --tb=short
git diff --check -- . ':!bench/tuning_config.json'
```

完整发布前再执行：

```powershell
& $py -m pytest tests/ -v --tb=short
cd entroly-core; cargo test --lib; cargo clippy --all-targets -- -D warnings; cd ..
```
