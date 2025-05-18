castka = float(input("Počáteční částka (Kč): "))
urok = float(input("Roční úrok (%): "))
roky = int(input("Počet let: "))

vysledek = castka * (1 + urok / 100) ** roky
print(f"Částka po {roky} letech: {vysledek:.2f} Kč")
