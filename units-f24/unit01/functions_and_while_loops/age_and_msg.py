def classify_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 60:
        return "Adult"
    else:
        return "Senior"

def generate_message(age):
    category = classify_age(age)
    if category == "Child":
        return "Enjoy your childhood!"
    elif category == "Teenager":
        return "Adolescence is a time for growth."
    elif category == "Adult":
        return "Embrace the responsibilities of adulthood."
    else:
        return "Wisdom comes with age."

def count_down_and_classify(start_age):
    while start_age >= 0:
        message = generate_message(start_age)
        print(f"Age {start_age}: {message}")
        start_age -= 5

count_down_and_classify(25)
