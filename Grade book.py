#Grade book
grades = {
    "Ana": [19, 16, 12],
    "Ben": [9, 19.9, 8],
    "Chloé": [18, 1, 19] }

grades["Ben"].append(15)

best_student = []
highest_avg = -1

for student, student_grades in grades.items():
    avg = sum(student_grades) / len(student_grades)
    print(f"{student}  {avg:.1f}")
    if avg > highest_avg:
        highest_avg = avg
        best_student = student

print(f"Best Student : {best_student}")