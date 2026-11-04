
import pandas as pd

# Load annotated dataset
df = pd.read_csv("outputs/annotated_tickets.csv")

# Approved annotation labels
valid_labels = {
    "sentiment": ["Positive", "Negative", "Neutral"],
    "intent": [
        "Refund", "Return", "Delivery", "Payment",
        "Cancellation", "Login", "Feedback", "Other"
    ],
    "category": ["Payment", "Order", "Account", "Product", "Service"],
    "priority": ["High", "Medium", "Low"]
}

print("CUSTOMER SUPPORT ANNOTATION QUALITY REPORT")
print("-" * 45)

# 1. Total records
print("Total records:", len(df))

# 2. Check missing values
annotation_columns = list(valid_labels.keys())
missing = df[annotation_columns].isnull().sum()

print("\nMissing annotation values:")
print(missing)

# 3. Check invalid labels
print("\nInvalid label counts:")

for column, allowed_values in valid_labels.items():
    invalid_count = (~df[column].isin(allowed_values)).sum()
    print(f"{column}: {invalid_count}")

# 4. Check duplicate ticket IDs
duplicate_count = df["ticket_id"].duplicated().sum()
print("\nDuplicate ticket IDs:", duplicate_count)

# 5. Calculate annotation completeness
total_cells = len(df) * len(annotation_columns)
completed_cells = df[annotation_columns].notnull().sum().sum()

completeness = (completed_cells / total_cells) * 100 if total_cells else 0

print(f"\nAnnotation completeness: {completeness:.2f}%")

# 6. Final result
if missing.sum() == 0 and duplicate_count == 0:
    print("\nBasic quality checks passed!")
else:
    print("\nQuality issues found. Please review the dataset.")
