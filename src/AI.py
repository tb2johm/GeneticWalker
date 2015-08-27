import Nodes
import random

treeList = []

for i in xrange(0,100):
    try:
        tree = Nodes.generateNodes()
    except RuntimeError:
        tree = None
        print Nodes.depth
    except Exception:
        tree = None

    treeList.append(tree)

for i in xrange(0, len(treeList)):
    print str(treeList[i])

for i in xrange(0, len(treeList)):
    a = treeList(random.randint(0, len(treeList)))
    b = treeList(random.randint(0, len(treeList)))
    c = treeList(random.randint(0, len(treeList)))
    d = treeList(random.randint(0, len(treeList)))

    
