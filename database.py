from pymongo import MongoClient
from abc import ABC, abstractmethod

class PlateRepository(ABC):

    @abstractmethod
    def save(self, plateNumber:str):
        pass

class MongoDB(PlateRepository):
    def __init__(self, connectionString: str):
        # Connect to database
        self._connectionString = connectionString
        self._client = MongoClient(self._connectionString)
        self._database = self._client["plate-db"]
        self._collection = self._database["plate"]

    def save(self, plateNumber):
        document = {
            "plateNumber": plateNumber
        }
        self._collection.insert_one(document)

if __name__ == "__main__":
    # Test Code
    test = MongoDB("mongodb://localhost:27017")
    test.save_to_database("15ABS875")


    