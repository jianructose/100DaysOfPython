from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
# clear()
print(logo)
auction_dict = dict()
end_flag = False
while not end_flag:
    name = input("What is your name please?\n")
    bid = float(input("What is your bid? \n$"))
    auction_dict[name] = bid
    print(auction_dict)
    keep = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if keep != 'no':
        clear()
    else:
        end_flag = True
max_bid = -1
for name in auction_dict:
    if auction_dict[name] > max_bid:
        max_name = name
        max_bid = auction_dict[max_name]

print(f"The winner is {max_name} with a bid of ${max_bid}.")
