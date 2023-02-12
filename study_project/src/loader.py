import requests


def load_operations(url):
    response = requests.get(url)
    return response.json()
