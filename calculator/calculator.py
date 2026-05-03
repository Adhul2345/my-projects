print("calculator")

while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    choice = input("Enter your choice: ")
    if choice not in ["1", "2", "3", "4"]:
        print("invalid choice. Enter a valid number 1, 2, 3 or 4")
        continue

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == "1":
        result = num1 + num2
        print(f"the result is: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"the result is: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"the result is: {result}")
    elif choice == "4":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1/num2
            print(f"the result is: {result}")
    while True:

        use_again = input("do you want to use calculator again?: (yes/no): ").lower()

        if use_again == "yes":
            break
        elif use_again == "no":
            print("thans for using calculator see yaa")
            exit()
        else:
            print("invalid input!!")    