def track_hours(hours_worked):
    total_hours = {}
    most_hours_employee = None
    highest_hours = None
    employees_over_40_hours = 0

    for employee in hours_worked:
        hours = hours_worked[employee]
        total = 0
        i = 0
        while i < len(hours):
            total += hours[i]
            i += 1

        total_hours[employee] = total

        if highest_hours is None or total > highest_hours:
            highest_hours = total
            most_hours_employee = employee

        if total > 40:
            employees_over_40_hours += 1

    return {
        'total_hours': total_hours,
        'most_hours_employee': (most_hours_employee, highest_hours),
        'employees_over_40_hours': employees_over_40_hours
    }

hours_worked = {
    'Alice': [8, 8, 8, 8, 8, 0, 0],
    'Bob': [9, 9, 9, 8, 8, 0, 0],
    'Charlie': [10, 10, 10, 10, 10, 0, 0],
    'Diana': [7, 7, 7, 7, 7, 7, 7]
}

print(track_hours(hours_worked))
