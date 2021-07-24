import sys
sys.path.append("..")

from dataclasses import dataclass, asdict
from datetime import datetime
from gaia.enum.sentiment import SentimentEnum
from gaia.dataclass.dataclass_utils import as_dict

@dataclass
class Article:
    date: str
    sentiment: 'SentimentEnum'
    title: str
    description: str
    article_id: str
    url: str
    brand: str

# article = Article(date=datetime.now(), sentiment=SentimentEnum.NEUTRAL, title='dummy', description='dummy', article_id='dummy', url='dummy', brand='dummy')
# print(as_dict(article))