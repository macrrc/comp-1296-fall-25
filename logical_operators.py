# logical operators
# and, or, not <-- in Python
# &, ||, ! <-- other languages

age = 15
has_id = True

if age > 18 and has_id == True:
    print("You may enter.")
else:
    print("Access denied.")
    
temperature = 5

if temperature < 0 or temperature > 100:
    print("Extreme temperature.")
else:
    print("Comfortable range.")
    
# Truth Tables and
print(True and True) # Evaluates to True
print(False and True) # Evaluates to False
print(True and False) # Evaluates to False
print(False and False) # Evaluates to False

# Truth Tables or
print(True or True) # Evaluates to True
print(False or True) # Evaluates to True
print(True or False) # Evaluates to True
print(False or False) # Evaluates to False

# Truth Tables with more than 2
print(True and True or False)
print(True and False and True and False or False)

