# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:50:22 2018

@author: admin
"""
import tile

board = [
        tile.Tile("GO"),
        tile.Property("Mediterranean Avenue", 60, 2),
        tile.Tile("Community Chest"),
        tile.Property("Baltic Avenue",60, 8),
        tile.Tile("Income Tax"),
        tile.Property("Reading Railroad", 200, 50),
        tile.Property("Oriental Avenue", 100, 6),
        tile.Tile("Chance"),
        tile.Property("Vermont Avenue", 100, 6),
        tile.Property("Connecticut Avenue", 120, 8),
        tile.Tile("Jail"),
        tile.Property("St. Charles Place", 140, 10),
        tile.Property("Electric Company", 150, 0, is_utility=True),
        tile.Property("States Avenue", 140, 10),
        tile.Property("Virginia Avenue", 160, 12),
        tile.Property("Pennsylvania Railroad", 200, 50),
        tile.Property("St. James Place", 180, 14),
        tile.Tile("Community Chest"),
        tile.Property("Tennessee Avenue", 180, 14),
        tile.Property("New York Avenue", 200, 16),
        tile.Tile("Free Parking"),
        tile.Property("Kentucky Avenue", 220, 18),
        tile.Tile("Chance"),
        tile.Property("Indiana Avenue", 220, 18),
        tile.Property("Illinois Avenue", 240, 20),
        tile.Property("B. & O. Railroad", 200, 50),
        tile.Property("Atlantic Avenue", 260, 22),
        tile.Property("Ventnor Avenue", 260, 22),
        tile.Property("Water Works", 150, 0, is_utility=True),
        tile.Property("Marvin Gardens", 280, 24),
        tile.Tile("Go To Jail"),
        tile.Property("Pacific Avenue", 300, 26),
        tile.Property("North Caroliina Avenue", 300, 26),
        tile.Tile("Community Chest"),
        tile.Property("Pennsylvania Avenue", 320, 28),
        tile.Property("Short Line", 200, 50),
        tile.Tile("Chance"),
        tile.Property("Park Place", 350, 35),
        tile.Tile("Luxury Tax"),
        tile.Property("Boardwalk", 400, 50)]