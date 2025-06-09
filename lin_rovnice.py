def reseni_linear_rovnice():
    """Řeší lineární rovnici ax + b = 0."""

    try:
        # Získání vstupu od uživatele
        a = float(input("Zadej koeficient a: "))
        b = float(input("Zadej koeficient b: "))

        # Zpracování případů
        if a == 0:
            if b == 0:
                print("Rovnice má nekonečně mnoho řešení (identita).")
            else:
                print("Rovnice nemá řešení.")
        else:
            x = -b / a
            print(f"Řešení rovnice je: x = {x}")

    except ValueError:
        print("Chyba: Zadej prosím čísla.")

# Spuštění funkce
reseni_linear_rovnice()
