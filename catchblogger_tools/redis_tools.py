import redis
from typing import Union, Optional, Dict
from tqdm.auto import tqdm


def create_redis_conn(redis_config):
    return redis.Redis(host=redis_config['host'],
                       port=redis_config['port'],
                       db=redis_config['db'], password=redis_config.get('password', None))


class RedisQueueIter:
    """Iterator for redis queue.
    """
    def __init__(self, redis_conn: Union[Dict, redis.Redis],
                 queue_key: Optional[str] = None, verbose: Union[bool, int] = 0,
                 clear_queue: Optional[bool] = True):
        if isinstance(redis_conn, Dict):
            self.redis_conn = create_redis_conn(redis_conn)
        elif isinstance(redis_conn, redis.Redis):
            self.redis_conn = redis_conn
        self.queue_key = queue_key
        self.verbose = verbose
        self.clear_queue = clear_queue

    def __iter__(self):
        if self.verbose > 0:
            self._pbar = tqdm(total=len(self))
        return self

    def __next__(self):
        val = self.redis_conn.lpop(self.queue_key)
        if val is None:
            raise StopIteration
        if self.verbose > 0:
            self._pbar.update()
        return val

    def __len__(self):
        return self.redis_conn.llen(self.queue_key)

    def __call__(self, queue_key: str):
        self.queue_key = queue_key
        return self

    def __del__(self):
        if getattr(self, '_pbar', None) is not None:
            self._pbar.close()

    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            if self.clear_queue:
                raise ValueError('Can\'t get redis queue slice with `clear_queue=True`')
            end = subscript.stop - 1 if subscript.stop is not None else len(self)
            return list(self.redis_conn.lrange(self.queue_key, subscript.start, end))
