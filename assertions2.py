##x = 57.9
##assert x > 10, 'x out of range'
##assert type(x) == int, 'x must be an int'

############################################################3

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "Should be 'hello'"

assert sum([1, 2, 3]) == 7, "Should be '6'"
