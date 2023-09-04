#!/bin/python3


"""
ЗАДАЧА:
Написать программуЮ в которой на основе текста, введенного пользователем, 
создается кортеж. Затем на основе этого кортежа создаётся новый кортеж. 
В новый кортеж включаются равноотстоящие элементы, 
начиная с первого (с нулевым индексом). 
Растояние между эллементами вводится пользователем

"""

def send_text():
    old_tuple = tuple(i for i in input("введите текст  >>> "))
    try:
        number = int(input("введите число  >>> "))
        range_index_old = tuple(i for i in range(0, len(old_tuple)))
        new_index = tuple(i for i in range_index_old if i % number == 0)
        new_dict = tuple(old_tuple[i] for i in new_index)
        return new_dict
    except ValueError:
        return "ValueError"

print(send_text())