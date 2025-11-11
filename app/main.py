from fastapi import FastAPI
from .db import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Welcome to Hill Country Land Intelligence API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}