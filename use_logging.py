import os,platform,logging

if platform.platform().startswith('Windows'): #проверяем, какая оперционная система на компьютере
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                #определяем диск, содержщий домашний каталог
                                os.getenv('HOMEPATH'),\
                                #опеделяем путь к домашнему каталогу на нем и имя фаила
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.log')
#для других платформ нужно знать только путь к домашнему каталогу польователю
#при помощи os.path.join объединяем пути к фаилу вместе

print('Save log in:', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)#специальная конфигурация чтобы записывал сообщения в опр.формате в указанный фаил
logging.debug('start program')
logging.info('Какие-то действия')
logging.warning('Program is dead')
#можем выводить специальные сообщения предназначенные для отладки, информирования, предупреждения и даже
#критические ошибки. После выполнения программы можно посмотреть в фаиле, что происходило с программой