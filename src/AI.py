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

    totalGenWinner = None
    totalGenWinnerPoints = 0
    genWinnerTrack = None

    for i in xrange(0, len(treeList)):
        a = treeList[random.randint(0, len(treeList)) - 1]
        b = treeList[random.randint(0, len(treeList)) - 1]
        c = treeList[random.randint(0, len(treeList)) - 1]
        d = treeList[random.randint(0, len(treeList)) - 1]

        ta = Track.Track()
        tb = Track.Track()
        pointA = Evaluate(a, ta.track)
        pointB = Evaluate(b, tb.track)
        if a > b:
            winner1 = a
            looser1 = b
            if pointA > totalGenWinnerPoints:
                totalGenWinnerPoints = pointA
                totalGenWinner = a
                genWinnerTrack = ta
        else:
            winner1 = b
            looser1 = a
            if pointB > totalGenWinnerPoints:
                totalGenWinnerPoints = pointB
                totalGenWinner = b
                genWinnerTrack = tb

        tc = Track.Track()
        td = Track.Track()
        pointC = Evaluate(c, tc.track)
        pointD = Evaluate(d, td.track)
        if c > d:
            winner2 = c
            looser2 = d
            if pointC > totalGenWinnerPoints:
                totalGenWinnerPoints = pointC
                totalGenWinner = c
                genWinnerTrack = tc
        else:
            winner2 = d
            looser2 = c
            if pointD > totalGenWinnerPoints:
                totalGenWinnerPoints = pointD
                totalGenWinner = d
                genWinnerTrack = td

        (looser1, looser2) = Nodes.merge(winner1, winner2)

    print "Total generation winner, with %d points is: %s" % (totalGenWinnerPoints, totalGenWinner)
    print genWinnerTrack

        #print "tree:", str(treeList[i]), "got:", pointA

def Evaluate(tree, track):
    startingPoint=Nodes.coord(5,5)
    moves = 0

    result = 0
    for x in xrange(0,59):
        res = Nodes.EvaluateTree(track, startingPoint, tree)
        #print "Result of tree", str(tree), ":", result
        if res == -1:
            return result
        result += res

    return result


if __name__ == "__main__":
    main()
