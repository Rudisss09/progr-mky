rok = int(input("Zadejte rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(f"Rok {rok} je přestupný.")
else:
    print(f"Rok {rok} není přestupný.")