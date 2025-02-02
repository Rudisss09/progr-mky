import random

def nahodne_cislo(minimum, maximum):
    return random.randint(minimum, maximum)

min_cislo = int(input("Zadejte minimální číslo: "))
max_cislo = int(input("Zadejte maximální číslo: "))

print(f"Náhodné číslo mezi {min_cislo} a {max_cislo} je: {nahodne_cislo(min_cislo, max_cislo)}")
