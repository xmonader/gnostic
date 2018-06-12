# GENERATED FILE: DO NOT EDIT!
# Types used by the API.

from dataclasses import dataclass, fields

# implements the service definition of Pet
@dataclass
class Pet:
    id: int
    name: str
    tag: str

# implements the service definition of Pets
@dataclass
class Pets:
    pass

# implements the service definition of Error
@dataclass
class Error:
    code: int
    message: str

# ListPetsParameters holds parameters to ListPets
@dataclass
class ListPetsParameters:
    limit: int

# ListPetsResponses holds responses of ListPets
@dataclass
class ListPetsResponses:
    OK: Pets
    default: Error

# CreatePetsResponses holds responses of CreatePets
@dataclass
class CreatePetsResponses:
    default: Error

# ShowPetByIdParameters holds parameters to ShowPetById
@dataclass
class ShowPetByIdParameters:
    petId: str

# ShowPetByIdResponses holds responses of ShowPetById
@dataclass
class ShowPetByIdResponses:
    OK: Pets
    default: Error

