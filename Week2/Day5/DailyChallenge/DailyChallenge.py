# Daily Challenge: OOP Quizz
# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?

# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

# Part 1: Quizz

# 1. A class is a blueprint for creating objects in object-oriented programming. It defines a set of attributes and methods that the objects created from the class will have.

# 2. An instance is a specific object created from a class. It represents a single occurrence of the class and has its own unique attributes and methods.

# 3. Encapsulation is the concept of bundling the data (attributes) and methods that operate on the data into a single unit, i.e., a class. It helps in hiding the internal details of the class and only exposing what is necessary.

# 4. Abstraction is the process of simplifying complex systems by modeling classes based on the essential properties and behaviors they possess. It involves focusing on the relevant features and ignoring unnecessary details.

# 5. Inheritance is a mechanism in object-oriented programming that allows a new class (subclass/derived class) to inherit the properties and behaviors of an existing class (superclass/base class). It promotes code reuse and establishes a relationship between classes.

# 6. Multiple inheritance is a feature in some object-oriented programming languages that allows a class to inherit properties and behaviors from more than one parent class. It introduces complexity and potential conflicts but can be useful in certain situations.

# 7. Polymorphism allows objects of different types to be treated as objects of a common type. It enables a single interface to be used for different types of objects, providing flexibility and extensibility in code design.

# 8. Method Resolution Order (MRO) is the order in which the base classes are searched when looking for a method in a class hierarchy. It defines the sequence in which the base classes are traversed to resolve method calls in the context of multiple inheritance.

import random
from enum import Enum

class Card:
    class Suit(Enum):
        Hearts = 'Hearts'
        Diamonds = 'Diamonds'
        Clubs = 'Clubs'
        Spades = 'Spades'

    class Value(Enum):
        A = 'A'
        _2 = '2'
        _3 = '3'
        _4 = '4'
        _5 = '5'
        _6 = '6'
        _7 = '7'
        _8 = '8'
        _9 = '9'
        _10 = '10'
        J = 'J'
        Q = 'Q'
        K = 'K'

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.Suit for value in Card.Value]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            print("No cards left in the deck.")
            return None
        return self.cards.pop()

deck = Deck()
deck.shuffle()

for _ in range(5):
    card = deck.deal()
    if card:
        print(f"Dealt card: {card.value.value} of {card.suit.value}")
