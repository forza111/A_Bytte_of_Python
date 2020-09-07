class Employee:
    '''Comonbase class for all employees'''
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print('Total employee {}'.format(Employee.empCount))

    def displayEmploye(self):
        print('Name: {}, Salary: {}'.format(self.name,self.salary))
        

emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

emp1.displayEmploye()
emp2.displayEmploye()
print('Total empoyee {}'.format(Employee.empCount))

#Можно добавлять, удалять или изменять атрибуты классов и объектов в любое время

emp1.age = 7 # добавляет атрибут age
emp1.age = 8 # изменяет атрибут age
#del  emp1.age # удаляет атрибут age

'''GetAttr (объект, имя [, по умолчанию]) — для доступа к атрибуту объекта.
Hasattr (объект, имя) — проверить , если атрибут существует или нет.
SetAttr (объект, имя, значение) — установить атрибут. Если атрибут не существует, он будет создан.
Delattr (объект, имя) — для удаления атрибута.'''

getattr(emp1,'age') # вернет значение атрибута age
hasattr(emp1,'age') # вернет True если атриут age существует
setattr(emp1,'age',9) #устанавливает значение атрибута = 9
delattr(emp1,'age') # удаляет атрибут age

