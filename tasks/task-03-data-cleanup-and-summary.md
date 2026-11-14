# Task 03 — Data cleanup and summary

Goal: Test multi-step calculation, anomaly spotting, and showing working.

Input: `inputs/data.csv` — paste it after the prompt.
Prompt file: `prompts/task-03.md`

Run it verbatim in a fresh chat in Gemini, Claude Pro, and ChatGPT.
Save each output to `runs/<model>/task-03-data-cleanup-and-summary.md`.

Expected check (for scoring only, do not put this in the prompt):
- books: 45, study-tools: 60, snacks: 1014, grand total: 1119
- The 999 snacks row is the anomaly. A strong answer flags it but does
  not silently drop it from the totals unless it says it is doing so.
