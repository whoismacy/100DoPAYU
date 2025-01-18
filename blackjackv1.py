from blackjack_art import LOGO

import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
random.shuffle(cards)
cards_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10, "A": 11}

users_card = []
dealers_card = []

the_user_score = 0
the_dealer_score = 0

def first_hit():
    """
        Appends the first two cards
        for both the dealer and the user.
    :return: no return
    """
    for i in range(1, 3):
        rand1 = random.choice(cards)
        rand2 = random.choice(cards)
        if i == 1:
            users_card.append(rand1)
            users_card.append(rand2)
        else:
            dealers_card.append(rand1)
            dealers_card.append(rand2)


def next_hit(val):
    """
    adds a new value (hit) to any of the players
    :param val: 1 adds hit to user else adds hit to dealer
    :return: no return
    """
    if val == 1:
        users_card.append(random.choice(cards))
    else:
        dealers_card.append(random.choice(cards))


def print_card(cards):
    """
    given a list of cards, prints the cards
    :param cards: takes a list of cards
    :return: no return prints, order of cards
    """
    if len(cards) == 1:
        return f"[{cards[0]}]"
    elif len(cards) == 2:
        return f"[{cards[0]}, {cards[1]}]"
    elif len(cards) == 3:
        return f"[{cards[0]}, {cards[1]}, {cards[2]}]"
    elif len(cards) == 4:
        return f"[{cards[0]}, {cards[1]}, {cards[2]}, {cards[3]}]"
    elif len(cards) == 5:
        return f"[{cards[0]}, {cards[1]}, {cards[2]}, {cards[3]}, {cards[4]}]"


def calc_score(given_cards):
    """
    given a list of cards, calculates the total score
    :param cards:takes a list of cards
    :return:returns the total score
    """
    temp_value = 0
    for i in range(0, len(given_cards)):
        temp_value += cards_value[given_cards[i]]
    return temp_value


def cards_at_the_moment():
    """
    prints out the number of cards each player has at that given moment.
    :return:no return value
    """
    print(f"\tYour Cards: {print_card(users_card)}, current score: {calc_score(users_card)}")
    print(f"\tComputer's first card: {dealers_card[0]}")


def comp_hand():
    """
    Ensures the computer plays no less than 17
    appends a card to the comp
    :return: no return value
    """
    if calc_score(dealers_card) < 10:
        next_hit(0)


def final_hand():
    """
    prints out the final hand
    of each player
    :return:no return value
    """
    print(f"Your final hand: {print_card(users_card)}, final score: {calc_score(users_card)}")
    print(f"Computer's final hand: {print_card(dealers_card)}, final score: {calc_score(dealers_card)}")



