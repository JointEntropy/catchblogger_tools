import pymongo
from typing import Dict


def spawn_mongo_db_conn(config: Dict):
    login, passw, host = config['login'], config['password'], config['host']
    CONNECTION_STRING = f"mongodb://{login}:{passw}@{host}"
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client[config['db']]