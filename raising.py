class ShortInputException(Exception):
    '''Пользовательский класс исключениия'''
    def __init__(self,lenght,atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast
try:
    text = input('Введите что нибудь')
    if len(text) < 3:
        raise ShortInputException(len(text), 3) #исключение можно поднять при помощи оператора raise,передав ему
    #имя ошибки/иисключения, а также объект исключеения, который нужно выбросить
    #Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF??? ):')
except ShortInputException as ex:
    print('ShortInputException: длина введенной строки: -- {}; \
          ожидалось, как минимум, {} '.format(ex.lenght, ex.atleast))
else:
    print('не было исключений')