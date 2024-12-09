from fastapi import FastAPI
import logging

logging.info("Test log")

app = FastAPI()

@app.get("/")
def read_root():
    print("Before Get")
    logging.info("Test avant le return")
    return {"message": "Hello World!"}
    logging.info("Test après le return")