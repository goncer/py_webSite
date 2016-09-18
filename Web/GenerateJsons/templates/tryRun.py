from __future__ import print_function

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

    print ("ERROR" + modelObject , "\n")
    return "ERROR";


def generateParameterForModel(typeObject, models, generatedPayload):
    pass


def generateParameter(key,typeObject, models):
    "generate value for basic types"
    m_payload = ""
    if(type(typeObject) is dict):
        if (typeObject["type"] == "string" or typeObject["type"] == "int"  or typeObject["type"] == "long" ):
            concatenated = "\"" + key + ":\""  + getPayload(typeObject["type"])
            print (concatenated ,end = "\n" )
            return  concatenated;
        if (typeObject["type"] == "Array" ):
            #str("[" + getItem + "]")
            name=typeObject["items"].values()[0]
            m_model = models.get(name)
            return "["  + recursive_getModelEleemntValues(models.get(name), m_payload, models) + "]"

    if (type(typeObject) is dict):
        m_model = models.get(typeObject["type"])
    elif(type(typeObject) is unicode):
        m_model = models.get(typeObject)
    if(m_model != None):
        return recursive_getModelEleemntValues(m_model, m_payload, models)
    else:
        print ("something wrong happens" )
    print ("something wrong happens")
    return "";


def recursive_getModelEleemntValues(m_model, m_payload, models):
    for m_key, m_value in m_model["properties"].iteritems():
        m_payload += generateParameter(m_key, m_value, models)
        print(m_payload, end="\n")
    # m_payload += generateParameterForModel(m_key,typeObject, models)
    return m_payload;


url = 'http://api-loop-publication.frontiersin.org/api/v1/info/ManuallyAddedPublications'
data = ''
generatedPayload =""
response = requests.get(url, data=data)
jData = json.loads(response.content)
typeObject = jData["apis"][0]["operations"][0]["parameters"][1]["dataType"]
nameObject = jData["apis"][0]["operations"][0]["parameters"][1]["name"]
parameterValue = generateParameter("asd",typeObject,jData["models"])
models = jData["models"]




