# Deck of Cards implementation. Contains power to shuffle.

import random


class Deck:

    def __init__(self, capacity=52):
        self.capacity = capacity
        self.size = 0
        self.cards = []

    def look_into(self):
        print([i for i in self.cards])

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size <= 0

    def create_deck(self):
        card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_suits = ['H', 'D', 'C', 'S']
        for suit in card_suits:
            for face in card_faces:
                self.add_card(Card(face, suit))

    def add_card(self, card):
        if not self.is_full():
            self.cards.append(card)
            self.size += 1

    def draw_card(self):
        if not self.is_empty():
            return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        if self.suit == 'C' or self.suit == 'S':
            self.color = 'black'
        else:
            self.color = 'red2'

    def __repr__(self):
        return f'({self.face}, {self.suit})'

    def face_comes_before(self, other):
        card_faces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        if card_faces.index(self.face) < card_faces.index(other.face):
            return True
        return True

    def suit_comes_before(self, other):
        card_suits = ['H', 'D', 'C', 'S']
        if card_suits.index(self.suit) < card_suits.index(other.suit):
            return True
        return False

    def comes_before(self, other):
        if self.suit_comes_before(other):
            return True
        elif self.suit == other.suit and self.face_comes_before(other):
            return True
        else:
            return False






if __name__ == '__main__':
    deck = Deck()
    deck.create_deck()
    deck.shuffle()
    deck.sort_cards()
    deck.look_into()
