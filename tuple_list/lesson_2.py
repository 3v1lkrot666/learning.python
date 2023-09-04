#!/bin/python3

"""
ЗАДАЧА:
Написать программу, в которой пользователь вводит целое число, а программа
формирует кортеж, который состоит из цифр, входящих в это число
Создать 2 кортежа, в которых число включается в кортеж в прямом и обратном порядке
"""

def main():
    try:
        number = tuple(i for i in str(int(input("Введите целое число>>> "))))
    except ValueError:
        number = "Указанное значение не является числом"
    return number[-1::]

print(main())