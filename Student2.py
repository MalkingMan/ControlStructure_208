def Temukuan_Nilai_Terbesar(Nilai1, Nilai2, Nilai3):
    if Nilai1 >= Nilai2 and Nilai1 >= Nilai3:
        return Nilai1
    elif Nilai2 >= Nilai1 and Nilai2 >= Nilai3:
        return Nilai2
    else:
        return Nilai3

Nilai1 = float(input("Masukkan Nilai 1: "))
Nilai2 = float(input("Masukkan Nilai 2: "))
Nilai3 = float(input("Masukkan Nilai 3: "))

Nilai_Terbesar = Temukan_Nilai_Terbesar(Nilai1, Nilai2, Nilai3)

print(f"The largest number among {Nilai1}, {Nilai2}, and {Nilai3} is: {Nilai_Terbesar}")
