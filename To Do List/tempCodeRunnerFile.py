with open("task.txt")as f:
        content=f.readlines()
        if content != "":
            remaining_tasks=content[1:]
            print(f"{content[0].strip() } removed successfully")
            with open("task.txt","w")as f:
                for task in remaining_tasks:
                    f.write(task)
        else:
            print("NO ANY LIST")
    