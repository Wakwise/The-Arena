"""The game's main script."""

# GOES UP ONE FILE!
import sys
sys.path.append('../')

import time
import random
import os

# Imports
from my_module.functions import wait_anim, bar, say
from my_module.classes import Player, Zombie, Goblin, Giant, Antihero

from scripts.allocation import allocate
from scripts.comment import comment
from scripts.stat_check import stat_check
from scripts.npc_action import npc_action
from scripts.player_menu import player_menu

from IPython.display import clear_output

    #############################################################################################################################
    #############################################################################################################################

# PYTHON SCRIPT HERE

def the_game():
    """
    It's a game!
    
    Parameters
    ----------
    Nothing.
    
    Returns
    -------
    A lot of printed statements.
    """
    
    # Create the player class
    player = Player()
    
    # Introduction
    skip_creator = False
    
    say("Welcome to the arena."); say("What is your name?")
    
    player.name = input("Name:")
    
    if player.name == "":
        
        say("Quiet type, huh? Suit yourself.", False)
    
    
    elif player.name == "skippy":
        
        # Dev condition for debug
        
        skip_creator = True
        say("Skipping!!", False)
    
    else:
        
        say("Well met, " + player.name + ".", False)
    
    # Begin asking about stats
    if not skip_creator:
        
        say("Say, what makes you believe you can handle yourself in a fight?\n", False)
        
        say("(Here, your strength, vitality, agility, intelligence, and luck will be evaluated.)\n", False)

        # Allocation

        done = False
        while not done:

            done, player.str, player.vit, player.agi, player.int, player.luk = allocate(player)
            # Show player stats gathered:
            # print(player.str, player.vit, player.agi, player.int, player.luk)
            
        # Talk about the player
        comment(player.str, player.vit, player.agi, player.int, player.luk)
        
    elif skip_creator:
        
        player.str = 5
        player.vit = 5
        player.agi = 5
        player.int = 5
        player.luk = 5
    
    # End of introduction
    say("When you're ready to head in, just say the word!")
    nothing = input("Ready?")
    
    what = nothing.lower()
    if 'the word' in what:
        say("Alright buddy. Guess you're a comedian too.", False)
        
    if what == 'no':
        say('Wait, really? Okay then. See you later, I guess.', False)
        time.sleep(1.5)
        raise Exception('Wait, did you seriously say NO? What the heck?? Get back in there!!')
        
    print('\n')
    
    say("Entering the arena in", False)
    
    say("3"); wait_anim(sleep=0.2)
    say("2"); wait_anim(sleep=0.2)
    say("1"); wait_anim(sleep=0.2)
    
    say("\nBEGIN!", sleep=0.4)
    
    clear_output()

    #############################################################################################################################
    #############################################################################################################################
    
    # Arena Introduction
    
    name_valid = False
    say('What (or who) are you expecting to fight in the arena?', False)
    
    while not name_valid:
        the_input = input('Who is your enemy? ')
        enemy_ask = the_input.lower()
        
        if 'zombie' in enemy_ask:
            zombie = Zombie()
            enemy = 'zombie'
            name_valid = True
            
        elif 'goblin' in enemy_ask:
            zombie = Goblin()
            enemy = 'goblin'
            name_valid = True
            
        elif 'giant' in enemy_ask:
            zombie = Giant()
            enemy = 'giant'
            name_valid = True
            
        elif 'antihero' in enemy_ask:
            zombie = Antihero()
            enemy = 'antihero'
            name_valid = True
            
        else:
            say("Not a valid enemy.", False)
    
    say("Suddenly, a "+zombie.name+" appears!", False)
    say("(Begin encounter!)\n", False)
    
    ### FIGHT INITIALIZE ###
    player_max_hp = stat_check(player, 'hp_count')
    player_hp = player_max_hp
    
    player_max_ap = stat_check(player, 'ap_count')
    player_ap = player_max_ap
    
    zombie_max_hp = stat_check(zombie, 'hp_count')
    zombie_hp = zombie_max_hp
    
    zombie_max_ap = stat_check(zombie, 'ap_count')
    zombie_ap = zombie_max_ap        
    
    player_mult = stat_check(player, 'ap_cost_mult')
    player_ap_cost = {'strong_attack' : 40*player_mult,
                      'medium_attack' : 25*player_mult,
                      'weak_attack' : 5*player_mult,
                      'defend' : 5*player_mult,
                      'rest' : 0}
    
    zombie_mult = stat_check(zombie, 'ap_cost_mult')
    zombie_ap_cost = {'strong_attack' : 40*zombie_mult,
                      'medium_attack' : 25*zombie_mult,
                      'weak_attack' : 5*zombie_mult,
                      'defend' : 5*zombie_mult,
                      'rest' : 0}
    
    player_crit = stat_check(player, 'crit_chance')
    player_hit_mult = stat_check(player, 'hit_chance')
    player_dodge_mult = stat_check(player, 'dodge_mult')
    
    zombie_crit = stat_check(zombie, 'crit_chance')
    zombie_hit_mult = stat_check(zombie, 'hit_chance')
    zombie_dodge_mult = stat_check(zombie, 'dodge_mult')
    
    player_first = True
    fight_complete = False
    first_turn = True
    player_defeated = False
    zombie_defeated = False
    
    # Who goes first?
    if player.agi > zombie.agi:
        
        player_first = True
        
    elif player.agi < zombie.agi:

        player_first = False
        
    else:
        
        if random.random() > 0.5:
            player_first = True
            
        else:
            player_first = False
            
    if player_first:
        say(player.name + ' goes first!', False)
        
    elif not player_first:
        say(zombie.name + ' goes first!', False)
        
    time.sleep(2)
    clear_output()
        
    ### START FIGHT! ###
    
    while not fight_complete:
        
        # Status update, voice lines
        zombie_hp_frac = zombie_hp/zombie_max_hp
        zombie_ap_frac = zombie_ap/zombie_max_ap
        
        if first_turn:
            pass
        
        elif not first_turn:
            say(zombie.phrases[random.randint(0, 4)], False)
            
            if zombie_hp_frac <= 0.2:
                say(zombie.name + " is very wounded.", False)
                
            elif zombie_hp_frac <= 0.4:
                say(zombie.name + " appears sluggish.", False)
            
    
        # Display bars
        bar(zombie_hp, zombie_max_hp, zombie.name+" Health")
        print('\n')
        print('\t\t', end="")
        bar(zombie_ap, zombie_max_ap, zombie.name+" AP")
        
        print('\n\n')
        
        bar(player_hp, player_max_hp, player.name+" Health")
        print('\n')
        print('\t\t', end="")
        bar(player_ap, player_max_ap, player.name+" AP")
        
        print('\n')
        print('\n')

        # Your turn to determine action (MENU)
        player_action = player_menu(player, player_hp, player_max_hp, player_ap, player_max_ap)
        clear_output()
        
        # Enemy determines action
        zombie_action = npc_action(zombie, zombie_hp, zombie_max_hp, zombie_ap, zombie_max_ap)
        
        # Aftermath, PLAY THE MOVES! Who's first?
        
        # Check defense and rest conditions
        player_defending = False
        if player_action == 'defend':
            player_defending = True
            
        player_resting = False
        if player_action == 'rest':
            player_resting = True
            
        zombie_defending = False
        if zombie_action == 'defend':
            zombie_defending = True
        
        zombie_resting = False
        if zombie_action == 'rest':
            zombie_resting = True
            
        # If zombie goes first:
        if not player_first:
            # Zombie goes
            
            if zombie_action == 'strong_attack':
                say(zombie.name+' uses strong attack!', False)
                dmg = stat_check(zombie, 'dam_strong')
                zombie_ap = zombie_ap - zombie_ap_cost['strong_attack']
                
            elif zombie_action == 'medium_attack':
                say(zombie.name+' uses medium attack!', False)
                dmg = stat_check(zombie, 'dam_medium')
                zombie_ap = zombie_ap - zombie_ap_cost['medium_attack']
                
            elif zombie_action == 'weak_attack':
                say(zombie.name+' uses weak attack!', False)
                dmg = stat_check(zombie, 'dam_weak')
                zombie_ap = zombie_ap - zombie_ap_cost['weak_attack']
                
            elif zombie_action == 'defend':
                say(zombie.name+' defends.', False)
                zombie_ap = zombie_ap - zombie_ap_cost['defend']
                
            elif zombie_action == 'rest':
                say(zombie.name+' rests.', False)
                
            if zombie_action in ('strong_attack', 'medium_attack', 'weak_attack'):
                
                hit_roll = random.random()
                zombie_hit_chance = 0.75*zombie_hit_mult*player_dodge_mult
                
                hit = True
                if hit_roll > zombie_hit_chance:
                    hit = False
                    
                if hit:
                
                    crit_roll = random.random()
                    if crit_roll <= zombie_crit:
                        say('CRIT!', False)
                        dmg = dmg * 1.5

                    if player_defending:
                        
                        say(player.name+' defends!', False)
                        def_mult = stat_check(player, 'def_mult')
                        dmg = dmg * def_mult
                        
                    say(player.name+' takes '+str(round(dmg, 1))+' damage!', False)
                    player_hp = player_hp - dmg
                    
                elif not hit:
                    say('Miss!', False)
                    
            print('\n')
            
            if player_hp <= 0:
                player_victory = False
                fight_complete = True
                player_defeated = True
                say(player.name+' has been defeated!', False)
        
        # PLAYER
        
        if not player_defeated:
            
            if player_action == 'strong_attack':
                say(player.name+' uses strong attack!', False)
                dmg = stat_check(player, 'dam_strong')
                player_ap = player_ap - player_ap_cost['strong_attack']

            elif player_action == 'medium_attack':
                say(player.name+' uses medium attack!', False)
                dmg = stat_check(player, 'dam_medium')
                player_ap = player_ap - player_ap_cost['medium_attack']

            elif player_action == 'weak_attack':
                say(player.name+' uses weak attack!', False)
                dmg = stat_check(player, 'dam_weak')
                player_ap = player_ap - player_ap_cost['weak_attack']

            elif player_action == 'defend':
                say(player.name+' defends.', False)
                player_ap = player_ap - player_ap_cost['defend']

            elif player_action == 'rest':
                say(player.name+' rests.', False)

            if player_action in ('strong_attack', 'medium_attack', 'weak_attack'):
                
                hit_roll = random.random()
                player_hit_chance = 0.75*player_hit_mult*zombie_dodge_mult
                
                hit = True
                if hit_roll > player_hit_chance:
                    hit = False
                    
                if hit:
                
                    crit_roll = random.random()
                    if crit_roll <= player_crit:
                        say('CRIT!', False)
                        dmg = dmg * 1.5

                    if zombie_defending:
                        
                        say(zombie.name+' defends!', False)
                        def_mult = stat_check(zombie, 'def_mult')
                        dmg = dmg * def_mult
                        
                    say(zombie.name+' takes '+str(round(dmg, 1))+' damage!', False)
                    zombie_hp = zombie_hp - dmg
                    
                elif not hit:
                    say('Miss!', False)
                    
            print('\n')
            
            if zombie_hp <= 0:
                player_victory = True
                fight_complete = True
                zombie_defeated = True
                say(zombie.name+' has been defeated!', False)
        
        # If player went first:
        if player_first and not zombie_defeated:
            # Zombie goes
            
            if zombie_action == 'strong_attack':
                say(zombie.name+' uses strong attack!', False)
                dmg = stat_check(zombie, 'dam_strong')
                zombie_ap = zombie_ap - zombie_ap_cost['strong_attack']
                
            elif zombie_action == 'medium_attack':
                say(zombie.name+' uses medium attack!', False)
                dmg = stat_check(zombie, 'dam_medium')
                zombie_ap = zombie_ap - zombie_ap_cost['medium_attack']
                
            elif zombie_action == 'weak_attack':
                say(zombie.name+' uses weak attack!', False)
                dmg = stat_check(zombie, 'dam_weak')
                zombie_ap = zombie_ap - zombie_ap_cost['weak_attack']
                
            elif zombie_action == 'defend':
                say(zombie.name+' defends.', False)
                zombie_ap = zombie_ap - zombie_ap_cost['defend']
                
            elif zombie_action == 'rest':
                say(zombie.name+' rests.', False)
                
            if zombie_action in ('strong_attack', 'medium_attack', 'weak_attack'):
                
                hit_roll = random.random()
                zombie_hit_chance = 0.75*zombie_hit_mult*player_dodge_mult
                
                hit = True
                if hit_roll > zombie_hit_chance:
                    hit = False
                    
                if hit:
                
                    crit_roll = random.random()
                    if crit_roll <= zombie_crit:
                        say('CRIT!', False)
                        dmg = dmg * 1.5

                    if player_defending:
                        
                        say(player.name+' defends!', False)
                        def_mult = stat_check(player, 'def_mult')
                        dmg = dmg * def_mult
                        
                    say(player.name+' takes '+str(round(dmg, 1))+' damage!', False)
                    player_hp = player_hp - dmg
                    
                elif not hit:
                    say('Miss!', False)
                    
            print('\n')
            
            if player_hp <= 0:
                player_victory = False
                fight_complete = True
                player_defeated = True
                say(player.name+' has been defeated!', False)
            
        # Calculate, announce    
        
        
        # Subtract AP, add AP
        if player_resting:
            player_ap = player_ap + 20
        elif not player_resting:
            player_ap = player_ap + 10
            
        if player_ap > player_max_ap:
            player_ap = player_max_ap
            
        if zombie_resting:
            zombie_ap = zombie_ap + 20
        elif not zombie_resting:
            zombie_ap = zombie_ap + 10
            
        if zombie_ap > zombie_max_ap:
            zombie_ap = zombie_max_ap
        
        # Repeat until someone is 0 HP        
    
        time.sleep(2)
        clear_output()
        
        first_turn = False
        
    # Fight wrap-up
    if player_victory:
        if enemy == 'zombie':
            say("With a final lash, the zombie topples over for the last time. It returns to the dirt, whence it came.", False)
            
        if enemy == 'goblin':
            say("Before the goblin can pester you again, you catch it with its guard off. The goblin lies defeated.", False)
            
        if enemy == 'giant':
            say("A bellowing roar envelops the arena. As the giant loses control of its body, it slowly goes limp. After you roll out of the landing zone, the giant falls to the ground with a mighty boom, as dust flies into the air.", False)
        
        if enemy == 'antihero':
            say("You know it's over. The Antihero isn't getting back up. You lean over their defeated body to observe, but all you see is yourself. You kneel. In the Antihero's figure you see all the worst parts of yourself gathered into a single poor creature. And now, after a lengthy battle, it is now lying in the dirt. You stand again, made anew.", False)
            
        print('\n')
            
        say("YOU WIN! Go give the developer an A+!", False)
        say("Thank you for playing!")
        
    if not player_victory:
        say("You have fallen in battle, but it is not the end. Pick yourself back up. You still have a task to fulfill.")
        print('\n')
        say("YOU LOSE! But the developer still deserves an A+!", False)
        say("Thank you for playing!")
