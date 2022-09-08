from fastapi import FastAPI, HTTPException
from app.Client import Client
from app.db import database


app = FastAPI()
@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/client")
def fetch_client(client):
    db = database()
    results = db.client.find()
    clients_liste = []
    for result in results:
        client = {
            "immatriculation": result["immatriculation"],
            "nom": result["nom"],
            "prenom": result["prenom"],
            "age": result["age"],
        }
        clients_liste.append(client)
    return clients_liste

@app.post("/client")
def create_client(clients_liste:Client):
    db = database()
    if db.client.find_one({"nom": Client.nom}) is not None:
        HTTPException(status=409, detail="[-] Nom is already registered")
    db.jeux.insert_one(clients_liste.dict())
    return clients_liste.dict()

