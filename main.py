from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Hill Country Land Intelligence API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}