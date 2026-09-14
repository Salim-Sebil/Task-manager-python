import pytest

from task_manager.task_utils import add_task, calculate_progress, mark_task_as_complete, tasks, view_pending_tasks
from task_manager.validation import validate_due_date, validate_task_description, validate_task_title


def setup_function():
    tasks.clear()


def test_add_task_successfully_records_task():
    task = add_task("Read book", "Finish chapter 1", "2026-10-01")

    assert task["title"] == "Read book"
    assert task["description"] == "Finish chapter 1"
    assert task["completed"] is False
    assert len(tasks) == 1


def test_mark_task_as_complete_updates_status():
    add_task("Write report", "Draft intro", "2026-10-02")

    mark_task_as_complete(0)

    assert tasks[0]["completed"] is True


def test_view_pending_tasks_handles_empty_list():
    view_pending_tasks()


def test_calculate_progress_tracks_completion():
    add_task("Task 1", "Desc 1", "2026-10-03")
    add_task("Task 2", "Desc 2", "2026-10-04")
    mark_task_as_complete(0)

    assert calculate_progress() == 50.0


def test_validation_rejects_blank_values():
    with pytest.raises(ValueError):
        validate_task_title("   ")

    with pytest.raises(ValueError):
        validate_task_description("   ")

    with pytest.raises(ValueError):
        validate_due_date("")
