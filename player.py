# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:25:14 2018

@author: admin
"""

# Import game to get access to board
import board as bd

import logging

class Player(object):
    """ Player class. """
        
    def __init__(self, name):
        
            self.name = name                            # The player's name
            self.position = 0                           # Position on Board
            self.current_tile = None                    # Player starts on GO 
            self.is_in_jail = True                      # Jail status
            self.num_turns_in_jail = 0                  # Number of turns player has been in jail
            self.owned_properties = []                  # List of player's owned properties
            self.balance = 1500                         # Amount of money
            self.is_bankrupt = False                    # Loss condition
            self.has_get_out_jail_free_card = False     # Get out jail free card
            
            print( "{} has been succesfully added!".format(self.name))   
            logging.info("Player {} created.".format(self.name))
              
    def move(self, move_amount): # should a method from one class depend on a data attribute from another class?
        """ Moves payer to new tile on board, triggers new tile's event. """
        
        # Update player's position on tile                                      
        self.position += move_amount
        
        # If player passes go:
        if self.position >= 40:
            self.position -= 40        
            self.current_tile = bd.board[self.position]
            self.balance += 200                                     # Pass Go. Collect 200
            
            print("You passed GO! Collect 200!")  
            logging.info("Player {} passed GO. Collected 200.".format(self.name))
                  
        else:
            # Update player's current tile
            self.current_tile = bd.board[self.position]
                    
        print("Your current tile is now", self.current_tile.name) 
        logging.info("Player {} is now on tile {}: position {}".format(self.name, 
                     self.current_tile.name, self.position))
        
        # Triggers the event of the tile the player landed on
        self.current_tile.trigger_event(self)
    
    def display_owned_properties(self):
        """ Prints the players owned properties to the console. """
        
        print("{}'s Properties: ".format(self.name))
        for p in self.owned_properties:
            print(p.name)
    
    def display_balance(self):
        """ Prints player's amount of money to console. """
        
        print("{}'s current balance is {}".format(self.name, self.balance))
        
    def get_out_of_jail(self):
        """ Moves player out of jail and into "just visiting" """
        
        self.is_in_jail = False
        self.position = 10
        self.current_tile = bd.board[self.position]
        
    def get_out_of_jail_free_card(self):
        """ Uses 'get out of jail free card' if has one. """
        
        if self.has_get_out_jail_free_card:
            self.get_out_of_jail()
            
            # Consume card use
            self.has_get_out_jail_free_card = False
            
            logging.info("Player {} has used a 'get out of jail free card'".format(self.name))
            
        else:
            print("You do not have a 'get out jail free card'")
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    