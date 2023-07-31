def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_numbers = [0, 1]
    while len(fib_numbers) < n:
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)

    return fib_numbers[:n]
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))