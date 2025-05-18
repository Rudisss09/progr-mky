cislo = int(input("Zadej číslo: "))
delitele = [i for i in range(1, cislo + 1) if cislo % i == 0]
print("Dělitelé:", delitele)
