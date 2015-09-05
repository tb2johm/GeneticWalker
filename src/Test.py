#!/usr/bin/env python

import Nodes
import Track

def main():
    Nodes.track = Track.Track.track

    """Testing SensorNode"""

    sn = Nodes.SensorNode(0, 0)
    Nodes.position = [5,5]
    for i in xrange(0,7):
        sn.direction = i
        result = sn.getResult()
        assert result == 0

    Nodes.position = [1,5]

    sn.direction = 0
    res = sn.getResult()
    assert res == 1

    sn.direction = 2
    res = sn.getResult()
    assert res == 0

    """Testing MoveNode"""

    mn = Nodes.MoveNode(0,0)
    res = Nodes.EvaluateTree(Track.Track.track, [1,5], mn)
    assert res == -1

    mn.direction = 1
    res = Nodes.EvaluateTree(Track.Track.track, [1,5], mn)
    assert res == 1

if __name__ == "__main__":
    main()
