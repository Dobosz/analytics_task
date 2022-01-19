import io
from datetime import datetime
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.responses import StreamingResponse

from models import Transaction, ResponseTransaction, TransactionType, ResponseSum, ResponseAverage, \
    ResponseOtherAccount, ResponsePopularTitles
from repository import TransactionRepository

app = FastAPI()
repository = TransactionRepository()


@app.get("/transaction", response_model=List[ResponseTransaction])
async def list_transaction():
    return repository.list()


@app.get("/transaction/{id}", response_model=ResponseTransaction)
async def list_transaction(id: int):
    transaction = repository.get(id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return repository.get(id)


@app.post("/transaction/", response_model=ResponseTransaction)
async def list_transaction(transaction: Transaction):
    result = repository.insert(transaction)
    return result


@app.put("/transaction/{id}", response_model=ResponseTransaction)
async def list_transaction(id: int, transaction: Transaction):
    result = repository.update(id, transaction)
    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return result


@app.get("/transaction_analysis/sum", response_model=ResponseSum)
async def get_sum(type: TransactionType, from_date: datetime, to_date: datetime) -> ResponseSum:
    """
    TODO
    Zwraca sumę transkcji w przedziele pomiędzy "from_date" i "to_date" dla zadanego typu transakcji "type"
    :param type: typ transkacji
    :param from_date: data od
    :param to_date: data do
    :return: Zwraca obiek z sumą transkacji
    """
    pass


@app.get("/transaction_analysis/average", response_model=ResponseAverage)
async def get_avg(type: TransactionType, from_date: datetime, to_date: datetime) -> ResponseAverage:
    """
    TODO
    Zwraca srednią arytmetyczną transkcji w przedziele pomiędzy "from_date" i "to_date"
    dla zadanego typu transakcji "type"
    :param type: typ transkacji
    :param from_date: data od
    :param to_date: data do
    :return: Zwraca obiek z srednią arytmetyczną transkacji
    """
    pass


@app.get("/transaction_analysis/popular_titles", response_model=List[ResponsePopularTitles])
async def get_popular_titles(from_date: datetime, to_date: datetime) -> List[ResponsePopularTitles]:
    """
    TODO
    Zwraca listę obiektów opisujących tytuły transakcji. Jest ona unikatowa i posortowana malejąco po ilości wystąpień
    w zadanym przedziele czasu.
    :param from_date: data od
    :param to_date: data do
    :return: Zwraca tytuły
    """
    pass


@app.get("/transaction_analysis/other_accounts", response_model=List[ResponseOtherAccount])
async def get_other_accounts(from_date: datetime, to_date: datetime) -> List[ResponseOtherAccount]:
    """
    TODO
    Zwraca listę obiektów opisujących drugą stronę transakcji. Jest to:
        * Unikatowa lista rachunków
        * Zawiera numer rachunku, ilość wystąpueć w zadanym czasie i sumę
        * Posortowana malejąco po kluczu (sum, count)
        * W zadanym przedziele czasu
    :param from_date: data od
    :param to_date: data do
    :return: Zwraca listę rachunków
    """
    pass


@app.get("/transaction_analysis/graph", response_class=StreamingResponse)
async def get_graph(from_date: datetime, to_date: datetime) -> StreamingResponse:
    """
    TODO
    Zwraca histogram z sumy wydatków dla zadanej daty.
    :param from_date:
    :param to_date:
    :return:
    """
    with open("/Users/mdobosz/Downloads/example.png", "br") as file:
        image = io.BytesIO()
        image.write(file.read())
        image.seek(0)
        return StreamingResponse(image, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
