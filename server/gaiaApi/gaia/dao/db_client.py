import os
from cloudant.client import CouchDB, Cloudant
from cloudant.adapters import Replay429Adapter

if os.getenv('ENV') is 'PROD':
    db_client = Cloudant(os.getenv('DB_USERNAME'), os.getenv('DB_PASSWORD'), 
        url=os.getenv('DB_URL'), adapter=Replay429Adapter(retries=10, initialBackoff=0.01))
else:
    db_client = CouchDB('guest', '1234', url='http://localhost:5984',
        connect=True, auto_renew=True)