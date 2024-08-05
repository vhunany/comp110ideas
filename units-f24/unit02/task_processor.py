def process_tasks(tasks):
    processed_tasks = []  # List to store processed tasks
    counter = 0  # Counter variable to count the number of tasks processed
    index = 0  # Indexing variable to track the position in the tasks list

    while len(tasks) > 0:  # Continue while there are tasks left in the list
        task = tasks.pop(0)  # Remove and get the first task from the list

        # Process every second task
        if index % 2 == 0:
            processed_tasks.append(task)  # Add the task to the processed list
            counter += 1  # Increment the counter

        index += 1  # Move to the next index

    print(f"Total tasks processed: {counter}")
    return processed_tasks

# Example usage
tasks = ["buy groceries", "finish report", "call mom", "fix computer", "do laundry"]
processed_tasks = process_tasks(tasks)
print(processed_tasks)
