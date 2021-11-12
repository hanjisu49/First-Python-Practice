a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)

print(id(a))
print(id(b))
june21