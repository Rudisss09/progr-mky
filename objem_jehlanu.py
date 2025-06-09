import math

def vypocitej_objem_jehlanu():
    """Vypočítá objem pravidelného čtyřbokého jehlanu."""

    try:
        # Získání vstupu od uživatele
        a = float(input("Zadej délku strany podstavy (a): "))
        vyska = float(input("Zadej výšku jehlanu (v): "))

        # Kontrola, zda jsou zadané hodnoty kladné
        if a <= 0 or vyska <= 0:
            print("Chyba: Délka strany a výška musí být kladná čísla.")
            return

        # Výpočet objemu
        objem = (1/3) * a**2 * vyska

        # Zobrazení výsledku
        print(f"Objem pravidelného čtyřbokého jehlanu je: {objem}")

    except ValueError:
        print("Chyba: Zadej prosím čísla.")

# Spuštění funkce
vypocitej_objem_jehlanu()
