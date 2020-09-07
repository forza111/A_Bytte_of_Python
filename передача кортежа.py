def get_error_details():
    return (2,'Описание ошибки')
errnum,errstr = get_error_details()

print(errnum)
print(errstr)

a,b, *c = [1,2,3,4,5] # присваиваем значения кортежа переменным, * означает a,b, <все остальное>
print(a)
print(b)
print(c)

a,b,c = c,b,a #как поменять местами три значения
print(a)