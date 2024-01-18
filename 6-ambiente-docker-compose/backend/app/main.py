from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Essa é uma resposta do container do back-end!!! 🎉🎉🎉"}

@app.get("/quebrar_app")
def quebrar_app():
    os.system("kill 1")
    return {"message": "O container parou..."}


