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

# __dict__ хранит список и позволяет уменьшить количество занимаемой памяти


# 1. Создайте класс Goods с атрибутами класса и значениями:
# a. title Мороженое
# b. weight 151
# c. tp “Еда”
# d. price 12321
# Изменить значение атрибута price и weight
# 2. Создайте пустой класс Car, и добавьте атрибуты со значениями:
# a. model Тойота
# b. color черный
# c. number П34А123
# 3. Что делает хранит атрибут __dict__?(самостоятельно узнать)