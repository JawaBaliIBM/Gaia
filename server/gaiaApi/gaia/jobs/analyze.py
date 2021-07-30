"""
    Function to analyze scraped articles:
    - Pull a json file containing articles from object storage
    - Analyze entities and sentiment using IBM NLU
    - Save article and brand data to database
    
    Maintainers:
    - kaniaprameswara5@gmail.com
"""

import os
import sys
from pathlib import Path

sys.path.append("..")

from tempfile import NamedTemporaryFile


from gaia.enum.sentiment import SentimentEnum, SentimentHelper
from gaia.jobs.object_storage import ObjectStorage
from gaia.jobs.ibm_nlu_helper import analyze_entity_sentiment
from gaia.dao.article_dao import ArticleDao
from gaia.dao.brand_dao import BrandDao
from gaia.dataclass.article import Article
from gaia.dataclass.brand import Brand


def analyze(filepath: Path) -> None:
    storage = ObjectStorage()

    local_filepath = NamedTemporaryFile(suffix=".json").name
    storage.download_fileobj(filepath, local_filepath)
    docs = analyze_entity_sentiment(local_filepath)

    articles = []
    brands_to_create = []
    brands_to_update = []
    brands_by_name = {}
    for doc in docs:
        for brand_name in doc.sentiment.keys():
            sentiment = doc.sentiment[brand_name]["label"]
            article = Article(
                date=doc.date,
                sentiment=sentiment,
                title=doc.title,
                description=doc.snippet,
                article_id=doc.id,
                url=doc.url,
                brand=brand_name
            )
            articles.append(article)

    ArticleDao.create_bulk_articles(articles)

    for doc in docs:
        for brand_name in doc.sentiment.keys():
            existing_brand = BrandDao.get_brand_by_name(brand_name)
            if existing_brand is not None:
                brands_to_update.append(brand)
            brand = brands_by_name.get(brand_name) or existing_brand
            if brand is None:
                brand = Brand(
                    name=brand_name,
                    score=0,
                    sentiment=SentimentEnum.NEUTRAL
                )
                brands_to_create.append(brand)
            article_dicts = ArticleDao.get_articles_by_brand(brand_name)
            articles = [Article.from_dict(d) for d in article_dicts]
            article_sentiments = [SentimentHelper.encode_sentiment(article.sentiment) for article in articles]
            article_sentiment_score = sum(article_sentiments)
            num_articles = len(article_sentiments)
            average_sentiment = article_sentiment_score // num_articles
            brand.score = average_sentiment
            brand.sentiment = SentimentHelper.decode_sentiment(average_sentiment)

            brands_by_name[brand_name] = brand

    BrandDao.create_bulk_brands(brands_to_create)
    for brand in brands_to_update:
        BrandDao.edit_brand(brand)
    os.remove(local_filepath)

# analyze("guardian-news-2021-06-26.json")
# analyze("guardian-news-2021-06-23.json")
# analyze("guardian-news-2021-06-24.json")
# analyze("guardian-news-2021-06-25.json")
# analyze("guardian-news-2021-06-27.json")
# analyze("guardian-news-2021-06-29.json")
