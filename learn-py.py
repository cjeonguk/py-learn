store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

import functools

reduced = functools.reduce(lambda acc, item: acc + (item[1] if item[1] > 20 else 0), store, 0)

print(reduced)