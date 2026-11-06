
import pandas as pd
from pathlib import Path

# Read human-reviewed annotations
df = pd.read_csv("data/human_review.csv")

# Annotation fields to evaluate
fields = {
    "Sentiment": ("auto_sentiment", "human_sentiment"),
    "Intent": ("auto_intent", "human_intent"),
    "Category": ("auto_category", "human_category"),
    "Priority": ("auto_priority", "human_priority"),
}


def calculate_kappa(actual, predicted):
    """Calculate Cohen's Kappa."""

    labels = sorted(set(actual) | set(predicted))

    table = pd.crosstab(actual, predicted)
    table = table.reindex(
        index=labels,
        columns=labels,
        fill_value=0
    )

    matrix = table.to_numpy()
    total = matrix.sum()

    if total == 0:
        return float("nan")

    observed = matrix.trace() / total

    actual_counts = matrix.sum(axis=1)
    predicted_counts = matrix.sum(axis=0)

    expected = (
        actual_counts * predicted_counts
    ).sum() / (total ** 2)

    if expected == 1:
        return float("nan")

    return (observed - expected) / (1 - expected)


# Calculate evaluation results
results = []

for field, (auto_col, human_col) in fields.items():

    accuracy = (
        df[auto_col] == df[human_col]
    ).mean() * 100

    kappa = calculate_kappa(
        df[human_col],
        df[auto_col]
    )

    results.append({
        "Annotation Field": field,
        "Accuracy (%)": round(accuracy, 2),
        "Cohen's Kappa": round(kappa, 4)
    })


# Create and save quality report
report = pd.DataFrame(results)

Path("outputs").mkdir(exist_ok=True)

report.to_csv(
    "outputs/annotation_quality_report.csv",
    index=False
)

print("\nANNOTATION QUALITY REPORT")
print(report.to_string(index=False))

print("\nQuality report saved successfully!")
