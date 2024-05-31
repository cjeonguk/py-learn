name = "John Doe"
first_name = name[:4]
last_name = name[5:]
funky_name = name[::2]
reverse_name = name[::-1]
slice_var = slice(4)
slice_var2 = slice(0, -4)

print(name, first_name, last_name, funky_name, reverse_name, name[slice_var], name[slice_var2])