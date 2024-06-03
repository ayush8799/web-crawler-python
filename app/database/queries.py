import json

"""
Created a singleton db query class
This can be extended to a real db query class which can have all the queries in one place
"""

class DatabaseQuery:
    __instance = None  

    def __init__(self):
        print("calling __init__ method of the singleton class: DatabseQuery")
        if DatabaseQuery.__instance is not None:  
            raise Exception("This class is a singleton!")
        else:
            DatabaseQuery.__instance = self

    @staticmethod
    def get_instance():
        if DatabaseQuery.__instance is None:
            print("created a new Instance")
            DatabaseQuery()  
        return DatabaseQuery.__instance

    def save_data_to_json(self, data: object, filename: str = "app/database/storage.json"):
        """Saves data to a JSON file.

        Args:
            data: The data to be saved (any serializable object).
            filename: The name of the JSON file (default: "app/database/storage.json").
        """
        try:
            print(f"JSON FILE_NAME: {filename}")
            with open(filename, "r+") as f:
                existing_data = json.load(f)
                existing_data.extend(data)
                f.seek(0)
                json.dump(existing_data, f, indent=4)
        except Exception as excp:
            print(f'Error: save_data_to_json: {excp}')


db_query_instance = DatabaseQuery.get_instance()

