def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(n - 2):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return " ".join(map(str, fib_sequence))
print(fibonacci(10))