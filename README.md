# Structured Clinical Summarization Pipeline

> LLM, RAG & Agentic AI portfolio project — independent open-source implementation.
> This is an original, from-scratch build. It is not affiliated with, and does not
> contain any code, prompts, data, or business logic from, any employer or client.

![status](https://img.shields.io/badge/status-in_progress-blue)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)

## 1. Problem

Turning a raw patient conversation into a clean, structured clinical summary is error-prone without a validated extraction and evaluation pipeline. This is a clean-room reimplementation, not tied to any employer's proprietary pipeline.

## 2. Architecture

```text
Conversation Text -> Field Extraction Nodes -> Validation/Missing-Value Handling -> Summarization Node -> Evaluation Node
```

## 3. Technology Stack

- Python
- Azure PromptFlow (or open-source equivalent)
- OpenAI API
- Pydantic (schema validation)

## 4. Feature List

- Patient conversation input
- Structured field extraction
- Vitals parsing
- Blood-pressure parsing
- Missing-value handling
- Clinical summarization
- Prompt evaluation
- PromptFlow-style pipeline orchestration

## 5. Implementation Plan

1. Phase 1: Define structured schema (vitals, symptoms, history) with Pydantic
2. Phase 2: Build extraction nodes with missing-value handling
3. Phase 3: Summarization node and evaluation harness
4. Phase 4: Wire into a PromptFlow-style DAG for repeatable runs
5. Phase 5: Testing, CI/CD, containerization, and documentation for reproducible runs

## Task Tracking

Work is broken into phase-tagged user stories tracked as GitHub Issues, not in this file. To see what's open:

    gh issue list --repo faheemkhaskheli9/clinical-summary-promptflow --state open --label type:user-story

Implement Phase 1 issues first (later phases depend on it). When you start one, add label `status:in-progress`. When you finish, close it referencing the commit (e.g. `git commit -m "... Closes #4"`) and push.

## 6. Repository Structure

```text
clinical-summary-promptflow/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── .env.example
├── docker/
├── docs/
│   ├── architecture.md
│   └── evaluation.md
├── src/
├── tests/
├── configs/
├── scripts/
├── notebooks/
├── examples/
├── assets/
└── .github/
    └── workflows/
```

## 7. Setup

```bash
git clone <this-repo-url>
cd clinical-summary-promptflow
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # or: pip install -e .
cp .env.example .env              # fill in API keys / config
```

## 8. Dataset

Document which public dataset(s) or synthetic data generators are used here.
No proprietary, employer-owned, or client-identifiable data is used in this project.

## 9. Training / Execution

Document the commands used to run training, ingestion, or the main pipeline, e.g.:

Phase 1 includes a schema-validation CLI. It accepts synthetic JSON and prints
the normalized vitals object:

```bash
python -m clinical_summary.cli --input examples/vitals.json
```

The command exits non-zero with a validation message for an invalid path,
malformed JSON, or an out-of-range value.

## 10. Evaluation

Document evaluation metrics and how to reproduce them here (see `docs/evaluation.md`).

## 11. Results

_To be filled in as the implementation progresses — screenshots, metrics tables, and
sample outputs go here._

## 12. API

_If this project exposes an API, document the main endpoints here (or link to
auto-generated OpenAPI docs, e.g. `/docs` for FastAPI)._

## 13. Docker

```bash
docker build -t clinical-summary-promptflow .
docker run -p 8000:8000 clinical-summary-promptflow
```

## 14. Tests

```bash
pytest tests/
```

## 15. Limitations

- This is a from-scratch, independent recreation built for portfolio purposes.
- Performance numbers, once added, are based on public datasets and are not
  representative of any production system's real-world results.

## 16. Future Work

- Expand evaluation coverage and add CI-based regression checks.
- Add more configuration presets and deployment targets.
- Track open items as GitHub Issues.

## 17. Disclosure

This repository is an **independent open-source recreation inspired by the kind of
production systems I have worked on professionally**. It contains no employer or
client source code, prompts, datasets, credentials, architecture diagrams, or
business logic. All code, data, and documentation here are original or built on
publicly available datasets and open-source tools.

---
_Last updated: 2026-08-18_
