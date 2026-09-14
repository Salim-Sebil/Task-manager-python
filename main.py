from task_utils import add_task, calculate_progress, mark_task_as_complete, tasks, view_pending_tasks


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            try:
                add_task(title, description, due_date)
            except ValueError as exc:
                print(exc)

        elif choice == "2":
            if not tasks:
                print("No tasks currently.")
                continue

            view_pending_tasks()
            try:
                task_index = int(input("Enter the pending task number to mark complete: ")) - 1
                pending_task = [task for task in tasks if not task["completed"]][task_index]
                task_position = tasks.index(pending_task)
                mark_task_as_complete(task_position)
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Task progress: {progress:.2f}%")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
