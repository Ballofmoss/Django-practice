from datetime import datetime

class Shop:
    def __init__(self):
        self.goods = []
    def add_product(self, product):
        self.goods.append(product)
    def remove_product(self, product):
        for index in range(len(self.goods)):
            if self.goods[index] == product:
                self.goods.pop(index)
                return

class Product:
    __id = 0
    def __new__(cls, *args. **kwargs):
        cls.__id+=1
        obj = super().__new__(cls)
        obj.id = cls.__id
        return obj
    def __init__(self,name:str,weight:float,price:float):
        self.name = name
        self.weight = weight
        self.price = price
    def __setattr__(self, name:str, value) -> None:
        type_dict = {
            "id": int,
            "name": str,
            "weight": (int,float),
            "price": (int,float),
        }
        if not isinstance(value, type_dict[name]):
            raise TypeError("Неверный тип присваиваемых данных")
        if name == 'weight' and not value > 0 :
            raise TypeError("Неверный тип присваиваемых данных")
        if name == 'price' and not value > 0 :
            raise TypeError("Неверный тип присваиваемых данных")
        super().__setattr__(name,value)
        
    def __delattr__(self, name: str) -> None:
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено")

class Library:
    name: str = None
    books: list[str] = []
    max_books: int = None

    @property
    def books(self):
        return self._books
    def __init__(self, name: str, max_books: int):
        self.name = name
        self.max_books = max_books
    def add_book(self, book:str):
        if len(self.books) < self.max_books:
            self.books.append(book)
    def remove_book(self, book:str):
        self.books.remove(book)
    def list_books(self):
        for book in self.books:
            print(book)
    
    

    def __getattribute__(self, name):
        print(f'[GET LOG | {datetime.now().strftime("%H:%M:%S")}] ', name)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == 'max_books' and self.max_books is not None:
            raise AttributeError('Нельзя изменить max_books после инициализации')
        
        if name == 'books' and len(self.books) > self.max_books:
            raise AttributeError('Кол-во книжек превышает max_books')
        super().__setattr__(name, value)
    
    def __delattr__(self, name:str) -> None:
        if name == 'name':
            raise AttributeError('Нельзя удалить атрибут name')
        print(f'[DELETE LOG | {datetime.now().strftime("%H:%M:%S")}]')
        super().__delattr__(name)
        
# # 1. Какие практические применения есть у магического метода __setattr__?
#  Этот метод вызывается, когда мы пытаемся установить значение атрибута
# объекта.

# # 2. В чем разница между __getattribute__ и __getattr__?
#  __getattribute__ - стандартный способ, а __getattr__ нужен если он не находит атрибут