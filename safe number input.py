def ask_int(message):
    while True:
        num = input(message)
        try:
            return int(num)
        except ValueError:
              print("please type a number")

age = ask_int("age : ")
print("next year: " , age+1)
    
