//! WITNESS deterministic core.
//!
//! Python owns API/proxy integration and optional LLM-backed NLI. The production
//! local proof engine lives here so the default path is fast, deterministic, and
//! wheel-packaged with the rest of Entroly's Rust core.

use regex::Regex;
use serde::{Deserialize, Serialize};
use std::collections::HashSet;
use std::sync::OnceLock;
use std::time::Instant;

static WORD_RE: OnceLock<Regex> = OnceLock::new();
static NUMBER_RE: OnceLock<Regex> = OnceLock::new();
static ENTITY_RE: OnceLock<Regex> = OnceLock::new();
static CAPS_RE: OnceLock<Regex> = OnceLock::new();
static QUOTED_RE: OnceLock<Regex> = OnceLock::new();

fn word_re() -> &'static Regex {
    WORD_RE.get_or_init(|| Regex::new(r"\b[A-Za-z][A-Za-z0-9_-]{3,}\b").expect("valid word regex"))
}

fn number_re() -> &'static Regex {
    NUMBER_RE.get_or_init(|| Regex::new(r"\$?\d[\d,]*(?:\.\d+)?%?").expect("valid number regex"))
}

fn entity_re() -> &'static Regex {
    ENTITY_RE.get_or_init(|| {
        Regex::new(r"\b[A-Z][a-zA-Z0-9]*(?:\s+[A-Z][a-zA-Z0-9]*){0,4}\b")
            .expect("valid entity regex")
    })
}

fn caps_re() -> &'static Regex {
    CAPS_RE.get_or_init(|| Regex::new(r"\b[A-Z][A-Z0-9]{1,}\b").expect("valid caps regex"))
}

