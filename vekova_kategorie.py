vek = int(input("Zadej svůj věk: "))
if vek < 12:
    print("Dítě")
elif vek < 18:
    print("Teenager")
elif vek < 65:
    print("Dospělý")
else:
    print("Senior")
