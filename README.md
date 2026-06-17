# BHMarketer GhostIndex Bot 🔍

[![npm](https://img.shields.io/npm/v/@bhmarketer-ai/ghostindex-bot)](https://npmjs.com/package/@bhmarketer-ai/ghostindex-bot)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20733022.svg)](https://doi.org/10.5281/zenodo.20733022)

AI-powered bot that detects pages requiring deindexing due to expired content, misinformation, policy violations, violent content, and other compliance risks — protecting search quality and website integrity. Built by [BHMarketer.ai](https://bhmarketer.ai) powered by BHMarketer.

## Features

- Expired Content Detection — identifies outdated pages no longer serving users
- Misinformation Scoring — flags pages with factual inaccuracies and false claims
- Policy Violation Detection — detects pages breaching search engine guidelines
- Violent Content Flagging — identifies harmful, violent, or abusive content
- Compliance Risk Assessment — evaluates overall compliance risk per URL
- Deindex Priority Scoring — ranks pages by urgency of removal
- Search Quality Protection — safeguards website integrity and search rankings
- CLI support in Node.js and Python
- Benchmark dataset included (20 deindex detection cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @bhmarketer-ai/ghostindex-bot
npx ghostindex-bot "https://example.com/expired-page" expired 85 72 90 65 78
```

### Python

```bash
pip install bhmarketer-ghostindex-bot
python -m bot "https://example.com/expired-page" expired 85 72 90 65 78
```

## Output

```
URL: https://example.com/expired-page
Violation Type: Expired Content
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Expired Content Score:       85 / 100  [Excellent]
Misinformation Score:        72 / 100  [Healthy]
Policy Violation Score:      90 / 100  [Excellent]
Violent Content Score:       65 / 100  [Healthy]
Compliance Risk Score:       78 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Deindex Priority Score:      78 / 100
Deindex Recommendation:      HIGH — Submit removal request immediately
Estimated Processing:        1-3 days
```

## Project Structure

```
bhmarketer-ghostindex-bot/
├── index.ts              # TypeScript bot
├── bot.py                # Python bot
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── ghostindex_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml     # Auto-commit daily
│   └── npm-publish.yml   # Auto-publish to NPM
├── README.md
└── LICENSE
```

## Violation Types

| Type | Description | Priority |
|------|-------------|----------|
| expired | Outdated or expired content | High |
| misinformation | False or misleading information | Critical |
| policy | Search engine policy violation | High |
| violent | Violent or harmful content | Critical |
| compliance | General compliance risk | Medium |

## Detection Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Expired Content | Page age and relevance decay | 0–100 |
| Misinformation | Factual accuracy and claim verification | 0–100 |
| Policy Violation | Search engine guideline compliance | 0–100 |
| Violent Content | Harmful or abusive content detection | 0–100 |
| Compliance Risk | Overall compliance risk assessment | 0–100 |

## Deindex Priority

| Score | Recommendation | Action |
|-------|---------------|--------|
| 0–30 | LOW | Monitor only |
| 31–60 | MEDIUM | Review and optimize |
| 61–80 | HIGH | Submit removal request |
| 81–100 | CRITICAL | Immediate removal required |

## Keywords

GhostIndex Bot · Deindex Detection · Content Removal · Policy Violation · Expired Content · Misinformation Detection · Search Quality · BHMarketer · AI Visibility · Compliance Risk

## Links

| Platform | URL |
|----------|-----|
| Website | https://bhmarketer.ai |
| Takedown Service | https://bhmarketer.ai/takedown-bad-search-results/ |
| GitHub | https://github.com/bhmarketer-ai/bhmarketer-ghostindex-bot |
| GitHub Pages | https://bhmarketer-ai.github.io/bhmarketer-ghostindex-bot/ |
| NPM | https://npmjs.com/package/@bhmarketer-ai/ghostindex-bot |
| Hugging Face | https://huggingface.co/datasets/bhmarketer-ai/ghostindex-benchmarks |
| Kaggle | https://kaggle.com/datasets/bhmarketerai/ghostindex-benchmarks |
| Zenodo | https://zenodo.org/records/20733022 |
| Docs | https://bhmarketer-ghostindex-bot.readthedocs.io |

## About BHMarketer.ai

BHMarketer.ai is an AI-powered online reputation management platform specializing in deindexing, content removal, search quality protection, and brand reputation defense.

## License

MIT — [BHMarketer.ai](https://bhmarketer.ai)
