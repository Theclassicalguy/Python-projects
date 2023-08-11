def adding_tasks():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def displaying_tasks():
    print("<---------------------------------------------->")
    print("Tasks:")
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            print("<---------------------------------------------->")    
    except FileNotFoundError:
        print("No tasks found !!")

def deleting_tasks():
    print("<---------------------------------------------->")
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            print("All Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            print("<---------------------------------------------->")
            task_to_delete = int(input("Enter the number of the task you want to delete: "))
            

            if 1 <= task_to_delete <= len(tasks):
                deleted_task = tasks.pop(task_to_delete - 1).strip()
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number!")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    try:
        with open("tasks.txt", "x"):
            pass
    except FileExistsError:
        pass

    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        print("<---------------------------------------------->")

        if choice == "1":
            adding_tasks()
        elif choice == "2":
            displaying_tasks()
        elif choice == "3":
            deleting_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
