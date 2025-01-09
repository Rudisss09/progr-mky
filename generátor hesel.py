import random, string

def randomword():
   password = ""
   letters = string.ascii_letters

   return password.join(random.choice(letters) for i in range(12))

print(randomword())