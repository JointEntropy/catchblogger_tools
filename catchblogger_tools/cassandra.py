from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Session
import json
from typing import Dict


def spawn_session(bundle_path: str, tokens_info: Dict) -> Session:
    # Зачем нужно use_default_tempdir=True...
    # ...написано тутhttps://docs.datastax.com/en/developer/python-driver/3.25/cloud/#use-default-tempdir
    cloud_config = {'secure_connect_bundle': bundle_path,
                    'use_default_tempdir': True}
    auth_provider = PlainTextAuthProvider(tokens_info['clientId'], tokens_info['secret'])
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    session.default_timeout = 60
    return session


def simple_session_test(session: Session):
    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")

