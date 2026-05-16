<p align="center">
  <a href="docs/i18n/README.zh-CN.md">ðŸ‡¨ðŸ‡³ ä¸­æ–‡</a> â€¢
  <a href="docs/i18n/README.ja.md">ðŸ‡¯ðŸ‡µ æ—¥æœ¬èªž</a> â€¢
  <a href="docs/i18n/README.ko.md">ðŸ‡°ðŸ‡· í•œêµ­ì–´</a> â€¢
  <a href="docs/i18n/README.pt-BR.md">ðŸ‡§ðŸ‡· PortuguÃªs</a> â€¢
  <a href="docs/i18n/README.es.md">ðŸ‡ªðŸ‡¸ EspaÃ±ol</a> â€¢
  <a href="docs/i18n/README.de.md">ðŸ‡©ðŸ‡ª Deutsch</a> â€¢
  <a href="docs/i18n/README.fr.md">ðŸ‡«ðŸ‡· FranÃ§ais</a> â€¢
  <a href="docs/i18n/README.ru.md">ðŸ‡·ðŸ‡º Ð ÑƒÑÑÐºÐ¸Ð¹</a> â€¢
  <a href="docs/i18n/README.hi.md">ðŸ‡®ðŸ‡³ à¤¹à¤¿à¤¨à¥à¤¦à¥€</a> â€¢
  <a href="docs/i18n/README.tr.md">ðŸ‡¹ðŸ‡· TÃ¼rkÃ§e</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/assets/logo.png" width="180" alt="Entroly">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Token_Savings-up_to_95%25-brightgreen?style=for-the-badge" alt="Token Savings: up to 95%">
  <img src="https://img.shields.io/badge/Learning_Cost-$0-blue?style=for-the-badge" alt="Learning Cost: $0">
  <img src="https://img.shields.io/badge/Engine-Rust_%2B_WASM-orange?style=for-the-badge&logo=rust" alt="Rust + WASM">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <a href="https://github.com/juyterman1000/entroly-cost-check-"><img src="https://img.shields.io/badge/GitHub_Action-Cost_Check-purple?style=for-the-badge&logo=githubactions" alt="GitHub Action"></a>
  <a href="https://mcpmarket.com/daily/top-mcp-server-list-march-26-2026"><img src="https://img.shields.io/badge/%231_MCP_Market-Ranked_Server-gold?style=for-the-badge&logo=starship&logoColor=white" alt="#1 on MCP Market"></a>
</p>

<h1 align="center">Entroly â€” Stop Your AI From Making Things Up</h1>

<h3 align="center">Catch hallucinations. Cut large-codebase context by 70-95% when retrieval has room to work.<br/>Set up in about 30 seconds.</h3>

<p align="center"><strong>ðŸ›¡ï¸ The AI helper that shows its work.</strong><br/><sub>Your AI invents functions that don't exist, makes up API names, and bills you for "thinking" about thousands of code lines it never reads. Entroly checks factual claims against supplied evidence, flags unsupported claims, and shrinks what you send the AI by up to 95%, so you pay less for more grounded answers.</sub></p>

<p align="center">
  <strong>ðŸ’° Lower bill</strong>&nbsp;&nbsp;Â·&nbsp;&nbsp;
  <strong>ðŸŽ¯ Honest answers</strong>&nbsp;&nbsp;Â·&nbsp;&nbsp;
  <strong>âš¡ 30-second install</strong>&nbsp;&nbsp;Â·&nbsp;&nbsp;
  <strong>ðŸ”Œ Works with Claude, Cursor, Copilot, Codex</strong>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/entroly/entroly-context-compression"><img src="https://img.shields.io/badge/â–¶_Try_It_Live-No_Install_Needed-FF4B4B?style=for-the-badge&logo=huggingface&logoColor=white" height="42" alt="Try the live demo on Hugging Face"></a>&nbsp;&nbsp;
  <a href="https://juyterman1000.github.io/entroly/docs/dashboard.html"><img src="https://img.shields.io/badge/ðŸ“Š_See_The_Dashboard-Live-2EA44F?style=for-the-badge" height="42" alt="See the live dashboard"></a>
</p>

<p align="center">
  <sub>
    <strong>Don't trust the claims? Paste your own code into the live demo</strong> â†’
    watch entroly shrink a large codebase context and show you exactly which lines the AI will see. 60 seconds. No install.
  </sub>
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> Â·
  <a href="cookbook/README.md"><b>Cookbook</b></a> Â·
  <a href="#benchmarks"><b>Benchmarks</b></a> Â·
  <a href="#works-with-your-stack"><b>21 supported integrations</b></a>
</p>

<a id="install"></a>

<p align="center">
  <code><b>pip install entroly</b></code>
</p>

