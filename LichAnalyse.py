import requests

with open('./lichess.token') as f:
    token = f.read()

hed = requests.headers = {'Authorization': f'Bearer {token}'}

print(requests.get("https://lichess.org/api/account", headers=hed).json())