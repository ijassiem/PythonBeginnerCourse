##from math import multiply
## 
##def test_numbers_3_4():
##    assert multiply(3,4) == 12 
## 
##def test_strings_a_3():
##    assert multiply('a',3) == 'aaa'

from math import pow
 
def test_numbers_2_3():
    assert pow(2, 3) == 8

def test_numbers_10_4():
    assert pow(10, 4) == 10000
 
def test_strings_a_5():
    assert pow('a',5) == 32

def my_sum(x,y,z):
    return x + y + z

def test_my_sum():
    assert my_sum(1,4,5) == 10
