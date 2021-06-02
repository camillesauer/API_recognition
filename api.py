from fastapi import FastAPI
from main import fonction_nlp, square

app = FastAPI()

@app.get("/test")
async def root():
    return {"message": fonction_nlp()}

