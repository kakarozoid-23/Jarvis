from plyer import notification

def add_to_todo():
    """Takes user input, adds a task to the to-do list, and sends a notification."""
    task = input("Enter your task: ").strip()
    
    if task:  # Ensure the task is not empty
        filename = "todo_list.txt"
        with open(filename, "a") as file:
            file.write(task + "\n")
        
        # Show desktop notification
        notification.notify(
            title="To-Do List",
            message=f'Task Added: {task}',
            timeout=5  # Notification duration in seconds
        )
        print(f'Task "{task}" added to the to-do list.')
    else:
        print("Task cannot be empty!")

# Example usage
add_to_todo()
