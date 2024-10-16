#Fibonacci

def fibonacci_series(n):
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

n = int(input("Masukkan Nilai: "))

fib_series = fibonacci_series(n)
print(f"Seri FIbonacci {n} Nilai: {fib_series}")