"""Process to allocate values to the player class."""

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
def say_points(pts):
    """
    States the remaining allocation points. Assumes
    say is imported.
    
    Parameters
    ----------
    pts : integer expected
        Number of points remaining to be stated.
        
    Returns
    -------
    Prints the statement as aforementioned.
    """
    
    state_points = "(You have " + str(pts) + " points remaining.)\n"
    say(state_points, False, sleep=0)

def check_it(att, att_str, pts):
    """
    For the allocation function, checks if the point
    value inputted by user is valid. Checks if integer,
    if between 0 and 10, and if enough points are
    available.
    
    Parameters
    ----------
    att : integer
        Inputted amount of points to be allocated, as
        input from the user.
    
    att_str : string
        Name of the attribute, structured as:
        ' Attribute:'
        
    pts : integer
        Points remaining for allocation.
        
    Returns
    -------
    new_att : integer
        Inputted att turns into a string. Turn it back
        into an integer and return as new_att.
        
    If input is not valid, print what went wrong.
    """
    
    check = False
    while not check:                

        # Try to turn att to integer IF POSSIBLE
        try:
            
            att = int(att)
            
        except:
            
            pass
        
        if type(att) != int:

            say("Mind giving an integer?\n")
            att = input(att_str)
        
        elif att < 0 or att > 10:

            say("Out of ten, please.\n")
            att = input(att_str)

        elif att > pts:

            say("Hm, I don't believe you. (Not enough points!)\n")
            att = input(att_str)
            
        elif att >= 0 and att <= 10 and type(att) == int and att <= pts:

            check = True
            
    new_att = att
        
    return new_att
            

def allocate(player):
    """
    Allocates player values to the player class.
    Begin with max point value and input will
    allocate the points to five different attributes
    to be used later on in the game script.
    
    Parameters
    ----------
    player : class
        Takes the player class to be edited. Edits the
        class' str, vit, agi, int, and luk attributes.
        
    Returns
    -------
    done : boolean
        Shows whether the allocation process is complete.
        Assumes False, otherwise True if the user decides
        allocation is complete when all attributes are gone
        through.
    """
    
    pts = 25
    
    skip = False
    done = False
    
    # STRENGTH    
    say_points(pts)
    
    say("Can you throw a punch or wield an axe?", False)    
    strng = input(" Strength:")
    
    new_att = check_it(strng, "Strength:", pts)
    
    strng = int(new_att)
            
    player.str = strng
    pts = pts - strng
    
    # VITALITY
    say_points(pts)
    
    say("Would you consider yourself hardy?", False)
    vital = input(" Vitality:")
    
    new_att = check_it(vital, "Vitality:", pts)
    
    vital = int(new_att)
                        
    player.vit = vital
    pts = pts - vital
    
    # AGILITY
    say_points(pts)    
    
    say("Are you confidently quick on your feet?", False)
    aglty = input(" Agility:")
    
    new_att = check_it(aglty, "Agility:", pts)
    
    aglty = int(new_att)
                        
    player.agi = aglty
    pts = pts - aglty
    
    # INTELLIGENCE
    empty = False
    
    if pts == 0:
        
        empty = True
    
    if empty:
        
        # Points are empty? Default rest to zero
        say("Right, I think I've got the gist of it.")
        say("I sense you're not a bright one, nor as lucky.\n")
        
        intel = 0
        lucky = 0
        
        skip = True
        
    elif not empty: 
        
        say_points(pts)
        
        say("Great, but can you THINK on your feet?", False)
        intel = input(" Intelligence:")
        
        new_att = check_it(intel, "Intelligence:", pts)
        
        intel = int(new_att)

        player.int = intel
        pts = pts - intel
        
    # LUCK
    empty = False
    
    if pts == 0:
        
        empty = True
    
    if empty and not skip:
        
        # Points are empty? Default rest to zero
        say("Right, I think I've got the gist of it.")
        say("You seem talented, and require no luck.\n")
        
        lucky = 0
        
        skip = True
        
    elif not empty: 
        
        say_points(pts)        
        
        say("Lastly, do you see yourself as a character of fortune?", False)
        lucky = input(" Luck:")

        new_att = check_it(lucky, "Luck:", pts)
        
        lucky = int(new_att)

        player.luk = lucky
        pts = pts - lucky
    
    # WRAP UP

    if pts != 0:    
        say("(You still have points remaining!)", False)        
        say("(Are you okay with this?)\n", False)
        
    elif pts == 0:
        say("(Allocation complete, are you okay with these?)\n", False)
        
    say("Strength: " + str(strng), False, 0.02)
    say("Vitality: " + str(vital), False, 0.02)
    say("Agility: " + str(aglty), False, 0.02)
    say("Intelligence: " + str(intel), False, 0.02)
    say("Luck: " + str(lucky) + "\n", False, 0.02)
        
    valid = False
        
    while not valid:
            
        resp = input("(Y/N):\n")
            
        if resp == "Y":
                
            say("(Points allocated!)\n", False)
                
            done = True
            valid = True
                
        elif resp == "N":
                
            say("(Right, please allocate your points again.)")
                
            strng = 0
            vital = 0
            aglty = 0
            intel = 0
            lucky = 0
                
            done = False
            valid = True
                
        else:
                
            say("(Please only answer Y or N!)")               
    
    return done, strng, vital, aglty, intel, lucky
            