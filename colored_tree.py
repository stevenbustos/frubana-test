# coding=utf-8
__author__ = 'Steven Bustos'

import sys

# Funcion para hacer un link y construir el grafo
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

# Funciones para calcular el camino de un nodo a otro
def DFS_Visit_p(G, node, color, parent):
    color[node] = 'gray'
    total_marked = 1
    for neighbor in G[node]:
        if color[neighbor] == 'white':
            parent[neighbor] = node
            total_marked += DFS_Visit_p(G, neighbor, color, parent)
    color[node] = 'black'
    return total_marked

# Funcion modificada de para calcular el camino de un nodo a otro
def path(G, v1, v2, colour):
    color = {}
    parent = {}
    for v in G:
        color[v] = 'white'
        parent[v] = None
    DFS_Visit_p(G, v1, color, parent)
    pathlist = []
    node = v2
    while node <> None:
        nodex = {}
        nodex[node] = colour[node]
        pathlist.append(int(colour[node]))
        node = parent[node]
    if color[v2] == 'black':
        return pathlist[::-1] # los vértices en pathlist están en orden inverso, [::-1] los invierte
    else:
        return []

N = int(sys.stdin.readline().strip())
n = (sys.stdin.readline().strip()).split()

colour = {}
for j in xrange(len(n)):
    colour[j+1] = n[j]

Lines = sys.stdin.readlines()
G1 = {}
for i in Lines:
    m,n = map(int, i.strip().split())
    make_link(G1, m, n)

for v1 in G1:
    sumx = 0
    for v2 in G1:
        suma = 1
        arr = list(set(path(G1, v1, v2, colour)))
        for (x, y) in zip(arr[:-1], arr[1:]):
            if x == y:
                suma += 0
            else:
                suma += 1
        sumx += suma
    print sumx