import json

my_dict = {'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}

# Сериализация - перевод в JSON
json_format = json.dumps(my_dict)
print(f"JSON: {type(json_format)}, {json_format}")

# Десериализация - перевод в словарь
dict_format = json.loads(json_format)
print(f"DICT: {type(dict_format)}, {dict_format}")