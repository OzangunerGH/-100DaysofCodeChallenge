import random
from replit import clear
from art import logo
def compare(user_score,dealer_score):
  """Compares the user score and the dealer score to announce who won the game of blackjack."""
  if user_score > 21:
    print("User went over 21. Dealer wins.")
  elif user_score == dealer_score:
    print(f"Both user and dealer got a score of {user_score}. It's a draw.")
  elif user_score == 0:
    print("User got a blackjack. User wins.")
  elif dealer_score == 0:
    print("Dealer got a blackjack. Dealer wins.")
  elif dealer_score > 21:
    print("Dealer went over 21. User wins.")
  elif dealer_score > user_score:
    print(f"Dealer's score is : {dealer_score}.\nUser's score is : {user_score}.\n Dealer wins.")
  else:
    print(f"Dealer's score is : {dealer_score}.\nUser's score is : {user_score}.\n User wins.")
def deal_card():
  """Returns a random card from the deck of cards."""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  """Calculates the score of user and the dealer as well as allowing to use ace as 1 or 11 depending on the total sum."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  while sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

play_again = True
while play_again:
  clear()
  print(logo)
  user_cards = []
  dealer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  is_game_over = False
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  print(f"User cards are : {user_cards},\nDealer's card are [{dealer_cards[0]}, *]")
  while not is_game_over:
    if user_score == 0:
      print("User got a blackjack. User wins.")
      is_game_over = True
    elif dealer_score == 0:
      print("Dealer got a blackjack. Dealer wins.")
      is_game_over = True
    elif user_score > 21:
      print("User went over 21. Dealer wins.")
      is_game_over = True
      
    else:
      user_should_deal = input("Type y to get another card.Type n to pass.\n").lower()
      if user_should_deal == "y":
        clear()
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(logo)
        print(f"User cards are : {user_cards},\nDealer's card are [{dealer_cards[0]}, *]")
      else:
        while dealer_score != 0 and dealer_score < 17:
          is_game_over = True
          dealer_cards.append(deal_card())
          dealer_score = calculate_score(dealer_cards)
          compare(user_score,dealer_score)
      

        print(f"User's final hand is : {user_cards}\n User final score is : {user_score}\nDealer's final hand is : {dealer_cards}\n Dealer final score is : {dealer_score}\n")     
  play_more = input("Do you want to play another game ? Type y to play again, n to pass.\n").lower()
  if play_more == "n":
    print("Game over.Take care :)")
    play_again = False
