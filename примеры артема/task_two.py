import re
from io import TextIOWrapper

class UserSchema:
    pass

class DataBase:
    data: list = []

    def get_data(self, url: str):
        with open(url, 'r', encoding='UTF-8') as file:
            result = file.readlines()
            self.serialize(result)
            file.close()
            return result

    def serialize(self, data: TextIOWrapper):
        content = []
        for i in data:
            schema = dict()
            line = [i for i in re.split(r'\s', i) if i != '']
            for j in range(0, len(line) - 1, 2):
                schema[line[j]] = line[j + 1]
            content.append(schema)
        self.create(content)
        return content
    
    def search(self, query: str) -> dict:
        for i in self.data:
            for key, value in i.__dict__.items():
                if query in str(value):
                    return {
                        "key": key,
                        "value": value
                    }

    def create(self, data):
        for i in data:
            user = UserSchema()
            for key, item in i.items():
                setattr(user, key, item)
            self.data.append(user)

class Translator:
    dictionary: dict = {}

    def add(self, eng: str, rus: str):
        if self.dictionary.get(eng) is not None:
            if type(self.dictionary.get(eng)) is list:
                self.dictionary[eng].append(rus)
            else:
                temp = self.dictionary[eng]
                self.dictionary[eng] = [temp, rus]
        else:
            self.dictionary[eng] = rus
    
    def remove(self, eng: str):
        if self.dictionary.get(eng) is not None:
            del self.dictionary[eng]

    def translate(self, eng: str):
        return self.dictionary.get(eng)
    
# ! КОНТРОЛЬНЫЕ ВОПРОСЫ
# 1. Функция внутри класса
# 2. Обращается к самому экземляру класса, к его методам/свойтсвам