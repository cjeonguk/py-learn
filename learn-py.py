store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

# l = [i[0] for i in store if i[1] >= 20.00]
l = [i[0] if i[1] >= 20.00 else "--" for i in store]

print(l)