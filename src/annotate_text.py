
import pandas as pd
from pathlib import Path


# 1. Sentiment annotation
def annotate_sentiment(message):
    message = str(message).lower()

    if any(word in message for word in ["excellent", "happy", "thank you"]):
        return "Positive"

    elif any(word in message for word in [
        "poor", "damaged", "not arrived", "wrong",
        "twice", "cannot", "not been"
    ]):
        return "Negative"

    return "Neutral"


# 2. Intent annotation
def annotate_intent(message):
    message = str(message).lower()

    if "refund" in message:
        return "Refund"

    elif any(word in message for word in ["return", "wrong item"]):
        return "Return"

    elif "arrived" in message:
        return "Delivery"

    elif "payment" in message or "deducted" in message:
        return "Payment"

    elif "cancel" in message:
        return "Cancellation"

    elif "log in" in message:
        return "Login"

    elif any(word in message for word in [
        "quality", "happy", "excellent", "thank you"
    ]):
        return "Feedback"

    return "Other"


# 3. Category annotation
def annotate_category(message):
    message = str(message).lower()

    if any(word in message for word in ["payment", "deducted", "refund"]):
        return "Payment"

    elif any(word in message for word in [
        "order", "arrived", "cancel", "wrong item"
    ]):
        return "Order"

    elif any(word in message for word in ["log in", "account"]):
        return "Account"

    elif any(word in message for word in [
        "product", "quality", "damaged", "purchase"
    ]):
        return "Product"

    return "Service"


# 4. Priority annotation
def annotate_priority(sentiment, intent):

    if intent in ["Payment", "Refund", "Cancellation"] or sentiment == "Negative":
        return "High"

    elif intent in ["Delivery", "Return"]:
        return "Medium"

    return "Low"


# 5. Main annotation process
def main():

    df = pd.read_csv("data/customer_support_tickets.csv")

    df["sentiment"] = df["message"].apply(annotate_sentiment)
    df["intent"] = df["message"].apply(annotate_intent)
    df["category"] = df["message"].apply(annotate_category)

    df["priority"] = df.apply(
        lambda row: annotate_priority(
            row["sentiment"],
            row["intent"]
        ),
        axis=1
    )

    Path("outputs").mkdir(exist_ok=True)

    df.to_csv("outputs/annotated_tickets.csv", index=False)

    print("Text annotation completed successfully!")
    print("Total annotated records:", len(df))

    print("\nUpdated annotation results:")

    print(
        df[[
            "ticket_id",
            "message",
            "sentiment",
            "intent",
            "category",
            "priority"
        ]].head(10).to_string(index=False)
    )


# 6. Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
