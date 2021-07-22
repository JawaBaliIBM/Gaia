import logging
from dataclasses import asdict, dataclass, is_dataclass
from datetime import datetime
from enum import Enum

def __dict_factory(article):
    def convert_value(obj):
            if isinstance(obj, Enum):
                return obj.value

            return obj

    return dict((k, convert_value(v)) for k, v in article)

def as_dict(data):
    if not is_dataclass(data):
        logging.error('Type should be dataclass intance.')
        return None
        
    return asdict(data, dict_factory=__dict_factory)