import json
from typing import Union, Dict, List
from pathlib import Path

path = Path(__file__)
PATH_DB = path.parent.parent / "database/db.json"

class DatabaseRepository:

    def get(self, key: str) -> Union[any, None]:
        with open(PATH_DB, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("Database is empty")
                return None
            results = json.loads(content)
            list_of_values = list(filter(lambda row: row.get(key), results))
            if not list_of_values:
                return None

            return list_of_values[0].get(key)

    def add(self, key: str, value: any) -> None:
        item = {key: value}
        try:
            with open(PATH_DB, "r+", encoding="utf-8") as file:
                content = file.read()
                
                if not content.strip():
                    data = [item]
                else:
                    data = json.loads(content)
                    data.append(item) 
                
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                
        except FileNotFoundError:
            with open(PATH_DB, "w") as file:
                json.dump([item], file, indent=4)


    def update(self, key: str, new_value: any) -> any:
        if not self.key_exists(key):
            print("There is no data to be updated")
            return None

        db_final_result = '[]'
        with open(PATH_DB, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("Database is empty")
                return None

            results: List[Dict] = json.loads(content)
            for result in results:
                if result.get(key):
                    result[key] = new_value
                    break

            db_final_result = json.dumps(results, indent=4)

        with open(PATH_DB, "w", encoding="utf-8") as file:
            file.write(db_final_result)

        return True


    def key_exists(self, key: str) -> bool:
        print("Checking whether the key exists or not")
        with open(PATH_DB, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                return False
            
            results = json.loads(content)
            for result in results:
                value = result.get(key)
                if value:
                    return True

            return False

            

if __name__ == "__main__":
    print(DatabaseRepository().key_exists("name"))