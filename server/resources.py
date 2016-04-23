__author__ = 'rcj1492'
__created__ = '2015.12'

'''
    a collection of constructors for resources available to interface
'''

import json
from jsonmodel.validators import jsonModel

class requestModel(object):

    def __init__(self, json_model):
        if not isinstance(json_model, jsonModel):
            raise TypeError('requestModel input must be a jsonModel object.')
        self.model = json_model

    def validate(self, request):
        response = {}
        code = 0
        return response, code

class databaseModel(object):

    def __init__(self, json_model):
        if not isinstance(json_model, jsonModel):
            raise TypeError('databaseModel input must be a jsonModel object.')
        self.model = json_model

class resourceModel(object):

    def __init__(self, json_model):
        if not isinstance(json_model, jsonModel):
            raise TypeError('resourceModel input must be a jsonModel object.')
        self.model = json_model
        self.request = requestModel(self.model)
        self.database = databaseModel(self.model)

# import json object files
operationFile = json.loads(open('models/operation-model.json').read())
catchFile = json.loads(open('models/catch-model.json').read())
specimenFile = json.loads(open('models/specimen-model.json').read())

# construct object models from files
operationModel = jsonModel(operationFile)
catchModel = jsonModel(catchFile)
specimenModel = jsonModel(specimenFile)

# construct resource objects from object models
operationResource = resourceModel(operationModel)
catchResource = resourceModel(catchModel)
specimenResource = resourceModel(specimenModel)

if __name__ == '__main__':
    print(operationResource.request.model.schema)



