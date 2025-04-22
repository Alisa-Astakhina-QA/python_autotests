import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4278b534ce6cb3f531705d5947452666'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Пикачу",
    "photo_id": 25
}
body_rename = {
    "pokemon_id": "295272",
    "name": "Pikachy",
    "photo_id": 26
}
body_add_pokeball = {
    "pokemon_id": "295272"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
