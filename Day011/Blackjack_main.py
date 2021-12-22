def thewinner(user_sum,dealer_sum):
  if dealer_sum > 21:
    print(f"Dealer score is {dealer_sum}, above 21. User wins!")
  elif dealer_sum == user_sum:
    print(f"User and dealer score is {user_sum} Its a draw.")
  elif user_sum > dealer_sum:
    print(f"User total score is : {user_sum}. Dealer total score is :{dealer_sum} User wins!" )
  else:
    print(f"User total score is : {user_sum}. Dealer total score is : {dealer_sum} User loses." )

def first_cards():
  for i in range(11):
    user_hand.append(cards[random.randint(0,12)])
    dealer_hand.append(cards[random.randint(0,12)])
  for card in range(2):
    reveal_uhand.append(user_hand[card])
  for card in range(dealer_cards()):
    reveal_dhand.append(dealer_hand[card])
  return(reveal_uhand,reveal_dhand)

def get_results(reveal_uhand,reveal_dhand):
  user_sum = 0
  dealer_sum = 0
  for i in range(len(reveal_uhand)):
    user_sum += reveal_uhand[i]
  for i in range(len(reveal_dhand)):
    dealer_sum += reveal_dhand[i]
  print(f"Dealer's hand: {reveal_dhand}")
  thewinner(user_sum,dealer_sum)
   
def above_21check(reveal_uhand):
  cards_sum = 0
  for i in range (len(reveal_uhand)):
    cards_sum += reveal_uhand[i]
  if cards_sum > 21:
      return True
  else:
    clear()
    print(logo)
    print(f"Your hand: {reveal_uhand}")
    print(f"Dealer's hand [{reveal_dhand[0]}, *]")
    print(f"Your current score is : {cards_sum}")
    return False
def another_card(reveal_ucards,reveal_uhand):
  if not above_21check(reveal_uhand):
    get_card = input("Do you want another card? Press y for yes, n for no\n")
    if get_card == "y":
      reveal_ucards += 1
      reveal_uhand.append(user_hand[reveal_ucards-1])
      print(reveal_uhand)
      another_card(reveal_ucards,reveal_uhand)
    else:
      get_results(reveal_uhand,reveal_dhand)
  else:
    print("You lose. You went above 21.")
    return
def dealer_cards():
  dealer_sum = 0
  dealer_cards = 0
  for i in range(6):
    dealer_cards += 1
    dealer_sum += dealer_hand[i]
    if dealer_sum > 16:
      return dealer_cards
from replit import clear
import random
from art import logo
should_continue = True
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
while should_continue:
  user_hand = []
  dealer_hand = []
  reveal_uhand = []
  reveal_dhand = []
  reveal_uhand, reveal_dhand = first_cards()
  another_card(2,reveal_uhand)
  another_game = input("Do you want to play another? Type y for yes, n for no.\n").lower()
  if another_game == "n":
    should_continue = False
  









 
