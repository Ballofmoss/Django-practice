

class Resource:
    def __init__(self, name: str, resource_type:str):
        self.name = name
        self.resource_type = resource_type 
    def __del__(self):
        print(f"Ресурс {self.name} типа {self.resource_type} удалён.")
        
r1 = Resource("Соединение1", "подключеине к базе данных")
r2 = Resource("Соединение2", "подключеине к базе данных")

for _ in range(1,11):
    print(_)
    if _ == 5:
        del r2
        
class Node:
    data = None
    next = None
    def __init__(self, data) -> None:
        self.data = data
class Linked:
    start: Node = None
    end: Node = None
    
    def leng(self):
        temp = self.start
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count
    def search(self, data):
        temp = self.data
        while(self.start):
            if
        
        
        