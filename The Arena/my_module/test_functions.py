"""Functions only return printed statements! Tests modules instead."""

# GOES UP ONE FILE!
import sys
sys.path.append('../')

from scripts.allocation import check_it
from scripts.stat_check import stat_check
from scripts.npc_action import npc_action

from my_module.classes import Zombie

##
##

def test_check_it():
    
    assert callable(check_it)
    
    assert type(check_it(5, ' Strength:', 10)) == int
    
    old_att = 5
    new_att = check_it(old_att, ' Strength:', 10)
    assert old_att == new_att
    
    
def test_stat_check():
    
    zombie = Zombie()
    
    assert callable(stat_check)
    
    # Attribute matrix is 3 7 2 2 2
    assert type(stat_check(zombie, 'hp_count')) == int
    assert stat_check(zombie, 'hp_count') == 120
    
    
def test_npc_action():
    
    zombie = Zombie()
    
    assert callable(npc_action)
    
    assert type(npc_action(zombie, 100, 120, 40, 48)) == str
    
    action_list = ('strong_attack', 'medium_attack', 'weak_attack', 'defend', 'rest')
    assert npc_action(zombie, 100, 120, 40, 48) in action_list
    


                 
    