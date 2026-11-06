# Customer Support Data Annotation Guidelines

## 1. Project Purpose

The purpose of this project is to classify customer support messages into four annotation fields:

- Sentiment
- Intent
- Category
- Priority

These guidelines help annotators apply labels consistently.

## 2. Sentiment Labels

| Label | Definition | Example |
|---|---|---|
| Positive | Customer expresses satisfaction or appreciation | Thank you for the excellent service. |
| Negative | Customer expresses a problem, complaint, or dissatisfaction | My order has not arrived yet. |
| Neutral | Message does not clearly express positive or negative emotion | Please cancel my order immediately. |

## 3. Intent Labels

| Label | Definition |
|---|---|
| Refund | Customer requests or asks about a refund |
| Return | Customer wants to return or replace an item |
| Delivery | Customer asks about delivery or a delayed order |
| Payment | Customer reports a payment issue |
| Cancellation | Customer requests order cancellation |
| Login | Customer reports an account login issue |
| Feedback | Customer shares an opinion or experience |
| Other | Message does not match the defined intents |

## 4. Category Labels

| Label | Definition |
|---|---|
| Order | Order placement, cancellation, or delivery issues |
| Product | Product quality, damage, or product-related feedback |
| Payment | Payment and refund-related issues |
| Account | Login and account access problems |
| Service | Customer service experience and general feedback |

## 5. Priority Labels

| Label | Definition |
|---|---|
| High | Urgent complaints, payment problems, refunds, cancellations, or serious negative issues |
| Medium | Issues such as delivery delays and product returns that need attention |
| Low | General feedback and positive messages without an urgent issue |

## 6. Annotation Rules

1. Read the complete customer message before assigning labels.
2. Choose labels based on the meaning of the message, not just individual keywords.
3. Assign exactly one label for each annotation field.
4. Use Other for intents that do not match the defined intent labels.
5. Record disagreements between automatic and human annotations.
6. Add reviewer notes whenever a label is corrected or a decision needs explanation.

## 7. Quality Review

Automatic annotations are compared with human-reviewed labels using:

- Accuracy
- Cohen's Kappa
- Field-level agreement

Disagreements should be reviewed and corrected before finalizing the annotations.

## 8. Dataset Limitation

The current dataset contains 100 records generated from 10 unique sample messages. Therefore, the current evaluation is a small demonstration and should not be treated as proof of production-level annotation performance.
