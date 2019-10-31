with open ('config.txt') as f:
    line = None
    while line!='':
        line = f.read(5)
        print(line)
