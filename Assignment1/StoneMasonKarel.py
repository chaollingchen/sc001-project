from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-condition: Karel start at (1,1), facing east
    post-condition: Karel finish building ,facing east
    """
    build()


# Karel build pillars of the arch
def build():
    while front_is_clear():

        if left_is_clear():
            up()

        if front_is_clear():
            for i in range(4):
                move()

        if right_is_clear():
            down()

        if front_is_clear():
            for i in range(4):
                move()
    pass



# karel build left side of  arch's pillars

def up():

    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()


    if on_beeper():
        turn_right()
    else:
        put_beeper()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()

# karel build right side of  arch's pillars
def down():

    turn_right()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()


    if on_beeper():
        turn_left()
    else:
        put_beeper()
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)