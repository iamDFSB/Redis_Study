from datetime import datetime
import sys
from pathlib import Path

path = Path(__file__)
sys.path.insert(0, str(path.parent.parent))

from connection import RedisConnectionHandle
from redis_repository_ttl import RedisRepositoryWithTTL

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepositoryWithTTL(redis_conn)

now = datetime.now()
date_now = now.strftime("%Y-%m-%d")

redis_repository.insert_hash_ex(date_now, "user_2", "Luna", 20)
redis_repository.insert_hash_ex(date_now, "user_1", "Josh", 20)
redis_repository.insert_hash_ex(date_now, "user_3", "Jessica", 20)