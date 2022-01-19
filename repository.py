import csv
from typing import Dict, List, Optional

from models import Transaction, ResponseTransaction
from utils import Singleton


class TransactionRepository(metaclass=Singleton):
    def __init__(self):
        self.db: Dict[int, ResponseTransaction] = {}
        self._current_id = 0
        self._load_csv("transactions.csv")

    def _load_csv(self, path):
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            for row in reader:
                row_data = {}
                for idx, header in enumerate(headers):
                    row_data[header] = row[idx]
                id = int(row_data["id"])
                self.db[id] = ResponseTransaction(**row_data)
                self._current_id = max(id, self._current_id)

    def list(self) -> List[ResponseTransaction]:
        return list(self.db.values())

    def get(self, id: int) -> Optional[ResponseTransaction]:
        if id not in self.db:
            return None
        return self.db[id]

    def insert(self, transaction: Transaction) -> Optional[ResponseTransaction]:
        id = self._current_id + 1
        result = ResponseTransaction(id=id, **transaction.dict())
        self.db[id] = result
        self._current_id = id
        return result

    def update(self, id: int, transaction: Transaction) -> Optional[ResponseTransaction]:
        if id not in self.db:
            return None
        result = ResponseTransaction(id=id, **transaction.dict())
        self.db[id] = result
        return result
