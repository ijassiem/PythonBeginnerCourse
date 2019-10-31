import logging as log

test = [1,2,3]

try:
    test[3]
    1/0
    
except IndexError as e:
    test.append('a')
    print(e)
    
except ZeroDivisionError as e:
    print('cannot divide by zero')
    print(e)
    log.exception()
