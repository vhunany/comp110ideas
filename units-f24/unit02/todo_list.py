def add_task(todo_list, task):
    todo_list[task] = 'not done'

def mark_done(todo_list, task):
    if task in todo_list:
        todo_list[task] = 'done'

def count_tasks(todo_list):
    done_count = 0
    not_done_count = 0
    task_list = list(todo_list)  # List of task descriptions

    # Using a for loop with range() to iterate through task_list
    for i in range(len(task_list)):
        task = task_list[i]
        if todo_list[task] == 'done':
            done_count += 1
        elif todo_list[task] == 'not done':
            not_done_count += 1

    return {'done': done_count, 'not done': not_done_count}

def get_not_done_tasks(todo_list):
    not_done_tasks = []
    task_list = list(todo_list)  # List of task descriptions

    # Using a while loop to iterate through task_list
    i = 0
    while i < len(task_list):
        task = task_list[i]
        if todo_list[task] == 'not done':
            not_done_tasks.append(task)
        i += 1
    
    return not_done_tasks

# Example usage
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
print(count_tasks(todo_list))  # {'done': 3, 'not done': 2}

# Get not done tasks
print(get_not_done_tasks(todo_list))  # ['Buy groceries', 'Finish homework']
