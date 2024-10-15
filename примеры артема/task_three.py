class Resource:
    def __init__(self, name: str, resource_type: str) -> None:
        self.name = name
        self.resource_type = resource_type
    
    def __del__(self):
        print(f'Ресурс {self.name} типа {self.resource_type} удалён')

r1 = Resource("test", "test1")
r2 = Resource("test1", "test2")

class Node:
    data = None
    next = None

    def __init__(self, data) -> None:
        self.data = data

class LinkedList:
    start: Node = None
    end: Node = None

    def search(self, data):
        temp = self.start
        while (temp):
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

    def len(self):
        temp = self.start
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count


# ! КОНТРОЛЬНЫЕ ВОПРОСЫ
# 1. __init__ срабатывает при инициализации обьекта, а __del__ при его удалении
# 2. 10