# Customer Support Data Annotation Project

## 1. Project Overview

This project demonstrates an end-to-end customer support data annotation and quality evaluation workflow using Python, Pandas, SQL, MySQL, and Power BI.

A synthetic dataset of 100 customer support tickets is processed and annotated using rule-based text classification. Each ticket is classified by sentiment, intent, category, and priority.

The project also includes human review, annotation quality evaluation, automated testing, SQL analysis, and dashboard visualization.

## 2. Project Objectives

- Generate and validate customer support ticket data.
- Automate text annotation using Python.
- Classify tickets into sentiment, intent, category, and priority.
- Perform human review of automatic annotations.
- Evaluate annotation quality using accuracy and Cohen's Kappa.
- Store and analyze annotated data using MySQL.
- Develop a Power BI dashboard for data insights.
- Test annotation functions using Python unit testing.

## 3. Technologies Used

- **Programming:** Python
- **Data Processing:** Pandas
- **Database:** MySQL
- **Query Language:** SQL
- **Visualization:** Power BI
- **Testing:** Python unittest
- **Development:** VS Code
- **Version Control:** Git and GitHub

## 4. Project Structure

```text
customer-support-data-annotation/
├── data/
├── Guidelines/
├── Notebooks/
├── Outputs/
├── Reports/
├── SQL/
├── SRC/
├── Tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## 5. Annotation Labels

| Field | Available Labels |
|---|---|
| Sentiment | Positive, Negative, Neutral |
| Intent | Refund, Return, Delivery, Payment, Cancellation, Login, Feedback, Other |
| Category | Order, Product, Payment, Account, Service |
| Priority | High, Medium, Low |

## 6. Project Workflow

1. Generated 100 synthetic customer support records.
2. Performed data validation and duplicate checks.
3. Developed Python functions for automatic annotation.
4. Classified tickets using sentiment, intent, category, and priority.
5. Created a human-review dataset.
6. Compared automatic annotations with reviewed labels.
7. Calculated accuracy and Cohen's Kappa.
8. Analyzed annotation disagreements and improved classification rules.
9. Developed 16 unit tests using Python unittest.
10. Integrated annotated data with MySQL.
11. Performed SQL analysis using joins, CTEs, and window functions.
12. Developed a Power BI dashboard.

## 7. Annotation Quality Evaluation

| Annotation Field | Accuracy | Cohen's Kappa |
|---|---:|---:|
| Sentiment | 100% | 1.0000 |
| Intent | 100% | 1.0000 |
| Category | 100% | 1.0000 |
| Priority | 100% | 1.0000 |

**Important:** These results represent agreement on the 10 reviewed examples. The dataset contains 100 records but only 10 unique messages repeated multiple times. The reviewed labels were prepared through guided review, not independent annotation. Therefore, these results do not establish production-level accuracy.

## 8. Unit Testing

Created 16 test cases using Python's unittest framework to validate:

- Positive, negative, and neutral sentiment.
- Different customer intents.
- Product, payment, and order categories.
- High, medium, and low priority.
- Empty-message handling.
- Uppercase-message handling.

Run the tests using:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 9. SQL Analysis

SQL analysis includes:

- Ticket distribution by sentiment and intent.
- Category and priority analysis.
- High-priority ticket identification.
- Common Table Expressions (CTEs).
- Ranking and row-number functions.
- Customer support issue analysis.

## 10. Data Quality Checks

Implemented validation for:

- Missing annotation values.
- Invalid annotation labels.
- Duplicate ticket IDs.
- Annotation completeness.
- Automatic and human-reviewed label agreement.

## 11. Reports

The `Reports/` directory contains:

- `Error_Analysis.md` – documents annotation disagreements and improvements.
- `Final_Project_Report.md` – summarizes the project workflow, technologies, evaluation, and limitations.

## 12. Limitations and Future Improvements

- Expand the dataset with more diverse customer messages.
- Obtain independent annotations from multiple reviewers.
- Improve classification using NLP and machine learning.
- Handle sarcasm, ambiguous messages, and complex language.
- Perform larger-scale quality evaluation before production deployment.

## 13. Conclusion

This project demonstrates a complete beginner-level customer support data annotation workflow, covering Python automation, human review, annotation quality evaluation, SQL analysis, Power BI visualization, unit testing, and project documentation.