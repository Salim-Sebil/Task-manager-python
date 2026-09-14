from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return title.strip()


def validate_task_description(description):
    if not isinstance(description, str) or len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return description.strip()


def validate_due_date(due_date):
    if not isinstance(due_date, str) or len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty.")

    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Due date must be in YYYY-MM-DD format.") from exc

    return due_date.strip()