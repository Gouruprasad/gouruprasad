questions = [
    "What is 81 + 100?", 
    "What is the capital of France?", 
    "What is the capital of Japan?"]
answers = ["181", "Paris", "Tokyo"]

while True:
    score = 0
    for q, a in zip(questions, answers):
        user_answer = input(q + ": ").strip()
        if user_answer.lower() == a.lower():
            score += 1
            
    print(f"Your score: {score}/{len(questions)}")
    
    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        break