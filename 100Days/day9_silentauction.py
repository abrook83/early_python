from day9_art import logo, clear_screen
print(logo)

bid_dict = {}

auction_open = True

def find_highest_bidder(bidding_record):        # plugs in the bid dictionary as its input
  highest_bid = 0                               # creates empty reposits for bid and name....
  winner = ""
  for bidder in bidding_record:                 # for each item in the plugged-in dictionary...
    bid_amount = int(bidding_record[bidder])    # 'bid_amount' is the value associated to each key ('bidder')
    if bid_amount > highest_bid:                # if that amount is higher than the highest (starting at 0)...
      highest_bid = bid_amount                  # replace it with the new value
      winner = bidder                           # then the 'winner' is the key
  print(f"The winner is {winner} with a bid of ${highest_bid}")    

while auction_open:
    bidder_name = input('What is your name?:\n').title()
    bid = input("Enter your bid:\n$")
    bid = int(bid)
    bid_dict[bidder_name] = bid
    add_bid = input("Are there other bids to enter? (y/n):\n")
    if add_bid == 'y':
        print(clear_screen)
        continue
    else:
        auction_open = False
        find_highest_bidder(bid_dict)