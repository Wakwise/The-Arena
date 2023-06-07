"""Brings up the player's menu."""

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
def player_menu(player_object, hp, hp_max, ap, ap_max):
    """
    Displays an interactice player menu to be used in
    arena combat. Decorational, but gives potential
    inputs for combat turns.
    
    Returns the player's chosen action.
    
    """
    
    # Check AP costs
    mult = stat_check(player_object, 'ap_cost_mult')
    ap_cost = {'strong_attack' : 40*mult,
               'medium_attack' : 25*mult,
               'weak_attack' : 5*mult,
               'defend' : 5*mult,
               'rest' : 0}
    
    complete = False
    
    while not complete:
        
        insuf_ap = False
        back_condition = False  
        valid_action = False 
        
        print('----------   ----------   --------'); time.sleep(0.02)
        print('| ATTACK |   | DEFEND |   | REST |'); time.sleep(0.02)
        print('----------   ----------   --------'); time.sleep(0.02)
        print('\n')

        
        while not valid_action:
            
            player_input = input('What will you do? ')
            response = player_input.lower()

            if response not in ('attack', 'defend', 'rest'):
                valid_action = False
                say('Not a valid action!', False)

            else:
                valid_action = True

        if 'attack' in response:

            valid_attack = False
            
            print('--------   ----------   ----------'); time.sleep(0.02)
            print('| WEAK |   | MEDIUM |   | STRONG |'); time.sleep(0.02)
            print('--------   ----------   ----------'); time.sleep(0.02)
            print('                                    ------'); time.sleep(0.02)
            print('                                    |BACK|'); time.sleep(0.02)
            print('                                    ------'); time.sleep(0.02)
            print('\n')
            
            while not valid_attack:
                

                player_input = input('How strong? ')
                response = player_input.lower()

                if 'weak' in response:
                    response = 'weak_attack'

                elif 'medium' in response:
                    response = 'medium_attack'

                elif 'strong' in response:
                    response = 'strong_attack'

                elif 'back' in response:
                    back_condition = True
                    complete = False
                    valid_attack = True

                if response in ('weak_attack', 'medium_attack', 'strong_attack'):

                    if ap >= ap_cost[response]:
                        complete = True
                        valid_attack = True

                    else:
                        complete = False
                        insuf_ap = True
                        valid_attack = False
                        say('Not enough AP!', False)
                        
                elif not back_condition:
                    
                    say('Invalid attack!', False)

        elif 'defend' in response:
            if ap >= ap_cost[response]:
                complete = True
            else:
                complete = False
                insuf_ap = True
                say('Not enough AP!', False)

        elif 'rest' in response:
            if ap >= ap_cost[response]:
                complete = True

            else:
                complete = False
                insuf_ap = True
                say('Not enough AP!', False)

        if not complete and not insuf_ap and not back_condition:
            say('Not a valid action!', False)
    
    return response