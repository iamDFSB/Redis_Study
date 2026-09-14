from redis import Redis
from .connection_options import ConnectionOptions

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
