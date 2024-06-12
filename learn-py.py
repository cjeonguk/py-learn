d = {"a": 1, "b": 2, "c": 3}

print(d.get("a"))

print(d.keys())

print(d.values())

print(d.items())

d.update({"d": 4})
d.update({"a": 5})

for key, value in d.items():
    print(key, value)