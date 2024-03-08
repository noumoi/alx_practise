letters = ['q', 'w', 'e', 'r', 't', 'y']
# to replace from 1 to 3 and display it
letters[0:2] = ['b', 'k', 'h']
print(f"the answer is given as {letters}")
new_letter = letters
new_letter[:] = []
print(f"print a null output {new_letter}") # print an empty index
len(letters)

letter_count = ['q', 'w', 'e', 'r', 't', 'y']
print(f"write the nos of letter {len(letter_count)}")

#fibonacci series
'''
a, b = 0, 1
while a<10:
    print(a)
    a, b = b, a + b
'''
a, b = 0, 1
while a<10:
    print(a, end='')
    a, b = b, a + b

    '''DATA STRUCTURES IN BRIEF'''
#object appending
family = ['father', 'mother', 'son', 'daughter', 'siblings']
family.append ('cousin')
print(f"a family member tagged has been added {family}")
#family.iterable('uncle') #error: no built-in iterable() function in Python for adding elements to a list
#print(f"a family member tagged has been added {family}")

#object Inserting
family.insert(2, 'nephew')
print(f"a family member inserted is  {family}") #siblings

#0bject remove
family.remove('cousin')
print(f"a family member  has been removed {family}")

#object pop
family_remove = family.pop()
family.remove('siblings')

print(f"the    rest of the family {family}")
print(f"the selected member of the family {family_remove}")
