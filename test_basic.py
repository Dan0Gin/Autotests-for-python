import pytest
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADERS = {"Content-Type": "application/json"}

def test_get_trainers():
    """"
    KTI-1 Get trainers
    """
    response=requests.get(url=f'{URL}/trainers', headers=HEADERS, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_name():
    """"
    KTI-2 Get my trainer name
    """
    response=requests.get(url=f'{URL}/trainers?trainer_id=3600', headers=HEADERS, timeout=5)
    assert response.json()["trainer_name"] == "Kentakki", 'Unexpected trainer name'
