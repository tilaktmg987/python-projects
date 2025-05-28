# To-Do List Menu print garincha
print("\n===== To-Do List Menu =====")

Todo = True  # Loop lai control garna flag variable

while Todo:
    # Option haru dekhaune
    print("\n1. View Tasks\n2. Add a Task\n3. Remove a Task\n4. Exit")
    
    try:
        # User bata choice line (int ma convert gareko)
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        # Integer bahek arko input aayo bhane error dekhaune
        print("Please enter a valid number!")
        continue

    if choice == 1:
        # Task haru herna ko lagi
        print("\n--- Your Tasks ---")
        with open("task.txt") as f:
            View_Task = f.read().strip()  # File padhera space hataune
            if View_Task:
                print(View_Task)
            else:
                print("No tasks available.")  # File khali cha bhane

    elif choice == 2:
        # Naya task add garna ko lagi
        task = input("Enter a new Task: ").strip()
        with open("task.txt") as f:
            first_line = f.readline()  # First line check garincha
            if first_line:
                # File ma pahile kai content cha bhane append garincha
                with open("task.txt", "a") as f_append:
                    f_append.write(f"\n{task}")
            else:
                # File khali cha bhane nai lekhincha
                with open("task.txt", "w") as f_write:
                    f_write.write(task)
        print(f"'{task}' added successfully.")  # Confirmation message

    elif choice == 3:
        # Sabai task haru padhera list ma halincha
        with open("task.txt") as f:
            content = f.readlines()
        if content:
            removed_task = content[0].strip()  # First task lai remove garna
            remaining_tasks = content[1:]  # Baaki task haru rakhincha
            with open("task.txt", "w") as f_write:
                for task in remaining_tasks:
                    f_write.write(task)  # File ma baaki task haru lekhincha
            print(f"'{removed_task}' removed successfully.")  # Confirmation
        else:
            print("No tasks to remove.")  # File khali bhaye

    elif choice == 4:
        # Program exit garne
        print("Exiting To-Do List. Goodbye!")
        Todo = False  # Loop end garincha

    else:
        # Wrong input aayo bhane
        print("Invalid choice. Please enter a number between 1 and 4.")
