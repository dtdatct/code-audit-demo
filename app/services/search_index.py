import requests

ES_URL = "http://elasticsearch:9200/products/_search"


def search(term):
    body = '{"query": {"match": {"name": "' + term + '"}}}'
    return requests.post(ES_URL, data=body, headers={"Content-Type": "application/json"}).json()
