points = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Нахождение самой левой точки
def left_point(points):
    min = 0

    for i in range(1, len(points)):
        if points[i].x < points[min].x:
            min = i
        elif points[i].x == points[min].x:
            if points[i].y < points[min].y:
                min = i
    return min

# Нахождение направления движения
def orientation(A, B, C):
    val = (B.y - A.y) * (C.x - B.x) - (B.x - A.x) * (C.y - B.y)
    if val == 0:
#        print('collinear_vectors/коллинеарные вектора')
        return 0
    elif val > 0:
#        print('clockwise/по часовой стрелке')
        return 1
    else:
#        print('counterclockwise/против часовой стрелки')
        return 2

# Выпуклая оболочка
def convex_hull_graham(points):
    n = len(points)            # число точек
    num = list(range(n))       # список номеров точек
    print('-----------')
    print('BEFOR: ', num)
    for j in range(0, n-1):
        for i in range(j, n):
            if points[num[i]].x < points[num[j]].x: # если points[i]-ая точка лежит левее points[0]-ой точки по Х
                num[i], num[j] = num[j], num[i] # меняем местами номера этих точек
                print('AFTER: ', num) # номера элементов упорядоченного массива после перебора
            else:
                print('False')
    print('Массив нумерации элементов: ')
    print('[array_ord_elem] =', num)

    for i in range(2, n):  # сортировка
       j = i
       while j > 1 and (orientation(points[num[0]], points[num[j - 1]], points[num[j]]) < 0):
            num[j], num[j - 1] = num[j - 1], num[j]
            j -= 1
       print('j =', j, 'num[j] =', num[j])

    convex_hull = [num[0], num[1]]  # создаем стек
    convex_hull = []
    print(convex_hull)

    for i in range(2, n):
        while orientation(points[num[i-2]], points[num[i-1]], points[num[i]]) == 1:
            print('orientation: ', orientation(points[num[i-2]], points[num[i-1]], points[num[i]]))
            del convex_hull[i-1]
        convex_hull.append(num[i])

# Ввод точек
points.append(Point(1, 1))
points.append(Point(5, 5))
points.append(Point(3, 1))
points.append(Point(3, 3))
points.append(Point(1, 3))
points.append(Point(2, 2))
points.append(Point(0, 0))
points.append(Point(4, 4))


# Вывод точек
print('point:| x |', '| y |')
print('=================')
for i in range(len(points)):
    print(i, '-->', '|', points[i].x, '| |', points[i].y, '|')

num_min = left_point(points)
print('number_min_elementa =', num_min)
print('coordination', '[', points[num_min].x, ':', points[num_min].y, ']')
P = []
P.append(left_point(points))
print('num_left_point', P)

orientation(points[1], points[4], points[2])
print(convex_hull_graham(points))