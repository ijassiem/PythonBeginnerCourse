f = open('scope.py')
print(f.read()) # read complete file
print("-----------------------")
f.seek(0) # move cursor to start of file
print(f.read(20)) # read 20 bytes of file
print("-----------------------")
f.seek(0) # move cursor to start of file
print(f.readline(20)) # read one line not exceeding 20 bytes
f.seek(0) # move cursor to start of file
print(f.readlines(10)) # read 3 lines
f.close() # close file

with open('scope.py') as g:
    for line in g:
        print(line, ends='')
