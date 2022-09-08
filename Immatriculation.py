from pydantic import BaseModel, validator
import re

class ModeleImmatriculation(BaseModel):
    immatriculation: str

