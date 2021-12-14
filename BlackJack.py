#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:45:48 2021

@author: austinlanglinais
"""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
gameon = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()      
    
    
class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = []
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def sum_total(self):
        sum = 0
        for i in self.all_cards:
            sum = sum + i.value
        return sum
    
    
    def __str__(self):
        return f"{self.name} is displaying {self.all_cards[0]}"
           
#Setup game
def play_game(bank):
    game_deck = Deck()
    game_deck.shuffle()
    p1 = Player("P1")
    dealer = Player("Dealer")

    #deal games
    p1.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())
    p1.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())
    
    gamble = int(input(f"You currently have ${bank}, how much would you like to bet?: "))
    bank = bank - gamble
    
    if dealer.sum_total() == 21:
        print("You lost, the dealer had BlackJack!")
        return bank
     
    print(" ")
    print(p1)
    print(f"and {p1.all_cards[1]}")
    print(f"Your total is {p1.sum_total()}")
    print(" ")
    print(dealer)
    
    if p1.all_cards[0].value == 11:
        print (f"You have an ace, your total is {p1.sum_total()}. Would you like it to be one[1] or eleven?[11]\n")
        ace_decision = int(input("What will it be?: "))
        if ace_decision == 1:
            p1.all_cards[0].value = 1
    else:
        pass
    
    if p1.all_cards[1].value == 11:
        print (f"You have an ace, your total is {p1.sum_total()}. Would you like it to be one[1] or eleven?[11]\n")
        ace_decision = int(input("What will it be?: "))
        if ace_decision == 1:
            p1.all_cards[1].value = 1
    else:
        pass

    
    decision = input("Hit[H] or Stay[S]?: ")
    if decision.lower() == "h":
        answer = "Y"
        while answer == "Y":
            p1.add_cards(game_deck.deal_one())
            print(f"Your total is now {p1.sum_total()}")
            if p1.sum_total() > 21:
                print("Busted! You lose!")
                print(f"You now have ${bank} left.")
                return bank
            else:
                answer = input("Hit again? [Y] or [N]: ")
                
 
    while dealer.sum_total() < 16:
        dealer.add_cards(game_deck.deal_one())
    
    if p1.sum_total() > 21:
        print ("")
    elif dealer.sum_total() > 21:
        print("The dealer busted, you win!")
        bank = bank + (2*gamble)
        print(f"You now have ${bank} left")
        return bank

    elif dealer.sum_total() >= p1.sum_total() or p1.sum_total() > 21:
        print (f"You have {p1.sum_total()} and the dealer has {dealer.sum_total()}. You lose.")
        print(f"You now have ${bank} left")
        return bank
        
    else:
        print (f"You have {p1.sum_total()} and the dealer has {dealer.sum_total()}. You win.")
        bank = bank + (2*gamble)
        print(f"You now have ${bank} left")
        return bank
    

amount = 100
start = "y"
while start == "y":
    start = input("Hello. Would you like to play BlackJack?: [Y] or [N]: ")
    if start == "n":
        print(f"You left the casino with ${amount}.")
        break
    amount = play_game(amount)



# =============================================================================
# print(p1.sum_total())
# print(dealer.sum_total())
# 
# print(p1.all_cards[1])
# print(dealer.all_cards[1])
# 
# =============================================================================

    










    