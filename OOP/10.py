# class Model:
#     def query(self, *args, **kwargs):
#         for key, item in kwargs.items():
#             self.__dict__[key]=item
#     def __str__(self):
#         result=[]
#         for key, item in self.__dict__.items():
#             result.append(f"{key}={item}")

#             return "Model:"+",".join(result)
        
#     def __len__(self):
#         return len(self.__dict__)
    
class ShoppingCart:
    products=[]
    def __len__(self):
        return len(self.products)
    
class Book:
    title = None
    author = None
    pages = None

    def __str__(self):
        result=[]
        for key, item in self.__dict__.items():
            result.append(f"{key}={item}")
            return "Model:"+",".join(result)
    def __repr__(self):
        result=[]
        for key, item in self.__dict__.items():
            result.append(f"{key}={item}")
            return "Model:"+",".join(result)
    def __len__(self):
        return len(self.__dict__)

# 1. В чем разница между методами __str__ и __repr__?
# __str__ предназначен для вывода, понятного конечному пользователю, а __repr__ ориентирован на разработчиков и используется для отображения объекта

# 2. Что произойдёт, если вызвать print(object) для объекта, у которого не определен метод
# __str__?
# Отобразится название класса и ячейка в памяти, которую он занимает

# 3. Какую задачу решает метод __abs__, и в каких случаях его реализация может быть
# полезной?
# определяет, что должно возвращаться при вызове abs(object). Обычно его
# используют для чисел или объектов, где можно определить абсолютное значение.
