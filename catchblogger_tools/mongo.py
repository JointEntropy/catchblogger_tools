import pymongo
from typing import Dict


def spawn_mongo_db_conn(config: Dict[str, str]) -> pymongo.database.Database:
    """
    :param config:
    :return:
    """
    login, passw, host = config['login'], config['password'], config['host']
    CONNECTION_STRING = f"mongodb://{login}:{passw}@{host}"
    client = pymongo.MongoClient(CONNECTION_STRING)
    return client[config['db']]


def spawn_mongocloud_db_conn(config: Dict[str, str]) -> pymongo.database.Database:
    """
    TODO Might fail if str contains special chars that should be URI encoded.
    :param config:
        Should contain `login`, `password`, `project_name`, `db`  fields.
    :return:
    """
    connect_uri_template = 'mongodb+srv://{login}:{password}@{project_name}.sjbvb.mongodb.net/?retryWrites=true&w=majority'
    connect_uri = connect_uri_template.format(**config)
    db = pymongo.MongoClient(connect_uri)[config['db']]
    return db