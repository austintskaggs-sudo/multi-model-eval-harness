## Summary

Systematic evaluation requires scoring identical tasks consistently using a rubric created prior to viewing outputs. While a single run serves as an initial baseline, conducting repeated runs and logging the model label, date, and time for each establishes stability. Following this structured process helps identify common failure modes such as missed steps, incorrect calculations, hallucinated details, and ignored formatting.

## Key points

* Score the same tasks the same way rather than relying on informal impressions ("vibes").
* Write the evaluation rubric before looking at any outputs.
* Treat a single run as a starting point and use repeated runs to demonstrate stability.
* Record the model label, date, and time for every run.
* Watch for four common failure modes: missed steps, wrong calculations, hallucinated details, and ignored formats.

## Risks

* Writing a rubric after viewing outputs or failing to score the same tasks consistently can skew evaluations toward subjective impressions rather than objective standards.
* Relying on a single run without logging the model label, date, and time prevents verifying stability or tracking recurring failure modes across runs.

## Open questions

* How many repeated runs are needed to adequately demonstrate stability?
* How should the specific scoring criteria within the pre-written rubric be weighted across different failure modes?