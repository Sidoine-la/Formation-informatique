def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input(""))

if is_prime(number):
    print(f"Prime")
else:
    print(f"Not Prime")

