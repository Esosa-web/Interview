from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "customer_id": 1, "amount": 120, "status": "paid"},
    {"id": 2, "customer_id": 2, "amount": 50, "status": "pending"},
    {"id": 3, "customer_id": 1, "amount": 80, "status": "paid"},
    {"id": 4, "customer_id": 1, "amount": 30, "status": "cancelled"},
]
