from pymongo import MongoClient

class SaveMongoDb:
    def __init__(self, connectionString: str):
        self._connectionString = connectionString
        self._client = MongoClient(self._connectionString)
        self._database = self._client["plate-db"]
        self._collection = self._database["plate"]

    def save_to_database(self, text):
        document = {
            "plateNumber": text
        }
        self._collection.insert_one(document)

if __name__ == "__main__":
    # Test Code
    test = SaveMongoDb("mongodb://localhost:27017")
    test.save_to_database("15ABS875")


    