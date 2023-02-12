import requests


def load_operations(url):
    response = requests.get(url)
    #print(response.status_code)
    #if response.status_code != 200:
        #return None, f'ERROR: {response.status_code}'
    #else:
    return response.json()
