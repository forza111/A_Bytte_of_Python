poem = '''\
Программировать весело,
Если работа скучна,
Чтобы придать ей веселый тон - 
   используй Python!
'''

f = open('poem.txt','w') # открываем для записи
f.write(poem) #записываем текст в фаил
f.close() #закрываем фаил

f = open('poem.txt') #по умолчанию режим чтения

while True:
    line = f.readline()
    if len(line) == 0: #нулевая длина обозначает конец фаила
        break
    print(line, end='')

f.close()#закрываем фаил