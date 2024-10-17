

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
        while(temp):
            if data == temp.data:
                return temp
        temp = temp.next
    def append(self, obj):
        new_node = Node(obj)
        if self.start is None:
            self.start = new_node
            return
        current_node = self.start
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    def remove(self, index: int):
        if self.start == None:
            return
        current_node = self.start
        position = 0
        if position == index:
            self.start = self.start.next
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next

# 1. Как работают метод __init__ и __del__.
# __init__ срабатывает при инициализации обьекта, а __del__ при его удалении

# 2. Какая последняя строчка вывелась после выполнения программы из практической
# части?   10



    

        
        
        