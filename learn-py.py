store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

filtered = list(filter(lambda data: data[1] >= 20, store))

print(filtered)