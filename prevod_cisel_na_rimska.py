cislo = int(input("Zadej číslo (1–30): "))
rimsky = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"]
if 1 <= cislo <= 30:
    print("Římsky:", rimsky[cislo - 1])
else:
    print("Číslo není v rozsahu.")
