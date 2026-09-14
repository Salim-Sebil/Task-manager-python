from datetime import datetime

try:
    from task_manager.validation import validate_due_date, validate_task_description, validate_task_title
except ModuleNotFoundError:
    from validation import validate_due_date, validate_task_description, validate_task_title

# Define tasks list
tasks = []

# Example task dictionary structure
# task = {"title": "Groceries", "description": "Shop at Market Basket for food", "due_date": "2024-06-26", "completed": True}


# Implement add_task function
def add_task(title, description, due_date):
    valid_title = validate_task_title(title)
    valid_description = validate_task_description(description)
    valid_due_date = validate_due_date(due_date)

    task = {
        "title": valid_title,
        "description": valid_description,
        "due_date": valid_due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    print("Task added successfully!")
    return task


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        raise IndexError("Task index out of range.")

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return tasks[index]


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task.get("completed", False)]

    if not pending_tasks:
        print("No pending tasks.")
        return []

    print("Pending tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']} - Due: {task['due_date']}")

    return pending_tasks


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0

    completed_tasks = sum(1 for task in tasks if task.get("completed", False))
    progress = (completed_tasks / len(tasks)) * 100
    return progress