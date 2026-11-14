# Multi-model agent evaluation harness

A small, honest evaluation project for an AI engineering degree.
Run the same tasks through Gemini, Claude Pro, and ChatGPT, score them
the same way, and look for patterns — not just which model "feels best".

## What you need

- A Gemini account (student free tier is fine)
- A Claude Pro account
- A ChatGPT account
- VS Code and/or Cursor, plus git and GitHub

No API keys are needed for the manual version below. Chat subscriptions
are not the same as API access, so this version evaluates the tools as
you actually use them.

## Setup

```bash
git init
git add .
git commit -m "Baseline: tasks and rubric before any runs"
```

Open the folder in VS Code for the main work. You can open the exact
same folder in Cursor when you want AI help scaffolding code, writing
the summary script, or spotting patterns in results. Git keeps both
in sync, so you do not have to choose only one editor.

## Method — keep this identical for every model

1. Pick a task from `tasks/`.
2. Copy the prompt from `prompts/` word for word. Do not rephrase it
   for a particular model.
3. Start a fresh chat in that model. No follow-ups for the first run.
4. Paste the prompt, plus any input file named in the task.
5. Save the full, unedited output to `runs/<model>/<task>.md`.
6. Log the date, the model label shown by the service, and the time
   taken in `results.csv`.
7. Score it using `rubric.md` — ideally after all models for that
   task are done, so you are not scoring one model while still
   remembering another's answer in detail.

## Scoring

Each criterion is 0, 1, or 2:

- 0 = missing or wrong
- 1 = partly correct
- 2 = correct and complete

Total is out of 10. Write a short note for anything surprising,
especially a failure mode you could test again later.

## Summarising results

```bash
python summarize.py
```

This prints the average total score per model from `results.csv`.
It needs no extra packages.

## Limitations to state in your write-up

- Chat interfaces do not let you lock temperature or other sampling
  settings the way an API would, so this is a realistic-use
  evaluation, not a perfectly controlled lab experiment.
- Model versions change over time. Record the label and date for
  every run.
- One run per model per task is a starting point. For a stronger
  project, repeat a task, add a task, or add a failure-mode analysis.

## Extending it

- Add a fifth task from your current coursework.
- Add a failure-mode analysis: group errors by type (missed step,
  wrong calculation, hallucinated detail, format ignored).
- Make the repo public on GitHub for your portfolio once you have
  removed anything personal from the inputs and outputs.
