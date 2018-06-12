
from flask import Flask, send_from_directory, send_file

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

# we will add all of the resources here for now.
		
		
OpenAPI Petstore_api = Blueprint('OpenAPI Petstore_api', __name__)

# 


@OpenAPI Petstore_api.route('/pets', methods=['GET']
def listPets(*fields(parameters) :): pass
# 


@OpenAPI Petstore_api.route('/pets', methods=['POST']
def createPets(): pass
# 


@OpenAPI Petstore_api.route('/pets/{petId}', methods=['GET']
def showPetById(*fields(parameters) :): pass

