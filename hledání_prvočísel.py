def je_prvocislo(cislo):
  """
  Zkontroluje, zda je dané číslo prvočíslem.

  Args:
    cislo: Číslo, které se má zkontrolovat.

  Returns:
    True, pokud je číslo prvočíslem, jinak False.
  """

  if cislo <= 1:
    return False
  for i in range(2, int(cislo**0.5) + 1):
    if cislo % i == 0:
      return False
  return True

while True:
  try:
    cislo = int(input("Zadej číslo: "))
  except ValueError:
    print("Neplatný vstup. Zadej číslo.")
    continue

  if je_prvocislo(cislo):
    print(cislo, "je prvočíslo.")
  else:
    print(cislo, "není prvočíslo.")

  if input("Chceš zkontrolovat další číslo? (ano/ne): ").lower() != 'ano':
    break
