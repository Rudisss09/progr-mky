import random

def game():
    randomNum = random.randint(1, 10)
    guess = int(input("uhadni cisilko od 1-10: "))

    if guess > 10 or guess < 1:
        print("hezky si to napsal zkus to znovu")
        game()

    if guess == randomNum:
        print("tos to uhadl gratuluju nic nedostanes")
    else:
        print("se ti to moc nepovedlo, spravne cisilko bylo", randomNum) 

game()
