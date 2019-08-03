__author__ = 'Steven Bustos'

import sys

T = int(sys.stdin.readline().strip())

# Lists that contains the numbers
# limin contains the numbers below n/2
limin = []
# limax contains the numbers above n/2
limax = []

while ( T > 0 ):
    T -= 1
    o, n = (sys.stdin.readline().strip()).split()
    n = int(n)
    # print o, n

    # Adding or removing elements in both lists
    if( o == 'a' ):
        if( len(limin) == 0 ):
            limin.append(n)
        else:
            if( n > max(limin) ):
                limax.append(n)
                limax.sort()
            else:
                limin.append(n)
                limin.sort()
    elif ( o == 'r' ):
        if( limin.count(n) >= 1 ):
            limin.remove(n)
        elif( limax.count(n) >= 1 ):
            limax.remove(n)

    # Fixing the n/2 rule in both lists
    if( len(limax) > len(limin) ):
        m = limax.pop(0)
        limin.append(m)
        limin.sort()
    elif( len(limin) > len(limax)+1 ):
        m = limin.pop()
        limax.append(m)
        limax.sort()

    # Calculing the media
    if( len(limin) > len(limax) ):
        m = limin[-1]
        print m
    elif( len(limax) > len(limin) ):
        m = limax[0]
        print m
    elif( len(limax) == len(limin) == 1):
        minN = float(limin[0])
        maxN = float(limax[0])
        m = float((minN+maxN)/2)
        print (round(m, 1))
    elif( len(limax) == len(limin) > 1):
        minN = float(limin[len(limin)-1])
        maxN = float(limax[0])
        m = float((minN+maxN)/2)
        print (round(m, 1))
    else:
        print ("Wrong!")
