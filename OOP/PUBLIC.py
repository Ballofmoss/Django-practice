import datetime
class Book:
    def __init__(self, title, author, pages)
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
            raise ValueError("Количество страниц должно быть положительным")

    def display_info(self):
        return f"Название: '{self.title}', Автор: {self._author}, Страницы: {self.__pages}"
    
class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self._year = year
        self.__mileage = mileage
    
    def set_year(self, year):
        if year > 1886 and year <= datetime.now.year:
            self._year = year
        else:
            raise ValueError("Укажите валидный год выпуска")
    
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным")
        
    def get_year(self): 
        return self._year

    def get_mileage(self):
        return self.__mileage
    
# 1. Почему важно использовать сеттеры и геттеры в ООП?
# Это необходимо чтобы ограничить доступ к атрибутам класса из вне, добавить валидацию атрибутов

# 2. Приведите пример ситуации, когда использование защищенных атрибутов является более
# предпочтительным, чем использование публичных.
# все атрибуты для которых нужна валидация а еще хз 


            
            
            
            


    
    

