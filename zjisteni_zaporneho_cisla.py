seznam = [3, -1, 5, 0]
if any(x < 0 for x in seznam):
    print("Seznam obsahuje záporné číslo.")
else:
    print("Všechna čísla jsou kladná nebo nula.")
