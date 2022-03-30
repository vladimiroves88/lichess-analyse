from urllib import response
import requests
import ndjson

with open('./lichess.token') as f:
    token = f.read()

class LichAnalyse:   

    def __init__(self, token):
        self.hed = requests.headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/x-ndjson'}
        self.token = token
        self.res = requests.get("https://lichess.org/api/account", headers=self.hed).json()
        self.account_name = self.res['username']

    def get_games(self):
        response = requests.get(f"https://lichess.org/api/games/user/{self.account_name}", headers=self.hed).json(cls=ndjson.Decoder)
        return response