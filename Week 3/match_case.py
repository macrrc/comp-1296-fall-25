# match/case
command = input("Enter a command: ")

match command:
    case "start":
        print("The system is starting...")
    case "stop":
        print("The system is stopping...")
    case "restart":
        print("System restarting...")
    case _:
        print("Unknown command")
        
number = 10

match number:
    case number if number < 10 and number < 0:
        print("number is less than 10")
    case number if number > 10:
        print("number is greater than 10")