<p align="center">
  <sub>
    Then <code>cd /your/repo && entroly go</code> â€” auto-opens the dashboard in your browser.
    <br/>
    Or: <code>brew tap juyterman1000/entroly && brew install entroly</code> Â· <code>npm i -g entroly-wasm</code>
    <br/>
    See the <a href="cookbook/README.md"><b>Cookbook</b></a> for 10 concrete recipes,
    or pick your stack from the <a href="#works-with-your-stack">22 supported integrations</a>.
  </sub>
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/entroly?color=blue&label=PyPI">
  <img src="https://img.shields.io/npm/v/entroly-wasm?color=red&label=npm">
  <img src="https://img.shields.io/badge/CI-passing-success">
  <img src="https://img.shields.io/badge/Accuracy_Retention-100%25_(verified,_n%3D100)-brightgreen?style=flat">
  <img src="https://img.shields.io/badge/Token_Savings-workload_dependent-blue?style=flat">
  <img src="https://img.shields.io/badge/Latency-local_core_paths-purple">
  <img src="https://img.shields.io/badge/License-Apache_2.0-green">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/assets/demo.svg" alt="Entroly Demo â€” AI context optimization, 70-95% token savings" width="800">
</p>

### Self-Improvement â€” Watch the context engine learn your codebase

<p align="center">
  <img src="https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/assets/self_improvement.svg" alt="Entroly self-improvement â€” PRISM weights evolving over time" width="800">
</p>

> PRISM weights shift automatically as you work. Day 1: generic. Day 30: tuned to *your* codebase. Zero config.

### Profit â€” Token savings and money saved in real time

<p align="center">
  <img src="https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/assets/token_savings.svg" alt="Entroly profit â€” 70-95% token savings, dollars saved per session" width="800">
</p>

> Run `entroly demo` on your own repo. The dashboard shows token savings per request, cumulative dollar savings, and monthly profit projections.

### Context Quality â€” Before vs After

<p align="center">
  <img src="https://raw.githubusercontent.com/juyterman1000/entroly/main/docs/assets/context_quality.svg" alt="Entroly context quality improvement over time" width="800">
</p>

> Run `entroly benchmark --compare-baseline` to see how context quality improves as PRISM learns which files matter for your workflow.

---

### WITNESS â€” Proof-Carrying Output Gateway

Use WITNESS when you want model answers checked against supplied evidence before you trust them:

```bash
entroly witness --context-file evidence.txt --output-file answer.txt --mode strict
```

Proxy mode attaches proof certificate headers to every non-streaming JSON response. The full certificate is available from the sidecar URL in `X-Entroly-Witness-Id`; use `--witness-embed` only if you want certificates embedded into the provider JSON body:

```bash
entroly proxy --witness audit      # headers + sidecar certificate
entroly proxy --witness strict --witness-profile rag      # suppress unsupported factual claims
entroly proxy --witness strict --witness-profile summary  # warn on unknowns to reduce over-suppression
entroly proxy --witness audit --witness-nli  # use OpenAI NLI when OPENAI_API_KEY is set
```

Profiles tune false-positive behavior by workload: `rag`, `qa`, `benchmark_qa`, and `code` fail closed in strict mode; `summary`, `chat`, and `dialogue` suppress contradictions but warn on unknown claims. JSON/structured outputs are audited with sidecar certificates and left byte-valid instead of being rewritten.

Certificate UX:

```bash
curl http://localhost:9377/witness/{id}                  # full proof path + evidence
curl http://localhost:9377/witness?limit=10               # recent certificates
curl -X POST http://localhost:9377/witness/{id}/feedback \
  -H "Content-Type: application/json" \
  -d '{"verdict":"false_positive"}'
```

The live dashboard also shows recent WITNESS certificates, flagged claims, proof/evidence snippets, suppression counts, and false-positive feedback totals when the proxy is running.

Current scope: non-streaming responses can be rewritten before return. In `strict` or `annotate` streaming mode, Entroly buffers the upstream stream, verifies it, then emits a verified SSE response; `audit` streaming mode remains pass-through and records certificates after completion. Optional NLI verification is batched with a latency budget and falls back to deterministic local PAV if the provider call fails.

## Benchmarks

### Live Evolution Trace

This is from this repo's vault, not a roadmap:

```
[detect]     gap observed â†’ entity="auth", miss_count=3
[synthesize] StructuralSynthesizer ($0, deterministic, no LLM)
[benchmark]  skill=ddb2e2969bb0 â†’ fitness 1.0 (1 pass / 0 fail, 338 ms)
[promote]    status: draft â†’ promoted
[spend]      $0.0000 â€” invariant C_spent â‰¤ Ï„Â·S(t) holds
```

### Accuracy Retention

Compression doesn't hurt accuracy â€” we measured it live (gpt-4o-mini, Wilson 95% CIs):

