import mod

# mod.Human('Alice').say_hello()

# print(mod.Human('Bob').is_alive)

mod.Human.is_alive = False

print(mod.Student('Charlie', 3).is_alive)

s = mod.Student('David', 1)

s.say_hello()\
    .study()

mod.rename(s, 'Eve')

print(s.name)