VER = 2.0

def my_scope():
    global VER
    VER +=1
    print(VER)

my_scope()
