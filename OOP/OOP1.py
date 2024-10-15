# class Human:
#     height = None
#     age = None
    
# human_one = Human()
# human_two = Human()



# human_one.age = 22
# human_two.age = 452352

# print(human_one.age)
# print(human_two.age)

# delattr(human_one, 'height')
# delattr(human_two, 'height')

# print(hasattr(human_one, 'height'))
# print(hasattr(human_two, 'height'))



class Goods:
    title = 'Мороженое'
    weight = 151
    tp = '"еда"'
    price = 12321
    
Goods.price = 2342
Goods.weight = 230
print(Goods.price, Goods.weight )

class Car: pass

toyota_2 = Car()

toyota_2.model = 'Toyota'
toyota_2.color = 'Черный'
toyota_2.number = 'П34А123'

print(toyota_2.model, toyota_2.color, toyota_2.number)

# 1. напишите функции, которые удаляют атрибут класса, создают атрибут класса, проверяют
# существует ли атрибут класса и возвращают значение атрибута класса
#  hasattr, setattr, delattr, getattr

# 2. Чем отличается объект от класса 
# Класс - это абстракция, на основе которой создаются обьекты
