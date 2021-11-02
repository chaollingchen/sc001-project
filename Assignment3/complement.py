"""
File: Joanna_complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    input: a DNA sequence
    output:the complement of the DNA sequence
    """
    dna = input('Please give me a DNA strand and I will find the complement:')
    dna = dna.upper()
    newdna = build_complement(dna)
    print('The complement of' + str(dna)+'is' + str(newdna))


def build_complement(dna):
    ans = " "
    for i in dna:
        if i == 'A':
            ans += 'T'
        elif i == 'T':
            ans += 'A'
        elif i == 'C':
            ans += 'G'
        elif i == 'G':
            ans += 'C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
