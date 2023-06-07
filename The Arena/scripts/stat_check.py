"""Script to calculate certain stat for a player or NPC object."""

# GOES UP ONE FILE!
import sys
sys.path.append('../')

import os
import time
import random

# Imports
from my_module.functions import wait_anim, bar, say
from my_module.classes import Player
from IPython.display import clear_output

###
###

# PYTHON SCRIPT HERE
def stat_check(class_object, attribute):
        """
        Checks object stat values and returns some needed,
        operated on value.
        
        Parameters
        ----------
        class_object : class object
            Class object to extract data from.
            
        attribute : string
            The operated attribute to be returned.
            
        Returns
        -------
        Gives the value asked for through attribute.
        
        Attribute Dictionary
        --------------------
        {'dam_weak' : dam_weak,
        'dam_medium' : dam_medium,
        'dam_strong' : dam_strong,
        'hp_count' : hp_count,
        'def_mult' : def_mult,
        'ap_cost_mult' : ap_cost_mult,
        'dodge_mult' : dodge_mult,
        'ap_count' : ap_count,
        'hit_chance' : hit_chance,
        'crit_chance' : crit_chance}
        """
        
               
        # Calculate everything to do with these values
        
        ### STRENGTH ###
        
        dam_weak = 10 + (class_object.str-5)
        # Ranges 5dmg to 15dmg
        
        dam_medium = 15 + (class_object.str*2-5)
        # Ranges 10dmg to 30dmg
        
        dam_strong = 20 + (class_object.str*4-5)
        # Ranges 15dmg to 55dmg
        
        
        ### VITALITY ###
        
        hp_count = 150 + (class_object.vit*10-100)
        # Ranges 50hp to 250hp
        
        def_mult = 0.5 - (class_object.vit*0.05-0.25)
        # Ranges 0.75x to 0.25x
        
        ### AGILITY ###
        
        ap_cost_mult = 1 - (class_object.agi*0.05-0.25)
        # Ranges 1.25x to 0.75x
        
        dodge_mult = 1 - (class_object.agi*0.05-0.25)
        # Ranges 1.25x to 0.75x
        
        # AND determines who goes first
        
        
        ### INTELLIGENCE ###
        
        ap_count = 50 + (class_object.int*4-10)
        # Ranges 40ap to 80ap
        
        hit_chance = 1 + (class_object.int*0.05-0.25)
        # Ranges 1.25x to 0.75x
        
        ### LUCK ###
        
        crit_chance = (class_object.luk**3/2000)
        # Ranges from 0% to 50% chance crit
                               
        all_stats = {'dam_weak': dam_weak,
                 'dam_medium': dam_medium,
                 'dam_strong': dam_strong,
                 'hp_count': hp_count,
                 'def_mult': def_mult,
                 'ap_cost_mult': ap_cost_mult,
                 'dodge_mult' : dodge_mult,
                 'ap_count': ap_count,
                 'hit_chance': hit_chance,
                 'crit_chance': crit_chance}
                          
        out = all_stats[attribute]
                          
        return out