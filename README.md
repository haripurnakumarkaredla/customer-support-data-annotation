# Customer Support Data Annotation Project

## Project Overview

This project demonstrates a customer support ticket data annotation workflow using Python, SQL, and data quality checks.

The project uses a synthetic dataset of 100 customer support tickets. Each ticket is annotated with sentiment, intent, category, and priority labels.

## Objectives

- Generate a customer support ticket dataset.
- Perform text annotation using Python.
- Classify tickets by sentiment, intent, category, and priority.
- Store and analyze annotated data using MySQL.
- Perform data quality checks.
- Prepare insights for dashboard development.

## Technologies Used

- Python
- Pandas
- MySQL
- SQL
- VS Code
- Power BI (planned)

## Project Structure

```text
customer-support-data-annotation/
├── data/
├── dashboard/
├── guidelines/
├── notebooks/
├── outputs/
├── reports/
├── sql/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Annotation Labels

- Sentiment: Positive, Negative, Neutral
- Intent: Refund, Return, Delivery, Payment, Cancellation, Login, Feedback, Other
- Category: Order, Product, Payment, Account, Service
- Priority: High, Medium, Low

## SQL Analysis

SQL queries include:

- Ticket distribution by sentiment and intent
- Category and priority analysis
- High-priority ticket identification
- CTE-based category ranking
- Window functions and row numbering

## Data Quality

Basic validation checks include missing values, invalid labels, duplicate ticket IDs, and annotation completeness.

## Current Dataset Summary

- Total tickets: 100
- High-priority tickets: 80
- Negative sentiment tickets: 70
- Positive sentiment tickets: 20
- Neutral sentiment tickets: 10

## Important Note

This is a synthetic demonstration dataset. Initial annotations are rule-based and should be reviewed by human annotators before production use.

## Project Status

- [x] Dataset generation
- [x] Text annotation
- [x] Annotation guidelines
- [x] Python quality checks
- [x] MySQL database integration
- [x] Basic and advanced SQL analysis
- [ ] Power BI dashboard
- [ ] Human annotation review
- [ ] Inter-annotator agreement analysis
- [ ] Image, audio, and video annotation
