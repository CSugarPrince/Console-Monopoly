# -*- coding: utf-8 -*-
"""
Created on Thu May 24 13:54:54 2018

@author: admin
"""
import menu_system as ms

class Tile(object):
    """
        The Board is made up of individual tiles: properties, chance, community
        chest, free parking, income tax, jail, and GO
    """
    
    def __init__(self, name):
        self.name = name
        
    def trigger_event(self, player):
        print("Triggered Default Tile Event")

class Property(Tile):
    """ The property tiles are any tiles that can be bought  """
    
    def __init__(self, name, price, base_rent, is_utility=False, is_rr=False):
        """ Creates a a Property Tile 
        Param:
            name: string
            price: int
            base_rent = int
        """
        
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner=None
        
        if(is_utility):
            self.is_utility = True
        if(is_rr):
            self.is_rr = True
    
    def trigger_event(self, player):
        if self.owner is None:
            print("You landed on an unowned property")
            
            while True:
                print("\n\t\t\t", "Unowned Property Menu", sep="")    
                ms.display_menu(ms.unowned_property_menu)
                selection = input("Select an option by typing a number: ")
                if selection == '1':
                    # Buy Property
                    if player.balance >= self.price:
                        player.owned_properties.append(self)
                        player.balance -= self.price 
                        print("Congratulations! {} has successfully bought {} for the price of {}".format(player.name, 
                               self.name, self.price))
                        # Display player's balance after puchase
                        player.display_balance()
                    else:
                        print("Your balance of {} is insufficient to buy {} at the price of".format( player.balance,
                               self.name, self.price))
                        
                    break    
                elif selection == '2':
                    # Player chooses not to buy the property
                    print("You chose not to buy {}.".format(self.name))
                    break
                else:
                   print("Unknown option selected!")
    
    def view_property(self):
        print(self.name)    
        
        
class Chance(Tile):
    
    chance_card_stack = None
    
    def __init__(self, name):
        
        self.name = name                        # Name should be Chance
        
        # Creates a stack of Chance cards that all Chance Tiles can pull from
        if Chance.chance_card_stack is None:
            # Create chance card stack
        
        
    def trigger_event(self, player):
        
        print("You triggered the chance tile!")
        
        
        
        
        
        
        