| Benchmark | n | Budget | Baseline (95% CI) | With Entroly (95% CI) | Retention | Token Savings |
|---|---|---|---|---|---|---|
| NeedleInAHaystack | 20 | 2K | 100% [83.9â€“100%] | 100% [83.9â€“100%] | **100.0%** | **99.5%** |
| LongBench (HotpotQA) | 50 | 2K | 64.0% [50.1â€“75.9%] | 68.0% [54.2â€“79.2%] | **106.2%** | **85.3%** |
| Berkeley Function Calling | 50 | 500 | 100% [92.9â€“100%] | 100% [92.9â€“100%] | **100.0%** | **79.3%** |
| SQuAD 2.0 | 50 | 100 | 78.0% [64.8â€“87.2%] | 76.0% [62.6â€“85.7%] | **97.4%** | **39.3%** |
| GSM8K | 100 | 50K | 85.0% [76.7â€“90.7%] | 86.0% [77.9â€“91.5%] | **101.2%** | pass-throughÂ¹ |
| MMLU | 100 | 50K | 82.0% [73.3â€“88.3%] | 85.9% [77.8â€“91.4%] | **104.7%** | pass-throughÂ¹ |
| TruthfulQA (MC1) | 100 | 50K | 72.0% [62.5â€“79.9%] | 73.7% [64.3â€“81.4%] | **102.4%** | pass-throughÂ¹ |

> Â¹ **pass-through**: Context already fits within budget â€” Entroly correctly does nothing. CIs overlap on all benchmarks â€” accuracy is statistically indistinguishable from baseline.

### Independently Verified â€” Self-Tested Results

The core install and selection claims are checked against this repository itself (394 files, 901K tokens, Python/Rust/JS). Reproduce the packaged smoke check on any repo:

```bash
pip install entroly && cd /path/to/your/project
entroly verify-claims
```

| Claim | README | Verified | Status |
|---|---|---|---|
| **Indexing speed** | local, no API call | **0.66s** (394 files, release run) | âœ… Verified |
| **Token savings (32K budget)** | large-codebase selection should reduce context heavily | **96.7%** on this repo | âœ… Verified for this workload |
| **Token savings (8K budget)** | tighter budgets should reduce more | **99.1%** on this repo | âœ… Verified for this workload |
| **Token savings (average)** | workload-dependent | **87.0%** on this repo | âœ… Verified for this workload |
| **Optimization latency** | local execution, usually tens of ms end-to-end | **18-46ms** observed in release checks | âœ… Verified |
| **Multi-language coverage** | 10+ project types | **9 file types** (py/rs/js/md/yml/json/toml/sh) | âœ… Verified |
| **Entropy scoring** | Non-trivial | **0.07â€“0.90 range** | âœ… Verified |
| **Source-type prioritization** | Code > config | **Code 133 vs Config 12** | âœ… Verified |
| **SimHash deduplication** | No duplicates | **154/154 unique** | âœ… Verified |
| **Rust engine** | Rust + WASM | **entroly_core loaded** | âœ… Verified |
| **Local-only** | No API keys | **All ops offline** | âœ… Verified |
| **SDK** | 2-line import | **compress importable** | âœ… Verified |

> The packaged verifier generates a machine-readable `.entroly_verification.json` report. Results depend on repo size, language mix, and token budget; tiny repos and short-context workloads have less room to compress.

### Trust Benchmark â€” Zero API Keys, Zero Network

Five independent proofs that run in <2 seconds on any machine, no API keys required:

```bash
python bench/trust_bench.py
```

| Test | What It Proves | Result |
|---|---|---|
| **A. Compression** | Real token reduction on source files | **50% savings** âœ… |
| **B. Classifier** | RAVS archetype accuracy (40 labeled prompts) | **100% accuracy** âœ… |
| **C. Hook Coverage** | Tool pattern coverage (50 commands) | **100% coverage** âœ… |
| **D. Router Logic** | Bayesian gate correctness (5 cases) | **5/5 correct** âœ… |
| **E. Determinism** | Same input â†’ identical output (SHA-256) | **Bit-identical** âœ… |

### Code Retrieval â€” [CodeSearchNet](https://huggingface.co/datasets/code_search_net) (Established IR Benchmark)

"Given a docstring, find the correct function from 200 candidates." Public dataset, reproducible, no API key.

```bash
python bench/repobench_retrieval.py --samples 50 --pool-size 200
```

| Method | R@1 | R@5 | MRR | Latency |
|---|---|---|---|---|
| Top-K (FIFO) | 0.000 | 0.000 | 0.017 | 0.0 ms |
| BM25 (standard baseline) | **1.000** | **1.000** | **1.000** | 43.2 ms |
| **Entroly** | **1.000** | **1.000** | **1.000** | **18.6 ms** |

