import ibm_boto3
import io
import logging
import os
from ibm_botocore.client import Config

cos = ibm_boto3.client(service_name='s3',
                       ibm_api_key_id=os.getenv('IBM_API_KEY_ID'),
                       ibm_service_instance_id=os.getenv(
                           'IBM_SERVICE_INSTANCE_ID'),
                       config=Config(signature_version='oauth'),
                       endpoint_url=os.getenv('ENDPOINT_URL'))


def upload_fileobj(json_str, filename):
    try:
        data = io.BufferedReader(io.BytesIO(json_str.encode()))
        res = cos.upload_fileobj(data,
                                 os.getenv('BUCKET_NAME'), filename)
        data.close()

    except Exception as e:
        logging.exception('Got exception while uploading data. Exception: %s',
                          e)
        return {'success': False, 'errorMessage': e}
    else:
        return {'success': True, 'filename': filename}
