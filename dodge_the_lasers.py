'''
Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambdas collapsing space station in an escape pod with the rescued bunny prisoners - but Commander Lambda isnt about to let you get away that easily. She's sent her elite fighter pilot squadron after you - and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Commander Lambdas assistant, she asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function answer(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the answer would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_n = "5"
Output:
    (string) "19"

Inputs:
    (string) str_n = "77"
Output:
    (string) "4208"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''

# https://en.wikipedia.org/wiki/Beatty_sequence
# Compliment of Beatty Sequence floor(n*sqrt(2)) is floor(n*(2 + sqrt(2))) or 2*n+floor(n*sqrt(2))
# https://oeis.org/A001951
# https://oeis.org/A001952
# Thus (handwavy) recurrence: {sequence} = {all numbers} - {2*n+sequence}!
# Therefore grow the sequence iteratively and exponentially
from collections import deque
import math as m

def answer(str_n):
    n = int(str_n)
    if (n>m.pow(10,15)):
        return 0
    if (n==0):
        return 0
    if (n==1):
        return 1
    if (n==2):
        return 3

    count_so_far = 2
    sum_so_far = 3     # Sum from floor(1*sqrt(2)) till floor(count_so_far*sqrt(2))

    second = 3
    comp = deque([6])
    
    while True:
        first = second
        second = comp.popleft()

        for x in xrange(first+1,second):
            count_so_far += 1
            sum_so_far += x
            comp.append(2*count_so_far+x)

            if(count_so_far >= n):
                return sum_so_far;

    return sum_so_far
