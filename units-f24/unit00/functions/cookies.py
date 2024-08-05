def distribute_cookies(total_cookies, num_students) -> str:
    cookies_per_student = total_cookies // num_students
    cookies_left = total_cookies % num_students

    return "Each student gets " + str(cookies_per_student) + "cookies. Cookies left over: " + str(cookies_left)

total_cookies: int = 35
num_students: int = 4
print(distribute_cookies(total_cookies, num_students))

additional_cookies: int = 10
total_cookies += additional_cookies  # Update total cookies

# Recalculate distribution with the new total
distribution_info = distribute_cookies(total_cookies, num_students)

# Print updated results
print("After adding more cookies:")
print(distribution_info)