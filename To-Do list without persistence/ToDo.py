tasks = []
print("\n" + "*" * 45)
print("\nWelcome to the best To-Do list in the world!\n")
print("*" * 45)
def loop():
    while True:
        print("\nWhat would you like to do?\n1. Add new task\n2. Check tasks\n3. Remove a task\nX Exit the program")
        todo = input()
        if todo == str(1):
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif todo == str(2):
            print("\tHere are your current tasks:")
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"\t{i}. {task}")
            else:
                print("\tNo tasks, good job!")
        elif todo == str(3):
            print("\tChoose which task to remove:")
            for i, task in enumerate(tasks, start=1):
                print(f"\t{i}. {task}")
            task_number = int(input())
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task removed.")
        elif todo.lower() == 'x':
            print("Exiting...")
            break


loop()
