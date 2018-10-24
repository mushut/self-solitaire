# Deck class

import card
import random

class deck(object):
    def __init__(self):
        self.cards = []

        for i in range(1,14):
            # cards with suite diamond
            diamond = card.card(i, "diamond")

            # cards with suite club
            club = card.card(i, "club")

            # cards with suite heart
            heart = card.card(i, "heart")

            # cards with suite spade
            spade = card.card(i, "spade")

            self.cards.append(diamond)
            self.cards.append(club)
            self.cards.append(heart)
            self.cards.append(spade)

    def shuffle_deck(self):
        self.deck = []
        temp_cards = self.cards

        for i in range(52):
            index = random.randint(0,51-i)
            self.deck.append(temp_cards[index])
            temp_cards.remove(temp_cards[index])
