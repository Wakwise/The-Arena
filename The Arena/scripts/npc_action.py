"""Script to determine what the NPC decides to do some turn."""

# GOES UP ONE FILE!
import sys
sys.path.append('../')

import os
import time
import random

# Imports
from my_module.functions import wait_anim, bar, say
from my_module.classes import Player
from scripts.stat_check import stat_check
from IPython.display import clear_output

###
###

# PYTHON SCRIPT HERE
def npc_action(npc_object, hp, hp_max, ap, ap_max):
    """
    NPC decides what to do. Chances depend on how high or low the
    hp and ap given are.
    
    Parameters
    ----------
    npc_object : class
        NPC class.
        
    hp, hp_max, ap, ap_max : int or float
        Used to determine chances of NPC acting some certain way.
        
    Returns
    -------
    Gives the object decided by random chance. Otherwise, loop will
    repeat until a valid choice is selected
    """
    hp_frac = hp/hp_max
    ap_frac = ap/ap_max
    
    # Action probabilities:  
    attack_matrix = [*range(0, 7)]
    
    def_max = 9
    
    if hp_frac <= 0.3:
        def_max = 15
        
    elif hp_frac <= 0.5:
        def_max = 12
        
    defend_matrix = [*range(8, def_max)]
    
    rest_max = def_max+2
    
    if ap_frac <= 0.3:
        rest_max = def_max+6
        
    elif ap_frac <= 0.5:
        rest_max = def_max+4
    
    rest_matrix = [*range(def_max+1, rest_max)]
    
    # Pick some action
    valid_action = False
    while not valid_action:
        
        pick = random.randint(0, rest_max)

        if pick in attack_matrix:
            option = 'attack'

        elif pick in defend_matrix:
            option = 'defend'

        else:
            option = 'rest'

        if option == 'attack':

            strong_matrix = [*range(0, 4)]

            med_max = 8
            if ap_frac <= 0.5:
                med_max = 10

            medium_matrix = [*range(5, med_max)]

            weak_max = med_max+3
            if ap_frac <= 0.5:
                weak_max = med_max+9

            elif ap_frac <= 0.5:
                weak_max = med_max+5

            weak_matrix = [*range(med_max+1, weak_max)]

            pick_attack = random.randint(0, weak_max)

            if pick_attack in strong_matrix:
                option = 'strong_attack'

            elif pick_attack in medium_matrix:
                option = 'medium_attack'

            else:
                option = 'weak_attack'
        
        mult = stat_check(npc_object, 'ap_cost_mult')
        ap_cost = {'strong_attack' : 30*mult,
                   'medium_attack' : 20*mult,
                   'weak_attack' : 10*mult,
                   'defend' : 10*mult,
                   'rest' : 0}
        
        if ap_cost[option] <= ap:
            valid_action = True
            
        else:
            valid_action = False
            
        # NPC will never rest when high AP.
        if ap >= (ap_max-10) and option == 'rest':
            valid_action = False
            
    return option
