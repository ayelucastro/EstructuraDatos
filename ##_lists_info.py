# Lists
   
# Creating an empty List
List1 = []
print("Blank List: ")
print(List1)
   
# Creating a List of numbers
List2 = [10, 20, 14]
print("\nList of numbers: ")
print(List2)
   
# Creating a List of strings amd numbers and accessing them
# using index
List3 = ["Geeks",5, "rule"]
print("\nList Items: ", List3)
print(List3[0]) 
print(List3[2])

# to print list using: 
# for loop
listFor = ['Python', 'with',1, 2, 3, 4, 5]
print("\nList Items in for: ")
for item in range(0, len(listFor)):
    print(listFor[item])

listFor2 = ['for', 'more', 'simple']
for item in listFor2:
    print(item)

#prints list on one line, use: '' to print with no spaces, commas, or anything (in between list, not at the end. Ex:join....print....simple)
listjoin = ['join', 'print', 'simple']
print(' '.join(listjoin))


listsymbol = ['printing', 'with', 'Symbol', 1, 2, 3]
print(*listsymbol, sep=', ')