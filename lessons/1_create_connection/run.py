from redis import Redis 

redis_connection = Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Key-Value
redis_connection.set("key_1", "value_1")
redis_connection.set("key_2", "value_2")

# Get values by keys
value_1 = redis_connection.get("key_1")
print(value_1)
value_2 = redis_connection.get("key_2")
print(value_2)

# Hash-Values
redis_connection.hset("hash_name", "name", "John")
redis_connection.hset("hash_name", "age", 23)

# Get values by hash name
name = redis_connection.hget("hash_name", "name")
print(name)
result = redis_connection.hgetall("hash_name")
print(result)

# Delete value by hash name
redis_connection.hdel("hash_name", "name")

# Verify the existence of the value
key_1_validation = redis_connection.exists("key_1") # 1 = True and 0 = False
print(key_1_validation)
field_key = redis_connection.hexists("hash_name", "age")
print(field_key)