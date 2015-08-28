import random

depth = 0

class BaseNode:

    parent = None

    def __init__(self, nr):
        self.depth = nr

    def __str__(self):
        return "BaseNode"

    def getResult(self):
        return False

class AndNode(BaseNode):

    a = None
    b = None

    def __init__(self, nr):
        self.depth = nr
        self.a = randomizeNodes()
        self.b = randomizeNodes()

    def __str__(self):
        return "(" + str(self.a) + " && " + str(self.b) + ")"

    def getResult(self):
        return self.a.getResult() and self.b.getResult()


class OrNode(BaseNode):

    a = None
    b = None

    def __init__(self, nr):
        self.depth = nr
        self.a = randomizeNodes()
        self.b = randomizeNodes()

    def __str__(self):
        return "(" + str(self.a) + " || " + str(self.b) + ")"

    def getResult(self):
        return self.a.getResult() or self.b.getResult()

class NotNode(BaseNode):

    a = None

    def __init__(self, nr):
        self.depth = nr
        self.a = randomizeNodes()

    def __str__(self):
        return "!(" + str(self.a) + ")"

    def getResult(self):
        return not(self.a.getResult())

class IfNode(BaseNode):

    a = None
    b = None
    c = None

    def __init__(self, nr):
        self.depth = nr
        self.a = randomizeNodes()
        self.b = randomizeNodes()
        self.c = randomizeNodes()

    def __str__(self):
        return "((" + str(self.a) + ")?(" + str(self.b) + "):(" + str(self.c) + "))"

    def getResult(self):
        return self.a.getResult() if self.b.getResult() else self.c.getResult()

class SensorNode(BaseNode):

    #directions = dict(N = 1, NE = 2, E = 3, ES = 4, S = 5, SW = 6, W = 7, NW = 8)
    directions = ["N", "NE", "E", "ES", "S", "SW", "W", "NW"]

    direction = 0
    tile = None

    def __init__(self, nr, d):
        self.depth = nr
        if d < 0 or d > len(self.directions) - 1:
            raise ValueError("0 > " + str(d) + " < " + str(len(self.directions) - 1))
        self.direction = d

    def __str__(self):
        return "S[" + self.directions[self.direction] + "]"

    def getResult(self):
        return self.tile

class MoveNode(BaseNode):

    directions = ["N", "E", "S", "W"]

    direction = 0

    def __init__(self, nr, d):
        self.depth = nr
        if d < 0 or d > len(self.directions) - 1:
            raise ValueError("0 > " + str(d) + " < " + str(len(self.directions) - 1))
        self.direction = d

    def __str__(self):
        return "M[" + self.directions[self.direction] + "]"

    def getResult(self):
        pass

def randomizeNodes():
    global depth

    minRand = 0

    depth = depth + 1
    if depth > 60:
        minRand = 4

    rnd = random.randint(0, 15)

    if rnd == 0:
        return AndNode(depth)
    elif rnd == 1:
        return OrNode(depth)
    elif rnd == 2:
        return NotNode(depth)
    elif rnd == 3:
        return IfNode(depth)
    elif rnd >= 4 and rnd <= 11:
        return SensorNode(depth, random.randint(0,7))
    elif rnd >= 12 and rnd <= 15:
        return MoveNode(depth, random.randint(0,3))


def generateNodes():
    global depth
    depth = 0
    return randomizeNodes()
