## Summary
Evaluation works better than gut feel when the same tasks are scored the same way, using a rubric written before any outputs are reviewed. A single run is only a starting point, and repeated runs show whether results are stable. Every run should record the model label, date, and time, and reviewers should watch for four common failure modes: a missed step, a wrong calculation, a hallucinated detail, and ignored formatting.

## Key points
- Evaluation beats vibes: score the same tasks the same way every time.
- Write the rubric before looking at any outputs.
- One run is a starting point; repeated runs show stability.
- Record the model label, date, and time for every run.
- Common failure modes are a missed step, a wrong calculation, a hallucinated detail, and ignored formatting.

## Risks
- If the rubric is written after seeing outputs, or tasks are scored inconsistently, the evaluation drifts back toward vibes.
- If you rely on one run and don't record the model label, date, and time, you can't tell whether a result is stable or compare it against other runs.

## Open questions
- How many repeated runs are enough to call a result stable?
- How should each failure mode be weighted or scored in the rubric?