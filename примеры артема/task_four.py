class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
class OnlyFiveObjects:
    count_classes: int = 0
    last_created_object = None

    def __new__(cls, *args, **kwargs):
        if OnlyFiveObjects.count_classes < 5:
            return super(OnlyFiveObjects, cls).__new__(cls)
        else:
            return cls.last_created_object
        
    def __init__(self):
        OnlyFiveObjects.count_classes += 1
        if OnlyFiveObjects.count_classes == 5:
            OnlyFiveObjects.last_created_object = self
            

class Book:
    all_books: list = []
    title: str = None
    author: str = None
    year: int = None

    def __new__(cls, *args, **kwargs):
        for i in Book.all_books:
            if i.title == args[0] and i.author == args[1]:
                return i
        return super(Book, cls).__new__(cls)

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        Book.all_books.append(self)

book1 = Book("эм", "em", 123)
book2 = Book("эм", "em", 123)

# ! КОНТРОЛЬНЫЕ ВОПРОСЫ
# 1. __new__ срабатывает до __init__ и определяет какой обьект будет создан
# 2. Для того чтобы получить доступ к родительскому классу