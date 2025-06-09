import math

def vypocitej_objem_kuzelu():
    """Vypočítá objem rotačního kužele."""

    try:
        # Získání vstupu od uživatele
        r = float(input("Zadej poloměr podstavy (r): "))
        vyska = float(input("Zadej výšku kužele (v): "))

        # Kontrola, zda jsou zadané hodnoty kladné
        if r <= 0 or vyska <= 0:
            print("Chyba: Poloměr a výška musí být kladná čísla.")
            return

        # Výpočet objemu
        objem = (1/3) * math.pi * r**2 * vyska

        # Zobrazení výsledku
        print(f"Objem rotačního kužele je: {objem}")

    except ValueError:
        print("Chyba: Zadej prosím čísla.")

# Spuštění funkce
vypocitej_objem_kuzelu()
