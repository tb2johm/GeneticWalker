#!/usr/bin/env python
import Track
from Nodes import SensorNode, MoveNode, EvaluateTree, coord, setPos, getPos, setTrack

def main():
    setTrack(Track.Track().track)

    """Testing SensorNode"""

    sn = SensorNode(0, 0)
    setPos(coord(5, 5))
    for i in xrange(0,7):
        sn.direction = i
        result = sn.getResult()
        assert result == 0

    setPos(coord(5, 1))

    sn.direction = 0
    res = sn.getResult()
    assert res == 1

    sn.direction = 2
    res = sn.getResult()
    assert res == 0

    """Testing MoveNode"""

    mn = MoveNode(0,0)
    res = EvaluateTree(Track.Track().track, coord(5,1), mn)
    assert res == -1

    mn.direction = 1
    res = EvaluateTree(Track.Track().track, coord(5,1), mn)
    assert res == 1

    """Testing moveCounting"""

    t = Track.Track()
    mn = MoveNode(0,0)
    res = EvaluateTree(t.track, coord(5,5), mn)
    assert res == 0
    res = EvaluateTree(t.track, getPos(), mn)
    assert res == 0
    res = EvaluateTree(t.track, getPos(), mn)
    assert res == 0
    res = EvaluateTree(t.track, getPos(), mn)
    assert res == 1
    res = EvaluateTree(t.track, getPos(), mn)
    assert res == -1


if __name__ == "__main__":
    main()
