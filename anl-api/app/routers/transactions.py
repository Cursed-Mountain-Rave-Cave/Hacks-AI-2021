from fastapi import APIRouter

from pydantic import BaseModel


class Transaction(BaseModel):
    id: int = 0
    # 1 - транзакция оформлена, завершена 8 - транзакция оформлена, производство незавершено
    status: str = "Complete/Incomplete"
    incomplete: bool = True  # 0 - обычное 1- незавершенное производство
    common_hs: str = "Common HS"  # ХС Integer business_entity
    common_enterprise: str = "Common enterprise"  # Предприятие Integer enterprise
    insertDate: str = "InsertDate"  # дата создания транзакции Timestamp
    formedDate: str = "FormedDate"  # дата оформления транзакции Timestamp


TRANSACTIONS = [Transaction(**{"id": 1}), Transaction(**{"id": 2}), Transaction(**{"id": 3})]


router = APIRouter()


@router.get("/transactions")
async def get_transactions():
    return TRANSACTIONS


@router.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: int):
    return TRANSACTIONS[transaction_id]
