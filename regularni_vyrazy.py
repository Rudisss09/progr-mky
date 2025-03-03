import re

text = "Telefonní číslo je 534-234-456 a emailová adresa je tomassolomus@gmail.com"

# Najít telefonní číslo
phone_number = re.search(r'\d{3}-\d{3}-\d{3}', text)
if phone_number:
  print(f"Telefonní číslo: {phone_number.group(0)}")

# Najít emailovou adresu
email = re.search(r'\S+@\S+', text)
if email:
  print(f"Emailová adresa: {email.group(0)}")

