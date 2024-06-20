def a(a, b):
    a(b)

a(print, "c")

d = print

d("e")

def devisor(x):
    def inner(y):
        return x / y
    return inner

devide = devisor(10)(5)

devide2 = devisor(10)

print(devide, devide2(5))