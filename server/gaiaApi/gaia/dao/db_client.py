import os
from cloudant.client import CouchDB, Cloudant
from cloudant.adapters import Replay429Adapter

if os.environ.get('VCAP_APPLICATION'):
    db_client = Cloudant(os.environ.get('DB_USERNAME'), os.environ.get('DB_PASSWORD'), 
        url=os.environ.get('DB_URL'), adapter=Replay429Adapter(retries=10, initialBackoff=0.01),
        connect=True)
else:
    db_client = CouchDB('guest', '1234', url='http://localhost:5984',
        connect=True, auto_renew=True)