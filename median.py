__author__ = 'Steven Bustos'

import sys

def num_format(m):
    # Format the result without trailing zeros
    format = "%d" if m.is_integer() else "%s"    
    print(format % m)

def median(limin, limax):
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
        num_format(m)
    elif( len(limax) == len(limin) > 1):
        minN = float(limin[len(limin)-1])
        maxN = float(limax[0])
        m = float((minN+maxN)/2)
        num_format(m)
    else:
        print ("Wrong!")

def n2rule(limin, limax):
    # Fixing the n/2 rule in both lists
    if( len(limax) > len(limin) ):
        m = limax.pop(0)
        limin.append(m)
        limin.sort()
    elif( len(limin) > len(limax)+1 ):
        m = limin.pop()
        limax.append(m)
        limax.sort()

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

    # Adding or removing elements in both lists
    if( o == 'a' ):
        if( len(limin) == 0 ):
            limin.append(n)
            n2rule(limin, limax)
            median(limin, limax)
        else:
            if( n > max(limin) ):
                limax.append(n)
                limax.sort()
                n2rule(limin, limax)
                median(limin, limax)    
            else:
                limin.append(n)
                limin.sort()
                n2rule(limin, limax)
                median(limin, limax)
    elif ( o == 'r' ):
        if( limin.count(n) >= 1 ):
            limin.remove(n)
            n2rule(limin, limax)
            median(limin, limax)
        elif( limax.count(n) >= 1 ):
            limax.remove(n)
            n2rule(limin, limax)
            median(limin, limax)
        else:
            print ("Wrong!")
