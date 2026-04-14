def viewTasks(tasks):
    if len(tasks) == 0:
        print("Your Todo list is currently empty.")
        return
    
    print("Your Todo List:")
    i = 1
    for task in tasks:
        print(f"{i}. {task}")
        i += 1

def addTask(tasks, newTask):
    tasks.append(newTask)
    print("New task added to your Todo list")

def rmvTask(tasks, oldTask):
    tasks.remove(oldTask)
    print("Task removed from your Todo list")

tasks = []

while True:
    print("""\nTodo List Menu:
1. View Tasks
2. Add a Task
3. Remove a Task
4. Exit""")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        viewTasks(tasks)
    elif choice == 2:
        new_task = input("Enter a new task: ")
        addTask(tasks, new_task)
    elif choice == 3:
        task_2_b_removed = input("Which task do you want to remove? ")
        rmvTask(tasks, task_2_b_removed)
    elif choice == 4:
        break
    else:
        print("Invalid Input")