class Man: 

    def __init__(self, balance: int, credit: int) -> None: 
        self.balance = balance
        self.credit = credit

    def __bool__(self):
        return self.balance > 0 and self.credit > 0

class Device:

    def __init__(self, is_on: bool, battery_level: int):
        self.is_on = is_on
        self.battery_level = battery_level

    def __bool__(self):
        return self.is_on and self.battery_level > 10


# Контрольные вопросы
# 1. Как Python определяет истинность объекта, если метод __bool__ отсутствует?
# по методу __len__

# 2. Чем метод __bool__ отличается от __len__?
# len это длина объекта
# bool возвращает булево значение при сравнении обхекта



# 3. Как результат метода __bool__ влияет на условные конструкции (if, while и т. д.)?
# подставляется значение true или false