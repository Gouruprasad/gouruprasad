#create 'grades.txt' with some data if it doesn't exist
with open("grades.txt", "w", encoding="utf-8") as f:
    f.write("Alice 15\nBob 12\nCharlie 18\nGuru 20\nAmal 13")

#Your existing functions
def read_grades(path):
    grades = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            name, g = line.split()
            grades[name] = int(g)
    return grades

def average(values):
    return sum(values) / len(values)

#Run the program
grades = read_grades("grades.txt")
print(f"Average: {average(grades.values()):.2f}")
