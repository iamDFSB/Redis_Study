from redis import Redis

class RedisRepositoryWithTTL(): # Time To Live (TTL) 
    def  __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def get(self, key: str) -> any:
        return self.__redis_conn.get(key)

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)

    def get_hash(self, key: str, field: str) -> any:
        return self.__redis_conn.hget(key, field)

    def insert_hash(self, key: str, field: str, value: any) -> None:
        self.__redis_conn.hset(key, field, value)

    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)
    