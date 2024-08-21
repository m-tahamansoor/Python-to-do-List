def main():
    tasks = []

    while True:
        print("\t==== To-Do List ====")
        print("\n1. Add Tasks")
        print("\n2. Show Tasks")
        print("\n3. Mark Task as Done")
        print("\n4. Exit :)")

        choice = input("\n  Enter your choice: ")

        if choice == "1":
            print()
            n_tasks = int(input("Enter the number of tasks you wanna add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == "2":
            print("\ntasks")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done:")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done...")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice, Please try again.")

main()      
            
