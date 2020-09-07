class Second:
    color = 'red'
    form = 'circle'
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform

obj1 = Second()
obj2 = Second()

print(obj1.color,obj1.form) #вывод на экран red circl
print(obj2.color,obj2.form) #вывод на экран red circle

obj1.changecolor('green') #изменение цвета первого объекта
obj2.changecolor('blue') #изменение цвета второго объекта
obj2.changeform('oval') #изменение формы второго объекта

print(obj1.color,obj1.form)  #вывод на экран green circl
print(obj2.color,obj2.form)  #вывод на экран blue oval