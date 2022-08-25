import redis


def create_redis_conn(redis_config):
    return redis.Redis(host=redis_config['host'],
                       port=redis_config['port'],
                       db=redis_config['db'], password=redis_config.get('password', None))