fn quoted_re() -> &'static Regex {
    QUOTED_RE.get_or_init(|| Regex::new(r#""([^"]{2,90})""#).expect("valid quote regex"))
}

fn stopwords() -> &'static HashSet<&'static str> {
    static STOPWORDS: OnceLock<HashSet<&'static str>> = OnceLock::new();
    STOPWORDS.get_or_init(|| {
        [
            "about", "after", "again", "against", "also", "although", "among", "another", "before",
            "being", "between", "both", "could", "does", "doing", "done", "each", "either",
            "every", "first", "from", "have", "into", "just", "last", "like", "made", "make",
            "many", "more", "most", "much", "only", "other", "over", "should", "some", "such",
            "than", "that", "their", "them", "then", "there", "these", "they", "this", "those",
            "very", "were", "what", "when", "where", "which", "while", "with", "would", "yes",
            "sure", "okay", "actually", "believe",
        ]
        .into_iter()
        .collect()
    })
}

fn question_starters() -> &'static HashSet<&'static str> {
    static STARTERS: OnceLock<HashSet<&'static str>> = OnceLock::new();
    STARTERS.get_or_init(|| {
        [
            "who", "what", "when", "where", "why", "how", "which", "whose", "is", "are", "was",
            "were", "do", "does", "did", "can", "could", "should", "would",
        ]
        .into_iter()
        .collect()
    })
}

fn number_words() -> &'static [(&'static str, i32)] {
    &[
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("ten", 10),
        ("eleven", 11),
        ("twelve", 12),
    ]
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Claim {
    pub id: usize,
    pub text: String,
    pub start: usize,
    pub end: usize,
    pub kind: String,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct EvidenceWindow {
    pub text: String,
    pub score: f64,
    pub adequacy: f64,
    pub entity_coverage: f64,
    pub number_coverage: f64,
    pub token_coverage: f64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ProofStep {
    pub operator: String,
    pub evidence: String,
    pub strength: f64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Certificate {
    pub claim_id: usize,
    pub claim_text: String,
    pub label: String,
    pub support_strength: f64,
    pub contradiction_strength: f64,
    pub evidence_adequacy: f64,
    pub risk: f64,
    pub proof_path: Vec<ProofStep>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct WitnessResult {
    pub output: String,
    pub certificates: Vec<Certificate>,
    pub summary_score: f64,
    pub n_grounded: usize,
    pub n_unsupported: usize,
    pub n_contradicted: usize,
    pub n_unknown: usize,
    pub latency_ms: f64,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct WitnessRewrite {
    pub output: String,
    pub changed: bool,
    pub mode: String,
    pub profile: String,
    pub flagged_count: usize,
    pub suppressed_count: usize,
    pub warned_count: usize,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct WitnessPayload {
    pub witness: WitnessResult,
    pub policy: WitnessRewrite,
    pub output: String,
}

#[derive(Clone, Copy, Debug)]
pub struct WitnessConfig {
    pub support_threshold: f64,
    pub contradiction_threshold: f64,
    pub adequacy_threshold: f64,
}

impl Default for WitnessConfig {
    fn default() -> Self {
        Self {
            support_threshold: 0.62,
            contradiction_threshold: 0.70,
            adequacy_threshold: 0.72,
        }
    }
}

pub fn analyze(context: &str, output: &str, config: WitnessConfig) -> WitnessResult {
    let t0 = Instant::now();
    let mut certificates = Vec::new();
    for claim in extract_claims(output) {
        certificates.push(certify_claim(&claim, context, config));
    }

    let mut n_grounded = 0;
    let mut n_unsupported = 0;
    let mut n_contradicted = 0;
    let mut n_unknown = 0;
    for cert in &certificates {
        match cert.label.as_str() {
            "grounded" => n_grounded += 1,
            "unsupported" => n_unsupported += 1,
            "contradicted" => n_contradicted += 1,
            "unknown" => n_unknown += 1,
            _ => {}
        }
    }

    let summary_score = if certificates.is_empty() {
        1.0
    } else {
        let risk_sum: f64 = certificates.iter().map(|c| c.risk).sum();
        (1.0 - risk_sum / certificates.len() as f64).clamp(0.0, 1.0)
    };

    WitnessResult {
        output: output.to_string(),
        certificates,
        summary_score,
        n_grounded,
        n_unsupported,
        n_contradicted,
        n_unknown,
        latency_ms: t0.elapsed().as_secs_f64() * 1000.0,
    }
}

pub fn analyze_with_policy(
    context: &str,
    output: &str,
    mode: &str,
    profile: &str,
    config: WitnessConfig,
) -> WitnessPayload {
    let witness = analyze(context, output, config);
    let policy = apply_policy(output, &witness, mode, profile, 6);
    let rewritten_output = policy.output.clone();
    WitnessPayload {
        witness,
        policy,
        output: rewritten_output,
    }
}

pub fn extract_claims(output: &str) -> Vec<Claim> {
    candidate_claim_segments(output)
        .into_iter()
        .filter_map(|(start, segment)| {
            let text = clean_claim_segment(&segment);
            if !is_claim_like(&text) {
                return None;
            }
            let kind = classify_claim(&text);
            Some((start, text, kind))
        })
        .enumerate()
        .map(|(id, (start, text, kind))| Claim {
            id,
            end: start + text.len(),
            start,
            text,
            kind,
        })
        .collect()
}

pub fn select_evidence_windows(
    context: &str,
    claim: &str,
    top_k: usize,
) -> (Vec<EvidenceWindow>, f64) {
    let claim_words = content_words(claim);
    let entities = extract_entities(claim);
    let numbers = extract_numbers(claim);
    let mut windows = Vec::new();

    for text in sentence_windows(context, 900) {
        let lower = text.to_lowercase();
        let words = content_words(&text);
        let entity_cov = coverage_fraction(&entities, &lower);
        let number_cov = coverage_fraction(&numbers, &lower);
        let token_cov = intersection_ratio(&claim_words, &words);
        let adequacy = weighted_adequacy(
            entity_cov,
            number_cov,
            token_cov,
            !entities.is_empty(),
            !numbers.is_empty(),
        );
        let score = 3.0 * entity_cov + 2.0 * number_cov + token_cov + adequacy;
        windows.push(EvidenceWindow {
            text,
            score,
            adequacy,
            entity_coverage: entity_cov,
            number_coverage: number_cov,
            token_coverage: token_cov,
        });
    }

    windows.sort_by(|a, b| {
        b.score
            .partial_cmp(&a.score)
            .unwrap_or(std::cmp::Ordering::Equal)
            .then_with(|| {
                b.adequacy
                    .partial_cmp(&a.adequacy)
                    .unwrap_or(std::cmp::Ordering::Equal)
            })
            .then_with(|| b.text.len().cmp(&a.text.len()))
    });
    let top: Vec<EvidenceWindow> = windows.into_iter().take(top_k).collect();
    let combined = top
        .iter()
        .map(|w| w.text.as_str())
        .collect::<Vec<_>>()
        .join("\n");
    let combined_lower = combined.to_lowercase();
    let mut combined_words = HashSet::new();
    for window in &top {
        combined_words.extend(content_words(&window.text));
    }
    let combined_adequacy = weighted_adequacy(
        coverage_fraction(&entities, &combined_lower),
        coverage_fraction(&numbers, &combined_lower),
        intersection_ratio(&claim_words, &combined_words),
        !entities.is_empty(),
        !numbers.is_empty(),
    );
    let best = top
        .iter()
        .map(|w| w.adequacy)
        .fold(combined_adequacy, f64::max);
    (top, best)
}

pub fn apply_policy(
    output: &str,
    result: &WitnessResult,
    mode: &str,
    profile: &str,
    max_items: usize,
) -> WitnessRewrite {
    let normalized_mode = mode.trim().to_lowercase();
    let normalized_profile = normalize_profile(profile, output);
    let flagged: Vec<&Certificate> = result
        .certificates
        .iter()
        .filter(|cert| cert.label != "grounded")
        .collect();

    if normalized_mode == "off" || normalized_mode == "audit" {
        return WitnessRewrite {
            output: output.to_string(),
            changed: false,
            mode: normalized_mode,
            profile: normalized_profile,
            flagged_count: flagged.len(),
            suppressed_count: 0,
            warned_count: 0,
        };
    }

    if flagged.is_empty() {
        return WitnessRewrite {
            output: output.to_string(),
            changed: false,
            mode: normalized_mode,
            profile: normalized_profile,
            flagged_count: 0,
            suppressed_count: 0,
            warned_count: 0,
        };
    }

    if normalized_mode == "annotate" {
        let mut rewritten = output.trim_end().to_string();
        rewritten.push_str("\n\n[Entroly WITNESS] Verification warnings:");
        for cert in flagged.iter().take(max_items) {
            rewritten.push_str(&format!("\n- {}: {}", cert.label, cert.claim_text));
        }
        if flagged.len() > max_items {
            rewritten.push_str(&format!("\n- ... {} more", flagged.len() - max_items));
        }
        return WitnessRewrite {
            output: rewritten,
            changed: true,
            mode: normalized_mode,
            profile: normalized_profile,
            flagged_count: flagged.len(),
            suppressed_count: 0,
            warned_count: flagged.len(),
        };
    }

    if normalized_mode == "strict" {
        let mut rewritten = output.to_string();
        let suppressed: Vec<&Certificate> = flagged
            .iter()
            .copied()
            .filter(|cert| should_suppress(cert, &normalized_profile))
            .collect();
        let warned: Vec<&Certificate> = flagged
            .iter()
            .copied()
            .filter(|cert| !should_suppress(cert, &normalized_profile))
            .collect();
        let suppressed_count = suppressed.len();
        let warned_count = warned.len();
        let mut sorted = suppressed;
        sorted.sort_by_key(|b| std::cmp::Reverse(b.claim_text.len()));
        for cert in sorted {
            rewritten = remove_claim_text(&rewritten, &cert.claim_text);
        }
        rewritten = cleanup_rewritten_output(&rewritten);
        if suppressed_count > 0 && rewritten.trim().is_empty() {
            rewritten =
                "Entroly WITNESS suppressed this answer because its factual claims lacked support."
                    .to_string();
        } else if suppressed_count > 0 && rewritten != output {
            rewritten.push_str(&format!(
                "\n\n[Entroly WITNESS suppressed {} unsupported factual claim(s).]",
                suppressed_count
            ));
        }
        if warned_count > 0 {
            rewritten.push_str(
                "\n\n[Entroly WITNESS warning: some factual claims could not be fully verified:",
            );
            for cert in warned.iter().take(max_items) {
                rewritten.push_str(&format!("\n- {}: {}", cert.label, cert.claim_text));
            }
            if warned_count > max_items {
                rewritten.push_str(&format!("\n- ... {} more", warned_count - max_items));
            }
            rewritten.push(']');
        }
        return WitnessRewrite {
            changed: rewritten != output,
            output: rewritten,
            mode: normalized_mode,
            profile: normalized_profile,
            flagged_count: flagged.len(),
            suppressed_count,
            warned_count,
        };
    }

    WitnessRewrite {
        output: output.to_string(),
        changed: false,
        mode: normalized_mode,
        profile: normalized_profile,
        flagged_count: flagged.len(),
        suppressed_count: 0,
        warned_count: 0,
    }
}

fn certify_claim(claim: &Claim, context: &str, config: WitnessConfig) -> Certificate {
    let (windows, adequacy) = select_evidence_windows(context, &claim.text, 4);
    let mut support_steps = Vec::new();
    let mut contradiction_steps = Vec::new();
    let question = question_from_context(context);

    let quote = quote_support(context, &claim.text);
    if quote > 0.0 && question.is_empty() {
        support_steps.push(ProofStep {
            operator: "quote_support".to_string(),
            evidence: format!("quote_strength={:.2}", quote),
            strength: quote,
        });
    }

    let slot = slot_support(context, &claim.text, adequacy);
    if slot > 0.0 && question.is_empty() {
        support_steps.push(ProofStep {
            operator: "slot_support".to_string(),
            evidence: format!("adequacy={:.2}", adequacy),
            strength: slot,
        });
    }

    let local = local_pav(context, &claim.text, &windows, adequacy);
    if local.0 == "entailment" {
        support_steps.push(ProofStep {
            operator: "local_entailment".to_string(),
            evidence: local.2.chars().take(180).collect(),
            strength: local.1,
        });
    } else if local.0 == "contradiction" {
        contradiction_steps.push(ProofStep {
            operator: "local_contradiction".to_string(),
            evidence: local.2.chars().take(180).collect(),
            strength: local.1,
        });
    }

    let support = support_steps.iter().map(|s| s.strength).fold(0.0, f64::max);
    let contradiction = contradiction_steps
        .iter()
        .map(|s| s.strength)
        .fold(0.0, f64::max);

    let (label, risk, proof_path) = if contradiction >= config.contradiction_threshold {
        let mut proof = contradiction_steps.clone();
        proof.extend(support_steps.iter().take(1).cloned());
        ("contradicted".to_string(), 0.92, proof)
    } else if support >= config.support_threshold {
        (
            "grounded".to_string(),
            (0.35 * (1.0 - support)).max(0.05),
            support_steps,
        )
    } else if adequacy >= config.adequacy_threshold {
        let mut proof = support_steps;
        proof.push(ProofStep {
            operator: "evidence_adequacy".to_string(),
            evidence: top_window_text(&windows),
            strength: adequacy,
        });
        ("unsupported".to_string(), 0.80, proof)
    } else {
        (
            "unknown".to_string(),
            0.55,
            vec![ProofStep {
                operator: "weak_evidence".to_string(),
                evidence: top_window_text(&windows),
                strength: adequacy,
            }],
        )
    };

    Certificate {
        claim_id: claim.id,
        claim_text: claim.text.clone(),
        label,
        support_strength: round4(support),
        contradiction_strength: round4(contradiction),
        evidence_adequacy: round4(adequacy),
        risk: round4(risk),
        proof_path,
    }
}

fn local_pav(
    context: &str,
    claim: &str,
    windows: &[EvidenceWindow],
    adequacy: f64,
) -> (String, f64, String) {
    let evidence = windows
        .iter()
        .map(|w| w.text.as_str())
        .collect::<Vec<_>>()
        .join("\n");
    if let Some((label, confidence)) = comparative_verdict(context, claim) {
        return (label, confidence, evidence);
    }

    if !question_from_context(context).is_empty() {
        return ("neutral".to_string(), 0.35, evidence);
    }

    let quote = quote_support(context, claim);
    if quote >= 0.82 {
        return ("entailment".to_string(), quote.min(0.85), evidence);
    }

    let claim_nums: Vec<String> = extract_numbers(claim)
        .into_iter()
        .filter(|n| !n.is_empty())
        .collect();
    let evidence_nums: Vec<String> = extract_numbers(&evidence)
        .into_iter()
        .filter(|n| !n.is_empty())
        .collect();
    if !claim_nums.is_empty() && adequacy >= 0.72 {
        if claim_nums.iter().all(|n| evidence_nums.contains(n)) {
            return ("entailment".to_string(), 0.68, evidence);
        }
        if !evidence_nums.is_empty() {
            return ("contradiction".to_string(), 0.66, evidence);
        }
    }

    if adequacy >= 0.88 && slot_support(context, claim, adequacy) >= 0.70 {
        return ("entailment".to_string(), 0.66, evidence);
    }
    ("neutral".to_string(), 0.35, evidence)
}

fn quote_support(context: &str, claim: &str) -> f64 {
    let norm_context = normalize_text(context);
    let norm_claim = normalize_text(claim);
    if norm_claim.is_empty() {
        return 0.0;
    }
    if norm_context.contains(&norm_claim) {
        if norm_claim.len() > 80 {
            0.95
        } else {
            0.82
        }
    } else {
        0.0
    }
}

fn slot_support(context: &str, claim: &str, adequacy: f64) -> f64 {
    let words = content_words(claim);
    let entities = extract_entities(claim);
    let numbers = extract_numbers(claim);
    let lower = context.to_lowercase();
    let token_cov = intersection_ratio(&words, &content_words(context));
    let entity_cov = coverage_fraction(&entities, &lower);
    let number_cov = coverage_fraction(&numbers, &lower);
    if !numbers.is_empty() && number_cov < 1.0 {
        return 0.0;
    }
    if !entities.is_empty() && entity_cov < 0.65 {
        return 0.0;
    }
    (0.25 + 0.35 * adequacy + 0.20 * token_cov).min(0.74)
}

fn comparative_verdict(context: &str, claim: &str) -> Option<(String, f64)> {
    let question = question_from_context(context);
    let candidates = candidate_entities(&question);
    if candidates.len() != 2 {
        return None;
    }
    let clean_context = match context.to_lowercase().find("question:") {
        Some(idx) => &context[..idx],
        None => context,
    };
    let values: Vec<Vec<i32>> = candidates
        .iter()
        .map(|candidate| numbers_near(clean_context, candidate, 260))
        .collect();
    if values.iter().any(|v| v.is_empty()) {
        return None;
    }
    let q_lower = question.to_lowercase();
    let expected = if ["first", "earlier", "older", "started", "founded"]
        .iter()
        .any(|term| q_lower.contains(term))
    {
        let i = if values[0].iter().min()? <= values[1].iter().min()? {
            0
        } else {
            1
        };
        Some(candidates[i].clone())
    } else if ["more", "most", "larger", "higher"]
        .iter()
        .any(|term| q_lower.contains(term))
    {
        let i = if values[0].iter().max()? >= values[1].iter().max()? {
            0
        } else {
            1
        };
        Some(candidates[i].clone())
    } else {
        None
    }?;

    let claim_lower = claim.to_lowercase();
    if claim_lower.contains(&expected.to_lowercase()) {
        return Some(("entailment".to_string(), 0.76));
    }
    if candidates
        .iter()
        .any(|c| c != &expected && claim_lower.contains(&c.to_lowercase()))
    {
        return Some(("contradiction".to_string(), 0.78));
    }
    None
}

fn candidate_claim_segments(text: &str) -> Vec<(usize, String)> {
    let mut out: Vec<(usize, String)> = Vec::new();
    let mut seen = HashSet::new();

    for (start, sentence) in split_sentences(text) {
        push_claim_candidate(start, &sentence, &mut out, &mut seen);
        for (part_start, part) in split_compound_claims(start, &sentence) {
            push_claim_candidate(part_start, &part, &mut out, &mut seen);
        }
    }

    let mut line_start = 0usize;
    for raw_line in text.split_inclusive('\n') {
        let line = raw_line.trim_end_matches(['\r', '\n']);
        let trimmed = line.trim();
        if !trimmed.is_empty() {
            let leading = line.find(trimmed).unwrap_or(0);
            let cleaned = clean_claim_segment(trimmed);
            let start = line_start + leading;
            if is_list_or_table_row(trimmed) || looks_like_code_claim(&cleaned) {
                push_claim_candidate(start, &cleaned, &mut out, &mut seen);
            }
            for (part_start, part) in split_compound_claims(start, &cleaned) {
                push_claim_candidate(part_start, &part, &mut out, &mut seen);
            }
        }
        line_start += raw_line.len();
    }

    out.sort_by(|a, b| a.0.cmp(&b.0).then_with(|| b.1.len().cmp(&a.1.len())));
    out
}

fn push_claim_candidate(
    start: usize,
    text: &str,
    out: &mut Vec<(usize, String)>,
    seen: &mut HashSet<String>,
) {
    let cleaned = clean_claim_segment(text);
    if cleaned.is_empty() {
        return;
    }
    let key = normalize_text(&cleaned);
    if key.is_empty() || !seen.insert(key) {
        return;
    }
    out.push((start, cleaned));
}

fn clean_claim_segment(segment: &str) -> String {
    let mut s = segment.trim().trim_matches('`').trim().to_string();
    for marker in ["- ", "* ", "+ "] {
        if s.starts_with(marker) {
            s = s[marker.len()..].trim().to_string();
        }
    }
    let bytes = s.as_bytes();
    if bytes.len() > 2 && bytes[0].is_ascii_digit() && bytes[1] == b'.' {
        s = s[2..].trim().to_string();
    }
    if s.starts_with('|') && s.ends_with('|') {
        let cells: Vec<&str> = s
            .trim_matches('|')
            .split('|')
            .map(|c| c.trim())
            .filter(|c| {
                !c.is_empty()
                    && !c
                        .chars()
                        .all(|ch| ch == '-' || ch == ':' || ch.is_whitespace())
            })
            .collect();
        if cells.len() >= 2 {
            s = cells.join(" | ");
        }
    }
    s.trim_matches(|c: char| c == '-' || c == '*' || c == ':' || c.is_whitespace())
        .trim()
        .to_string()
}

fn is_list_or_table_row(segment: &str) -> bool {
    let s = segment.trim();
    s.starts_with("- ")
        || s.starts_with("* ")
        || s.starts_with("+ ")
        || s.starts_with("|")
        || s.as_bytes().first().is_some_and(|b| b.is_ascii_digit())
            && s.as_bytes().get(1) == Some(&b'.')
}

fn split_compound_claims(start: usize, segment: &str) -> Vec<(usize, String)> {
    let mut parts = Vec::new();
    for delimiter in ["; ", " and "] {
        let lower = segment.to_lowercase();
        let Some(idx) = lower.find(delimiter) else {
            continue;
        };
        let left = segment[..idx].trim();
        let right = segment[idx + delimiter.len()..].trim();
        if left.len() < 8 || right.len() < 8 {
            continue;
        }
        if has_fact_signal(left) && has_fact_signal(right) {
            parts.push((start, left.to_string()));
            parts.push((start + idx + delimiter.len(), right.to_string()));
        }
    }
    parts
}

fn is_claim_like(sentence: &str) -> bool {
    let s = sentence.trim();
    if s.len() < 2 || is_question_like(s) {
        return false;
    }
    if s.starts_with("```") || s.eq_ignore_ascii_case("json") || s.eq_ignore_ascii_case("python") {
        return false;
    }
    if looks_like_code_claim(s) {
        return true;
    }
    has_fact_signal(s) || contains_claim_verb(s)
}

fn has_fact_signal(text: &str) -> bool {
    !extract_entities(text).is_empty()
        || !extract_numbers(text).is_empty()
        || looks_like_code_claim(text)
}

fn contains_claim_verb(text: &str) -> bool {
    let lower = text.to_lowercase();
    [
        " is ",
        " are ",
        " was ",
        " were ",
        " has ",
        " have ",
        " had ",
        " uses ",
        " returns ",
        " contains ",
        " supports ",
        " requires ",
        " equals ",
        " means ",
        " runs ",
        " fails ",
    ]
    .iter()
    .any(|needle| lower.contains(needle))
}

fn looks_like_code_claim(text: &str) -> bool {
    let lower = text.to_lowercase();
    text.contains("()")
        || text.contains('_')
        || text.contains("::")
        || lower.contains("function")
        || lower.contains("method")
        || lower.contains("class ")
        || lower.contains("module ")
        || lower.contains("import ")
        || lower.contains(".py")
        || lower.contains(".rs")
        || lower.contains(".js")
        || lower.contains(".ts")
}

fn classify_claim(text: &str) -> String {
    if looks_like_code_claim(text) {
        "code_ref".to_string()
    } else if !extract_numbers(text).is_empty() {
        "quantity".to_string()
    } else {
        "proposition".to_string()
    }
}

fn normalize_profile(profile: &str, output: &str) -> String {
    let normalized = profile.trim().to_lowercase().replace('-', "_");
    match normalized.as_str() {
        "code" | "rag" | "qa" | "benchmark_qa" | "summary" | "summarization" | "chat"
        | "dialogue" => {
            if normalized == "summarization" {
                "summary".to_string()
            } else {
                normalized
            }
        }
        _ => infer_profile(output),
    }
}

fn infer_profile(output: &str) -> String {
    let lower = output.to_lowercase();
    if lower.contains("```")
        || lower.contains(".py")
        || lower.contains(".rs")
        || lower.contains("function")
        || lower.contains("class ")
    {
        "code".to_string()
    } else if output.len() > 900
        || output
            .lines()
            .filter(|line| line.trim_start().starts_with("- "))
            .count()
            >= 3
    {
        "summary".to_string()
    } else {
        "rag".to_string()
    }
}

fn should_suppress(cert: &Certificate, profile: &str) -> bool {
    match cert.label.as_str() {
        "grounded" => false,
        "contradicted" => true,
        "unsupported" => !matches!(profile, "chat" | "dialogue"),
        "unknown" => matches!(profile, "code" | "rag" | "qa" | "benchmark_qa") || cert.risk >= 0.75,
        _ => false,
    }
}

fn split_sentences(text: &str) -> Vec<(usize, String)> {
    let mut out = Vec::new();
    let mut start = 0usize;
    let mut last_boundary = 0usize;
    let mut prev_was_term = false;
    for (idx, ch) in text.char_indices() {
        if ch == '\n' || (prev_was_term && ch.is_whitespace()) {
            let end = if ch == '\n' { idx } else { last_boundary };
            push_sentence(text, start, end, &mut out);
            start = idx + ch.len_utf8();
            prev_was_term = false;
            continue;
        }
        if matches!(ch, '.' | '!' | '?') {
            last_boundary = idx + ch.len_utf8();
            prev_was_term = true;
        } else if !ch.is_whitespace() {
            prev_was_term = false;
        }
    }
    push_sentence(text, start, text.len(), &mut out);
    out
}

fn push_sentence(text: &str, start: usize, end: usize, out: &mut Vec<(usize, String)>) {
    if end <= start || start >= text.len() {
        return;
    }
    let raw = &text[start..end.min(text.len())];
    let trimmed = raw.trim();
    if trimmed.is_empty() {
        return;
    }
    let leading = raw.find(trimmed).unwrap_or(0);
    out.push((start + leading, trimmed.to_string()));
}

fn is_question_like(sentence: &str) -> bool {
    let s = sentence.trim();
    if s.ends_with('?') {
        return true;
    }
    let first = s
        .split(|c: char| !c.is_ascii_alphabetic())
        .find(|part| !part.is_empty())
        .unwrap_or("")
        .to_lowercase();
    question_starters().contains(first.as_str())
}

fn normalize_text(text: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut last_space = false;
    for ch in text.chars().flat_map(|c| c.to_lowercase()) {
        let keep = ch.is_alphanumeric() || matches!(ch, '_' | '%' | '\'' | '-' | '.');
        if keep {
            out.push(ch);
            last_space = false;
        } else if !last_space {
            out.push(' ');
            last_space = true;
        }
    }
    out.split_whitespace().collect::<Vec<_>>().join(" ")
}

fn content_words(text: &str) -> HashSet<String> {
    word_re()
        .find_iter(text)
        .map(|m| m.as_str().to_lowercase())
        .filter(|w| !stopwords().contains(w.as_str()))
        .collect()
}

fn extract_numbers(text: &str) -> Vec<String> {
    let lower = text.to_lowercase();
    let mut nums: Vec<String> = number_re()
        .find_iter(text)
        .map(|m| {
            let mut s = m.as_str().replace([',', '$', '%'], "");
            while s.len() > 1 && s.starts_with('0') {
                s.remove(0);
            }
            s
        })
        .filter(|s| !s.is_empty())
        .collect();
    for (word, value) in number_words() {
        if lower
            .split(|c: char| !c.is_ascii_alphabetic())
            .any(|part| part == *word)
        {
            nums.push(value.to_string());
        }
    }
    nums
}

fn extract_entities(text: &str) -> Vec<String> {
    let mut raw = Vec::new();
    for caps in quoted_re().captures_iter(text) {
        if let Some(m) = caps.get(1) {
            raw.push(m.as_str().trim().to_string());
        }
    }
    for m in caps_re().find_iter(text) {
        raw.push(m.as_str().to_string());
    }
    for m in entity_re().find_iter(text) {
        let value = m.as_str().trim();
        if value.len() >= 3 && !stopwords().contains(value.to_lowercase().as_str()) {
            raw.push(value.to_string());
        }
    }
    let mut seen = HashSet::new();
    let mut unique = Vec::new();
    for entity in raw {
        let key: String = entity
            .chars()
            .filter(|c| c.is_alphanumeric())
            .flat_map(|c| c.to_lowercase())
            .collect();
        if !key.is_empty() && seen.insert(key) {
            unique.push(entity);
        }
    }
    unique
}

fn sentence_windows(context: &str, max_chars: usize) -> Vec<String> {
    let mut windows = Vec::new();
    for (_, sentence) in split_sentences(context) {
        if sentence.len() <= max_chars {
            windows.push(sentence);
        } else {
            let mut start = 0;
            while start < sentence.len() {
                let mut end = (start + max_chars).min(sentence.len());
                while end < sentence.len() && !sentence.is_char_boundary(end) {
                    end += 1;
                }
                windows.push(sentence[start..end].trim().to_string());
                start = end;
            }
        }
    }
    if windows.is_empty() {
        windows.push(context.chars().take(max_chars).collect());
    }
    windows.into_iter().filter(|w| !w.is_empty()).collect()
}

fn coverage_fraction(items: &[String], haystack_lower: &str) -> f64 {
    if items.is_empty() {
        return 0.0;
    }
    let hits = items
        .iter()
        .filter(|item| !item.is_empty() && haystack_lower.contains(&item.to_lowercase()))
        .count();
    hits as f64 / items.len() as f64
}

fn intersection_ratio(a: &HashSet<String>, b: &HashSet<String>) -> f64 {
    if a.is_empty() {
        return 0.0;
    }
    a.intersection(b).count() as f64 / a.len() as f64
}

fn weighted_adequacy(
    entity_cov: f64,
    number_cov: f64,
    token_cov: f64,
    has_entities: bool,
    has_numbers: bool,
) -> f64 {
    let mut weighted = 0.0;
    let mut denom = 0.0;
    if has_entities {
        weighted += 0.45 * entity_cov;
        denom += 0.45;
    }
    if has_numbers {
        weighted += 0.35 * number_cov;
        denom += 0.35;
    }
    let token_weight = if has_entities || has_numbers {
        0.20
    } else {
        1.0
    };
    weighted += token_weight * token_cov;
    denom += token_weight;
    (weighted / denom.max(1e-9_f64)).clamp(0.0, 1.0)
}

fn question_from_context(context: &str) -> String {
    let lower = context.to_lowercase();
    if let Some(idx) = lower.find("question:") {
        context[idx + "question:".len()..].trim().to_string()
    } else {
        String::new()
    }
}

fn candidate_entities(question: &str) -> Vec<String> {
    if !question.to_lowercase().contains(" or ") {
        return vec![];
    }
    let mut tail = question.trim().trim_end_matches('?').to_string();
    if let Some(idx) = tail.rfind(',') {
        tail = tail[idx + 1..].to_string();
    }
    let lower = tail.to_lowercase();
    for marker in [
        " first ",
        " more ",
        " older ",
        " earlier ",
        " larger ",
        " higher ",
    ] {
        if let Some(idx) = lower.find(marker) {
            tail = tail[idx + marker.len()..].to_string();
            break;
        }
    }
    tail.split(" or ")
        .map(|p| {
            p.trim_matches(|c: char| c.is_whitespace() || ".?\"'".contains(c))
                .to_string()
        })
        .filter(|p| p.len() > 1)
        .collect()
}

fn numbers_near(context: &str, entity: &str, radius: usize) -> Vec<i32> {
    let mut nums = Vec::new();
    let lower = context.to_lowercase();
    let key = entity.to_lowercase();
    let mut start = 0usize;
    while let Some(rel_idx) = lower[start..].find(&key) {
        let idx = start + rel_idx;
        let left = idx.saturating_sub(radius);
        let right = (idx + entity.len() + radius).min(context.len());
        let window = &context[left..right];
        nums.extend(
            number_re()
                .find_iter(window)
                .filter_map(|m| m.as_str().replace([',', '$', '%'], "").parse::<i32>().ok()),
        );
        let window_lower = window.to_lowercase();
        for (word, value) in number_words() {
            if window_lower
                .split(|c: char| !c.is_ascii_alphabetic())
                .any(|part| part == *word)
            {
                nums.push(*value);
            }
        }
        start = idx + key.len();
    }
    nums
}

fn top_window_text(windows: &[EvidenceWindow]) -> String {
    windows
        .first()
        .map(|w| w.text.chars().take(200).collect())
        .unwrap_or_default()
}

fn remove_claim_text(output: &str, claim: &str) -> String {
    if let Some(idx) = output.find(claim) {
        let before = output[..idx].trim_end();
        let after = output[idx + claim.len()..].trim_start();
        return format!("{}\n{}", before, after).trim().to_string();
    }

    let claim_words = content_words(claim);
    if claim_words.is_empty() {
        return output.to_string();
    }
    let mut spans = split_sentences(output);
    spans.sort_by_key(|b| std::cmp::Reverse(b.0));
    let mut rewritten = output.to_string();
    for (start, sentence) in spans {
        let words = content_words(&sentence);
        let overlap = intersection_ratio(&claim_words, &words);
        if overlap >= 0.72 {
            let end = (start + sentence.len()).min(rewritten.len());
            rewritten = format!(
                "{}\n{}",
                rewritten[..start].trim_end(),
                rewritten[end..].trim_start()
            );
            break;
        }
    }
    rewritten
}

fn cleanup_rewritten_output(text: &str) -> String {
    let mut out = Vec::new();
    let mut blank = false;
    for line in text.lines() {
        let trimmed = line.trim_end();
        if trimmed.trim().is_empty() {
            if !blank {
                out.push(String::new());
            }
            blank = true;
        } else if trimmed.trim() != "-" && trimmed.trim() != "*" {
            out.push(trimmed.to_string());
            blank = false;
        }
    }
    out.join("\n").trim().to_string()
}

fn round4(value: f64) -> f64 {
    (value * 10000.0).round() / 10000.0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn grounded_and_strict_suppression() {
        let context = "The Oberoi Group has its head office in Delhi.";
        let output =
            "The Oberoi Group has its head office in Delhi. Paris is the capital of Germany.";
        let payload =
            analyze_with_policy(context, output, "strict", "rag", WitnessConfig::default());
        assert_eq!(payload.witness.n_grounded, 1);
        assert_eq!(payload.witness.n_unknown, 1);
        assert!(!payload.output.contains("Paris is the capital of Germany"));
        assert!(payload.output.contains("Delhi"));
    }

    #[test]
    fn comparative_contradiction() {
        let context = concat!(
            "Arthur's Magazine (1844-1846) was an American literary periodical. ",
            "First for Women is a woman's magazine published by Bauer Media Group, started in 1989.\n\n",
            "Question: Which magazine was started first Arthur's Magazine or First for Women?"
        );
        let result = analyze(
            context,
            "First for Women was started first.",
            WitnessConfig::default(),
        );
        assert_eq!(result.certificates[0].label, "contradicted");
    }

    #[test]
    fn summary_profile_warns_unknown_without_suppressing() {
        let context = "The report says revenue increased in 2024.";
        let output = "Revenue increased in 2024. The report also confirms a new Tokyo office.";
        let payload = analyze_with_policy(
            context,
            output,
            "strict",
            "summary",
            WitnessConfig::default(),
        );
        assert!(payload.output.contains("Tokyo office"));
        assert_eq!(payload.policy.suppressed_count, 0);
        assert!(payload.policy.warned_count >= 1);
    }

    #[test]
    fn extracts_bullets_tables_and_code_refs() {
        let output = "- Alpha launched in 2024.\n| Name | Value |\n| Beta | 42 |\n`load_config()` reads config.yaml.";
        let claims = extract_claims(output);
        assert!(claims.iter().any(|c| c.text.contains("Alpha launched")));
        assert!(claims
            .iter()
            .any(|c| c.text.contains("Beta") && c.text.contains("42")));
        assert!(claims.iter().any(|c| c.kind == "code_ref"));
    }
}
