from fastapi import FastAPI
import sys
import logging
import joblib

# Logs
logging.basicConfig(level=logging.INFO)
sys.stdout = sys.stderr

# Variables
model_path = "model.pkl"
scaler_path = "scaler.pkl"

# Création de l'API
app = FastAPI()

# Chargement du modele de ML et du scaler avec joblib
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except Exception as e:
    print(f"Erreur lors du chargement des fichiers : {e}")
    model = None
    scaler = None

print("model : ", model)
print("scaler : ", scaler)

@app.get("/")
def read_root():
    print("print : test pendant le get")
    logging.info("log : test pendant le get")
    return {"message": "Hello World!"}