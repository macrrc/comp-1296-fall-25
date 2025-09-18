# for loops - iterate over something??
# range() - a built in function for creating ranges of numbers
# gives us a simple way to count
# range(10) - the first argument is the stop number
# inclusive of the start
# exclusive of the end
# range(2, 20) start, stop
# range(2, 100, 5) start, stop, step

# iterable  - something you can iterate over

# NOTE: this is where a single letter variable is OK
for i in range(5): # 0 1 2 3 4
    x = 'some variable'
    print(i)
    print("the loop ran")

for i in range(4):
    print("second for loop")
    print(i)
    
print(i, "outside the loop") 
print(x) 
# We need a sequence in order to use a for loop
# a string is a sequence (collection) of characters

message = "Hello"

for char in message:
    print(char)

# write a for loop that counts the number of vowels in the text 
text = "programming"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
        
print("Vowel count:", count)


# Lists (mutable collection)

colours = ["red", "green", "blue"] # this list a sequence (collection) of strings
numbers = [10, 14, 5, 3, 7, 111] # this list is a sequence (collection) of ints
lists = [["one", "two"], [1, 2]] # this list is a squence (collection of lists)
mixed_list = [1, 'two', [3, 'four']]

# List Qualities
# Ordered - order is guaranteed to be the order of insertion
# mutable - changeable
for colour in colours:
    print(colour)
    
for number in numbers:
    print(number)
    



colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)
    
# print(colours[0]) # index notation
print(colours[1])
print(colours[2])

colours[1] = "purple"

# print(colours[1])

colours[0] = 100
# print(colours[0])
colours.append("purple")
colours.

for colour in colours:
    print(colour)
    
    
# strings are sequences of chars
# strings are immutable

some_string = "Hello"

print(some_string[0])
print(some_string[1])
print(some_string[-1])

# some_string[0] = "T"

# some_string = "Bob"
# print(some_string)

# slicing strings using indexes
# inclusive of the start
# exclusive of the end
print(some_string[0:2])

print(some_string[2:5])

longer_string = "some longer string value"

print(longer_string[4:10])

some_list = [5, 5, 8, 91, 12, 2]

print(some_list[2:-1])
print(some_list[2:])