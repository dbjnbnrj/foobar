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

str_n will be a positive integer between 1 and 10^100, inclusive.
Since n can be very large (up to 101 digits!),
using just sqrt(2) and a loop won't work.
Sometimes, it's easier to take a step back and concentrate
not on what you have in front of you, but on what you don't.

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



    for i in xrange(N+1):
        s+=LW(i)
'''

import math as m
from decimal import *

getcontext().prec = 1000

sq = Decimal(2).sqrt()
LW = lambda x : Decimal(Decimal(x) * sq).quantize(Decimal('1.'), rounding=ROUND_DOWN)
UW = lambda x : Decimal(Decimal(x) * (sq+2)).quantize(Decimal('1.'), rounding=ROUND_DOWN)


def getSum(num):
    return num*(num+1)/2

def getMid(N):
    mid = long(N*sq/(2+sq))
    #print mid, UW(mid), LW(N)
    return mid

def getResult1(N):
    result= 0
    for i in xrange(N+1):
        result+= LW(i)
    return result

def getResult2(N, N1, N2):
    return getSum(LW(N)) - getSum(N1)*2 - N2

def getResult(N, M):
    return getSum(LW(N)) - sum([UW(i) for i in range(M)])

def answer(str_n):
    N = long(str_n)

    mid = getMid(N)
    A = [N, mid]
    LIM = pow(10,4)
    result = 0

    if mid <= LIM:
        result = getSum(LW(N)) -sum([UW(i) for i in xrange(mid+1)])
    else:
        while mid > LIM:
            mid = getMid(mid)
            A+= [mid]
        N1 = A[-1]
        temp = getResult2(A[-2], A[-1], sum([LW(i) for i in xrange(N1+1)]))
        A.pop()

        while len(A) > 1:
            N1 = A[-1]
            result = getResult2(A[-2], A[-1], temp)
            temp = result
            A.pop()

    return '{0:f}'.format(result)

print answer(10**100)
