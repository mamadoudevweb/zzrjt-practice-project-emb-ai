import unittest

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    def test_positive_sentiment(self) -> None:
        sentiment = sentiment_analyzer("I love working with computers")
        self.assertEqual(sentiment["label"], "SENT_POSITIVE")

    def test_negative_sentiment(self) -> None:
        sentiment = sentiment_analyzer("I hate working with computers")
        self.assertEqual(sentiment["label"], "SENT_NEGATIVE")

    def test_neutral_sentiment(self) -> None:
        sentiment = sentiment_analyzer("I am on computers")
        self.assertEqual(sentiment["label"], "SENT_NEUTRAL")

    def test_invalid_input(self) -> None:
        sentiment = sentiment_analyzer("fqkldfjqdlkfjf")
        self.assertFalse(bool(sentiment["label"]))
        self.assertFalse(bool(sentiment["score"]))

if __name__ == "__main__":
    unittest.main()