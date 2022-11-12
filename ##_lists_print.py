# Printing Lists
   
# to print list using: 
# for loop
listFor = ['Python', 'with',1, 2, 3, 4, 5]
print("\nList Items in for: ")
for item in range(0, len(listFor)):
    print(listFor[item])

listFor2 = ['for', 'more', 'simple']
for item in listFor2:
    print(item)

#prints list on one line, use: '' to print with no spaces, commas, or anything (in between list, not at the end.) 
#output:join....print....simple
listjoin = ['join', 'print', 'simple']
print(' '.join(listjoin))

#print using *listname, sep=', '  
#output:printing, with, Symbol, 1, 2, 3
listsymbol = ['printing', 'with', 'Symbol', 1, 2, 3]
print(*listsymbol, sep=', ')

