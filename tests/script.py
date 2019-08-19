import json
import requests
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
res = requests.get('http://localhost:9200')

#print(res.content)
#print(es.get(index='sw', doc_type='people', id=5))
print(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}}))

#let's iterate over swapi people documents and index them
r = requests.get('http://localhost:9200')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
    print(r.content)
print(i)



r = requests.get('http://localhost:9200')
i = 18
while r.status_code == 200:
   r = requests.get('http://swapi.co/api/people/'+ str(i))
   es.index(index='sw', doc_type='people', id=i,     body=json.loads(r.content))
   i=i+1
