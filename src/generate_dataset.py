
import pandas as pd

data = [
    {
        "ticket_id": f"TICKET_{i:03d}",
        "customer_id": f"CUST_{i:03d}",
        "message": message,
        "product": product,
        "channel": channel,
        "date": f"2026-10-{(i % 28) + 1:02d}"
    }
    for i, (message, product, channel) in enumerate([
        ("My order has not arrived yet.", "Electronics", "Email"),
        ("I want to return my damaged product.", "Fashion", "Chat"),
        ("The payment was deducted twice.", "Electronics", "Phone"),
        ("Thank you for the excellent service.", "Home", "Email"),
        ("I cannot log in to my account.", "Software", "Chat"),
        ("Please cancel my order immediately.", "Fashion", "Phone"),
        ("The product quality is very poor.", "Home", "Email"),
        ("I received the wrong item.", "Electronics", "Chat"),
        ("I am happy with my purchase.", "Fashion", "Email"),
        ("My refund has not been processed.", "Home", "Phone")
    ] * 10)
]

df = pd.DataFrame(data)

df.to_csv("data/customer_support_tickets.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())
