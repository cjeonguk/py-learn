import mod

mod.Human('Alice').say_hello()

print(mod.Human('Bob').is_alive)

mod.Human.is_alive = False

print(mod.Student('Charlie').is_alive)