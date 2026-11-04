# Customer Support Data Annotation Guidelines

## 1. Project Objective
To classify customer support messages consistently for sentiment, intent, category, and priority.

## 2. Sentiment Labels

- **Positive:** Customer expresses satisfaction or happiness.
- **Negative:** Customer expresses dissatisfaction, complaints, or problems.
- **Neutral:** Customer provides information without clear positive or negative emotion.

## 3. Intent Labels

- **Refund:** Customer requests or asks about a refund.
- **Return:** Customer wants to return a product.
- **Delivery:** Customer reports a delivery issue.
- **Payment:** Customer reports payment-related problems.
- **Cancellation:** Customer wants to cancel an order.
- **Login:** Customer reports account login problems.
- **Feedback:** Customer shares an opinion about a product or service.
- **Other:** Message does not match the above intents.

## 4. Category Labels

- **Payment:** Payment and refund issues.
- **Order:** Order, delivery, and cancellation issues.
- **Account:** Login and account-related issues.
- **Product:** Product quality, damage, and product-related issues.
- **Service:** General customer service issues.

## 5. Priority Labels

- **High:** Urgent complaints, payment problems, refund issues, or serious customer dissatisfaction.
- **Medium:** Delivery and return issues requiring attention.
- **Low:** General feedback and non-urgent requests.

## 6. Quality Rules

1. Read the complete customer message before assigning labels.
2. Use only the approved labels.
3. Do not guess when information is unclear.
4. Maintain consistency across similar messages.
5. Flag uncertain annotations for human review.

## 7. Important Note

The current Python script uses keyword-based automatic annotation. Its labels must be reviewed by a human annotator before being treated as verified ground-truth data.