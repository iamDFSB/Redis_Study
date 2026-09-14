from repositories import DatabaseRepository, RedisRepository
from interfaces import DatabaseServiceInterface

class DatabaseService(DatabaseServiceInterface):
    def __init__(self, redis_repo: RedisRepository, db_repo: DatabaseRepository) -> None:
        self.__redis_repo = redis_repo
        self.__db_repo = db_repo


    def create_key_value_operation(self, args) -> None:
        key = args.key
        value = args.value

        self.__redis_repo.insert(key, value)
        self.__db_repo.add(key, value)
        print("Key-Value created with success")


    def get_value_by_key_operation(self, args) -> None:
        key = args.key
        if self.__redis_repo.key_exists(key):
            print("Getting Redis response")
            value = self.__redis_repo.get(key)
        else:
            print("Getting DB response")
            value = self.__db_repo.get(key)

        print(f"Value: {value}") if value else print("The key doesn't exist")


    def update_value_operation(self, args) -> None:
        key = args.key
        value = args.value

        self.__redis_repo.insert(key, value)
        response = self.__db_repo.update(key, value)

        if not response:
            return None
        
        print("Key-Value updated with success")
        