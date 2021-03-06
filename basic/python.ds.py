# List:
# A list is a collection which is ordered and changeable.
li = [1, 2, 3, 4]
li2 = list(range(5))  # out: [0, 1, 2, 3, 4]
li.reverse()          # Reverse the actual list
li.sort()             # Sort the actual list
li.insert(0, 0)       # Insert item in specific index, insert(index, item)
li.append(4)          # Append item in the list
li.pop(0)             # Delete & returns the deleted list item, 0 is li index.
li.remove(1)          # Removes the element
li.clear()            # emties the list out: []
li.extend(li2)        # li2 added in li
li.count(2)           # Count specific element
li.copy()             # shallow copy
len(li)
type(li)
li2 = [*range(5)]     # out: [0, 1, 2, 3, 4]
li[::-1]              # Returns a reversed list without modifiing the actual list
del li[0]             # Delete the list item
li = li + [4]         # List concate, out: [1, 2, 3, 4]
li = [1] * 3          # out: [1, 1, 1]
li = ['a', 'b', 'c']
''.join(li)           # out: 'abc'
list('abc')           # out: ['a', 'b', 'c']

# List Comprehension
# Normal way
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for item in li:
    if item % 2:
        even.append(item)
print(even)              # out: [2, 4, 6, 8, 10]

# List comprehension way
even = [item for item in li if item % 2 == 0]
print(even)              # out: [2, 4, 6, 8, 10]

# Stack - LIFO - Last in first out
li = [1, 2, 3]
li.append(4)    # out: [1, 2, 3, 4]
li.pop()        # out: 4, Removes the last element

# Queue - FIFO - First in first out
li.pop(0)       # out: 1, Removes the first element


# Set:
# A set is a collection which is unordered and unindexed.
# set object does not support indexing
s = {"a", "b", "c"}
s1 = {'c', 'd', 'e'}
s.add("d")                  # add single item in set
s.update(['m', 'g'])        # add multiple item in set
s.remove('m')               # If the item does not exist, raise an error.
s.discard('m')
s.pop()                     # remove the last item
s.clear()                   # empties the set
s.copy()                    # Returns a copy of the set
s.difference(s1)            # return items that only exist in set s
s.difference_update(s1)     # update s with items that only exist in set s
s.intersection(s1)          # return common items
s.intersection_update(s1)   # update s with common items
s.isdisjoint(s1)            # return true if two sets have a null intersection
s.issubset(s1)              # report whether another set contains this set
s.issuperset(s1)            # report whether this contains another set
s.union(s1)                 # combine all items of two set
s.symmetric_difference(s1)  # return all item of 2 set except common items
s.symmetric_difference_update(s1)  # update s with symmetric difference
del s                       # delete the set complely


# Tuple:
# A tuple is a collection which is ordered and unchangeable.
# tuple items can be accessed by index number
t = (1, 2, 3, 4)
t.count(3)
t.index(2)
del t


# Dictionary:
# A dictionary is a collection which is unordered, changeable and indexed.
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d['k1']      # out: 'v1'
d.get('k1')  # out: 'v1'
d.pop('k1')

# Print all key names in the dictionary, one by one:
for x in d.keys():
    print(x)

# You can also use the values() function to return values of a dictionary:
for x in d.values():
    print(x)

# Loop through both keys and values, by using the items() function:
for x, y in d.items():
    print(x, y)

d1 = d.copy()      # shallow copy
d.clear()          # removes all items from the dictionary
d.keys()           # Returns a list contianing the dictionary's keys
d.pop('k1')        # Removes the element with the specified key
d.popitem()        # Removes the last inserted key-value pair

# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value
d.setdefault("key", "value")

# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object.
d.update({'k4': 'v4', 'k5': 'v5'})

# - returns a dictionary with the specified keys and values.
d.fromkeys('k', 'v')
del d['k1']
del d
