points = [{'x':2,'y':3},{'x': 4, 'y':1},{'x':1000 , 'y':0.1}]
print(points)
points.sort(key=lambda i : i ['x'])
#производим сортировку при помощи лямды
print(points)