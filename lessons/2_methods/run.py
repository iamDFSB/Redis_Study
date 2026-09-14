import sys
from pathlib import Path

path = Path(__file__)
sys.path.insert(0, str(path.parent.parent))

from connection import RedisConnectionHandle
from redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
redis_repository.insert("Nome", "John Doo")
redis_repository.insert_hash("user", "name", "John Doo2")
