"""
File: Joanna_caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    input Secret number and ciphered string
    output the deciphered string
    """
    shift = input('Secret number:')
    ciphered = input('What is the ciphered string?')
    ciphered = ciphered.upper()
    print('The deciphered string is :'+str(caesar(ciphered, shift)))

def caesar(ciphered,shift):
    deciphered = ''
    for i in range(len(ciphered)):
        if ciphered[i] in ALPHABET:
            num = ALPHABET.find(ciphered[i])
            num = int(shift) + num
            if num >= 26:
                num = num - len(ALPHABET)
            deciphered = deciphered + ALPHABET[num]
        if not ciphered[i].isalpha():
            deciphered = deciphered + ciphered[i]

    return deciphered




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
