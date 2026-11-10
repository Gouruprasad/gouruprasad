names = ["trumb", "puten" , "kem" , "selensky",]
grades = [10 , 12.3 , -0.1 , 15.5]
count = 0
sum = 0
for names , grades in zip(names,grades):
    count=count+1
    sum = sum+grades
    result = "pass" if grades>=10 else ("fail")
    print(f"{count}.{names} : {grades} {result}")
avg = sum/count
print(f"average : {avg}")