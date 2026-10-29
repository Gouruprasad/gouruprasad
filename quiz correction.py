Answer = [ "b" , "a" , "d" , "c" ]
correct = [ "b" , "c" , "d" , "c" ]
total_questions = 4
score = 0 
for right, given in zip(Answer,correct):
     if right == given:
         score = score + 1
print(f"score : {score}/{total_questions}")
