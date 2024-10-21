# class Singleton:
#     _instance = None
    
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance    
    
# sing1 = Singleton()
# sing2 = Singleton()

# print(sing1 is sing2)
# print(sing1)
# print(sing2)\

class Book:

    self.title = title
    self.author = author
    self.year = year   
    def __new__(cls, *args, **kwargs):
        for i in book.bibliothec:
            
            
        if book.bibliothec.__count<5:
            obj = super(five, cls).__new__(cls)
            return obj
        elif five.__count<6:
            obj = super(five, cls).__new__(cls)
            return obj
        else:
            print('Вы уже создали максимальное число объектов класса five')
    def __init__(self):
        Book.bibliothec.append(self.name)

class five: 
    
    __count = 0
    
    def __new__(cls, *args, **kwargs):
        if five.__count<5:
            obj = super(five, cls).__new__(cls)
            return obj
        elif five.__count<6:
            obj = super(five, cls).__new__(cls)
            return obj
        else:
            print('Вы уже создали максимальное число объектов класса five')
    def __init__(self):
        five.__count += 1
        
f1 = five()
f2 = five()
f3 = five()
f4 = five()
f5 = five()
f6 = five()
f6 = five()



# 1. Чем отличаются метод __new__ от __init__?

# 2. Для чего нужен класс super()?

# Метод super предоставляет доступ к методам родительского класса. Он используется для вызова
# методов, определенных в родительских классах, что особенно полезно в многократном
# наследовании. super помогает избежать явного указания имени родительского класса и
# обеспечивает более гибкое и безопасное взаимодействие между классами




 
        
        
   