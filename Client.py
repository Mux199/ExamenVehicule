import re

from pydantic import validator

class Client:
    def __init__(self, nom, prenom, age, immatriculations):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.immatriculations = immatriculations

    @validator("age")
    def controle_minimum_age(cls,value):
        #"verifier l'age entre 20 et 60"
        if (value<20) or (value>60):
            raise ValueError('age non accepte')
        return value

    @validator("immatriculation")
    def controle_immatriculation(self,value):
        #"verifier l'immatriculation
        if not re.Match("^[012345689{4}([VDR]|([0-9]|10){2})[A-Za-z]{1,2}[0-9]{1}(UV|LB"):
            if not re.match("^[012345689]{4}((T|CO|CA)|([0-9]|10){2})[A-Za-z]{1,2}[0-9]{1}(UV|LB)"):
                raise ValueError('immatriculation invalide')
        return value

