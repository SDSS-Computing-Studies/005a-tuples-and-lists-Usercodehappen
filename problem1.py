#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ['Alain', 'Brian','Chris','Justin','Angela']
a = input(" please choose a person from the list to replace: ").strip()
b = input("Enter the replacement: ").strip()

pos = (people.index(a))
num = people[pos]
people = [a.replace(num,b)] for a in people]
print(people)