15#ODD Numbers

def Bilangan_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:  # Check if the number is odd
            print(i, end=" ")

n = int(input("Masukkan Nilai: "))

print(f"Bilangan ganjil {n}:")
Bilangan_ganjil(n)