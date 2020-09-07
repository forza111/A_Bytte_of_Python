'''Умноижить каждое чиисло из списка на  2 при определенном условии'''

listone = [2,3,4,5,6]
listtwo = [2*i for i in listone if i >2]

print(listtwo)