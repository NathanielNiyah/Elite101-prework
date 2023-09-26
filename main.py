print("Welcome to the elite 101 Chatbot!")
name = input("Please enter your name: ")
age = input("Nice to meet you, " + name + "! How old are you?")
print("How may I help you " + name + "?")
choice = int(input("option 1 - placeholder\noption 2 - placeholder\noption 3 - placeholder\noption 4 - placeholder\noption 5 - exit the conversation\nPlease choose a number from an option listed."))
if choice == 1:
    print('Hello')
elif choice == 2:
    print('Okay')
elif choice == 3:
    print('Maybe')
elif choice == 4:
    print('No')
else:
    print('Thank you for working with us.')