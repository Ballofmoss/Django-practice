import re


class UserSchem: pass

class DataBase: 
    users_data:list = []
    def get_data(self, url):
        with open(url, 'r', encoding='UTF=8') as f:
            result = f.readlines()
            f.close()
            return result
    def serializers(self, data):
        content = []
        for i in data:
            schema=dict()
            line = [i for i in re.split(r'\s',i) if i != ' ']
            for index in range(0,len(line)-1, 2):
                schema[line[index]] = line[index+1]
            content.append(schema)
        print(content)
        return content
    def create(self, data):
        for i in data:
            user = UserSchem()
            for key, item in i.items():
                setattr(user, key, item)
            self.users_data.append(user)
    def search(self, search):
        for user in self.users_data:
            for _, value in user.__dier__.items():
                if search in str(value):
                    return user
        return None
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
                
        
        
    
            
            
            
            
# daata = DataBase()
# text = daata.get_data('pivo.txt')
# text = daata.serializers(text)
# print(daata.create(text))
# print(daata.users_data[2].__dict__)


 
        
            