import random
import requests
from requests.auth import HTTPDigestAuth
import json


def getPayload(modelObject):
    import uuid;
    "function_docstring"
    if (type(modelObject) is unicode):
        if(modelObject == "string"):
            return  str(uuid.uuid4().get_hex().upper()[0:10])
        elif(modelObject == "int"):
            return str(random.randint(0, 100))
        elif (modelObject == "long"):
            return str(random.randint(10000, 1000000) )
    print "ERROR" + modelObject
    return "ERROR";


def generateParameterForModel(typeObject, models, generatedPayload):
    pass


def generateParameter(key,typeObject, models):
    "generate value for basic types"
    m_payload = ""
    if(type(typeObject) is dict):
        if (typeObject["type"] == "string" or typeObject["type"] == "int"  or typeObject["type"] == "long" ):
            concatenated = "\"" + key + ":\""  + getPayload(typeObject["type"])
            print concatenated
            return  concatenated;
    else:
        if typeObject in models.keys():
            m_model = models.get(typeObject)

            for m_key,m_value in m_model["properties"].iteritems():
                m_payload += generateParameter(m_key,m_value,models)
                print m_payload
            m_payload += generateParameterForModel(typeObject, models)
            return m_payload;
        else:
            print "something wrong happens"
    print "something wrong happens"
    return "";



url = 'http://api-loop-publication.frontiersin.org/api/v1/info/ManuallyAddedPublications'
data = ''
generatedPayload =""
response = requests.get(url, data=data)
jData = json.loads(response.content)
typeObject = jData["apis"][0]["operations"][0]["parameters"][1]["dataType"]
nameObject = jData["apis"][0]["operations"][0]["parameters"][1]["name"]
parameterValue = generateParameter("asd",typeObject,jData["models"])
models = jData["models"]
for model in models:
    for property in model["properties"]:
        print property
    print model
props = models[0]["properties"]
a = props[1]
k = 0




