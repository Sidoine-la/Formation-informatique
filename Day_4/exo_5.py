n = int(input(" "))
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
print(f"{factorial(n)}")