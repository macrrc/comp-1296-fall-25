# two kinds of loops in Python
# while loops - repeat while a condition remains true
# for loops - repeat of items in a sequence (iterate over)

count = 0 # 1) initialize the loop variable
other_count = 0
while count < 5: # 2) condition (that will eventually be false)
    print("Count is ", count)
    other_count += 1
    count += 1 # 3) progress (prevents an infinite loop)
    
print("stuff that comes after the loop runs when it's done.")

# a while loop using a sentinal value

while True:
    text = input("Enter something ( or \"done\" to stop):")
    if text.lower() == "done":
        print("Thanks for stopping.")
        break

    print("You entered: ", text)
    
    
while True:
    text = input("Enter something ( or \"done\" to stop):")
    if text.lower() == "done":
        print("Thanks for stopping.")
        break # loop control
    print("You entered: ", text)
    
# when to use a while loop?
# when you don't know how many times something needs to loop