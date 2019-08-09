__author__ = 'Steven Bustos'

import sys

sys.setrecursionlimit( 3*10000 )

# Funcion para hacer un link
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

N = int(sys.stdin.readline().strip())
n = (sys.stdin.readline().strip()).split()

color = {}
for j in xrange(len(n)):
    color[j+1] = n[j]

print color

Lines = sys.stdin.readlines()
G1 = {}
for i in Lines:
    m,n = map(int, i.strip().split())
    print m,n

    make_link(G1, m, n)
print G1
    