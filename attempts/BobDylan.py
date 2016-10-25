# BobDylan.py - our implementation of the Incremental Conceptual Clustering
from Node import *


def BobDylan(N, O):
    # Add Object to the hierarchy represented by Node

    if N.isLeaf() and (N.objects == []):
        print "case with empty tree"
        # first entry just put one child in!
        C = Node()
        N.appendChildObj(C)

        C.addObjectsStats(O)
        C.addObject(O)

        N.addObjectsStats(O)
        #N.updateCountMatrixFromChildren()

    elif N.isLeaf():
        print "inserting in leaf"
        # insert here
        C1 = Node()
        C2 = Node()
        N.appendChildObj(C1)
        N.appendChildObj(C2)

        C1.setCountMatrix( N.getCountMatrix() )
        C1.objects =  N.objects

        C2.addObjectsStats(O)
        C2.addObject(O)

        N.addObjectsStats(O)
        #N.updateCountMatrixFromChildren()

        #N.reportTree()
        #print N.listAllObjects()

    else:
        print "case two"
        # figure out what to do next
        N.addObjectsStats(O)

        AllLists = N.getAllListsFromChildren()
        CU_Child_Pairs = []

        print AllLists

        for child_idx in N.children_indices:
            child = N.getChildrenById(child_idx)

    
    return ""



O1 = {'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O2 = {'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
Objects = [O1, O2]
#Objects = [O1]

Root = Node()
#Root.reportTree()

for Object in Objects:
    #print Object
    BobDylan( Root, Object )
    Root.reportTree()


#print "Final Tree:"
#Root.reportTree()
