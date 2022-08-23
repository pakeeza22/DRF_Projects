import requests
import json

URL = "http://127.0.0.1:8000/std_model_api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(2)


def post_data():
    data = {
        'name': "ahmad",
        'age': 99,
        'city': 'Lahore',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)

# post_data()

def update_data(id = None):
    data = {
        'id': id,
        'name': 'Konpal Eman',
    }
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data, headers=headers)
    data = r.json()
    print(data)


# update_data(6)

def delete_data(id = None):
    data = {
        'id': id,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data(9)
get_data()
