'''Каждый класс Python поддерживает следующие встроенные атрибуты, и к ним можно получить доступ, используя
оператор точки, как и любой другой атрибут —

    __dict__ — словарь, содержащий пространство имен класса.
    __doc__ — Строка документации класса или нет, если она не определена.
    __name__ — Имя класса.
    __module__ — Имя модуля, в котором определяется класс. Этот атрибут «__main__» в интерактивном режиме.
    __bases__ — возможно пустой кортеж, содержащий базовые классы,в порядке их появления в списке базовых классов.
'''

from class2 import Employee

print('Employee.__doc__:', Employee.__doc__)
print('Employee.__name__:', Employee.__name__)
print('Employee.__module__:',Employee.__module__)
print('Employee.__bases__' ,Employee.__bases__)
print('Employee.__dict__' ,Employee.__dict__)
