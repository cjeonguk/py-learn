import mod

mod.Human('Alice').say_hello()

print(mod.Human('Bob').is_alive)

mod.Human.is_alive = False

print(mod.Human('Charlie').is_alive)