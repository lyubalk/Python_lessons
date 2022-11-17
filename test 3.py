"""Реализовать функцию my_func(), которая принимает
 три позиционных аргумента и возвращает сумму наибольших
 двух аргументов."""


def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif x > y and y < z:
        return x + z
    else:
        return y + z


print(f'Результат {my_func(int(input("Введите х - ")), int(input("Введите y - ")), int(input("Введите z - ")))}')
