# import modules needed for game
import logo
import os
import random

# Create a list of cards
cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Create a function to deal a card and calculate the score
def deal_card():
  """Returns a random card from the deck."""
  card = random.choice(cards)
  return card

def calculate_cards(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# logic for the game

run = True
while run:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        run = False
        os.system('clear')
    elif play_game == 'y':
        os.system('clear')
        print(f"\033[35m{logo.logo}\033[0m")
        print(f"\033[35m{logo.ace}\033[0m")
        user_cards = []
        computer_cards = []
        is_game_over = False
        
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        
        while not is_game_over:
            user_score = calculate_cards(user_cards)
            computer_score = calculate_cards(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_cards(computer_cards)
        
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        if user_score > 21:
            print("You went over. You lose!")
        elif computer_score > 21:
            print("Computer went over. You win!")
        elif user_score == computer_score:
            print("It's a draw!")
        elif user_score == 0:
            print("You win with a Blackjack!")
        elif computer_score == 0:
            print("Computer wins with a Blackjack!")
        elif user_score > computer_score:
            print("You win!")
        else:
            print("You lose!")
  