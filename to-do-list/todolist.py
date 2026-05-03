print("To Do List")

task = []

while True:
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. please try again")
        continue
    
    elif choice == "1":
        new_task = input("Enter new task:")
        task.append(new_task)
        print("Task added successfully!!")
    
    elif choice == "2":
        if len(task) == 0:
            print("No task to show!!")
        else:
            for i in task:
                print(i)
    
    elif choice == "3":
        if len(task) == 0:
            print("No task to delete!")
        else:
            for i in task:
                print(i)
            del_task = input("Enter task to delete:")
            if del_task in task:
                task.remove(del_task)
                print("task removed successfully!!")
            else:
                print("task not found!!")
    
    elif choice == "4":
        print("Exiting program. Byee!")
        break