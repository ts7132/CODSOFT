import time
from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f"{self.description} - Due: {self.due_date}"

def print_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
    else:
        print("TO-DO List:")
        for index, task in enumerate(task_list, start=1):
            due_date = task.due_date.strftime("%d/%m/%y")
            print(f"\033[1;36m{index}\033[0m: \033[1;33m{task.description} - Due: {due_date}\033[0m")

def add_task(task_list):
    add = input("Enter task description: ")
    due = input("Enter due date (DD/MM/YY): ")
    task_list.append(Task(add, datetime.strptime(due, "%d/%m/%y")))
    print("Task added successfully.")
    return task_list

def remove_task(task_list):
    if not task_list:
        print("No tasks to remove.")
    else:
        print_tasks(task_list)
        index = int(input("Enter the index of the task to remove: ")) - 1
        if 0 <= index < len(task_list):
            del task_list[index]
            print("Task removed successfully.")
        else:
            print("Invalid index.")
    return task_list

def edit_task(task_list):
    if not task_list:
        print("No tasks to edit.")
    else:
        print_tasks(task_list)
        index = int(input("Enter the index of the task to edit: ")) - 1
        if 0 <= index < len(task_list):
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date (DD/MM/YY): ")
            task_list[index] = Task(new_description, datetime.strptime(new_due_date, "%d/%m/%y"))
            print("Task edited successfully.")
        else:
            print("Invalid index.")
    return task_list

task_list = []

while True:
    print("""\033[1;32mTO-DO List Management System
1: Add
2: View
3: Remove
4: Edit
5: Exit\033[0m""")
    choice = input("Enter your choice: ")

    if choice == '1':
        task_list = add_task(task_list)
    elif choice == '2':
        print_tasks(task_list)
    elif choice == '3':
        task_list = remove_task(task_list)
    elif choice == '4':
        task_list = edit_task(task_list)
    elif choice == '5':
        print("Exiting...")
        time.sleep(1)
        break
    else:
        print("Invalid choice, please choose a number between 1-5.")