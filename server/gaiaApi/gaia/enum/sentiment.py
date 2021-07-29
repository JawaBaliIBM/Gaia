from enum import Enum

class SentimentEnum(Enum):
    NEGATIVE = 'negative'
    POSITIVE = 'positive'
    NEUTRAL = 'neutral'


class SentimentHelper:
    STR_TO_INT_MAPPING = {
        SentimentEnum.NEGATIVE: -1,
        SentimentEnum.POSITIVE: 1,
        SentimentEnum.NEUTRAL: 0
    }

    INT_TO_STR_MAPPING = {
        -1: SentimentEnum.NEGATIVE,
        1: SentimentEnum.POSITIVE, 
        0: SentimentEnum.NEUTRAL
    }

    @staticmethod
    def encode_sentiment(sentiment: str) -> int:
        sentiment_enum = SentimentEnum[sentiment.upper()]
        return SentimentHelper.STR_TO_INT_MAPPING[sentiment_enum]
    
    @staticmethod
    def decode_sentiment(sentiment: int) -> str:
        if sentiment != 0:
            sentiment = sentiment / abs(sentiment)
        return SentimentHelper.INT_TO_STR_MAPPING[sentiment]
