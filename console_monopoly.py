# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:55:21 2018

@author: Joshua Hew
"""
import menu_system as ms
import board
import dice
import player


    
class Game(object):
    """ Controls logic of game."""
    
    def __init__(self):
                
        self.MAX_NUM_PLAYERS = 4                            # Maximum number of players allowed
        self.player_list = []                               # Players in game
        self.current_player = None                          # Current player/ player turn
        self.turn_counter = None                            # Number of turns Game has cycled through
        self.dice = dice.Dice()                             # Game dice    
        
        
        # Setup Game        
        print("Welcome to Console Monopoly!")
        self.change_game_settings()        
        
        # The first player created gets the first turn
        self.current_player = self.player_list[0]    
        
        # Start the main game loop
        self.main()                                     
    
    def change_game_settings(self):
        """ Called by Game.init in order to setup game """
        
        while True:
            # Display Game's Setup Menu: 1. Add Player. 2. Start Game
            print("\n\t\t\tSetup Menu: ")
            ms.display_menu(ms.setup_menu)
            
            # Collect user input. Menu option selection
            selection = input("Select an option by typing a number: ")
            
            # Choose option based on user input
            num_players = len(self.player_list)          # Current amount of players in game
            if selection == '1': # Adds a Player to the game
                if  num_players < self.MAX_NUM_PLAYERS:   
                    player_name = input("Please enter player name: ")
                    self.player_list.append(player.Player(player_name))
                else:
                    print("Error: Cannot have more than {} players!".format( self.MAX_NUM_PLAYERS)) #DEBUG
            
            elif selection == '2': # Starts Game. There must be at least 1 player
                if num_players > 0:
                    break
                else:
                    print("Error: Cannot start game without players")
            else:
               print("Unknown option selected!")
        
    def start_player_turn(self, player):
        if player.is_in_jail:
            did_his_time = player.num_turns_in_jail == 3
            if did_his_time:
                player.get_out_of_jail()
            else:
                print("Haven't coded this bit yet!")
                #TODO:
                #increment current_player.num_turns_in_jail
                #display in_jail_menu
                #code logic for menu selections
        elif True==False: #if player is bankrupt/ has lost
            pass
        else:
            while True:
                # Display player menu
                print("\n\t\t\tPlayer Menu:")
                ms.display_menu(ms.player_menu)
                
                # Collect user input
                selection = input("Select an option by typing a number: ")
                
                # Choose option based on user input
                if selection == '1': # Roll Dice. Move player
                    move_amount = self.dice.roll()
                    player.move(move_amount)
                elif selection == '2':
                    # TODO:
                    print("TODO: Code diplay owned properties function")
                else:
                   print("Unknown option selected!")
    
    def end_player_turn(self, player):
        pass
    
    def main(self):
        while True:
            self.start_player_turn(self.current_player)
            self.end_player_turn(self.current_player)
        
        
    
if __name__ == "__main__":    
    Game()
    
    
       
    
        
   
        
    
    
        
    











