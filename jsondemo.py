import json

cities = ["Wien", "Graz", "London"]
dict = { "cities": cities, "degree": '27,5', "it_rains": False}
dict_json = json.dumps(dict)
print(dict_json)