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
        
    
    def roll(self):
        roll_1 = randint(1,6)               # Rolls first dye
        roll_2 = randint(1,6)               # Rolls second dye
        total_roll = roll_1 + roll_2
        
        if roll_1 == roll_2:
            self.rolled_doubles = True
            
        return total_roll    
    