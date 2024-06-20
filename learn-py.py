store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

to_wons = lambda data: (data[0], data[1] * 1000)
store_wons = list(map(to_wons, store))

print(store_wons)