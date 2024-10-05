def add_task(todo_list, task):
    task_found = False
    for existing_task in todo_list:
        if existing_task == task:
            task_found = True

        if not task_found:
            todo_list[task] = 'not done'

def mark_done(todo_list, task):
    for existing_task in todo_list:
        if existing_task == task:
            todo_list[existing_task] = 'done'

def main():
    todo_list = {
        'Buy groceries': 'not done',
        'Read a book': 'done',
        'Write report': 'not done',
        'Call mom': 'done'
    }

    add_task(todo_list, 'Finish homework')

    mark_done(todo_list, 'Write report')

    print("Current to-do list:", todo_list)

if __name__ == "__main__":
    main()