class Robot():
    '''Представляет робота с иименем'''
    #переменная класса,содержащая количество роботов
    population = 0

    def __init__(self,name):
        '''Инициализация данных'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        #при создании этой личности, робот добавляется к переменной population
        Robot.population += 1

    def __del__(self):
        """Я уммираю"""
        print('{0} уничтожается'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота

        Да,они это могут'''
        print('Приветствую! Мои хозяева называют меня {0}'.format(self.name))



    def howMany(self):
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))


    howMany = staticmethod(howMany) #можно записать проще @staticmethod и на след строке шла функция def howMany...
    #можем опр. как сlassmethod или staticmethod, в завис. от того, нужно ли нам знать в каком классе мы находимся

droid_1 = Robot('R2-D2')

droid_1.sayHi()
Robot.howMany(2)

droid_2 = Robot('C-500')
droid_2.sayHi()
Robot.howMany('fdvd')

print('\nЗдесь роботы могут проделать какую то работу. \n' )

print('Роботы закончили свою работу. Давайте уничтожим их')

del droid_1
del droid_2

Robot.howMany(2)