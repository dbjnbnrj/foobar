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
'''


import math as m
import time as t
import math as m
import time as t
def answer(str_n):
    if len(str_n) > 18:
        return 0
    N = int(str_n)
    LW = lambda x : m.floor(x*m.sqrt(2))
    UW = lambda x : m.floor(x*(2+m.sqrt(2)))

    def getSum(num):
        return num*(num+1)/2

    def getMid(N):
        #print m.log(N, 10)
        start, end= 0, N
        mid = m.floor((end + start)/2)
        num = LW(N)
        steps = 0
        while True:
            if start > end:
                break
            steps +=1
            mid = m.floor((end + start)/2)
            if UW(mid) < num < UW(mid+1):
                print 'steps; ',steps, N
                return int(mid)
            elif UW(mid) < num:
                start = mid + 1
            else:
                end = mid - 1

        return int(mid)

    def getResult(x, y):
        return getSum(LW(x)) - sum([UW(i) for i in range(y+1)])

    mid = getMid(N)
    A = [N, mid]
    #print N, mid
    LIM = pow(10, 6)
    if mid < LIM:
        result = getSum(LW(N)) - mid*(mid+1) - sum([LW(i) for i in range(mid+1)])
    else:
        mid = getMid(N)
        A = [N, mid]
        while mid >= LIM:
            mid = getMid(mid)
            A+= [mid]

        mid1, num1 = A.pop(), A.pop()
        #print mid1, num1
        temp1 = getSum(LW(num1)) - mid1*(mid1+1) - sum([LW(i) for i in range(mid1 +1)])
        A+=[num1]
        while len(A) > 1:
            #print A
            mid2, num2 = A.pop(), A.pop()
            temp2 = getSum(LW(num2)) - mid2*(mid2+1) - temp1
            temp1 = temp2
            A+=[num2]
        result = temp1
    s = '%d' % result
    return s.rstrip('.0')
    #return temp1



print answer("5")
print answer("77")
print answer("775")
print answer(`pow(10, 16)`)
