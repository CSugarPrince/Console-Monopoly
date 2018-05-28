# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:55:21 2018

@author: Joshua Hew
"""
# TODO: Test player in jail functions
# TODO: Code end_player_turn function
# TODO: Add better logging, figure out which information to log
# TODO: Code chance and community chest tiles
# TODO: Code owned property menu/ options


import menu_system as ms
import board
import dice
import player

import logging

logging.basicConfig(filename='game_log.log', filemode='w', level=logging.DEBUG,
                    format='%(levelname)s:%(msg)s')
    
class Game(object):
    """ Controls logic of game."""
    
    def __init__(self):
                
        self.MAX_NUM_PLAYERS = 4                            # Maximum number of players allowed
        self.player_list = []                               # Players in game
        self.current_player = None                          # Current player/ player turn
        self.turn_counter = 0                               # Number of turns Game has cycled through
        self.dice = dice.Dice()                             # Game dice    
        
        
        # Test logging 
        logging.debug('Game Created')  
        logging.info('Hello Log')
        
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
        """ Monopoly consists of turns. Each turn a player can choose to do something """
        
        # Increment game's turn counter
        self.turn_counter += 1                  
        
        if player.is_in_jail:
            # Default jail sentence time is 3 turns
            did_his_time = player.num_turns_in_jail == 3
            
            if did_his_time:
                # Move player from in_jail to 'just visiting'
                player.get_out_of_jail()
                
                print("{} has served his sentence. {} is now out of jail.".format(player.name, 
                      player.name))
                logging.info("{} is out of jail.".format(player.name))
                
            else:
                #increment current_player.num_turns_in_jail
                player.num_turns_in_jail += 1
                
                print("{} is serving jail sentence {} of 3.".format(player.name, 
                      player.num_turns_in_jail))
                
                while player.is_in_jail:
                    # Display in_jail_menu
                    print("\n\t\t\tPlayer in Jail Menu: ")
                    ms.display_menu(ms.player_in_jail_menu)
            
                    # Collect user input. Menu option selection
                    selection = input("Select an option by typing a number: ")
                    
                    # Select option
                    if selection == '1': # 1. Roll Dice. Try to get doubles
                        self.dice.roll()
                        
                        # If rolled doubles, player gets out of jail
                        if self.dice.rolled_doubles:
                            player.get_out_of_jail()
                            
                        else:
                            # If player doesn't roll doubles, continue player turn cycle
                            break
                        
                        # Reset dice for next use
                        self.dice.reset()
                    
                    elif selection == '2': # 2. Use Get Out of Jail Free Card
                        player.get_out_of_jail_free_card()
                        
                        # If player got out of jail, break out of in-jail-menu
                        if player.is_in_jail == False:
                            break
                        
                        # If player did not have card, start loop over 
                        else:
                            continue
                        
                    elif selection == '3': # 3. Tough it out 
                        print("{} chose to tough it out.".format(player.name))
                        logging.info("{} chose to tough it out.".format(player.name))  
                        
                        break
                            
                    else:
                       print("Unknown option selected!")
                       
        
        elif player.is_bankrupt: 
            # Remove player from game
            self.player_list.remove(player)
            
        else: # If player is neither bankrupt nor in jail
            while True:
                # Display player menu
                print("\n\t\t\tPlayer Menu:")
                ms.display_menu(ms.player_menu)
                
                # Collect user input
                selection = input("Select an option by typing a number: ")
                
                # Choose option based on user input
                if selection == '1': # Roll Dice. Move player
                   
                    # Roll dice
                    move_amount = self.dice.roll()
                    
                    # If player has rolled three doubles, go to jail
                    if self.dice.doubles_counter == 3:
                        player.go_to_jail()
                    
                    else:    
                        # Pass dice roll value to player's movement function
                        player.move(move_amount)
                    
                    # If player got sent to jail after moving, break out of player options
                    if player.is_in_jail == False and self.dice.rolled_doubles:
                        # PLayer gets to go again
                        continue
                    
                    # Break out of player menu
                    break
                               
                    
                elif selection == '2':
                    player.display_owned_properties()
                    
                    # Break out of player menu
                    break
                    
                else:
                   print("Unknown option selected!")
    
    def end_player_turn(self, player):
        
        self.turn_counter += 1
    
    def main(self):
        
        self.round_counter = 1
        
        while True:
            print("Round {}".format(self.turn_counter))
            logging.info("Round {}".format(self.turn_counter))
            
            self.start_player_turn(self.current_player)
            self.end_player_turn(self.current_player)
        
        
    
if __name__ == "__main__":    
    
    Game()
    
    
       
    
        
   
        
    
    
        
    











