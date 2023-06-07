"""Classes used throughout project. Mostly player or NPC data."""

import random
import time

class Player():
    "Information about the player character, their stats, and their abilities."
    
    def __init__(self):
        
        self.name = "?"
        
        self.str = 0
        self.vit = 0
        self.agi = 0
        self.int = 0
        self.luk = 0
                      
    
class Zombie():
    "A considerably weak enemy."
    
    noise = "Grah!"
    
    def __init__(self):
        
        self.name = 'Zombie'
        
        self.str = 3
        self.vit = 7
        self.agi = 2
        self.int = 2
        self.luk = 2
        
        self.phrases = ("Grar!",
                        "Blargh.",
                        "Bleh.",
                        "Grrah!",
                        "Grr.")
        
        
class Goblin():
    "A considerably fast enemy."
    
    noise = "Grah!"
    
    def __init__(self):
        
        self.name = 'Goblin'
        
        self.str = 3
        self.vit = 3
        self.agi = 7
        self.int = 6
        self.luk = 4
        
        self.phrases = ("Raah!",
                        "Hee hee har.",
                        "*sneezes*",
                        "Haa!",
                        "Hee hee haw.")
        
        
class Giant():
    "A considerably large enemy."
    
    noise = "Grah!"
    
    def __init__(self):
        
        self.name = 'Giant'
        
        self.str = 8
        self.vit = 10
        self.agi = 1
        self.int = 2
        self.luk = 2
        
        self.phrases = ("Brr.",
                        "Guh.",
                        "Muuhh.",
                        "Bluhh.",
                        "Hmm.")
        
        
class Antihero():
    "A considerably scary enemy!"
    
    noise = "Grah!"
    
    def __init__(self):
        
        self.name = 'Antihero'
        
        self.str = 7
        self.vit = 7
        self.agi = 7
        self.int = 7
        self.luk = 5
        
        self.phrases = ("Haha!",
                        "Grah!",
                        "Hmph.",
                        "Grr.",
                        "Ha!")


class Abilities():
    "A list of available abilities. Unused."
    
    def __init__(self):
        self.count = 0