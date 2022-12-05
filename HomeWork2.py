# 1. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

# X = int(input('Enter the boolean Х: '))
# Y = int(input('Enter the boolean Y: '))
# Z = int(input('Enter the boolean Z: '))

# if 0 <= X <= 1 and 0 <= Y <= 1 and 0 <= Z <= 1:
#     if (not (X or Y or Z)) == (not X and not Y and not Z):
#         print('Is work!')
# else:
#     print('Try again')


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Enter the coordinate Х: '))
# y = int(input('Enter the coordinate Y: '))
# if x == 0:
#     print('Point on axis Y')
# elif y == 0:
#     print('Point on axis X')
# elif x > 0:
#     if y > 0:
#         print('Point in 1st quarter')
#     else:
#         print('Point in 4th quarter')
# else:
#     if y > 0:
#         print('Point in 2nd quarter')
#     else:
#         print('Point in 3rd quarter')
