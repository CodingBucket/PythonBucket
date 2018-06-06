# List data structure
li = [1, 2, 3]
print(li)
print(type(li))

# Tuple data structure
tpl = (1, 2, 3)
print(tpl)
print(type(tpl))

# Set data structure
# all unique value
set1 = {1, 2, 3, 4, 5, 6}
set2 = {6, 7, 8, 9}
print(type(set1))

# Dictionary example
dt = {'a': 10, 'b': 12}
print(dt)
for d in dt:
    print(d, dt[d])
print(dt.keys())

print("---")

print(set1 & set2)  # Union
print(set1 | set2)  # Intersect
print(set1 ^ set2)  # Not intersected
