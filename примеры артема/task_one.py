class Goods:
    title: str = None
    weight: int = None
    tp: str = None
    price: int = None

    def __init__(self, title: str, weight: int, tp: str, price: int) -> None:
        self.title = title
        self.weight = weight
        self.tp = tp
        self.price = price

ice_cream = Goods("Мороженое", 151, "Еда", 12321)
ice_cream.price = 9999
ice_cream.weight = 95

class Car:
    model: str = None
    color: str = None
    number: str = None

    def __init__(self, model: str, color: str, number: str) -> None:
        self.model = model
        self.color = color
        self.number = number

    
toyota = Car("Toyota", "Черный", "П123А34")

# 3. Выводит все свойства в виде словаря
print(toyota.__dict__)

# ! КОНТРОЛЬНЫЕ ВОПРОСЫ
# 1. hasattr, setattr, delattr, getattr
# 2. Класс - это абстракция, на основе которой создаются обьекты