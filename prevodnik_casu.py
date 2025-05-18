minuty = int(input("Zadej počet minut: "))
hodiny = minuty // 60
zbyvajici_minuty = minuty % 60
print(f"{hodiny} hod a {zbyvajici_minuty} min")
