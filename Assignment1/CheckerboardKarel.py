from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    pre-condition: Karel start at (1,1), facing east
    post-condition: Karel finish painting
    """
    if not front_is_clear():
        turn_left()
        fill_one_line()
    while front_is_clear():
        if facing_east():
            fill_one_line()
            if left_is_clear():
                turn1()
        if facing_west():
            fill_one_line()
            if right_is_clear():
                turn2()


# karel put beeper one by one in a row
def fill_one_line():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

# Karel turn upward and facing west
def turn1():
    if not on_beeper():
        turn_left()
        move()
        turn_left()
    else:
        for i in range(2):
            turn_left()
            move()

# Karel turn upward and facing east
def turn2():
    turn_right()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)