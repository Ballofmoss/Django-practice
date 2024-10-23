from datetime import datetime

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self.__age = age

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")
        
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self._author = author
        self.__pages = pages

    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным числом")
        
    def display_info(self):
        return f'Название: {self.title}, автор: {self._author}, страниц: {self.__pages}'

class Car:
    def __init__(self, model: str, year: int, mileage: int):
        self.model = model
        self._year = year
        self.__mileage = mileage

    def get_year(self):
        return self._year
    
    def set_year(self, year: int):
        if year > 1886 and year <= datetime.now().year:
            self._year = year
        else:
            raise ValueError(f"Год не может быть менее 1886 или более текущего ({datetime.now().year})") 
        
    def get_mileage(self):
        return self.__mileage
    
    def set_mileage(self, mileage: int):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным")

# ! КОНТРОЛЬНЫЕ ВОПРОСЫ        
# 1. Для того чтобы менять/получать приватные поля обьекта, не нарушая правил установленным классом
# 2. Когда нужно ограничить действия с свойствами обьекта, но давая доступ к их получению / изменению

