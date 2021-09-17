# Created by Marcin "Cozoob" Kozub 17.09.2021

class Card:

    def __init__(self, name, color, flavor_text = None, ability = None, cost = 0):
        self.name = name
        self.color = color
        self.kind = "None"
        self.flavor_text = flavor_text
        self.ability = ability
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.color})\n{self.kind}\nAbility - {self.ability}\nFlavor text - {self.flavor_text}\nCost - {self.cost}"


class Creature(Card):

    def __init__(self, name, color, flavor_text, ability, cost):
        super(Creature, self).__init__(name, color, flavor_text, ability, cost)
        self.kind = "Creature"

    def power(self):
        pass

    def toughness(self):
        pass


class Land(Card):

    def __init__(self, name, color, flavor_text, ability, cost):
        super(Land, self).__init__(name, color, flavor_text, ability, cost)
        self.kind = "Land"

    def give_mana(self):
        pass


class Instant(Card):

    def __init__(self, name, color, flavor_text, ability, cost):
        super(Instant, self).__init__(name, color, flavor_text, ability, cost)
        self.kind = "Instant"

    def attack_opponent(self):
        pass


class Hand:

    def __init__(self, cards = None):
        self.cards = cards

    def add_a_card(self, card):
        self.cards.append(card)

    def remove_a_card(self, card):
        self.cards.remove(card)

    def how_many_cards(self):
        return len(self.cards)

    # above but in the different way
    def __len__(self):
        return len(self.cards)

    def is_name(self, name):
        return name in self.cards.name

    # above but in the different way
    def __contains__(self, item):
        return item in self.cards

    # If kind is None this means we show all the cards in the hand
    def show_me_cards(self, kind = None):
        if kind is None:
            for card in self.cards:
                print(card)
                print()
        else:
            for card in self.cards:
                if card.kind is kind:
                    print(card)
                    print()


if __name__ == '__main__':
    A = Creature("A cow", "black", None, None, 34)
    print(A)