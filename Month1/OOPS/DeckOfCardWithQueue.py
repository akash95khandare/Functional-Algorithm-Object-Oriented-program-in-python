from OOPS.DeckOfCard import DeckOfCard
from util.Queue import Queue


class DeckOfCardWithQueue:
    def __init__(self):
        self.deck_of_card = DeckOfCard()
        self.player = Queue()
        self.player1 = Queue()
        self.player2 = Queue()
        self.player3 = Queue()
        self.player4 = Queue()

    def sort_deck_of_card(self,player):
        suit = self.deck_of_card.suit
        for i in range(4):
            player[suit[i]]


    def deck_of_card_with_queue(self):
        self.deck_of_card.deck_of_card()
        self.deck_of_card.deck_of_card_assign_to_players()
        for i in range(4):



