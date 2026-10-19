# list:
# Definition: A list is an ordered and 
# changeable collection of elements enclosed in square brackets []. 
# It allows duplicate values.

# 1)create and display
# a = [10, 20, 30, 40]
# print("List:", a)

# 2)add a elememt in list
# Definition: append() adds an element at the end of a list.
a = [10, 20, 30]
a.append(40)
print("Updated list:", a)

# 3)remove element
# Definition: remove() removes the first matching element.

a = [10, 20, 30, 40]
a.remove(30)
print("Updated list:", a)

# 4)sort a list
# Definition: sort() arranges list elements in ascending order by default.

a = [40, 10, 30, 20]
a.sort()
print("Sorted list:", a)

# 5)sum of elements in a list
# Definition: sum() calculates the total of numeric elements.

a = [10, 20, 30, 40]
print("Sum:", sum(a))



# tuple:
# Definition: A tuple is an ordered collection of elements enclosed in parentheses (). 
# It is immutable, meaning its elements cannot be changed after creation.

# 1)create and display a tuple
# Definition: A tuple stores multiple elements in one variable.

t = (10, 20, 30, 40)
print("Tuple:", t)

# 2)access a element
# Definition: Indexing accesses an element using its position.

t = (10, 20, 30, 40)
print("First element:", t[0])

# 3)length of tuple
# Definition: len() returns the number of elements in a tuple.

t = (10, 20, 30, 40)
print("Length:", len(t))

# 4)count the occurence of element
# Definition: count() returns how many times an element occurs.

t = (10, 20, 10, 30, 10)
print("Count of 10:", t.count(10))

# 5)find max and min
# Definition: max() finds the largest value and min() finds the smallest.

t = (40, 10, 30, 20)
print("Maximum:", max(t))
print("Minimum:", min(t))


# dictionary:
# Definition: A dictionary is a collection of key-value pairs enclosed in curly brackets {}.
#  Each key is unique and is used to access its value

# 1)create and display
# Definition: A dictionary stores data as key-value pairs.

student = {"name": "Amit", "marks": 85}
print("Dictionary:", student)

# 2)access element
# Definition: A key is used to retrieve its corresponding value.

student = {"name": "Amit", "marks": 85}
print("Name:", student["name"])

# 3)add anew key value
# Definition: Assigning a value to a new key adds an entry.

student = {"name": "Amit", "marks": 85}
student["city"] = "Kolhapur"
print(student)

# 4)update a value 
# Definition: Assigning a new value to an existing key updates it.

student = {"name": "Amit", "marks": 85}
student["marks"] = 95
print(student)

# 5)display all the keys and values 
# Definition: keys() returns the keys and values() returns the values.

student = {"name": "Amit", "marks": 85, "city": "Kolhapur"}

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))



# set
# Definition: A set is a collection of unique elements.
# It does not allow duplicate values, and its elements are written inside curly braces {}. 
# Sets are mutable, 
# meaning we can add or remove elements.

# 1)create and display
s = {10, 20, 30, 40}
print("Set:", s)

# 2)add a elemnt 
s = {10, 20, 30}
s.add(40)
print(s)

# 3)remove the element
s = {10, 20, 30, 40}
s.remove(30)
print(s)

# 4)union of 2 set
a = {10, 20, 30}
b = {30, 40, 50}
print(a.union(b))

# 5)intersection of 2 sets
a = {10, 20, 30}
b = {20, 30, 40}
print(a.intersection(b))