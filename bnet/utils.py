from os import environ
import requests

from .exceptions import BattleNetError

AUTH_URL = "https://us.battle.net/oauth/token"

def generate_access_token(client_id=None, secret=None):
    if client_id is None and secret is None:
        try:
            client_id = environ["BATTLE_NET_CLIENT_ID"]
            secret = environ["BATTLE_NET_SECRET"]
        except KeyError:
            raise ValueError("Either provide client_id and secret or set environment variables BATTLE_NET_CLIENT_ID, BATTLE_NET_SECRET")
    response = requests.post(AUTH_URL, auth=(client_id, secret), data={"grant_type": "client_credentials"}).json()
    if "error" in response:
        raise BattleNetError(response)
    return response
