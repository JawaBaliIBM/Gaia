import sys
sys.path.append("..")

from dataclasses import dataclass
from gaia.enum.sentiment import SentimentEnum
from gaia.dataclass.dataclass_utils import as_dict

@dataclass
class Brand:
    name: str
    score: float
    sentiment: 'SentimentEnum'

# brand = Brand(name='dummy', score=0.75, sentiment=SentimentEnum.POSITIVE)
# print(as_dict(brand))