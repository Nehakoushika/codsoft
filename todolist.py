def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []
    
    while True:
        print("\n1. Display to-do list")
        print("2. Add task to to-do list")
        print("3. Remove task from to-do list")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            display_todo_list(todo_list)
            task_number = int(input("Enter the task number to remove: "))
            remove_task(todo_list, task_number)
        elif choice == '4':
            print("thankyou")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





