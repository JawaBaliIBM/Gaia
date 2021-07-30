"""
    Helper class to encapsulate download and upload file from IBM Object Storage.
    
    Maintainers:
    - fellitacandini@gmail.com
    - kaniaprameswara5@gmail.com
"""

import ibm_boto3
import io
import logging
import os
from ibm_botocore.client import Config

class ObjectStorage:
    def __init__(self) -> None:
        self.client = ibm_boto3.client(service_name='s3',
                                       ibm_api_key_id=os.getenv('IBM_API_KEY_ID'),
                                       ibm_service_instance_id=os.getenv(
                                            'IBM_SERVICE_INSTANCE_ID'),
                                       config=Config(signature_version='oauth'),
                                       endpoint_url=os.getenv('ENDPOINT_URL'))
        
    def upload_fileobj(self, json_str, filename):
        try:
            data = io.BufferedReader(io.BytesIO(json_str.encode()))
            self.client.upload_fileobj(data,
                                    os.getenv('BUCKET_NAME'), filename)
            data.close()

        except Exception as e:
            logging.exception('Got exception while uploading data. Exception: %s',
                            e)
            return {'success': False, 'errorMessage': e}
        else:
            return {'success': True, 'filename': filename}


    def download_fileobj(self, filename, dest):
        try:
            with open(dest, 'wb') as data:
                self.client.download_fileobj(os.getenv('BUCKET_NAME', 'news-scrapper-bucket'), filename, data)

        except Exception as e:
            logging.exception('Got exception while downloading data. Exception: %s',
                            e)
            return {'success': False, 'errorMessage': e}
        return {'success': True, 'dest': dest}
