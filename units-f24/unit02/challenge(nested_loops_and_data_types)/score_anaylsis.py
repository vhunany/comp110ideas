def analyze_scores(students_scores: dict[str, list[int]]):
    total_scores: list = []
    score_counts: dict = {}
    highest_score: bool = None
    highest_scorers: list = []

    student_names: list = []
    student_scores: list = []

    # Convert dictionary to list of keys and values
    for student in students_scores:
        student_names.append(student)
        student_scores.append(students_scores[student])

    i: int = 0
    while i < len(student_names):
        student_name: str = student_names[i]
        scores: list[int] = student_scores[i]

        j: int = 0
        while j < len(scores):
            score: int = scores[j]
            total_scores.append(score)

            if score in score_counts:
                score_counts[score] += 1
            else:
                score_counts[score] = 1

            if highest_score is None or score > highest_score:
                highest_score = score
                highest_scorers = [student_name]
            elif score == highest_score:
                if student_name not in highest_scorers:
                    highest_scorers.append(student_name)

            j += 1
        i += 1

    total_sum: int = 0
    k: int = 0
    while k < len(total_scores):
        total_sum += total_scores[k]
        k += 1

    average_score = total_sum / len(total_scores)

    above_average_students: list[str] = []
    i = 0
    while i < len(student_names):
        student_name = student_names[i]
        scores = student_scores[i]

        score_sum: int = 0
        j = 0
        while j < len(scores):
            score_sum += scores[j]
            j += 1

        if score_sum / len(scores) > average_score:
            above_average_students.append(student_name)

        i += 1

    return {
        'average_score': average_score,
        'above_average_students': above_average_students,
        'highest_score': (highest_score, highest_scorers),
        'score_counts': score_counts
    }

students_scores = {
    'Alice': [85, 92, 88],
    'Bob': [78, 81, 79],
    'Charlie': [90, 95, 100],
    'Diana': [88, 84, 86],
    'Eve': [75, 77, 80]
}

print(analyze_scores(students_scores))
