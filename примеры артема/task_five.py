from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))

    @staticmethod
    def check_name(cls, name: str):
        words = name.split()
        if len(words) != 2:
            return False
        
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and all(char in cls.CHARS_FOR_NAME for char in last_name)
    
class TemperatureConverter:
    data: float = None

    @staticmethod
    def celsius_to_fahrenheit(celsius: float):
        return celsius * 9/5 + 32

    @classmethod
    def from_kelvin(cls, kelvin: float):
        cls.data = kelvin - 273.15
        return super(TemperatureConverter, cls).__new__(cls)

class Employee:
    name: str = None
    age: int = None
    post: str = None

    @staticmethod
    def is_valid_age(age: int):
        return age >= 18 and age < 65
    
    @classmethod
    def from_string(cls, data: str):
        arr = data.split(', ')
        if Employee.is_valid_age(int(arr[1])):
            cls.name = arr[0]
            cls.age = int(arr[1])
            cls.post = arr[2]
            return super().__new__(cls) 
        else:
            raise ValueError('Недопустимый возраст')
        
    def get_details(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nДолжность: {self.post}"
    
# ! КОНТРОЛЬНЫЕ ВОПРОСЫ
# 1. classmethod получает cls первым аргументом и позволяет создать различные фабричные методы для класса, а staticmethod - метод класса, который не нуждается в доступе к объекту класса
# 2. нельзя, потому что staticmethod не имеет доступа к объекту класса