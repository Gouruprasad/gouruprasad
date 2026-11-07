for n in range(2, 50):
    is_prime = True

    for d in range(2, n):

        if n % d == 0:
            is_prime = False
            break

    if is_prime:
        print(n, end=" ")
