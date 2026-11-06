
import unittest

from src.annotate_text import (
    annotate_sentiment,
    annotate_intent,
    annotate_category,
    annotate_priority
)


class TestAnnotation(unittest.TestCase):

    # Test sentiment
    def test_positive_sentiment(self):
        self.assertEqual(
            annotate_sentiment("I am happy with my purchase."),
            "Positive"
        )

    def test_negative_sentiment(self):
        self.assertEqual(
            annotate_sentiment("My product is damaged."),
            "Negative"
        )

    def test_neutral_sentiment(self):
        self.assertEqual(
            annotate_sentiment("Please provide product details."),
            "Neutral"
        )

    # Test intent
    def test_refund_intent(self):
        self.assertEqual(
            annotate_intent("My refund has not been processed."),
            "Refund"
        )

    def test_return_intent(self):
        self.assertEqual(
            annotate_intent("I received the wrong item."),
            "Return"
        )

    def test_delivery_intent(self):
        self.assertEqual(
            annotate_intent("My order has not arrived yet."),
            "Delivery"
        )

    # Test category
    def test_product_category(self):
        self.assertEqual(
            annotate_category("I am happy with my purchase."),
            "Product"
        )

    def test_payment_category(self):
        self.assertEqual(
            annotate_category("The payment was deducted twice."),
            "Payment"
        )

    def test_order_category(self):
        self.assertEqual(
            annotate_category("Please cancel my order."),
            "Order"
        )

    # Test priority
    def test_high_priority(self):
        self.assertEqual(
            annotate_priority("Negative", "Refund"),
            "High"
        )

    def test_medium_priority(self):
        self.assertEqual(
            annotate_priority("Neutral", "Delivery"),
            "Medium"
        )

    def test_low_priority(self):
        self.assertEqual(
            annotate_priority("Positive", "Feedback"),
            "Low"
        )

    # Edge-case tests
    def test_empty_message_sentiment(self):
        self.assertEqual(annotate_sentiment(""), "Neutral")

    def test_empty_message_intent(self):
        self.assertEqual(annotate_intent(""), "Other")

    def test_empty_message_category(self):
        self.assertEqual(annotate_category(""), "Service")

    def test_uppercase_message(self):
        self.assertEqual(
            annotate_sentiment("I AM HAPPY WITH MY PURCHASE"),
            "Positive"
        )


if __name__ == "__main__":
    unittest.main()
