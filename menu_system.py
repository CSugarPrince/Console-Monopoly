# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:41:27 2018

@author: admin
"""

""" Code 'Library' for menus that will show up in the game """
# TODO: Create "player_in_jail_menu".

# Game menu: setup
setup_menu = {}
setup_menu['1'] = "Add Player." 
setup_menu['2'] = "Start Game."

# Player menu: default
player_menu = {}
player_menu['1'] = "Roll Dice."
player_menu['2'] = "Display Owned Properties."

# Player menu: in jail
player_in_jail_menu = {}
player_in_jail_menu['1'] = "Roll Dice."
player_in_jail_menu['2'] = "Use Get Out of Jail Free Card."
player_in_jail_menu['3'] = "Tough it Out."

# Tile menu: unowned property
unowned_property_menu = {}
unowned_property_menu['1'] = "Buy Property"
unowned_property_menu['2'] = "Do Not Buy Property"

def display_menu(menu: dict):
        for option in menu:
            print("\t\t\t{}. {}".format(option, menu[option]))