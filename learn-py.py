s = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
s2 = {"k", "l", "m", "n", "o", "p", "q", "r", "s", "t"}

# s.add("k")
# s.remove("a")
# s.clear()
# s.update(s2)
s3 = s.union(s2)

# print(s)
print(s3)

print(s3.difference(s2))
print(s3.intersection(s2))