import re

# ^ begin
# $ end
# . any character
# + one or more
# * one or zero


MY_STRING = 'hello2 hale3 hall1 hillclimb78 hull had'

a = re.findall("[a-g]", MY_STRING) # returns list of finds
print(a)

a = re.search("h.ll",MY_STRING) # returns object
print(a.string)

a = re.findall("h.ll",MY_STRING) # returns list of finds
print(a)

a = re.split("\s", MY_STRING) # returns list of finds
print(a)

a = re.findall("abc*","ab") # returns list of finds 
print('\n',a)

a = re.findall("abc{2}","abccccdef") # returns list of finds 
print('\n',a)


##
##a = re.findall(SEARCH,MY_STRING)
##print(a)
##
##a = re.findall(SEARCH,MY_STRING)
##print(a)

