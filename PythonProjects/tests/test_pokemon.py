import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4278b534ce6cb3f531705d5947452666'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '31186'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == TRAINER_ID    

@pytest.mark.parametrize('key, value', [('trainer_name', 'Алиса'), ('id', TRAINER_ID), ('avatar_id', 1)])
def test_parametrize (key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value