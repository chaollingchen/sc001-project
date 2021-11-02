from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    pre-condition: Karel start at (1,1), facing east
    post-condition: Karel stop in the mid-point of street 1 and put down a beeper
    """
    if front_is_clear():
        put1()
        turn_around()
        check()
        collect_right()
        go_mid()
        collect_left()
        go_mid()
        pick_beeper
    else:
        put_beeper()

# Karel put beeper at the end of both sides of street 1
def put1():
    put_beeper()
    while front_is_clear():
        move()

    put_beeper()

def turn_around():
    turn_left()
    turn_left()

# Karel move inward ,put down the beeper, and fill street 1 with beeper
def check():
    while front_is_clear():
        move()
        if on_beeper():
            turn_around()
            move()
            put_beeper()

            """
            In the while loop, since Karel will put more than one beeper at the mid-point 
            we can use the following method to let Karel stop in the mid-point
            """
            pick_beeper()
            if on_beeper():
                if facing_east():
                    turn_right()
                else:
                    turn_left()
            else:
                put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# Karel will pick up the beeper in the right-side of the mid-point
def collect_right():
    turn_left()

    while front_is_clear():
        move()
        pick_beeper()
    turn_around()

# Karel will pick up the beeper in the left-side of the mid-point
def collect_left():
    move()
    while on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
    turn_around()

# Karel find the mid-point and stop 
def go_mid():
    while not on_beeper():
        move()





####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)