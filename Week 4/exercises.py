# Part A: Loops
# Exercise 1 – While loop basics
# Write a program that uses a while loop to count down from 10 to 1 and then prints "Blastoff!".

# declare a value outside
counter = 10

while counter > 0:
    print(counter)
    counter -= 1
    
print("Blastoff!")

# Exercise 2 – User input with while
# Keep asking the user to enter a number until they type 0. When they do, print "Done!".
while True:
    user_input = int(input("Type a number: "))
    if user_input == 0:
        print("Done!")
        break # loop control statement
    

# Exercise 3 – For loop with range
# Use a for loop and range() to print all even numbers from 2 to 20.
for number in range(2, 21, 2):
    print(number)
    

# Exercise 4 – Looping through a list
# Given the list colors = ["red", "green", "blue", "yellow"], write a for loop that prints each color on a separate line.
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

# Exercise 5 – Loop control statements
# Write a loop that goes through the numbers 1 to 10:
# Skip printing the number 5 using continue.
# Stop the loop completely if the number is 8 using break.

for number in range(1, 11):
    if number == 5:
        continue
    elif number == 8:
        break
    else:
        print(number)

# Part B: Sequences
# Exercise 6 – String indexing
# Given word = "Python", print:
# The first letter
# The last letter
# The substring "yth"
word = "Python"
print(word[0])
print(word[-1])
print(word[1:4])

# Exercise 7 – String iteration
# Write a for loop that prints each character of "banana" on its own line.
word = "banana"
for char in word:
    print(char)

for char in "banana":
    print(char)
    
# Exercise 8 – List modification
# Start with numbers = [5, 10, 15].
# Add 20 to the end of the list.
# Change the second item to 12.
# Remove the first item.
numbers = [5, 10, 15]
print(numbers)

numbers.append(20)
print(numbers)

numbers[1] = 12
print(numbers)

# del numbers[0] # if we know the location but not the value
# numbers.remove(5) # if we know the value but not the location
# numbers.pop(0) # defaults to -1 (the last item)
numbers = numbers[1:]
print(numbers)

## EXTRA STUFF!!!
new_list = [["one", "two"], "one", "two"]
print(new_list[0][1][2])

# Exercise 9 – Tuple access
# Create a tuple called point with the values (4, 7). Print the x-coordinate (first value) and y-coordinate (second value).
point = (4, 7)
print(f"First value: {point[0]}")
print(f"Second value: {point[1]}")

# Exercise 10 – Iterating over sequences
# Write one program that:

# Prints each fruit in the list ["apple", "pear", "peach"].
# Prints each letter in the string "cat".
# Prints each number in the tuple (1, 2, 3, 4).

# Part C: Mixed Practice
# Exercise 11 – Counting characters
# Ask the user to type a word. Use a loop to count how many times the letter "a" appears.

# Exercise 12 – Sequence summary
# Given the list scores = [88, 92, 79, 93, 85]:

# Use a loop to print each score.
# Use indexing to print the first and last score.
# Append 90 to the list and print the updated list.
# Explain why a list works here instead of a tuple.

## pass allows you to create "placeholder" code in a block
if 10 == 100:
    pass