import random
import art
print(art.logo)

#TODO 1: Provide cards function
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#TODO 2: Calculate scores function
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#TODO 8: Play game function
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

#TODO 3: Compare and return end result of the game
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw 🫠"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😮"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😍"
        elif user_score > computer_score:
            return "You win 😍"
        else:
            return "You lose 😭"

#TODO 4: Provide two cards randomly to you and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

#TODO 5: Keep dealing cards to user and calculate score till the game ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

#TODO 6: Deal cards to the computer as long as the score is not above 17
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#TODO 7: Starting point of code to ask the user if he wants to play the game and keep asking
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*100)
    play_game()
