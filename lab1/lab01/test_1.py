import pytest
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

def test_calculateArea():
    assert calculateArea(10) == 314.1593
    assert calculateArea(1) == 3.1416
    assert calculateArea(3) == 28.2743

def test_pointInCircle():
    assert poinInCiecle((0, 0), 2, (0, 0)) == True
    assert poinInCiecle((5, 5), 5, (0, 5)) == True
    assert poinInCiecle((100, 5), 5, (0, 5)) == False

def test_father_hight():
    assert getHightFather() == 181
def test_hight():
    total = 160 + 165 + 181 + 161 + 170
    assert totalHight() == total