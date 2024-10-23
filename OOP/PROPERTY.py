class BankAccount:
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount: int):
        if amount < 0:
            raise ValueError("Баланс не может быть меньше нуля")
        self._balance = amount
        
    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Баланс не может быть меньше нуля")
        self._balance += amount
        
    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Баланс не может быть меньше нуля")
        self._balance -= amount
    
    def __init__(self, initial_balance = 0) -> None:
        self._balance = initial_balance
        
class Product:
    def __init__(self, name, price, discount):
        self._name = name
        self._price = price
        self._discount = discount
        
    def set_price(self, price):
        if price >= 0:
            self._price = price
        else: 
            raise ValueError("Цена не должна быть отрицательной")
    def set_discount(self, discount):
        if 0 < discount > 100:
            self._discount = discount
        else:
            raise ValueError("Укажите скидку от 1 до 100 %")
    @property
    def price_with_discount(self, price, discount):
        result = price * discount / 100
        return result
    
    
# Сделать имплоииии

# 1. Чем декоратор @property отличается от обычных методов?
# позволяет скрывать реализацию атрибута

# 2. Какие преимущества даёт использование свойств по сравнению с прямым доступом к
# атрибутам?
# инкапсуляцияб чистота кодаб контроль над изменениями
    
        
        


        