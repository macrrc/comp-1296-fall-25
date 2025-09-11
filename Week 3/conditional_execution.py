# making decisions - Conditional Execution
# run this code if a condition is true

# What is a condition?
# A condition is an Expression evaluated in a Boolean Context (True or False)

# Boolean values are either True or False
# Boolean is a type in Python
# True/False

temperature = 25

# indentation denotes a code block in Python
if temperature > 30: 
    print("it's hot outside!")
    print("another line")
else: # else is optional
    print("It's not too hot.")
    print("another line")
    
print("this is outside of the code block")

# Truthy and Falsy

# Falsy Values
# Boolean False
# Any 0 (0, 0.0, -0, -0.0, 0j, -0j)
# Any Empty Value
# str("")
# str('')
# list(), tuple(), dict{}, set()
print(bool(False)) # boolean False
print(bool(None)) # the special value None
print(bool("")) # any empty string
print(bool('')) # any empty string
print(bool(0)) # any zero
print(bool(0.0)) # any zero
print(bool([])) # empty list
print(bool(())) # empty tuple
print(bool({})) # empty dictionary

# truthy values
print(bool(True)) # boolean True
print(bool("any string")) # any non-empty string
print(bool(10)) # any non zero int
print(bool(-5)) # including negative numbers
print(bool(0.1)) # any non zero float
print(bool(["one"])) # any non empty list

# Comparison Operators
# == equality
# != not equal
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
## chaining operators - 10 < 20 > 5
# if (some condition, probably a comparison):
#   the code to run if the condition is true

if 10 == 10: # condition evaluates to True
    # this code block runs if the condition evaluates to True
    print("the condition/comparison evaluates to True")
else:
    # this code block runs if the condition evaluate to False
    print("the condition evaluates to False")
    
    
    
    
if True: # condition evaluates to True
    # this code block runs if the condition evaluates to True
    print("the condition/comparison evaluates to True")
else:
    # this code block runs if the condition evaluate to False
    print("the condition evaluates to False")
    
    
    
    
    
if False: # condition evaluates to True
    # this code block runs if the condition evaluates to True
    print("the condition/comparison evaluates to True")
else:
    # this code block runs if the condition evaluate to False
    print("the condition evaluates to False")