from redis import Redis
from dataclasses import dataclass

@dataclass
class ConnectionOptions:
    HOST: str = "localhost"
    PORT: int = 6379
    DB: int = 0


class RedisConnectionHandle:
    def __init__(self) -> None:
        self.__host = ConnectionOptions.HOST
        self.__port = ConnectionOptions.PORT
        self.__db = ConnectionOptions.DB
        self.__connection = None


    def connect(self) -> Redis:
        self.__connection = Redis(
            host=self.__host, 
            port=self.__port, 
            db=self.__db,
            decode_responses=True,
        )
        return self.__connection


    def get_conn(self) -> Redis:
        return self.__connection


class RedisRepository:
    def  __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def get(self, key: str) -> any:
        return self.__redis_conn.get(key)

    def insert(self, key: str, value: any, ex=30) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def get_hash(self, key: str, field: str) -> any:
        return self.__redis_conn.hget(key, field)

    def insert_hash(self, key: str, field: str, value: any) -> None:
        self.__redis_conn.hset(key, field, value)

    def key_exists(self, key: str) -> bool:
        return True if self.__redis_conn.exists(key) else False