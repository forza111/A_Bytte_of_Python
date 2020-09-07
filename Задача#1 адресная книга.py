import pickle,json
class AdressBook():


    def __init__(self,name,info):
        '''Инициализация класса'''
        #print('Введите имя контакта, информацию о котором вам необходимо просмотреть')
        self.name = name
        self.info = info

        b = 'b.json'
        slovar = {}
        slovar[self.name] = self.info
        with open(b, 'a',) as f:
            json.dump(slovar, f,separators=' ', )


        with open(b,'r') as f1:
            store = json.load(f1)
            print(store)

AdressBook('forz212122',456465)

