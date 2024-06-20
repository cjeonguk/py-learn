names = ['Alice', 'Bob', 'Charlie']

ages = [24, 50, 18]

is_adult = [True, True, False]


# profiles = zip(names, ages, is_adult)
profiles = dict(zip(names, zip(ages, is_adult)))

print(profiles)
