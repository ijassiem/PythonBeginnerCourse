import re 

def find_num(filename, word):
    f = open(filename)
    my_file = f.read()
    print(my_file) # read complete file
    a = re.findall(word, my_file)
    print(a)
    f.seek(0) # move cursor to start of file
    f.close() # close file
    return len(a)

try:
    num = find_num("text.txt", "Town")
    print("Matches found: ", num)
except:
    print("Error has occurred")





