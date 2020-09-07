i = []
i.append('item')
print(repr(i)) # выведет ['item']

eval(repr(i))
eval(repr(i)) == i