import random

x = random.randint(1, 100)
print(x)

y = random.random()

print(y)

z = random.choice(["apple", "banana", "cherry"])

print(z)

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]

random.shuffle(cities)

print(cities)