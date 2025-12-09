#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# # или проще (/сложнее ?)
# lamp_code = goods['Лампа']
# lamps_item = store[lamp_code][0]
# lamps_quantity = lamps_item['quantity']
# lamps_price = lamps_item['price']
# lamps_cost = lamps_quantity * lamps_price
# print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']+\
#     store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
#
# sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']+\
#     store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
# chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']+\
#     store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']+\
#     store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
#
# print("Стол - ", store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity'],\
#       "шт, стоимость ",table_cost, "руб")
# print("Диван - ", store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity'],\
#       "шт, стоимость", sofa_cost, "руб")
# print("Стул - ", store[goods['Стул']][0]['quantity'] +store[goods['Стул']][1]['quantity']\
#       +store[goods['Стул']][2]['quantity'],\
#       "шт, стоимость", chair_cost, "руб")

def lampCost():
    lamp_code = goods['Лампа']
    lamps_item = store[lamp_code][0]
    lamps_quantity = lamps_item['quantity']
    lamps_price = lamps_item['price']
    lamps_cost = lamps_quantity * lamps_price
    print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
    return ""
def tableCost():
    table_code = goods['Стол']
    table_item = store[table_code]
    table_quantity1 = table_item[0]['quantity']
    table_quantity2 = table_item[1]['quantity']
    table_quantity = table_quantity1 + table_quantity2
    table_price1 = table_item[0]['price']
    table_price2 = table_item[1]['price']
    table_cost = table_quantity1 * table_price1 + table_quantity2 * table_price2
    print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')
    return ""
def sofaCost():
    sofa_code = goods['Диван']
    sofa_item = store[sofa_code]
    sofa_quantity1 = sofa_item[0]['quantity']
    sofa_quantity2 = sofa_item[1]['quantity']
    sofa_quantity = sofa_quantity1 + sofa_quantity2
    sofa_price1 = sofa_item[0]['price']
    sofa_price2 = sofa_item[1]['price']
    sofa_cost = sofa_quantity1 * sofa_price1 + sofa_quantity2 * sofa_price2
    print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')
    return ""
def chairCost():
    chair_code = goods['Стул']
    chair_item = store[chair_code]
    chair_quantity1 = chair_item[0]['quantity']
    chair_quantity2 = chair_item[1]['quantity']
    chair_quantity3 = chair_item[2]['quantity']
    chair_quantity = chair_quantity1 + chair_quantity2 + chair_quantity3
    chair_price1 = chair_item[0]['price']
    chair_price2 = chair_item[1]['price']
    chair_price3 = chair_item[2]['price']
    chair_cost = chair_quantity1 * chair_price1 + chair_quantity2 * chair_price2 + chair_quantity3 * chair_price3
    print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
    return ""
