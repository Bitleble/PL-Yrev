import math


def Rast(y1, x1, y2, x2,):
    k = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return k


a = []
x1 = int(input('X1:'))
x2 = int(input('X2:'))
x = [x1, x2]
y1 = int(input('Y1:'))
y2 = int(input('Y2:'))
y = [y1, y2]
z1 = int(input('Z1:'))
z2 = int(input('Z2:'))
z = [z1, z2]
p1 = int(input('P1:'))
p2 = int(input('P2:'))
p = [p1, p2]
print('Координаты точек -- x:', x, 'y:', y, 'z:', z, 'p:', p)
a.append(round((Rast(y1, x1, y2, x2)), 4))
a.append(round((Rast(z1, x1, z2, x2)), 4))
a.append(round((Rast(p1, x1, p2, x2)), 4))
a.append(round((Rast(z1, y1, z2, y2)), 4))
a.append(round((Rast(p1, y1, p2, y2)), 4))
a.append(round((Rast(p1, z1, p2, z2)), 4))
print('Расстояния: ', a)
print('Максимальное рассотояние: ', max(a))