seznam = ["hruška", "banán", "třešeň", "pomelo"]
ovoce = input("Zadej hledané ovoce: ")
if ovoce in seznam:
    print("Index:", seznam.index(ovoce))
else:
    print("Ovoce není v seznamu.")
