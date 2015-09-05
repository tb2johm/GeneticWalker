#!/usr/bin/env python

import Nodes
import Track

import random

def main():
    treeList = []

    for i in xrange(0,5000):
        tree = Nodes.generateNodes()

        treeList.append(tree)

    #for i in xrange(0, len(treeList)):
    #    print str(treeList[i])

    for i in xrange(0, len(treeList)):
        #a = treeList[random.randint(0, len(treeList)) - 1]
        #b = treeList[random.randint(0, len(treeList)) - 1]
        #c = treeList[random.randint(0, len(treeList)) - 1]
        #d = treeList[random.randint(0, len(treeList)) - 1]

        pointA = Evaluate(treeList[i], Track.Track.track)
        if pointA > 1: print "tree:", str(treeList[i]), "got:", pointA

def Evaluate(tree, track):
    startingPoint=[5,5]
    moves = 0

    result = 0
    for x in xrange(0,59):
        res = Nodes.EvaluateTree(track, startingPoint, tree)
        #print "Result of tree", str(tree), ":", result
        if res == -1:
            return -1
        result += res

    return result


if __name__ == "__main__":
    main()
