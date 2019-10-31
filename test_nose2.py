##from math import multiply
## 
##def test_numbers_3_4():
##    assert multiply(3,4) == 12 
## 
##def test_strings_a_3():
##    assert multiply('a',3) == 'aaa'

from math import pow

def setup_module(module):
    print("")
    print("setup_module before anything in this file")

def teardown_module(module):
    print("teardown_module after evrything in this file")

def my_setup_function():
    print ("my_setup_function")
 
def my_teardown_function():
    print ("my_teardown_function")

@with_setup(my_setup_function, my_teardown_function)
def test_numbers_2_3():
    print 'test_numbers_2_3  <============================ actual test code'
    assert pow(2, 3) == 8

##def test_numbers_10_4():
##    assert pow(10, 4) == 10000
## 
##def test_strings_a_5():
##    assert pow('a',5) == 32 
