#! python3
"""
Ask the user to enter positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
numlist = []

while True:
    a = input("Enter an integer: ")
    a = int(a)
    if a == -1:
        numlist.sort()
        b = str(numlist[-1])
        print("The largest number you entered is " + b)
        break
    else:
        numlist.append(a)


