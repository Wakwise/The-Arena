"""Many a function."""

# Imports
import random
import time

# ANIMATION FUNCTIONS

def wait_anim(string=".", num=3, sleep=1):
    '''Prints out the same string some amount of times with a wait in between and after.
    Functions as an animation. Assumes time has been imported.
    
    Parameters
    ----------
    string : string
        String to be repeated
        
    num : integer
        Number of times string is repeated
        
    sleep : integer
        Number of seconds to wait after each string is printed
        
    Returns
    -------
    Prints the animation aforementioned.
    '''
    count = 0
    while count < num:
        
        print(string, end=" ")
        
        time.sleep(sleep)
        
        count += 1

                 
def say(text, sameline=True, sleep=0.04):
    """
    'Says' some input text. Prints input out
    character by character in an animation.
    
    Parameters
    ----------
    text : string
        Input to be printed.
        
    sameline : boolean
        Should the next line be printed on the
        same line?
        
    sleep : float
        Speed of the animation. Higher means slower.
        
    Returns
    -------
    Prints the animation aforementioned.
    """
    
    text = text + " "
    
    count = 0
    if sameline:
        
        for i in text:
            
            print(i, end="")
            
            time.sleep(sleep)
            
            count += 1
            
    elif not sameline:
        
        for i in text:
            
            if count < (len(text) - 1):
                
                print(i, end="")
                
                time.sleep(sleep)
                
                count += 1
                
            elif count == (len(text) - 1):
                
                print(i)
                
                time.sleep(sleep)
                
                count += 1
                
    time.sleep(0.3)

    
def bar(rem, max_val, att="Health"):
    """
    Displays a bar, animated.
    Assumes time and say are imported.

    Parameters
    ----------
    rem : float
        Object's current value. Cannot be larger than max.

    maxh : float
        Object's maximum value.
        
    att : string
        The attribute being evaluated. Prints with bar.

    Returns
    -------
    Prints a small bar graphic and the amount 
    of value (out of max) the object has left.
    """

    count = 0
    frac = rem/max_val*10

    print('[', end="")
    time.sleep(0.00)

    while count < frac:

        print('█', end="")

        count += 1

        time.sleep(0.00)

    while count < 10:

        print(' ', end="")

        count += 1

        time.sleep(0.00)

    print(']', end="")
    
    if frac <= 2:
        
        state = " LOW " + att.upper() + "!: " + str(rem) + " / " + str(max_val)
        say(state, sleep=0.02)
        
    else:
        
        state = " " + att + ": " + str(rem) + " / " + str(max_val)
        say(state, sleep=0.02)
   

            