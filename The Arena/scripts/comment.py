"""Script to run some part of my project."""

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
def com_phrase(att, phrases):
    """
    Judges a character's given attribute, depending
    on how proficient the attribute is.
    Assumes say is imported.
    
    Parameters
    ----------
    att : integer
        Attribute value of character.
        
    phrases : tuple
        Tuple of phrases to respond given different
        value ranges of att. Assumes five in the tuplee.
        
    Returns
    -------
    Prints one value from phrases tuple.
    """
    if att == 0:
        say(phrases[0], False, 0.02)
        
    elif att >= 1 and att <= 3:
        say(phrases[1], False, 0.02)
        
    elif att >= 4 and att <= 6:
        say(phrases[2], False, 0.02)
        
    elif att >= 7 and att <= 9:
        say(phrases[3], False, 0.02)
        
    elif att == 10:
        say(phrases[4], False, 0.02)
    
    
def comment(strng, vital, aglty, intel, lucky):
    
    clear_output()

    say("Right, here's what I've gathered about you and your abilities:\n", False)
    
    # Strength
    str_phrases = ("I'm sorry to say, I fear for your life. you're weaker than a worm!",
                   "Be careful out there, your grip appears to be weak.",
                   "You're not a hard-hitter, but not a pushover neither.",
                   "I trust you could reliably knock any foe down, with some effort.",
                   "You are a master in all things battering and hammering! Watch where you point your fists.")
    com_phrase(strng, str_phrases)
    
    # Vitality
    vit_phrases = ("You're looking a little pale there. You sure you're fit to fight?",
                   "Put a little more focus on keeping yourself safe and holding your own.",
                   "You can stand yourself upright and hold your own when you need to.",
                   "I think you'd withstand more blows than the average Joe.",
                   "Are you sure you haven't got bones of steel? You have the physique of a mountain!")
    com_phrase(vital, vit_phrases)
    
    # Agility
    agi_phrases = ("Your shoe's untied. Also, you're quite clumsy. Don't trip on your way out.",
                   "You seem like a heavy mover. I could teach you to dodge, if you'd like?",
                   "You're not too bad on the move, and you get to where you need to be.",
                   "I think you could outrun most others without breaking a sweat.",
                   "You're leaving all your foes behind in the dust! Use your speediness well.")
    com_phrase(aglty, agi_phrases)
                   
    # Intelligence
    int_phrases = ("Hey, anybody in there? Just kidding with you. Don't lose yourself.",
                   "Your psyche isn't your strong suit, but I hope it shouldn't be too debilitating.",
                   "Mentally, you're nothing special. Erm, don't take that as an insult.",
                   "You're quite the smart cookie. Just don't let it get to your head.",
                   "Are you sure you're a fighter, and not a philosopher? Physician, perhaps?")
    com_phrase(intel, int_phrases)
    
    # Luck
    luk_phrases = ("And I know you got hit by bird feces on the way here, but it's not the end of the world.",
                   "And it seems like you've been through some tough times before arriving here.",
                   "But otherwise, as a person, you seem quite unsubstantial. Which is fine.",
                   "And I noticed how frequently prime opportunities come your way. Quite lucky.",
                   "And I was wondering where you got that diamond ring. Oh, you came by it on your way here? Huh.")
    com_phrase(lucky, luk_phrases)               

    print("\n")
