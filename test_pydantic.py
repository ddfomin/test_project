import requests
from pydantic import BaseModel, ValidationError

# 1. Описываем модель (схему)
class User(BaseModel):
    title: str
    body: str
    userId: str
    id: str

# 2. API вернул такой JSON
a = requests.post("https://jsonplaceholder.typicode.com" + "/posts", json={"title": "foo", "body": "bar", "userId": 1})
json_data = a.json()
print(json_data)

# 3. Валидируем (создаем объект)
try:
    user = User(**json_data)
except ValidationError as e:
    print("Ошибка валидации:", e)