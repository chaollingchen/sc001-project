"""
File: Joanna_hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    input guess word
    output whether the guess word is in the answer
    player has N_TURNS to guess
    if the guess word is not in the answer: N_TURNS - 1
    if the guess word is  in the answer: guess word fill the '_'
    The program stop when the player get the answer or there are no turns left
    """
    ans = random_word()
    dashed = dash(ans)
    print('The word looks like:' + str(dashed))
    print('You have '+str(N_TURNS)+' guesses left')
    new_turn = N_TURNS
    while True:
        guess = input('Your guess:')
        if len(guess) > 1 or not guess.isalpha():
            print('illegal format.')
        else:
            guess = guess.upper()
            i = ans.find(guess)

            if i == -1:
                print('There is no ' + str(guess) + "'s in the word.")
                print('The word looks like:' + str(dashed))
                new_turn -= 1
                if new_turn == 0:
                    print('You are completely hung :( ')
                    print('The word was:' + str(ans))
                    break
                print('You have ' + str(new_turn) + ' guesses left')

            else:
                print('You are correct!')
                word =''
                for j in range(len(dashed)):
                    if ans[j] == guess:
                        word += guess
                    else:
                        word += dashed[j]
                dashed = word
                if dashed == ans:
                    print('You win!!')
                    print('The word was:' + str(ans))
                    break
                print('The word looks like:'+str(dashed))
                print('You have ' + str(new_turn) + ' guesses left')


def dash(word):
    ans = ''
    for i in range(len(word)):
        ans += '_'
    return ans







def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
