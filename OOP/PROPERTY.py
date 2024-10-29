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
    
class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age
    
    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self, name):
        self._name = name
    
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def set_salary(self, amount):
        if amount>=30000:
            self._salary=amount
        else:
           raise ValueError("Зарплата не может быть меньше 30000")
    def apply_raise(self,count):
        self.salary=int(self.salary*count)

    
    @property 
    def age(self):
        return self._age
    @age.setter
    def set_age(self, age):
        self._age = age
    @age.deleter
    def del_age(self):
        self._age = None
    
    


# 1. Чем декоратор @property отличается от обычных методов?
# позволяет скрывать реализацию атрибута

# 2. Какие преимущества даёт использование свойств по сравнению с прямым доступом к
# атрибутам?
# инкапсуляцияб чистота кодаб контроль над изменениями
    
        
        


        