import re


class UserSchem: pass

class DataBase: 
    users_data = []
    def get_data(self, url):
        with open(url, 'r', encoding='UTF=8') as f:
            result = f.readlines()
            f.close()
            return result
    def serializers(self, data):
        content = []
        for i in data:
            schema=dict()
            line = [i for i in re.split(r'\s',i) if i != '']
            for index in range(0,len(line)-1, 2):
                schema[line[index]] = line[index+1]
            content.append(schema)
            return content
    def create(self, data):
        for i in data:
            user = UserSchem()
            for key, item in i.items():
                setattr(user, key, item)
                self.users_data.append(user)
    # def search()

daata = DataBase()
text = daata.get_data('pivo.txt')
daata.create(text)
print(daata.users_data)
 
        
            