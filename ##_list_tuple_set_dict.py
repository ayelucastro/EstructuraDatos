# use of list, tuple, set and
# dictionary
 
# Lists
l = []
 
# Adding Element into list
#using append adds in last position
l.append(5)
l.append(7)
l.append(33)
l.append(37)
l.append(15)
l.append(25)
print("Adding odd numbers in list", l)
 
# Popping Elements from list
# removes only the last element
l.pop()
print("Popped one element from list", l)
print()
 
# Set
s = set()
 
# Adding element into set. Add only for sets
s.add(2)
s.add(14)
s.add(26)
s.add(18)
s.add(22)
print("Adding even numbers in set", s)
 
# Removing element from set, mention the element not the place
s.remove(22)
print("Removing 22 from set", s)
print()
 
# Tuple
tl = tuple(l)
ts = tuple(s)
 
# Tuples are immutable
print("Tuple list", tl)
print("Tuple set", ts)
print()
 
# Dictionary, created empty
d = {}
print(d)
 
# Adding the key value pair
d[5] = "Five"
d[6] = "six"
d[10] = "Ten"
d[1] = "one"
print("Dictionary", d) #prints the whole dictionary
 
# Removing key-value pair
del d[10]
print("Dictionary", d)