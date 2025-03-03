import random

def guess_number():
  """Hra na hádání čísla."""
  secret_number = random.randint(1, 100)
  attempts = 0
  while True:
    try:
      guess = int(input("Hádej číslo (1-100): "))
      attempts += 1
      if guess < secret_number:
        print("Příliš malé.")
      elif guess > secret_number:
        print("Příliš velké.")
      else:
        print(f"Správně! Uhádl jsi na {attempts}. pokus.")
        break
    except ValueError:
      print("Zadej platné číslo.")

guess_number()
