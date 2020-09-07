'''Базовые методы перегрузки
етод, описание и пример вызова
1 	__init__ (self [, args …])
Конструктор (с любыми необязательными аргументами)
Пример вызова: obj = className (args)

2 	__del __ (самостоятельно)
Деструктор, удаляет объект
Образец звонка: del obj

3 	__repr __ (самостоятельно)
Оцениваемое строковое представление
Пример вызова: repr (obj)

4 	__str __ (самостоятельно)
Печатное представление строки
Пример вызова: str (obj)

5 	__cmp__ (self, x)
Сравнение объектов
Пример вызова: cmp (obj, x)'''

class Vector():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector ({}, {})' .format(self.a, self.b)
    def __add__(self, other):
        return Vector (self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)

print(v1 + v2)
#для сложение векторов используем метод add


