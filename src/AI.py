import Nodes
import Track

import random

treeList = []

for i in xrange(0,50):
    tree = Nodes.generateNodes()

    treeList.append(tree)

for i in xrange(0, len(treeList)):
    print str(treeList[i])

for i in xrange(0, len(treeList)):
    a = treeList[random.randint(0, len(treeList)) - 1]
    b = treeList[random.randint(0, len(treeList)) - 1]
    c = treeList[random.randint(0, len(treeList)) - 1]
    d = treeList[random.randint(0, len(treeList)) - 1]

pointA = Evaluate(a, Track.track)

def Evaluate(tree, track):
    startingPoint=[5,5]
    moves = 0
