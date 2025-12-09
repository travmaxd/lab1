from distance import *
from circle import *
from favorite_movies import movies
from my_family import *
from operations import res
from zoo import  result
from songs_list import (totalTimeList, totalTimeDict)
from secret import secretMessage
from garden import flowersSet
from shopping import printShops
from store import *
print("Задание 0")
print(distances)

print("\nЗадание 1")
print("Площадь круга: ", calculateArea(radius))
print("Точка№1: ", poinInCiecle(point_1, radius, center))
print("Точка№2: ", poinInCiecle(point_2, radius, center))

print("\nЗадание 2")
res()

print("\nЗадание 3")
movies()

print("\nЗадание 4")
print("Рост отца - ", getHightFather(), "см")
print("общий рост семьи - ", totalHight(), "см")

print("\nЗадание 5")
result()

print("\nЗадание 6")
print("Три песни звучат ", totalTimeList(), "минут")
print("А другие три песни", totalTimeDict(), "минут")

print("\nЗадание 7")
print(secretMessage())

print("\nЗадание 8")
flowersSet()

print("\nЗадание 9")
printShops()

print("\nЗадание 10")
lampCost()
tableCost()
sofaCost()
chairCost()
