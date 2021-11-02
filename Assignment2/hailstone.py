"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program can run the Hailstone sequences and count it takes haw many steps to reach 1
    """
    print('This program computes Hailstone sequences')
    num = int(input('Enter a number:'))
    # calculate how many steps
    length = 0
    while True:
        if num == 1:
            print('It took' + str(length) + 'steps to reach 1.')
            break
        elif num > 1 and num % 2 == 0:
            print(str(num)+'is even, so I take half :'+str(int(num/2)))
            num = int(num/2)
            length += 1
        elif num > 1 and num % 2 == 1:
            print(str(num)+'is odd, so I make 3n+1 :'+str(3*num+1))
            num = 3*num+1
            length += 1




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
