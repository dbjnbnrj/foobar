'''
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot,
she has several visually-impaired minions.
But she never bothered to follow intergalactic standards for workplace accommodations,
so those minions have a hard time navigating her space station.
You figure printing out Braille signs will help them, and -
since you'll be promoting efficiency at the same time - increase your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight.
Each character is composed of 6 dots in a 2x3 grid,
where each dot can either be a bump or be flat (no bump).
You plan to translate the signs around the space station
to Braille so that the minions under Commander Lambda's
command can feel the bumps on the signs and "read" the text with their touch.
The special printer which can print the
bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word "code", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00


where 1 represents a bump and 0 represents no bump.  Put together, "code" becomes the output string "[100100][101010][100110][100010]".

Write a function answer(plaintext) that takes a string parameter and returns a string of 1's and 0's
representing the bumps and absence of bumps in the input string.
Your function should be able to encode the 26 lowercase letters,
handle capital letters by adding a Braille capitalization mark before that character,
and use a blank character (000000) for spaces. All signs on the space station are less
than fifty characters long and use only letters and spaces.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) plaintext = "code"
Output:
    (string) "100100101010100110100010"

Inputs:
    (string) plaintext = "Braille"
Output:
    (string) "000001110000111010100000010100111000111000100010"

Inputs:
    (string) plaintext = "The quick brown fox jumped over the lazy dog"
Output:
    (string) "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
'''

import string

def special(a):
    print a[0]+a[3]
    print a[1]+a[4]
    print a[2]+a[5]
    print ""

def answer(plaintext):
    istr = "The quick brown fox jumped over the lazy dog"
    ires = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    m = {}
    m[" "] = "000000"
    m["s"] = "011100"
    m["S"] = "000001"+m[s]
    i = 0
    for c in istr:
        if c not in m:
            if c.islower():
                m[c] = ires[i:i+6]
                m[c.upper()] = "000001"+m[c]
            elif c.isupper():
                i+=6
                m[c.lower()] = ires[i:i+6]
                m[c.upper()] = "000001"+m[c.lower()]
        i+=6


    result = ""
    for c in plaintext:
        result+=m[c]
    return result, m

print answer('code')
