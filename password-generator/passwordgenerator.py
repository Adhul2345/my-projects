import random
import string 

while True:
    print("Password Generator")
    print("1. Generate password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice not in [ "1", "2"]:
        print("Invalid choice. Please try again.")
        continue
    elif choice == "1":
        password_length = int(input("Enter the desired length of password: "))
        if password_length < 6:
            print("Password length should be at least 6 characters. please try again")
            continue
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(password_length))
            print("Generated password: ", password)
    elif choice == "2":
        print("Exiting program")
        break