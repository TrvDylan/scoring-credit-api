from fastapi import FastAPI

app = FastAPI()

print("Before Get")

@app.get("/")
def read_root():
    return {"message": "Hello World!"}
    print("Modification passed")