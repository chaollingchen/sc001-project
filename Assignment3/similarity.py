"""
File: Joanna_similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    input the long dna sequence and the short dna sequence
    result:compare the long dna sequence and the short dna sequence, find the sequence from the
    long dna sequence that best match the short dna sequence
    """
    long_sequence = input('Please give me a DNA sequence to search:')
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match?')
    short_sequence = short_sequence.upper()

    best_match = try_all_match(long_sequence,short_sequence)
    print('The best match is' + str(best_match))

def try_all_match(long_sequence,short_sequence):
    maxium = 0
    new_sub_long = " "
    for i in range(0, len(long_sequence)-len(short_sequence)+1):
        sub_long = ""
        sub_long += long_sequence[0+i:len(short_sequence)+i]
        count = 0

        for j in range(len(sub_long)):
            if sub_long[j] == short_sequence[j]:
                count += 1
        similar = count/len(short_sequence)
        if similar > maxium:
            maxium = similar
            new_sub_long = sub_long
    return new_sub_long











###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