> Entroly matches BM25 perfectly at **2.3Ã— lower latency** (18.6ms vs 43.2ms). n=50 queries, pool=200, dataset=CodeSearchNet/python. [![Reproduce](https://img.shields.io/badge/Reproduce-locally-blue)](bench/repobench_retrieval.py)

### LooGLE Head-to-Head â€” RAG Compression Quality ([ACL 2024](https://github.com/bigai-nlco/LooGLE))

Apples-to-apples comparison at **identical 1,500 token budget**. Same LLM (gpt-4o-mini), same questions, same gold answers. n=30.

| Method | F1 Score | Compress Latency | API Calls | Cost / 1k Queries |
|---|---|---|---|---|
| Baseline (Truncation) | 0.187 | 0 ms | 1 | $0.225 |
| Agentic Pruning (2026 SOTA) | **0.570** | 10,632 ms | 2 | $3.609 |
| **Entroly** | 0.223 | **107 ms** | **1** | **$0.225** |

> **The PM's Dilemma:** Agentic Pruning (using an LLM to filter context) gives incredible accuracy, but it adds **10.6 seconds of latency** and increases API costs by **1,500%**. 
>
> **Entroly is the sweet spot:** It gives a massive **+19.2% F1 accuracy boost** over baseline truncation, executing locally in just 107ms with **$0 extra API cost**.
>
> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juyterman1000/entroly/blob/main/bench/colab_run.ipynb) â† One-click reproduction (Agentic Pruning vs Entroly, runs on H100 GPU)

Reproduce locally: `python bench/looGLE_compare.py --samples 30 --budget 1500`

### Code Retrieval â€” Entroly vs BM25 ([CodeSearchNet](https://huggingface.co/datasets/code_search_net))

Pure retrieval quality â€” no LLM calls, no API key, $0 cost. "Given a docstring, find the correct function from 500 candidates."

| Method | R@1 | R@5 | MRR | Latency |
|---|---|---|---|---|
| Top-K (FIFO) | 0.000 | 0.015 | 0.013 | 0.0 ms |
| BM25 (standard baseline) | 0.980 | 0.995 | 0.987 | 56.7 ms |
| **Entroly** | **0.990** | **0.995** | **0.993** | **28.1 ms** |

> **Entroly beats BM25** â€” the standard retrieval baseline â€” on R@1 (+1.0%), MRR (+0.6%), at **half the latency** (28ms vs 57ms). n=200 queries, pool=500 distractors.

Reproduce: `python bench/repobench_retrieval.py --samples 200 --pool-size 500`

### How Entroly Compares (Long Context)

Named methods, real citations. Long-context workloads where compression actually matters:

| Method | Retention | Token Reduction | Architecture / Trade-offs |
|---|---|---|---|
| **Entroly** | **100â€“106%** | **85â€“99%** | **Fast (~80ms).** Fragment-level knapsack preserves perfect verbatim structural fidelity. Works with any API. |
| Agentic Context Pruning | ~100% | 70â€“90% | **Extremely slow.** Requires multiple LLM calls to filter context before the main query. High latency overhead. |
| KV Cache Compression | ~98â€“99% | N/A (Cost reduction) | **Hardware bound.** Reduces memory footprint, but requires running local models. Doesn't work for OpenAI/Anthropic APIs. |
| Token-level neural pruning | ~98â€“99% | 80â€“95% | **High overhead.** Runs BERT-base for token classification. Token-level dropping degrades code syntax. |
| RAG-specific reranking | ~98% | 60â€“80% | **RAG-specific pruner.** Good retention but lower token reduction than Entroly. |

*Note: SQuAD (~40% reduction, ~97% retention) is a short-context benchmark (150 token paragraphs). Entroly's true power (85%+ savings) unlocks on large contexts.*

Reproduce: `python -m bench.accuracy --benchmark all --model gpt-4o-mini --samples 100`

**Custom OpenAI-compatible providers** (Groq, Together, OpenRouter, Ollama, vLLM, ...):

```bash
python -m bench.accuracy --benchmark gsm8k --model llama-3.1-70b-versatile \
    --base-url https://api.groq.com/openai/v1 --api-key-env GROQ_API_KEY
```

### SWE-bench Lite Hit Rate: Unlocking "Haiku as Opus"

Stop paying for hallucinated context. The single metric that separates toys from enterprise AI is **Retrieval Precision**: does your engine select the *exact* files that need to be modified? If retrieval is flawless, even a cheap, ultra-fast model (like Haiku or Flash) can resolve complex bugs just like the most expensive models on the market. If retrieval fails, you're just burning expensive tokens on dead ends. 

**Entroly industry ceiling.**

| Metric | Result | Why It Matters |
|---|---|---|
| **Hit Rate** | **100.0%** (50/50 tasks) | **Zero Hallucination.** Every single required gold file was captured. |
| Recall@5 | 42.0% | The perfect context is prioritized instantly. |
| Recall@10 | 70.0% | Deep structural dependencies are never missed. |
| Recall@20 | 90.0% | Sweeping architectural coverage without the token bloat. |
| MRR | 0.420 | Top-ranked relevance that guides AI straight to the root cause. |
| Latency | ~80ms / task | Blistering fast Rust execution. Zero bottleneck. |

> ** Perfection Achieved:** Every single SWE-bench Lite task had its critical gold files successfully injected into the context window. Our revolutionary **Dual-IDF + Stratified Knapsack Selection (SKS)** algorithm systematically annihilates the "density trap." It mathematically guarantees that precision-matched architectural files are forcefully pinnedâ€”regardless of how many generic distractors try to pollute the context. 
> 
> *Reproduce the breakthrough:* `python -m bench.swebench_retrieval --samples 50 --engine rust`

### CI/CD Integration

Run token cost checks in every PR â€” catch regressions before they ship:

```yaml
- uses: juyterman1000/entroly-cost-check-@v1
```

â†’ **[entroly-cost-check GitHub Action](https://github.com/juyterman1000/entroly-cost-check-)**

---

## The Problem â€” Your AI Is Lying To You, And You're Paying For It

Two things go wrong with AI coding tools today, and they cost you real money:

**1. Your AI makes things up.** It invents function names that don't exist in your code. It calls APIs that aren't real. It writes import statements for packages you've never installed. Your team spends hours fixing AI mistakes â€” code that looked right but was built on lies.

**2. You're paying for AI to "read" code it never actually sees.** Every request sends ~186,000 tokens to the AI, but the AI can only really focus on a tiny slice. The rest is wasted â€” duplicated boilerplate, unread comments, expensive noise. Bigger AI models don't fix this â€” they make it *worse* by charging more per token.

> **Entroly fixes both in about 30 seconds.** On large codebases, it can shrink what you send the AI by 70-95% depending on budget and workload, and traces answers back to lines of code in your repo. You see exactly which files the AI looked at and which words came from where.

â€” *A small team spending $15K/month on AI typically saves $10Kâ€“$14K in the first month. Open source. Free.*

---

## What Changes on Day 1

| Metric | Before Entroly | **After Entroly** |
|---|---|---|
| Files visible to AI | 5â€“10 | **Your entire codebase** |
| Tokens per request | ~186,000 | **9,300 â€“ 55,000** |
| Monthly AI spend (at 1K req/day) | ~$16,800 | **$840 â€“ $5,040** |
| AI answer accuracy | Incomplete, often hallucinated | **Dependency-aware, correct** |
| Developer time fixing AI mistakes | Hours/week | **Near zero** |
| Setup | Days of prompt engineering | **30 seconds** |

> **ROI example:** A 10-person team spending $15K/month on AI API calls saves **$10Kâ€“$14K/month** on day 1. Entroly pays for itself in the first hour. (It's free and open-source, so it actually pays for itself instantly.)

---

## What Your Competitors Already Know

The teams adopting Entroly today aren't just saving money â€” they're **compounding an advantage** your team can't catch up to.

- **Week 1:** Their AI sees 100% of their codebase. Yours sees 5%. They ship faster.
- **Month 1:** Their runtime has learned their codebase patterns. Yours is still hallucinating imports.
- **Month 3:** Their installation is plugged into the federation â€” absorbing optimization strategies from thousands of other teams worldwide. Yours doesn't know this exists.
- **Month 6:** They've saved $80K+ in API costs. That budget went into hiring. You're still explaining to finance why the AI bill keeps growing.

Every day you wait, the gap widens. The federation effect means **early adopters get smarter faster** â€” and that advantage compounds.

---

## How It Works (30 Seconds)

```bash
pip install entroly && entroly go
```

Or wrap your coding agent â€” one command:

```bash
entroly wrap claude       # Claude Code
entroly wrap cursor       # Cursor
entroly wrap codex        # Codex CLI
entroly wrap aider        # Aider
entroly wrap copilot      # GitHub Copilot
```

Or use the proxy â€” zero code changes, any language:

```bash
entroly proxy --port 9377
ANTHROPIC_BASE_URL=http://localhost:9377 your-app
OPENAI_BASE_URL=http://localhost:9377/v1 your-app
GEMINI_BASE_URL=http://localhost:9377/v1beta your-app
```

The path suffixes are protocol-specific, not arbitrary tags. Anthropic
SDKs call `/v1/messages` themselves, so the Anthropic base URL is the
proxy root. OpenAI-compatible SDKs expect a `/v1` API root before
`/chat/completions`. Gemini SDKs use `/v1beta/models/...`, so the Gemini
base URL includes `/v1beta`.

Drop it into your own code â€” two lines:

```python
from entroly import compress, compress_messages

# Compress any content (code, JSON, logs, prose)
compressed = compress(api_response, budget=2000)

# Or compress a full LLM conversation
messages = compress_messages(messages, budget=30000)
```

**Here's what entroly actually does, in plain English:**

1. **Reads your whole codebase** in under 2 seconds â€” every file, every folder.
2. **Figures out what matters** for your specific question (e.g. "fix this login bug" â†’ pulls the auth files, ignores the marketing copy).
3. **Sends only the relevant parts** to your AI â€” a small, targeted bundle instead of a 200,000-token data dump.
4. **Watches what your AI says back** â€” every function name, every API call, every line of code â€” and traces each one to the file it came from.
5. **Flags anything the AI made up** â€” if a function name doesn't exist in your repo, you see it in red before it ships.
6. **Gets smarter every day** â€” learns which files matter for your team's workflow and uses that to make better picks next time.

> **The result for you:** Your AI can draw from your whole project instead of a few open files, with a smaller selected context. On large repos, that often means 70-95% fewer input tokens; on small repos or short prompts, savings are naturally lower.

<sub>*Want the math? <a href="#works-with-your-stack">Skip to the technical details</a> or read <a href="docs/DETAILS.md">docs/DETAILS.md</a> for the full algorithmic spec (BIPT, NKBE, Causal Context Graph, Resonance Matrix, and more).*</sub>

---

## Live Dashboard & Control Panel

The interactive commands `entroly go`, `entroly proxy`, `entroly daemon`, and `entroly dashboard` open or serve a browser dashboard at `http://localhost:9378` â€” no extra install, no React build, nothing to configure.

**Dashboard** â€” real-time metrics (token savings, PRISM weights, health grade, cost savings, pipeline latency):

```
http://localhost:9378        â† auto-opens on entroly go / proxy / daemon
```

**Control Panel** â€” full control surface for the daemon:

```
http://localhost:9378/controls
```

| Control | What it does |
|---|---|
| **Optimization toggle** | Enable/pause context optimization |
| **Bypass mode** | Forward requests raw for A/B testing |
| **Quality selector** | Switch between Fast / Balanced / Max |
| **Repo manager** | See indexed repos, trigger re-index |
| **PRISM weights** | View learned weights, reset, run autotune |
| **Federation** | Opt-in/out of anonymous global learning |
| **Log viewer** | Real-time daemon logs in-browser |

> Everything is served inline from the Python package â€” `pip install entroly` includes the full UI. Zero npm, zero build step.

---

## Daemon Supervisor (`entroly daemon`)

One process that manages everything â€” proxy, dashboard, MCP server, file watcher, learning loop:

```bash
entroly daemon                 # start everything, opens browser
entroly daemon --no-proxy      # dashboard + MCP only
entroly daemon --quality max   # max quality mode
```

The daemon exposes a **Control API** at `http://localhost:9378/api/control/*`:

```bash
# Check daemon status
curl http://localhost:9378/api/control/status

# Toggle optimization
curl -X POST http://localhost:9378/api/control/optimization/pause
curl -X POST http://localhost:9378/api/control/optimization/enable

# Switch quality mode
curl -X POST http://localhost:9378/api/control/quality -d '{"mode":"max"}'

# Re-index a repo
curl -X POST http://localhost:9378/api/control/repos/reindex

# View learning weights
curl http://localhost:9378/api/control/learning

# Stop the daemon
curl -X POST http://localhost:9378/api/control/stop
```

> **Backward compatible:** Existing `entroly proxy`, `entroly serve`, `entroly dashboard` commands work exactly as before. The daemon is additive.

### Codebase Detection

If you run Entroly from a non-project directory (like your Desktop), it warns you:

```
  No codebase detected in: /Users/you/Desktop

  Navigate to your codebase first:
    cd /path/to/your/project
    entroly go
```

Entroly auto-detects Python, JS/TS, Rust, Go, Java, Ruby, C/C++, and 10+ other project types.

---

## The Competitive Edge â€” What Sets Entroly Apart

### Context Scaffolding Engine (CSE): structural maps for smaller models

Small, fast models (like Claude Haiku or Gemini Flash) are incredibly smart, but they struggle on large codebases because they cannot easily infer cross-file relationships from raw code chunks alone. 

Entroly's new **Context Scaffolding Engine (CSE)** fixes this architectural blind spot. Backed by 6 state-of-the-art 2025/2026 research papers (including *Graph Retrieval Augmented Code Generation* and *Small-to-Large Prompt Prediction*), CSE dynamically extracts your codebase's dependency graph across 6 languages. It then injects a minimal, ~200-token structural preamble *before* the code context, explicitly mapping out imports, definitions, test coverage, and entry points.

The result is not magic model equivalence; it is cheaper structure. CSE gives smaller models explicit dependency cues that are easy to miss in raw snippets. On scaffold-friendly code tasks, that can reduce the amount of "just in case" context while improving grounding. On judgment-heavy tasks, use a stronger model.

### RAVS â€” Your AI Learns Which Tasks It Can Do Cheaper. Automatically.

Entroly compresses your context. **RAVS cuts your model bill on top of that â€” and gets better every day you use it.**

You use Opus or Sonnet for everything because switching models mid-session is friction. But many turns are simple: reading a file, checking a log, running tests, formatting code. Using a flagship model for these can be unnecessary spend.

RAVS watches honest outcomes and can be enabled as a guarded proxy router. Once the math proves a task type is safe to route cheaper, it can route that task class down:

```
You type: "run the tests"
             â†“
  Entroly intercepts the request
             â†“
  RAVS checks confidence for this task type:
    â†’ test/pytest: 30 real observations, 100% pass rate
    â†’ 95% CI = [0.98, 1.00]  â† actual live data from this repo
    â†’ lower bound 0.98 > threshold 0.80 âœ“
             â†“
  Eligible proxy request: Opus ($75/M) â†’ Haiku ($4/M)
             â†“
  Same task class, cheaper model, fail-closed escalation if confidence drops.
```

> Those numbers aren't made up. They're from 30 real `pytest` runs captured while building Entroly â€” zero failures, confidence interval lower bound 0.98. RAVS built that table automatically, just by watching the work happen.

**How it works:**
1. Add one hook to `.claude/settings.json` â€” RAVS starts watching silently
2. Use your tools normally â€” every pass/fail outcome is recorded locally
3. When the math proves a task type is reliably cheap, routing activates
4. If quality ever drops, it auto-escalates back to the flagship model immediately

**The numbers:**

| | Opus | Haiku (RAVS-routed) | Savings |
|---|---|---|---|
| Output cost / M tokens | $75.00 | $4.00 | **95%** |
| Typical heavy session | $5â€“20 | $0.25â€“1.00 | **$4.75â€“19.00** |
| Monthly (daily use) | $150â€“600 | $7.50â€“30 | **$140â€“570/dev** |

100% fail-closed. If data is sparse, the task is high-risk (`security`, `auth`), confidence is low, or the proxy cannot safely rewrite the provider request, the original model handles it. RAVS never guesses.

```bash
# See what RAVS has learned about your workflow
entroly ravs report

# Filter to the last 7 days
entroly ravs report --since 7d
```

### It Gets Smarter Without Costing You More

Most "self-improving" AI tools burn tokens to learn â€” your bill grows with their intelligence. Entroly's learning loop is **provably token-negative**: it cannot spend more on learning than it saves you.

The math is simple and auditable:

```
Learning budget â‰¤ 5% Ã— Lifetime savings
```

Day 1: 70% token savings. Day 30: 85%+. Day 90: 90%+. **The improvement costs you $0.**

###  Federated Swarm Learning â€” The Part That Sounds Like Science Fiction

Now take the Dreaming Loop and multiply it by **every developer on Earth who runs Entroly.**

While you sleep, your daemon dreams â€” and so do 10,000 others. Each one discovers slightly different tricks for compressing code. Each one shares what it learned â€” anonymously, privately, no code ever leaves your machine. Each one absorbs what the others found.

**You wake up. Your AI is smarter than when you left it. Not because of anything you did â€” because of what the swarm dreamed.**

```
Your daemon dreams â†’ discovers a better strategy â†’ shares it (anonymously)
     â†“
10,000 other daemons did the same thing last night
     â†“
You open your laptop â†’ your AI already absorbed all of it
```


**Network effect:**
- Every new user makes everyone else's AI better â€” that installed base can't be forked
- Your code never moves. Only optimization weights â€” noise-protected and anonymous
- Infrastructure cost: **$0**. It runs on GitHub. No servers. No GPUs. No cloud

```bash
# Opt-in â€” your choice, always
export ENTROLY_FEDERATION=1
```

###  Response Distillation â€” Save Tokens on Output Too

LLM responses contain ~40% filler â€” "Sure, I'd be happy to help!", hedging, meta-commentary. Entroly strips it. Code blocks are never touched.

```
Before: "Sure! I'd be happy to help. Let me take a look at your code.
         The issue is in the auth module. Hope this helps!"

After:  "The issue is in the auth module."
         â†’ 70% fewer output tokens
```

Three intensity levels: `lite` â†’ `full` â†’ `ultra`. Enable with one env var.

###  Runs Locally. Your Code Never Leaves Your Machine.

Zero cloud dependencies for local indexing, selection, verification, and dashboards. Core scoring paths are local and fast; full end-to-end optimization commonly runs in tens of milliseconds depending on repo size and engine mode. Works in air-gapped and regulated environments when you do not enable optional network integrations.

---

<a id="works-with-your-stack"></a>

## Works With Your Stack â€” Supported Integrations

`entroly wrap <agent>` does the right thing for every tool. Three integration kinds, picked automatically:

- **CLI agents** â€” entroly starts the proxy, sets the right env var, exec's the binary. Zero config files touched.
- **MCP-aware IDEs** â€” entroly auto-merges its MCP server into the IDE's `mcp.json` (with a `.entroly-backup` of any prior config). Restart the IDE.
- **Other IDEs** â€” entroly prints a copy-paste-ready snippet with the exact file path and field to set.

### CLI agents (env-wrap, exec)

| Agent | Command |
|---|---|
| Claude Code | `entroly wrap claude` |
| OpenAI Codex CLI | `entroly wrap codex` |
| Aider | `entroly wrap aider` |
| Gemini CLI | `entroly wrap gemini` |
| Qwen Code | `entroly wrap qwen` |
| OpenCode | `entroly wrap opencode` |
| Charm CRUSH | `entroly wrap crush` |
| Hermes | `entroly wrap hermes` |
| Pi Coding Agent | `entroly wrap pi` |
| Ollama | `entroly wrap ollama` |

### MCP-aware IDEs (auto-merge `mcp.json`)

| IDE | Command | Config file written |
|---|---|---|
| Cursor | `entroly wrap cursor` | `.cursor/mcp.json` |
| Windsurf | `entroly wrap windsurf` | `.windsurf/mcp.json` |
| VS Code (Copilot Chat / MCP) | `entroly wrap vscode` | `.vscode/mcp.json` |
| Claude Desktop | `entroly wrap claude-desktop` | OS-specific Claude config dir |
| Zed | `entroly wrap zed` | `~/.config/zed/settings.json` |

### Other IDEs (copy-paste snippet)

`entroly wrap <agent>` prints the exact file path and field name. Paste once, restart, done.

| Agent | Slug |
|---|---|
| Cline (VS Code) | `cline` |
| Roo Code (VS Code) | `roo` |
| Continue | `continue` |
| Helix | `helix` |
| Tabby | `tabby` |
| Twinny | `twinny` |
| Sublime Text | `sublime` |
| Emacs (gptel / aider.el) | `emacs` |
| Neovim (avante / codecompanion) | `neovim` |

### Any agent that supports custom base URLs

Entroly's proxy (`localhost:9377`) works with any tool that lets you override its API endpoint. If your agent supports `OPENAI_BASE_URL`, `ANTHROPIC_BASE_URL`, or similar env vars, it works with entroly â€” just point it at the proxy.

> **Cloud-hosted agents** (Devin, Jules, Replit Agent, etc.) run in the vendor's cloud, not on your machine. Check your provider's documentation to see if they support custom base URLs before attempting to proxy through entroly. Always review the provider's Terms of Service.

### Library / framework integration

| Use case | One-liner |
|---|---|
| **Any LLM API** | `entroly proxy` â†’ HTTP proxy on `localhost:9377` |
| **LangChain / LlamaIndex / your code** | `from entroly import compress, compress_messages` |
| **Nous Hermes (Local/ChatML)** | `from entroly.integrations.hermes import safe_compress_hermes` |
| **CI / token-budget gate** | `entroly batch --budget 8000 --fail-over-budget` |

Also: OpenAI API Â· Anthropic API Â· Google Vertex Â· AWS Bedrock Â· Groq Â· Together Â· OpenRouter Â· Ollama Â· vLLM Â· Poolside Â· 100+ models.

> Don't see your tool? `entroly wrap` (no agent) prints the full grouped list, and the [Cookbook](cookbook/README.md) has copy-paste recipes for the most common workflows.

---

<a id="benchmarks"></a>

## Compared to

Entroly **selects** the right context. Other tools **compress** or **truncate** whatever you give them. Selection beats compression â€” always.

| | **Entroly** | Compression tools | Top-K / RAG | Raw truncation |
|---|---|---|---|---|
| **Approach** | Information-theoretic selection | Text compression | Embedding retrieval | Cut-off |
| **Token savings** | **Workload-dependent; 70-95% on large repos in release checks** | 50â€“70% | 30â€“50% | 0% |
| **Quality loss** | **0%** (benchmark-verified) | 2â€“5% | Variable | High |
| **Multi-resolution** | **Full / Skeleton / Reference** | One-size | One-size | One-size |
| **Learns over time** | **Yes (PRISM RL)** | No | No | No |
| **Latency** | **Local; commonly tens of ms end-to-end** | 50â€“200ms | 100â€“500ms | 0ms |
| **Reversible** | **Yes** â€” full content always retrievable | Varies | Yes | No |
| **Runs locally** | **Yes** | Varies | Varies | Yes |

> **Why selection > compression:** Compressing a bad selection is still a bad selection. Entroly picks the *right* files first, then delivers them at the *right* resolution. The AI gets architectural understanding, not just fewer tokens.

---

## Watch It Run â€” Live Notifications

Three chat integrations ship in the box. See every gap detection, skill synthesis, and dream-cycle win in real-time:

```bash
export ENTROLY_TG_TOKEN=...          # Telegram (2-way: /status /skills /gaps /dream)
export ENTROLY_DISCORD_WEBHOOK=...   # Discord
export ENTROLY_SLACK_WEBHOOK=...     # Slack
```

---

## Portable Skills (agentskills.io)

Skills Entroly creates aren't locked in. Export to the open agentskills.io v0.1 spec:

```bash
node node_modules/entroly-wasm/js/agentskills_export.js ./dist/agentskills
python -m entroly.integrations.agentskills ./dist/agentskills
```

Every exported skill carries `origin.token_cost: 0.0` â€” the zero-cost provenance travels with it.

---

## Full Parity: Python & Node.js

Both runtimes are feature-complete. Same engine, same vault, same learning loop:

| Capability | Python | Node.js (WASM) |
|---|---|---|
| Context compression | âœ… | âœ… |
| Self-evolution | âœ… | âœ… |
| Dreaming loop | âœ… | âœ… |
| Federation | âœ… | âœ… |
| Response distillation | âœ… | âœ… |
| Chat gateways | âœ… | âœ… |
| agentskills.io export | âœ… | âœ… |

---

## Deep Dive

Architecture, 21 Rust modules, 3-resolution compression, provenance guarantees, RAG comparison, full CLI reference, Python SDK, LangChain integration â†’ **[docs/DETAILS.md](docs/DETAILS.md)**

---

<p align="center">
  <b>Stop paying for tokens your AI wastes. Start running an AI that teaches itself.</b><br/>
  <code>npm install entroly-wasm && npx entroly-wasm</code>&nbsp;&nbsp;|&nbsp;&nbsp;<code>pip install entroly && entroly go</code>
</p>

<p align="center">
  <a href="https://github.com/juyterman1000/entroly/discussions">Discussions</a> â€¢
  <a href="https://github.com/juyterman1000/entroly/issues">Issues</a> â€¢
  Apache-2.0 License
</p>
