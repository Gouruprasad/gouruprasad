from statistics import mean

class student:
    def __init__(self,name):
        self.name = name
        self.grade = []
    def add_grade(self, g):
        self.grade.append(g)
    def compute_average(self):
        if len(self.grade)==0: 
          return 0
          return mean(self.grade)

ana = student("ana")
ana.add_grade(12)
ana.add_grade(16)
ben= student("ben")
ana.compute_average()
print(ana.name, ana.compute_average())
print(ben.name, ben.compute_average())
