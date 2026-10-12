# Agent instructions

## Repository role

This repository is a research/engineering system. Accuracy and provenance are more important than flashy autonomous behavior.

## Work style

Before coding:

1. Inspect the existing tree.
2. Read relevant docs/rules.
3. Identify the smallest change that satisfies the requirement.
4. Preserve architecture boundaries.

During coding:

- Keep functions small.
- Validate external input.
- Add tests with each non-trivial behavior.
- Keep network access behind adapters.
- Keep LLM calls behind an interface.
- Store source and evidence references with extracted facts.

After coding:

- Run targeted tests.
- Run lint/type checks available in the repository.
- Report exactly what passed and what was not run.
- Never claim success for a command that was not executed.
