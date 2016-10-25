# BobDylan.py - our implementation of the Incremental Conceptual Clustering
from Node import *
from CU_measure import *

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

        #AllLists = range(1,5)
        #print AllLists

        for i in range(0, len(AllLists)):
            # for node N and its children C1 to Cn
            # for i = 1 ... n
            # merge Ci with O
            selList = AllLists[i]
            selList.append(O)

            withoutSel = AllLists[:i] + AllLists[(i + 1):]
            # get CU measure evaluation for clusters as [C1, ... Ci+O, ... Cn]
            withoutSel.append(selList)

            # for debug
            clusters = withoutSel
            
            DebugClusters(withoutSel, 'BodyCover')
            cu = CU(clusters, attributes)

            CU_Child_Pairs.append([cu, i])

            selList.remove(O)

        CU_Child_Pairs = sorted(CU_Child_Pairs, key=lambda x: (-x[0]))
        print CU_Child_Pairs

        Cfirst_index = CU_Child_Pairs[0][1]
        Cfirst_score = CU_Child_Pairs[0][0]
        Csecond_index = CU_Child_Pairs[1][1]

        # singleton score
        SingletonList = AllLists + [[O]]
        DebugClusters(SingletonList, 'BodyCover')
        singletonScore = CU(SingletonList, attributes)
        print singletonScore

        # if C1 score is biggest?
        if (Cfirst_score > singletonScore):
            print "best is to add it to C1"
            BobDylan(N.getChildrenById(Cfirst_index), O)

        # if singleton score is the best?
        else:
            print "best is to create new singleton"
            S = Node()
            S.addObjectsStats(O)
            S.addObject(O)

            N.appendChildObj(S)
        
    return ""



O1 = {'BodyCover': 'scales', 'HeartChamber': 'two', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O2 = {'BodyCover': 'moist-skin', 'HeartChamber': 'three', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O3 = {'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}

O4 = {'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O5 = {'BodyCover': 'cornified-skin', 'HeartChamber': 'imperfect-four', 'BodyTemp': 'unregulated', 'Fertilization': 'internal'}
#Objects = [O1, O2]
Objects = [O3, O4]

Root = Node()
#Root.reportTree()

N1 = Node()
N1.addObjectsStats(O1)
N1.addObject(O1)

#N1.addObjectsStats(O4)
#N1.addObject(O4)

N2 = Node()
N2.addObjectsStats(O2)
N2.addObject(O2)

Root.appendChildObj( N1 )
Root.appendChildObj( N2 )

Root.updateCountMatrixFromChildren()

for Object in Objects:
    #print Object
    BobDylan( Root, Object )
    Root.reportTree()


#print "Final Tree:"
#Root.reportTree()
