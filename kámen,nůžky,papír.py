import random

def play_rps():
    options = ['kámen', 'papír', 'nůžky']
    user_choice = input("Zadej kámen, papír, nebo nůžky: ").lower()
    soupeř_choice = random.choice(options)

    print(f"Soupeř vybral: {soupeř_choice}")
    
    if user_choice == soupeř_choice:
        print("Remíza!")
    elif (user_choice == 'kámen' and soupeř_choice == 'nůžky') or \
         (user_choice == 'nůžky' and soupeř_choice == 'papír') or \
         (user_choice == 'papír' and soupeř_choice == 'kámen'):
        print("Vyhrál jsi!")
    else:
        print("Prohrál jsi!")

play_rps()
