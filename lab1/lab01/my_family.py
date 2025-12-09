#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Брат", "Мать", "Отец", "Бабушка", "Дедушка"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Брат', 160],
    ['Мать', 165],
    ['Отец', 181],
    ['Бабушка', 161],
    ['Дедушка', 170],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
# print("Рот отца - ", my_family_height[2][1],"см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
# totalHight = 0
# for person in my_family_height:
#     totalHight += person[1]
# print(totalHight)

def getHightFather():
    return my_family_height[2][1]

def totalHight():
    hight = 0
    for person in my_family_height:
        hight += person[1]
    return hight