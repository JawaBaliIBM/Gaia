import os, logging, sys
from typing import List
sys.path.append("..")

from gaia.dao.db_client import db_client
from gaia.dataclass.brand import Brand
from gaia.dataclass.dataclass_utils import as_dict
from gaia.enum.sentiment import SentimentEnum

DATABASE_NAME = 'brands'
db = db_client[DATABASE_NAME]

class BrandDao:

    @staticmethod
    def create_brand(data: Brand):
        dict_data = as_dict(data)
        if dict_data is None:
            logging.error('Create brand failed because failed to convert to dictionary.')
            return

        if BrandDao.get_brand_by_name(data.name) is not None:
            logging.error('Brand already exist')
            return

        document = db.create_document(dict_data)

        logging.info('Document result {}'.format(document))

        if document.exists():
            logging.info('Create a brand is success.')

    @staticmethod
    def create_bulk_brands(data: List[Brand]):
        dict_data = [as_dict(x) for x in data]
        if dict_data[0] is None:
            logging.error('Create bulk articles failed because failed to convert to dictionary.')
            return

        documents = db.bulk_docs(dict_data)

        logging.info('Documents result {}'.format(documents))
        if documents[0]['ok']:
            logging.info("Create articles is success.")

    @staticmethod
    def get_brand_by_name(name: str):
        logging.info('Get brand with name {}'.format(name))

        selector = {'name': {'$eq': name}}
        result = db.get_query_result(selector, raw_result=True, 
            limit=1)

        brand_results = [x for x in result['docs']]
        
        return None if len(brand_results) < 1 else brand_results[0]

    @staticmethod
    def edit_brand(data: Brand):
        logging.info('Update brand with name {}'.format(data.name))

        selector = {'name': {'$eq': data.name}}
        doc = BrandDao.get_brand_by_name(data.name)
        if doc is None:
            logging.error('Brand with name {} doesn\'t exist.'.format(data.name))
            return

        dict_updated_data = as_dict(data)

        for key, value in dict_updated_data.items():
            doc[key] = value
        
        doc.save()

        logging.info('Document result {}'.format(doc))

# brand = Brand(name='dummy', score=0.75, sentiment=SentimentEnum.POSITIVE)
# update_brand = Brand(name='dummy', score=0.86, sentiment=SentimentEnum.POSITIVE)
# edit_brand(update_brand)