def other_card():
    """
    Main logic of the game, and calculates
    the score of each player, whether it is a win a loss or a tie
    :return: has no return value
    """
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == "y" or another_card[0] == "y":
            next_hit(1)
            cards_at_the_moment()
            if calc_score(users_card) < 17 and calc_score(dealers_card) < 17:
                comp_hand()
                if calc_score(dealers_card) == calc_score(users_card):
                    final_hand()
                    print("PUSH, tie")
                    break
                elif calc_score(users_card) > 21:
                    if "A" in users_card:
                        the_user_scores = calc_score(users_card) - 10
                        if the_user_scores > 21:
                            final_hand()
                            print("You went BUST!. Opponent wins.")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(dealers_card) > 21:
                    if "A" in dealers_card:
                        the_dealer_score = calc_score(users_card) - 10
                        if the_dealer_score > 21:
                            final_hand()
                            print("Opponent went BUST ! You win")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(users_card) > 21 and calc_score(dealers_card) <= 21:
                    final_hand()
                    print("You went BUST!. Opponent wins.")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) <= 21:
                    final_hand()
                    print("Opponent went BUST!. You win !!")
                    break
                elif calc_score(users_card) <= 21 and calc_score(users_card) > calc_score(dealers_card):
                    final_hand()
                    print("You win!")
                    break
                elif calc_score(dealers_card) <= 21 and calc_score(dealers_card) > calc_score(dealers_card):
                    final_hand()
                    print("Opponent {HOUSE} wins !")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) > 21:
                    print("BUST for BOTH")
                    break
            else:
                if calc_score(dealers_card) == calc_score(users_card):
                    final_hand()
                    print("PUSH, tie")
                    break
                elif calc_score(users_card) > 21:
                    if "A" in users_card:
                        the_user_scores = calc_score(users_card) - 11 + 1
                        if the_user_scores > 21:
                            final_hand()
                            print("You went BUST!. Opponent wins.")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(dealers_card) > 21:
                    if "A" in dealers_card:
                        the_dealer_score = calc_score(users_card) - 11 + 1
                        if the_dealer_score > 21:
                            final_hand()
                            print("Opponent went BUST! You win")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(users_card) > 21 and calc_score(dealers_card) <= 21:
                    final_hand()
                    print("You went BUST!. Opponent wins.")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) <= 21:
                    final_hand()
                    print("Opponent went BUST!. You win !!")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) > 21:
                    print("BUST for BOTH")
                    break

        elif another_card == "n" or another_card[0] == "n":
            comp_hand()
            if calc_score(users_card) < 17 and calc_score(dealers_card) < 17:
                if calc_score(dealers_card) == calc_score(users_card):
                    final_hand()
                    print("PUSH, tie")
                    break
                elif calc_score(users_card) > 21:
                    if "A" in users_card:
                        the_user_scores = calc_score(users_card) - 10
                        if the_user_scores > 21:
                            final_hand()
                            print("You went BUST!. Opponent wins.")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(dealers_card) > 21:
                    if "A" in dealers_card:
                        the_dealer_score = calc_score(users_card) - 10
                        if the_dealer_score > 21:
                            final_hand()
                            print("Opponent went BUST ! You win")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(users_card) > 21 and calc_score(dealers_card) <= 21:
                    final_hand()
                    print("You went BUST!. Opponent wins.")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) <= 21:
                    final_hand()
                    print("Opponent went BUST!. You win !!")
                    break
                elif calc_score(users_card) <= 21 and calc_score(users_card) > calc_score(dealers_card):
                    final_hand()
                    print("You win!")
                    break
                elif calc_score(dealers_card) <= 21 and calc_score(dealers_card) > calc_score(dealers_card):
                    final_hand()
                    print("Opponent {HOUSE} wins !")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) > 21:
                    print("BUST for BOTH")
                    break
            else:
                if calc_score(dealers_card) == calc_score(users_card):
                    final_hand()
                    print("PUSH, tie")
                    break
                elif calc_score(users_card) > 21:
                    if "A" in users_card:
                        the_user_scores = calc_score(users_card) - 10
                        if the_user_scores > 21:
                            final_hand()
                            print("You went BUST!. Opponent wins.")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(dealers_card) > 21:
                    if "A" in dealers_card:
                        the_dealer_score = calc_score(users_card) - 10
                        if the_dealer_score > 21:
                            final_hand()
                            print("Opponent went BUST ! You win")
                            break
                        elif the_user_scores < 21:
                            other_card()
                elif calc_score(users_card) > 21 and calc_score(dealers_card) <= 21:
                    final_hand()
                    print("You went BUST!. Opponent wins.")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) <= 21:
                    final_hand()
                    print("Opponent went BUST!. You win !!")
                    break
                elif calc_score(users_card) <= 21 and calc_score(users_card) > calc_score(dealers_card):
                    final_hand()
                    print("You win!")
                    break
                elif calc_score(dealers_card) <= 21 and calc_score(dealers_card) > calc_score(dealers_card):
                    final_hand()
                    print("Opponent {HOUSE} wins !")
                    break
                elif calc_score(dealers_card) > 21 and calc_score(users_card) > 21:
                    print("BUST for BOTH")
                    break

while True:
    users_card = []
    dealers_card = []
    user_choice_play_game = input(
        "\nWould you like to BlackJack ? type 'y' for yes and 'n' for no: ").lower()
    if user_choice_play_game == "y" or user_choice_play_game[0] == "y":
        print(LOGO)
        first_hit()
        if (users_card[0] == "K" and users_card[1] == "A") or (users_card[0] == "A" and users_card[1] == "K"):
            if (dealers_card[0] == "K" and dealers_card[-1] == "A") or (dealers_card[0] == "A" and dealers_card[1] == "K"):
                print("BLACKJACK !!! Dealer Wins !")
                break
            else:
                print("BLACKJACK !!! You Win !")
                break
        elif (dealers_card[0] == "K" and dealers_card[1] == "A") or (dealers_card[0] == "A" and dealers_card[1] == "K"):
            print("BLACKJACK !!! Dealer Wins !")
            break

        cards_at_the_moment()
        other_card()
    else:
        break
