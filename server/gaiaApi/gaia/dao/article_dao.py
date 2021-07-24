import os, logging, sys
sys.path.append("..")

from gaia.dao.db_client import db_client
from gaia.dataclass.article import Article
from gaia.dataclass.dataclass_utils import as_dict
from gaia.enum.sentiment import SentimentEnum

DATABASE_NAME = 'articles'
db = db_client[DATABASE_NAME]
PAGE_SIZE = int(os.getenv('PAGE_SIZE', default=5))

class ArticleDao:

    @staticmethod
    def create_article(data: Article):
        dict_data = as_dict(data)
        if dict_data is None:
            logging.error('Create article failed because failed to convert to dictionary.')
            return

        document = db.create_document(dict_data)

        logging.info('Document result {}'.format(document))

        if document.exists():
            logging.info('Create an article is success.')

    @staticmethod
    def create_bulk_articles(data: [Article]):
        dict_data = [as_dict(x) for x in data]
        if dict_data[0] is None:
            logging.error('Create bulk articles failed because failed to convert to dictionary.')
            return

        documents = db.bulk_docs(dict_data)

        logging.info('Documents result {}'.format(documents))

        if documents[0]['ok']:
            logging.info("Create articles is success.")

    @staticmethod
    def get_articles_by_brand(brand: str, page: int, limit=None):
        logging.info('Get articles from brand {}'.format(brand))

        if limit is None:
            limit = PAGE_SIZE

        skip = PAGE_SIZE * (page - 1)
        selector = {'brand': {'$eq': brand}}
        result = db.get_query_result(selector, skip=skip, limit=limit ,raw_result=True)

        return [x for x in result['docs']]

# article = Article(date='2008-09-17 14:02:00', sentiment=SentimentEnum.NEUTRAL, title='dummy', description='dummy', article_id='dummy', url='dummy', brand='dummy')
# create_bulk_articles([article, article])
# create_article(article)