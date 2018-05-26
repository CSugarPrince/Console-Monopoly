# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:19:15 2018

@author: admin
"""
from random import randint

class Dice(object):
    """ Two six sided dye """
    
    def __init__(self):
        
        self.rolled_doubles = False
        self.doubles_counter = 0
        
    
    def roll(self):
        """ Rolls dice. Returns an integer 1- 12. Checks for doubles. """
        
        roll_1 = randint(1,6)               # Rolls first dye
        roll_2 = randint(1,6)               # Rolls second dye
        total_roll = roll_1 + roll_2
        
        print("Rolled a {} and a {}.".format(roll_1,roll_2))
        
        # If doubles
        if roll_1 == roll_2:
            self.rolled_doubles = True
            self.doubles_counter += 1
        
        # Safeguard.
        else:
            self.rolled_doubles = False
            self.doubles_counter = 0
            
        return total_roll   
    
    def reset(self):
        """ Resets dice for next use. """
        
        self.rolled_doubles = False
        self.doubles_counter = 0
    