# Architecture Notes: Structured Clinical Summarization Pipeline

## Pipeline

```text
Conversation Text -> Field Extraction Nodes -> Validation/Missing-Value Handling -> Summarization Node -> Evaluation Node
```

## Components

- Patient conversation input
- Structured field extraction
- Vitals parsing
- Blood-pressure parsing
- Missing-value handling
- Clinical summarization
- Prompt evaluation
- PromptFlow-style pipeline orchestration

## Design Notes

- Keep provider/model choices swappable behind interfaces (see `multi-llm-router`
  and similar projects in this portfolio for the general pattern).
- Prefer configuration-driven pipelines (YAML/JSON in `configs/`) over hardcoded
  parameters so experiments are reproducible.
