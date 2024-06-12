var = 20
def func(name = "default"):
    var = 10
    print(f"Hello from a {name}")
    print(var)
    return f"Hi {name}"


print(func("function"))
print(func())

print(var)