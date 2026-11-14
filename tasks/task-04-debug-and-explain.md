# Task 04 — Debug and explain

Goal: Test whether the model finds real bugs, fixes only what is broken,
and explains the fixes clearly.

Input: `inputs/buggy-code.py` — paste it after the prompt.
Prompt file: `prompts/task-04.md`

Run it verbatim in a fresh chat in Gemini, Claude Pro, and ChatGPT.
Save each output to `runs/<model>/task-04-debug-and-explain.md`.

Expected bugs (for scoring only, do not put this in the prompt):
1. Division by zero when the list is empty.
2. The loop uses the wrong variable, so it adds the index instead of the value.
