# Customer Support Data Annotation – Final Project Report

## 1. Project Overview

This project demonstrates an end-to-end customer support data annotation workflow using Python, SQL, and Power BI.

The objective is to classify customer support messages into meaningful labels to help understand customer issues and support prioritization.

## 2. Technologies Used

- Python
- Pandas
- SQL
- MySQL
- Power BI
- Git and GitHub
- Python unittest framework

## 3. Project Workflow

1. Generated a customer support dataset containing 100 records.
2. Performed data validation and quality checks.
3. Developed Python functions for automatic text annotation.
4. Classified messages by sentiment, intent, category, and priority.
5. Created a human-review dataset.
6. Compared automatic annotations with reviewed labels.
7. Calculated accuracy and Cohen's Kappa.
8. Developed unit tests to verify annotation functions.
9. Analyzed annotation errors and improved classification rules.
10. Used SQL and Power BI for data analysis and visualization.

## 4. Annotation Fields

| Field | Purpose |
|---|---|
| Sentiment | Identifies positive, negative, or neutral messages |
| Intent | Identifies the customer's purpose |
| Category | Groups the customer's issue |
| Priority | Assigns high, medium, or low priority |

## 5. Quality Evaluation Results

| Annotation Field | Accuracy | Cohen's Kappa |
|---|---:|---:|
| Sentiment | 100% | 1.0000 |
| Intent | 100% | 1.0000 |
| Category | 100% | 1.0000 |
| Priority | 100% | 1.0000 |

These results represent agreement on the current 10 reviewed examples. They should not be interpreted as proof of production-level accuracy.

## 6. Testing

Created 16 unit tests using Python's unittest framework to verify:

- Sentiment classification
- Intent classification
- Category classification
- Priority classification
- Empty-message handling
- Uppercase-message handling

## 7. Key Learnings

- Text preprocessing and annotation using Python.
- Data validation using Pandas.
- Human review and annotation quality evaluation.
- Accuracy and Cohen's Kappa calculations.
- Python unit testing.
- SQL-based data analysis.
- Dashboard development using Power BI.
- Project documentation and GitHub version control.

## 8. Limitations and Future Improvements

- Increase dataset diversity and the number of unique messages.
- Collect independent annotations from multiple reviewers.
- Add advanced NLP or machine-learning-based classification.
- Improve handling of ambiguous messages and complex language.
- Perform additional validation before production deployment.

## 9. Conclusion

This project demonstrates a complete beginner-level customer support annotation workflow, combining Python automation, human review, quality evaluation, SQL analysis, testing, and visualization.