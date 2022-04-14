############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    hit = random.choice(cards)
    return hit


# print(deal_card())


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(lst_cards):
    """Take a list of cards and return the score calculated from the cards"""
    _sum = sum(lst_cards)
    if set(lst_cards) == {11, 10}:
        return 0
    elif _sum > 21 and 11 in lst_cards:
        lst_cards.remove(11)
        lst_cards.append(1)
    return sum(lst_cards)


def compare(uc, cc):
    if uc > 21 and cc > 21:
        return "You went over, you lose."
    if uc == cc:
        return ("It is a draw.")
    elif cc == 0 or uc > 21:
        return ("You loseee")
    elif uc == 0:
        return "You win with a blackjack"
    elif cc > 21:
        return ("You winn")
    elif uc > cc:
        return ("You winn")
    else:
        return ("You losee")


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # print(user_cards, computer_cards)

    #Hint 6: Create a function called calculate_score() that takes a List of cards as input
    #and returns the score.
    #Look up the sum() function to help you do this.

    # for testing
    # computer_cards = [11, 10]
    # user_cards = [11, 10]

    end_flag = False

    while not end_flag:
        cc = calculate_score(computer_cards)
        uc = calculate_score(user_cards)
        print(
            f"Your cards: {user_cards}, current score: {uc}\nComputer's first card: {computer_cards[0]}"
        )

        #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

        #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

        if uc > 21 or uc == 0 or cc == 0:
            end_flag = True
            # if uc > 21:
            #   print(f"You loseee")
            # elif uc == 0:
            #   print("You winn")
            # else:
            #   print("You lose")

        else:
            keep = input("Do you like to hit? y or n: \n")
            if keep == 'y':
                user_cards.append(deal_card())
            # elif keep == 'n':
            #   end_flag = True
            else:
                end_flag = True

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while cc != 0 and cc < 17:
        computer_cards.append(deal_card())
        cc = calculate_score(computer_cards)

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

    print(
        f"Your final hand: {user_cards}, final score: {uc}\nComputer's cards: {computer_cards}, and scores: {cc}"
    )
    print(compare(uc, cc))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("start? y or n\n") == 'y':
    clear()
    play_game()
