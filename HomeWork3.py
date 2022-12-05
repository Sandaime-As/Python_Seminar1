# 1. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# num = int(input('Enter quarter number:  '))
# if num == 1:
#     print('Сoordinates are in the range from 0 to +∞ and from 0 to +∞')
# elif num == 2:
#     print('Сoordinates are in the range from -∞ to 0 and from 0 to +∞')
# elif num == 3:
#     print('Сoordinates are in the range from -∞ to 0 and from -∞ to 0')
# elif num == 4:
#     print('Сoordinates are in the range from 0 to +∞ and from -∞ to 0')
# else:
#     print('We have only 4 system of coordinate')


# 2. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Enter the coordinate first Х: '))
y1 = int(input('Enter the coordinate first Y: '))
x2 = int(input('Enter the coordinate second Х: '))
y2 = int(input('Enter the coordinate second Y: '))
distance = round(((x1-x2)**2+(y1-y2)**2)**0.5, 2)
print(f'Distance between points: {distance}')
