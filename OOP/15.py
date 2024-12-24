from io import TextIOWrapper

class List: 
    def __init__(self, *data: list[any]):
        self.__data = list(data)

    def __getitem__(self, index):
        if index > len(self.__data):
            return self.__data[-1]
        return self.__data[index]
    
    def __setitem__(self, index, value):
        if index > len(self.__data):
            self.__data[-1] = value
            return self.__data
        self.__data[index] = value
        return self.__data
    
    def __delitem__(self, index):
        if index > len(self.__data):
            del self.__data[-1]
        del self.__data[index]
    
class KeyValueStore:
    filename_with_path: str = "logs/log.txt"
    file: TextIOWrapper = None 
    __data: dict[any] = {}

    def __init__(self, initial: dict, filename_with_path: str = 'logs/log.txt'):
        self.filename_with_path = filename_with_path
        self.__data = initial
        self.file = open(self.filename_with_path, 'w')

    def __del__(self):
        self.file.close()

    def __getitem__(self, key: any):
        return self.__data[key]
    
    def __setitem__(self, key: any, value: any):
        self.__data[key] = value
        self.file.write(self.__data)
        return self.__data
    
    def __delitem__(self, key: any):
        del self.__data[key]
        self.file.write(self.__data)


# 1. Для чего используются методы __getitem__, __setitem__ и __delitem__ в Python?
# Для получения, изменения и удаления элементов как при работе со списками, словарями и т.п.

# 2. Что происходит, если вызвать obj[key] для объекта, у которого реализован только метод
# __getitem__
# Получим значение которое вернет __getitem__

