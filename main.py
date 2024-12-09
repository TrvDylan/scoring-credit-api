from fastapi import FastAPI
import sys
import logging

# Logs
logging.basicConfig(level=logging.INFO)
sys.stdout = sys.stderr

print("print : test avant l'app")
logging.info("log : test avant l'app")

app = FastAPI()

print("print : test apres l'app")
logging.info("log : test apres l'app")

@app.get("/")
def read_root():
    print("print : test pendant le get")
    logging.info("log : test pendant le get")
    return {"message": "Hello World!"}