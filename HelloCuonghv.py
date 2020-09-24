print("Happy Birthday!!!")
while True:
    name = input("Please enter your name:")
    if name == "Cuong":
        print("Hello " + name + ", how are you today?")
    elif name == "Brian":
        print("Hello teacher, how are you today?")
    elif name == "bye" or name == "quit" or name == "exit":
        print("Quitting...")
        break
    else:
        print("Sorry " + name + ", you should not be here'")



