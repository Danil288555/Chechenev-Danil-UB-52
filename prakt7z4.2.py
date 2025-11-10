import math

a, b, R = 2, 3, 5

points = [(1, 2), (4, 5), (-1, -2)]

count = 0
for x, y in points:
    if (x - a)**2 + (y - b)**2 < R**2:
        count += 1

print("Точек внутри окружности:", count)

# Проверка для первой точки
x, y = points[0]
rad_squar = (x - a)**2 + (y - b)**2
inside = rad_squar < R**2

print(f"Точка P({x}, {y}):")
print(f"Расстояние^2 = {rad_squar}")
print(f"Внутри окружности: {'да' if inside else 'нет'}")