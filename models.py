from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class TransactionType(Enum):
    WITHDRAW = "WITHDRAW"
    DEPOSIT = "DEPOSIT"


class Transaction(BaseModel):
    title: str
    executed_at: datetime
    amount: Decimal = Field(..., gt=0)
    type: TransactionType
    other_account_nr: str


class ResponseTransaction(Transaction):
    id: int


class ResponseSum(BaseModel):
    sum: Decimal
    type: TransactionType


class ResponseAverage(BaseModel):
    average: Decimal
    type: TransactionType


class ResponsePopularTitles(BaseModel):
    title: str
    count: int


class ResponseOtherAccount(BaseModel):
    other_account_nr: str
    count: int
    sum: Decimal
