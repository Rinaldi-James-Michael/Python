art = '''
 __    __                          __                                   ______                                                             
/  \  /  |                        /  |                                 /      \                                                            
$$  \ $$ | __    __  _____  ____  $$ |____    ______    ______        /$$$$$$  | __    __   ______    _______  _______   ______    ______  
$$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \       $$ | _$$/ /  |  /  | /      \  /       |/       | /      \  /      \ 
$$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      $$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ /$$$$$$  |/$$$$$$  |
$$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$    $$ |$$ |  $$/ 
$$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |$$$$$$$$/ $$ |      
$$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |            $$    $$/ $$    $$/ $$       |/     $$//     $$/ $$       |$$ |      
$$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/              $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/       
                                                                                                                                                                                                                                                                                                                                                                                                                        
'''
#TODO 1: Print out artwork
print(art)
print("\nWelcome to the Number Guessing Game!")

#TODO 2: Generate random number from 1 to 100
import random
print("I have thought of a number between 1 and 100.")
random_number = random.randint(1,100)

#TODO 3: Make user choose difficulty, this defines number of attempts
difficulty=""
while difficulty not in ["easy","hard"]:
    difficulty = input("\nChoose a difficulty by typing -> 'easy' or 'hard': ")
    if difficulty not in ["easy","hard"]:
        print("Please provide input again....")

attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

#TODO 4: Loop as many times as attempts
result = False
for i in range(attempts):
    print(f"\nYou have {attempts-i} chance/s left to guess the number!")
    userGuess = int(input("Guess the number: "))
    if userGuess > random_number:
        print("You've guessed higher than the current number!")
    elif userGuess < random_number:
        print("You've guessed lower than the current number!")
    elif userGuess == random_number:
        result = True
        break

#TODO 5: Announce result (result is boolean)
if result:
    print("\nYou've guessed the number and won! Congratulations!")
else:
    print("\nYou've exceeded attempts and lost. No worries, try again :)")
