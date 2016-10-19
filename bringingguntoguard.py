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
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

    def magsqr(A):
        return (pow(A[0], 2) + pow(A[1], 2))

    def simplifyVector(A):
        # gcd cannot handle if any number is 0
        abs0 = abs(A[0])
        abs1 = abs(A[1])
        if ((A[0]==0) and (A[1]==0)):
            return (0, 0)
        if (A[0]==0):
            return (0, A[1]/abs1 )
        if (A[1]==0):
            return ( A[0]/abs0 ,0)
        vecgcd = gcd(abs0,abs1)
        return ( A[0]/vecgcd , A[1]/vecgcd )

    # direction vector (string of (int,int)) -> distance^2 to closest guard copy along that direction
    guardDirections = {}
    # direction vector (string of (int,int)) -> distance^2 to closest captain copy along that direction
    yourDirections = {}

    gL, gR, gT, gB = guard_position[0], dimensions[0] - guard_position[0], dimensions[1] - guard_position[1], guard_position[1]
    mL, mR, mT, mB = your_position[0], dimensions[0] - your_position[0], dimensions[1] - your_position[1], your_position[1]

    # Create dictionary of guardDirections and yourDirections as described
    row_range, column_range = distance/dimensions[0], distance/dimensions[1]
    for x in xrange(-row_range-1, row_range+1):
        for y in xrange(-column_range-1, column_range+1):
            gHstep = int(m.ceil(x*0.5)*2*gR + m.floor(x*0.5)*2*gL)
            gVstep = int(m.ceil(y*0.5)*2*gT + m.floor(y*0.5)*2*gB)
            mHstep = int(m.ceil(x*0.5)*2*mR + m.floor(x*0.5)*2*mL)
            mVstep = int(m.ceil(y*0.5)*2*mT + m.floor(y*0.5)*2*mB)

            # Note these "positions" are actually "directions" and have origin at your_position
            guard_new_pos = (guard_position[0] + gHstep - your_position[0], guard_position[1] + gVstep - your_position[1])
            your_new_pos = (mHstep, mVstep)

            
            guard_new_pos_magsqr = magsqr(guard_new_pos)
            your_new_pos_magsqr = magsqr(your_new_pos)

            if (guard_new_pos_magsqr <= distance*distance):
                guard_new_pos_dir = simplifyVector(guard_new_pos)
                if `guard_new_pos_dir` in guardDirections:
                    if (guardDirections[`guard_new_pos_dir`] > guard_new_pos_magsqr):
                        guardDirections[`guard_new_pos_dir`] = guard_new_pos_magsqr
                else:
                    guardDirections[`guard_new_pos_dir`] = guard_new_pos_magsqr

            if ( (your_new_pos_magsqr <= distance*distance) and (your_new_pos_magsqr > 0) ):
                your_new_pos_dir = simplifyVector(your_new_pos)
                if `your_new_pos_dir` in yourDirections:
                    if (yourDirections[`your_new_pos_dir`] > your_new_pos_magsqr):
                        yourDirections[`your_new_pos_dir`] = your_new_pos_magsqr
                else:
                    yourDirections[`your_new_pos_dir`] = your_new_pos_magsqr
     
    #print 'guardDirections',guardDirections
    #print 'yourDirections',yourDirections

    # Count valid guard positions:
    # If there is a direction to a guard copy with no captain copy on it or
    # has the closest guard copy closer than the closest captain copy then
    # is counted as a valid firing direction
    count = 0 
    for guarddir, mindistsqr in guardDirections.iteritems():
        if guarddir in yourDirections:
            if (yourDirections[guarddir] > mindistsqr):
                count += 1
                #print 'hitguard:',guarddir
            #else:
                #print 'hitme:',guarddir
        else:
            #print 'hitguard:',guarddir
            count+=1

    return count

#print answer([300,275], [150,150], [185,100], 500)
