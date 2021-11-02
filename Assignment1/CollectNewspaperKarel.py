from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    pre-codition :Karel is at the North-west of the house
    post-codition :Karel go back to original spot, facing east, and put down the newspaper
    """
    move_out()
    go_home()

# Karel move out the house and pick up the newspaper
def move_out():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

def turn_right():
    for i in range(3):
        turn_left()
# Karel go home and put down the newspaper
def go_home():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()



def turn_around():
    for i in range(2):
        turn_left()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
