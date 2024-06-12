def func(name = "default"):
    print(f"Hello from a {name}")
    return f"Hi {name}"


print(func("function"))
print(func())