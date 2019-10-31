import logging as log

FORMAT = '%(asctime)s:' + log.BASIC_FORMAT
log.basicConfig(format=FORMAT, level=log.DEBUG, filename='test.log')

log.debug('startup')

test = [1,2,3]

log.debug('test {}'.format(test))

try:
    var
    test[3]
    1/0

else:
    print('No exceptions occurred')
    
except IndexError as e:
    test.append('a')
    print(e)
    
except ZeroDivisionError as e:
    print('cannot divide by zero')
    print(e)

except Exception as e:
    print(e)
    log.exception('unknown exc {}'.format(e))

# must execute regardless of exception
finally
    print("Must do this')

