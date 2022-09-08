"""Module used to fill a mongo database with defined data.
"""

from pymongo import MongoClient

from Client import Client


class MongoSeeder:

    def __init__(self):
        host = 'mongodb'
        cl = MongoClient(host=f'{host}')
        self.__db = cl.registre

    @property
    def db(self):
        return self.__db

    def seed(self):
        """Seeds the database.
        """
        # Clearing collection
        self.db.client.drop()

        # Insert data
        registre = []

        # Valid data
        nom = "Zafindramoma"
        prenom = "Mitondratsara"
        age = 22
        immatriculation = "1234VDRCO2"
        registre.append(Client)

        print("Remplissage de la base de données...")
        MongoSeeder().seed()

        client = MongoClient(host="mongodb")
        db = client.registre
        print("Fait.")