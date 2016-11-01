# BobDylan.py - our implementation of the Incremental Conceptual Clustering
from Node import *
from CU_measure import *
import copy

def BobDylan(N, O):
    verbose = False
    # Add Object to the hierarchy represented by Node
    
    if N.isLeaf() and (N.objects == []):
        # first entry just put one child in!
        C = Node()
        N.appendChildObj(C)

        C.addObjectsStats(O)
        C.addObject(O)

        N.addObjectsStats(O)

    elif N.isLeaf():
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
        
    else:
        # figure out what to do next
        N.addObjectsStats(O)

        AllListsWithIdx = N.getAllListsFromChildrenWithIdx()
        AllLists = []
        for i in range(0,len(AllListsWithIdx)):
            AllLists.append(AllListsWithIdx[i][0])
        CU_Child_Pairs = []
        #
        '''
        print "ALL-LISTS"
        DebugClusters(AllLists, NAME_CAT)
        print "-"
        AllLists = N.getAllListsFromChildren()
        print "ALL-LISTS"
        DebugClusters(AllLists, NAME_CAT)
        print "-"
        '''

        for i in range(0, len(AllLists)):
            # for node N and its children C1 to Cn
            # for i = 1 ... n
            # merge Ci with O
            selList = AllLists[i]
            selList.append(O)

            withoutSel = AllLists[:i] + AllLists[(i + 1):]
            # get CU measure evaluation for clusters as [C1, ... Ci+O, ... Cn]
            withoutSel.append(selList)

            clusters = withoutSel
            
            if verbose:
                DebugClusters(withoutSel, NAME_CAT)
            cu = CU(clusters, attributes)

            #CU_Child_Pairs.append([cu, AllListsWithIdx[i][1]])
            CU_Child_Pairs.append([cu, i])

            selList.remove(O)

        CU_Child_Pairs = sorted(CU_Child_Pairs, key=lambda x: (-x[0]))
        if verbose:
            print CU_Child_Pairs

        Cfirst_index = CU_Child_Pairs[0][1]
        Cfirst = N.getChildrenById(Cfirst_index)
        Cfirst_score = CU_Child_Pairs[0][0]
        Csecond_index = CU_Child_Pairs[1][1]
        Csecond = N.getChildrenById(Csecond_index)

        # singleton score
        SingletonList = AllLists + [[O]]
        if verbose:
            DebugClusters(SingletonList, NAME_CAT)
        singletonScore = CU(SingletonList, attributes)
        if verbose:
            print singletonScore

        # split score
        # split the best one into all its children!
        splitScore = 0
        if not Cfirst.isLeaf():
            SplitListWithIdx = copy.copy(AllListsWithIdx)
            SplitList = []
            for i in range(0,len(SplitListWithIdx)):
                if Cfirst_index <> SplitListWithIdx[i][1]:
                    SplitList.append(SplitListWithIdx[i][0])
            #del SplitList[Cfirst_index]
            
            for child_idx in Cfirst.children_indices:
                child = Cfirst.getChildrenById(child_idx)
                SplitList.append( child.listAllObjects() )

            #DebugClusters(SplitList, NAME_CAT)
            splitScore = CU(SplitList, attributes)
            #print splitScore


        # merge score
        mergeScore = 0
        if (not(Cfirst.isLeaf()) and not(Csecond.isLeaf())):
            MergeList = copy.copy(AllLists)
            a = Cfirst_index
            b = Csecond_index
            if b > a:
                a = Csecond_index
                b = Cfirst_index
            del MergeList[a]
            del MergeList[b]

            MergeList.append( AllLists[a] + AllLists[b] + [O] )
            
            #DebugClusters(MergeList, NAME_CAT)
            mergeScore = CU(MergeList, attributes)
            #print "mergescore: ", mergeScore
            
        # if C1 score is biggest?
        if (Cfirst_score > singletonScore) and (Cfirst_score > mergeScore) and (Cfirst_score > splitScore):
            print "best ", Cfirst.node_index
            
            BobDylan(Cfirst, O)

        # if singleton score is the best?
        elif (singletonScore > mergeScore) and (singletonScore > splitScore):
            S = Node()
            S.addObjectsStats(O)
            S.addObject(O)

            print "new ", S.node_index
            
            N.appendChildObj(S)

        # is merge score is the best?
        elif (mergeScore > splitScore):
            print "merge"
            # CM = merged node from C1 and C2
            Cm = Node()

            for idx in Cfirst.children_indices:
                Cm.appendChild(idx)
            for idx in Csecond.children_indices:
                Cm.appendChild(idx)

            Cm.updateCountMatrixFromChildren()

            # remove those two
            a = Cfirst_index
            b = Csecond_index
            if b > a:
                a = Csecond_index
                b = Cfirst_index

            if verbose:
                print "rem ", a, b, ", new ", Cm.node_index

            N.removeChild(a)
            N.removeChild(b)

            # and connect it
            N.appendChildObj(Cm)
            BobDylan(Cm, O)
            
        # is split score is the best?
        else:
            print "split ", Cfirst_index

            SplitNode = Cfirst

            for idx in SplitNode.children_indices:
                N.appendChild(idx)

            N.removeChild(Cfirst_index)
            
            # also new node
            S = Node()
            S.addObjectsStats(O)
            S.addObject(O)
            N.appendChildObj(S)

            N.updateCountMatrixFromChildren()



O1 = {NAME_CAT: 'fish', 'BodyCover': 'scales', 'HeartChamber': 'two', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O2 = {NAME_CAT: 'amphibian', 'BodyCover': 'moist-skin', 'HeartChamber': 'three', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}

O3 = {NAME_CAT: 'mammal', 'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O4 = {NAME_CAT: 'bird', 'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O5 = {NAME_CAT: 'reptile', 'BodyCover': 'cornified-skin', 'HeartChamber': 'imperfect-four', 'BodyTemp': 'unregulated', 'Fertilization': 'internal'}
#Objects = [O1, O2]
#Objects = [O3, O4, O5]

Objects = [O3, O4, O5, O5, O5]


Root = Node()

N1 = Node()
N1.addObjectsStats(O1)
N1.addObject(O1)

N2 = Node()
N2.addObjectsStats(O2)
N2.addObject(O2)

Root.appendChildObj( N1 )
Root.appendChildObj( N2 )

Root.updateCountMatrixFromChildren()

for Object in Objects:
    BobDylan( Root, Object )

    #Root.reportTree()

print "\nFinal tree structure:"
Root.reportTree()
