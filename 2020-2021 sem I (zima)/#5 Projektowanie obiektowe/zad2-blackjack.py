# Created by Marcin "Cozoob" Kozub 20.09.2021
from random import randint
from time import sleep


class Human:

    def __init__(self, name, money, cards=None):
        self.name = name
        self.money = money
        self.cards = cards

    def __str__(self):
        return f"{self.name}"

    # take another card
    def hit(self, arr):
        res = arr[randint(0, 12)]
        card = Card(res[0], res[1])
        self.cards.append(card)

    def get_points(self):
        is_ace = False
        points = 0
        for card in self.cards:
            if card.name == "Ace":
                is_ace = True
            else:
                points += card.value

        if not is_ace:
            return points

        if abs(points + 1 - 21) < abs(points + 11 - 21):
            return points + 1
        return points + 11


class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if self.name == "Ace":
            return f"{self.name} which worths 1 or 11."

        return f"{self.name} which worths {self.value}."


def show_the_instructions():
    print("""Blackjack to popularna kasynowa gra karciana, w której celem \n\
gracza jest pokonanie krupiera poprzez uzyskanie sumy 21 punktów w kartach,\n\
nie przekraczając jednak 21. Punktacja kart jest następująca:\n\
●	Karty od dwójki do dziesiątki mają wartość równą numerowi karty.\n\
●	Walet, Dama i Król mają wartość równą 10 punktów.\n\
●	As ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.\n\
Na początku gry gracz i krupier dostają po dwie karty.\n\
Obydwie karty gracza są odkryte,\n\
natomiast tylko jedna karta krupiera jest pokazana graczowi.\n\
Gracz teraz może podjąć decyzje o swoim następnym ruchu. Gracz ma następujące możliwości:\n\
●	Dobrać kartę (hit).\n\
●	Nie dobierać kart (stand).\n\
Jeżeli gracz po dobraniu kart ma więcej niż 21 punktów, przegrywa zakład i krupier zabiera jego żetony.\n\
Jeżeli natomiast gracz ma 21 punktów lub mniej, krupier odkrywa swoją zakrytą kartę i w zależności od liczby\n\
jego punktów może dobrać więcej kart. Krupier musi grać według następujących przepisów: wziąć kartę,\n\
jeżeli ma 16 punktów lub mniej i nie brać więcej kart, gdy ma 17 punktów lub więcej (niezależnie, ile punktów ma gracz).\n\
Wygrywa ten, który ma sumę punktów bliższą lub równą 21.""")


if __name__ == '__main__':
    cards = [['Ace', -1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10],
             ['Jack', 10], ['Queen', 10], ['King', 10]]


    print("The blackjack game!")
    print("Made by Marcin \"Cozoob\" Kozub.")
    print("Hello there!")
    player_name = input("Please write your name:\n")

    print("Do you want instructions in polish?(y/n)")
    tutorial = input()
    while not (tutorial == "y" or tutorial == "n"):
        print("Please write \"y\" or \"n\"!")
        print("Do you want instructions in polish?(y/n)")
        tutorial = input()
    if tutorial == "y":
        show_the_instructions()
        print("\n")
        print("Press Enter to continue:")
        is_enter = input()
        while not is_enter == "":
            is_enter = input()

    end = False
    while not end:
        # randomise two cards for the Dealer and the player
        dealer = Human("Dealer", 100, [])
        player = Human(player_name, 100, [])
        for _ in range(2):
            dealer.hit(cards)
            player.hit(cards)

        # show only one card of the Dealer
        print("Dealer's cards:")
        print(dealer.cards[0])
        print("The second card is unknown.")
        print("\n")

        # show the player's cards
        print("Your cards:")
        print(player.cards[0])
        print(player.cards[1])
        print("The sum: ", player.get_points())
        print("\n")

        # show the options for the player
        print("What do you want to do next?(stand/hit)")
        what_now = input()
        while not (what_now == "stand" or what_now == "hit"):
            print("Please write \"stand\" or \"hit\".")
            print("What do you want to do next?(stand/hit)")
            what_now = input()

        if what_now == "hit":
            # randomise one card for the player
            player.hit(cards)

        if player.get_points() > 21:
            for card in player.cards:
                print(card)
            print()
            print(f"You have lost {player.name}! You've got {player.get_points()} which is more than 21!")
            print("\n")
        else:
            while dealer.get_points() < 17:
                dealer.hit(cards)

            player_points = player.get_points()
            dealer_points = dealer.get_points()
            if abs(player_points - 21) < abs(dealer_points - 21):
                # the player wins
                print(f"Congratulations {player.name}! You've won! You've got {player_points} points and the Dealer has {dealer_points} points.")
                print("\n")
            elif abs(player_points - 21) == abs(dealer_points - 21):
                print(f"Oh Mammamia! There's a draw! You two have {player_points} points!!")
            else:
                print(f"You have lost {player.name}! You've got {player_points} points and the Dealer has {dealer_points} points.")
                print("\n")


        print("Do you want to play again?(y/n)")
        answer = input()
        while not (answer == "y" or answer == "n"):
            print("Please write \"y\" or \"n\"!")
            print("Do you want to play again?(y/n)")
            answer = input()
        if answer == 'n':
            end = True

    print("Thanks for playing! Let me know if you like it.")
    print("Made by Marcin \"Cozoob\" Kozub")
    print("The game will be closed in 5 seconds.")
    sleep(5)
    exit()