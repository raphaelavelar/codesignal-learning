def next_prime(n):
    while True:
        n += 1
        prime = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break

        if prime:
            return n
