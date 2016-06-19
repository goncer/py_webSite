
import requests
from requests.auth import HTTPDigestAuth
import json

url = 'http://api-loop-publication.frontiersin.org/api/v1/info/ManuallyAddedPublications'
data = ''
response = requests.get(url, data=data)
jData = json.loads(response.content)
models = jData["models"]
for model in models:
    for propertie in model["properties"]:
        print propertie
    print model
props = models[0]["properties"]
a = props[1]
k = 0
