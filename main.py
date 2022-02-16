import random
import os


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def score_calculator(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def compare(user_score, computer_score):
    if computer_score == user_score:
        return ("Its a Draw")
    elif computer_score == 0:
        return ("You Lose")
    elif user_score > 21:
        return ("You Lose")
    elif user_score == 0:
        return ("You Win")
    elif computer_score > 21:
        return ("You win")
    elif computer_score > user_score:
        return ("You Lose")
    elif computer_score < user_score:
        return ("You Win")


def blackjack():

    user_cards = []
    computer_cards = []
    game_ends = False

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    while not game_ends:
        user_score = score_calculator(user_cards)
        computer_score = score_calculator(computer_cards)
        print(f"Your cards are: {user_cards} and your Score is: {user_score}")

        print(f"Computer's first card is {computer_cards[0]}")

        if user_score > 21 or computer_score == 0 or user_score == 0:
            game_ends = True
        else:
            ask_user = input("\nDo you want to draw more cards? \nType Y for yes and N for no: ").lower()
            if ask_user == "y":
                user_cards.append(deal_card())
            else:
                game_ends = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = score_calculator(computer_cards)

    print(f"Your hand was {user_cards} and your score is {user_score} ")
    print(f"Computer's hand was {computer_cards} and Computer score is {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    blackjack()

