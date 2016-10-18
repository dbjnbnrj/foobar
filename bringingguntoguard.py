'''
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards!
Fortunately, you grabbed a beam weapon from an abandoned guardpost while you were running through the station,
so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard:
its beams reflect off walls, meaning youll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance
before becoming too weak to cause damage. You also know that if a beam hits a corner,
it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard,
it will stop immediately (albeit painfully).

Write a function answer(dimensions, your_position, guard_position, distance) that gives an array of 2 integers
of the width and height of the room, an array of 2 integers of your x and y coordinates in the room,
an array of 2 integers of the guard's x and y coordinates in the room,
and returns an integer of the number of distinct directions
that you can fire to hit the elite guard,
given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1000, 1 < y_dim <= 1000].
You and the elite guard are both positioned on the integer lattice at different distinct positions
(x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance
that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2],
you_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot
in seven different directions to hit the elite guard (given as vector bearings from your location):
[1, 0], [1, 2], [1, -2], [3, 2], [-3, 2], [3, -2] and [-3, -2].
As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1,
the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the
elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just
the top wall before hitting the elite guard with a total shot distance of sqrt(5).


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) dimensions = [3, 2]
    (int list) captain_position = [1, 1]
    (int list) badguy_position = [2, 1]
    (int) distance = 4
Output:
    (int) 7

Inputs:
    (int list) dimensions = [300, 275]
    (int list) captain_position = [150, 150]
    (int list) badguy_position = [185, 100]
    (int) distance = 500
Output:
    (int) 9

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
'''

import math as m

def answer(dimensions, your_position, guard_position, distance):

    def dist(A, B):
        return m.sqrt(pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2))

    def is_between(a,c, b):
        if isEqual(a, c) and isEqual(b, c):
            return False
        return ( dist(a,c) + dist(c,b) )== dist(a,b)


    def getVector(A,B,D):
        if D > 0:
            return ( (A[0] - B[0]) / D, (A[1] - B[1]) / D)
        return ( (A[0] - B[0]) , (A[1] - B[1]) )

    def isEqual(A,B):
        return A[0] == B[0] and A[1] == B[1]

    L, R = guard_position[0], dimensions[0] - guard_position[0]
    T, B = dimensions[1] - guard_position[1], guard_position[1]

    mL, mR, mT, mB = your_position[0], dimensions[0] - your_position[0], dimensions[1] - your_position[1], your_position[1]
    count = 0

    row_range, column_range = distance/dimensions[0], distance/dimensions[1]
    cache = {}
    for x in xrange(-row_range-2, row_range+2):
        for y in xrange(-column_range-2, column_range+2):
            hstep = m.ceil(x*0.5)*2*R + m.floor(x*0.5)*2*L
            vstep = m.ceil(y*0.5)*2*T + m.floor(y*0.5)*2*B

            mhstep = m.ceil(x*0.5)*2*mR + m.floor(x*0.5)*2*mL
            mvstep = m.ceil(y*0.5)*2*mT + m.floor(y*0.5)*2*mB
            guard_new_pos = (guard_position[0] + hstep, guard_position[1] + vstep)
            your_new_pos = (your_position[0] + mhstep, your_position[1] + mvstep)

            crossed_captain = is_between(your_position, your_new_pos, guard_new_pos)
            crossed_guard = is_between(your_position, guard_position, guard_new_pos)
            D = dist(your_position, guard_new_pos)
            C = dist(your_position, your_new_pos)
            if D <= distance:
                vec = getVector(your_position, guard_new_pos, D)
                cvec = getVector(your_position, your_new_pos, C)
                if `vec` in cache or `cvec` in cache or isEqual(cvec, vec):
                    continue
                else:
                    cache[`vec`] = True
                    count +=1
    return count

print answer( [3, 2], [1, 1],[2, 1], 4)
print answer( [300, 275],  [150, 150], [185, 100], 500)
#print answer( [1000, 1000],  [999, 999], [998, 999], 10000)
