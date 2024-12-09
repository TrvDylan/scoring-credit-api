from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Before Get")
    return {"message": "Hello World!"}
    print("Modification passed")