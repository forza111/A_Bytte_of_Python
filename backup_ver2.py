import os
import time

#1 Фаилы и каталоги, которые необходимо скопировать, собираем в список
sourse = ['/home/nikita/PycharmProjects/untitled1/ariphm.py',
         '/home/nikita/PycharmProjects/untitled1/arithmetic.py']
#Для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки

#2 Резервные копии должны храниться в основном каталоге резерва
target_dir ='/home/nikita/backup'

#3 Фаилы помещаются в ЗИП архив
#4 Именем подкаталога в основном каталоге служит текущая дата
today = target_dir + os.sep + time.strftime('%Y%m%d')

#Текущее время служит именем zip - архива
now = time.strftime('%H%M%S')

#Создаем каталогЮ если его еще нет
if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)
#Функция os.path.exists проверяет существует ли каталог, соответсвтующий текущей дате
#Функция os.mkdir создает каталог today

#Имя ЗИП фаила
target = today + os.sep + now + '.zip'

# Используем команду 'zip' для помещения фаилов в zip архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(sourse))


# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    #команда возвращает 0, если выполнена успешно
    print('Резервная копия упешно создана в', target)

else:
    print('Создание резервной копии не удалось')
