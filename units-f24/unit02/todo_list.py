def add_task(todo_list, task):
    todo_list[task] = 'not done'

def mark_done(todo_list, task):
    found = False  # Flag to indicate if the task was found
    # Iterate through dictionary to find and update the task
    for existing_task in todo_list:
        if existing_task == task:
            todo_list[existing_task] = 'done'
            found = True
        # No need to break, just continue checking other tasks if needed

def count_tasks(todo_list):
    done_count = 0
    not_done_count = 0
    
    # Iterate through dictionary keys directly
    for task in todo_list:
        if todo_list[task] == 'done':
            done_count += 1
        elif todo_list[task] == 'not done':
            not_done_count += 1

    return {'done': done_count, 'not done': not_done_count}

def get_not_done_tasks(todo_list):
    not_done_tasks = []
    
    # Iterate through dictionary keys directly
    for task in todo_list:
        if todo_list[task] == 'not done':
            not_done_tasks.append(task)
    
    return not_done_tasks

def main():
    todo_list = {
        'Buy groceries': 'not done',
        'Read a book': 'done',
        'Write report': 'not done',
        'Call mom': 'done'
    }

    # Add tasks
    add_task(todo_list, 'Finish homework')
    add_task(todo_list, 'Read a book')

    # Mark tasks as done
    mark_done(todo_list, 'Write report')
    mark_done(todo_list, 'Go for a walk')

    # Count tasks
    task_counts = count_tasks(todo_list)
    print("Task counts:", task_counts)  # {'done': 3, 'not done': 2}

    # Get not done tasks
    not_done_tasks = get_not_done_tasks(todo_list)
    print("Not done tasks:", not_done_tasks)  # ['Buy groceries', 'Finish homework']

if __name__ == "__main__":
    main()
