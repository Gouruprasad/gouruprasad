n = int(input("Number: "))

is_prime = n >= 2

for d in range(2, n):

    if n % d == 0:
        print(f"{n} is divisible by {d}")
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
