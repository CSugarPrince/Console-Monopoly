# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:25:14 2018

@author: admin
"""

# Import game to get access to board
import board as bd

class Player(object):
    """ Player class """
        
    def __init__(self, name):
        
            self.name = name                # The player's name
            self.position = 0               # Position on Board
            self.current_tile = None        # Player starts on GO 
            self.is_in_jail = False         # Jail status
            self.num_turns_in_jail = 0     # Number of turns player has been in jail
            self.owned_properties = []      # List of player's owned properties
            self.balance = 1500             # Amount of money
            
            print(self.name, "has been succesfully added!") #DEBUG            
              
    def move(self, move_amount): # should a method from one class depend on a data attribute from another class?
        """ Moves payer to new tile on board, triggers new tile's event """
                                              
        self.position += move_amount
        
        if self.position >= 40:
            self.position -= 40        
            self.current_tile = bd.board[self.position]
            self.balance += 200                                     # Pass Go. Collect 200
            print("You passed GO! Collect 200!")                    # DEBUG
        else:
            self.current_tile = bd.board[self.position]
                    
        print("Your current tile is now", self.current_tile.name)   # DEBUG
        
        # trigger_event
        self.current_tile.trigger_event(self)
    
    def display_owned_properties(self):
        """ prints the players owned properties to the console"""
        
        print("{}'s Properties: ".format(self.name))
        for p in self.owned_properties:
            print(p.name)
    
    def display_balance(self):
        """ prints player's amount of money to console"""
        
        print("{}'s current balance is {}".format(self.name, self.balance))
        
    def get_out_of_jail(self):
        pass