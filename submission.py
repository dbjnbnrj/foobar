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
