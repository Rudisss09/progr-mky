def prumer_seznam(seznam):
    return sum(seznam) / len(seznam) if seznam else 0

delka = int(input("Zadejte počet čísel: "))
seznam = []

for i in range(delka):
    cislo = float(input(f"Zadejte číslo {i + 1}: "))
    seznam.append(cislo)

print(f"Průměr čísel v seznamu je: {prumer_seznam(seznam)}")
