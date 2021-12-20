## Function to calculate and announce who won the auction.
def find_highest_bidder(bids):
  highest_bid = 0
  winner = ""
  for name in bids:
      if bids[name] > highest_bid:
        highest_bid = bids[name]
        winner = name
        print(f"The winner is {winner.capitalize()} with {highest_bid}$ bid!")       
from replit import clear
from art import logo
print(f"{logo}\nWelcome to the secret auction program!")
bids = {}
auction_finished = False
## Loop to get the name and the input of users and store it in a dictionary.
while not auction_finished:
  name = input("What is your name ?").lower()
  bids[name] = int(input("What is your bid?")) 
  repeat = input("Are there other bidders? Type 'yes' or 'no'").lower()
  ## When repeat is something other than yes, function is called to calculate and auction_finished is true so the while loop stops executing.
  if repeat != "yes":
    auction_finished = True
    find_highest_bidder(bids)
  else:
    clear()

