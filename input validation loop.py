while True:
    grade = float(input("Grade (0-20): "))
    if 0 <= grade <= 20:
        break
    print("Invalid, try again.")
print(f"Grade saved: {grade}")
