import os

from draw import pic


print(pic)

bidding_list = {}

auction_finished = False


def check_bidder(records):
    current_highest = 0
    highest_bidder = ''
    for bidder in bidding_list:
        bidding_amount = bidding_list[bidder]

        if bidding_amount > current_highest:
            current_highest = bidding_amount
            highest_bidder = bidder
    

    print(f"The winner is {highest_bidder} with a bid of ${current_highest}")



while not auction_finished:
    name = input("What is your Name?:")
    price = int(input("What is your Bid? $"))
    bidding_list[name] = price

    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'.")

    if continue_auction == "no" :
        auction_finished = True
        check_bidder(bidding_list)
    elif continue_auction == 'yes' :
        os.system('clear')
