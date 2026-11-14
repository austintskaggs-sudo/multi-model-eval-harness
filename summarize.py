"""Print average total score per model from results.csv.

Run: python summarize.py
No extra packages needed.
"""

import csv
from collections import defaultdict
from pathlib import Path


def main():
    totals = defaultdict(list)
    counts = defaultdict(int)
    results_path = Path(__file__).parent / "results.csv"
    with open(results_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total = (row.get("total_0_10") or "").strip()
            model = (row.get("model") or "").strip()
            if model and total:
                try:
                    totals[model].append(float(total))
                except ValueError:
                    pass
            if model:
                counts[model] += 1

    print("Average total score (out of 10), scored runs only:")
    for model in sorted(totals):
        scores = totals[model]
        print(f"- {model}: {sum(scores) / len(scores):.2f}  ({len(scores)} scored runs)")

    print("\nRuns listed in results.csv (including unscored):")
    for model in sorted(counts):
        print(f"- {model}: {counts[model]}")


if __name__ == "__main__":
    main()
