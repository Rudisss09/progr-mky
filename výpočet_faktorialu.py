def faktorial(cislo):
  """
  Vypočítá faktorial daného čísla.

  Args:
    cislo: Číslo, jehož faktorial se má vypočítat.

  Returns:
    Faktorial daného čísla.
  """

  if cislo == 0:
    return 1
  else:
    return cislo * faktorial(cislo - 1)

while True:
  try:
    cislo = int(input("Zadej číslo: "))
  except ValueError:
    print("Neplatný vstup. Zadej číslo.")
    continue

  faktorial_vysledek = faktorial(cislo)
  print("Faktorial", cislo, "je", faktorial_vysledek)

  if input("Chceš vypočítat faktorial dalšího čísla? (ano/ne): ").lower() != 'ano':
    break
