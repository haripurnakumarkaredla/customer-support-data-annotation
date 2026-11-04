import pandas as pd

df = pd.read_csv("data/customer_support_tickets.csv")

def annotate_sentiment(message):
    message = message.lower()

    if any(word in message for word in ["excellent", "happy", "thank you"]):
        return "Positive"
    elif any(word in message for word in ["poor", "damaged", "not arrived",
                                          "wrong", "twice", "cannot", "not been"]):
        return "Negative"
    return "Neutral"


def annotate_intent(message):
    message = message.lower()

    if "refund" in message:
        return "Refund"
    elif "return" in message:
        return "Return"
    elif "arrived" in message:
        return "Delivery"
    elif "payment" in message or "deducted" in message:
        return "Payment"
    elif "cancel" in message:
        return "Cancellation"
    elif "log in" in message:
        return "Login"
    elif "quality" in message or "happy" in message or "excellent" in message:
        return "Feedback"
    return "Other"


def annotate_category(message):
    message = message.lower()

    if any(word in message for word in ["payment", "deducted", "refund"]):
        return "Payment"
    elif any(word in message for word in ["order", "arrived", "cancel", "wrong item"]):
        return "Order"
    elif any(word in message for word in ["log in", "account"]):
        return "Account"
    elif any(word in message for word in ["product", "quality", "damaged"]):
        return "Product"
    return "Service"


def annotate_priority(sentiment, intent):
    if intent in ["Payment", "Refund", "Cancellation"] or sentiment == "Negative":
        return "High"
    elif intent in ["Delivery", "Return"]:
        return "Medium"
    return "Low"


df["sentiment"] = df["message"].apply(annotate_sentiment)
df["intent"] = df["message"].apply(annotate_intent)
df["category"] = df["message"].apply(annotate_category)
df["priority"] = df.apply(
    lambda row: annotate_priority(row["sentiment"], row["intent"]),
    axis=1
)

df.to_csv("outputs/annotated_tickets.csv", index=False)

print("Text annotation completed!")
print("Total annotated records:", len(df))
print(df[["message", "sentiment", "intent", "category", "priority"]].head(10))