# Node class
from collections import defaultdict
from Attributes import *

class Node:
    '''
    Node in the concept cluster hierarchy
    '''
    node_index = -1

    # Descriptive part - which variables will describe the node
    number_of_objects = 0
    countMatrix = defaultdict(list) # null, needs initialization
    # adressing: self.countMatrix[<attrib>][<val>] --> <count>
    children_indices = []
    objects = [] # only LEAF, node with no children has objects


    # Funcitonal part - nodes functionality

    def __init__(self):
        # empty node
        global current_node_index
        self.node_index = current_node_index
        current_node_index += 1
        global NODES
        NODES.append(self)
        
        # init as individual vars
        self.number_of_objects = 0
        countMatrix = defaultdict(list) 
        self.children_indices = []
        self.objects = []
        
        self.initCountMatrix()

    def initCountMatrix(self):
        global attributes
        for attrib in attributes:
            #print attrib
            self.countMatrix[attrib] = defaultdict(list)
            for val in attributes[attrib]:
                #print val
                self.countMatrix[attrib][val] = 0
                
        #print "Counts: ", self.countMatrix.items()
        #print self.countMatrix['BodyCover']['hair']

    def addObjectsStats(self, Object):
        # updates the number_of_objects and countMatrix, not children
        # because children points to hierarchy of nodes, whereas the counts talk about the objects belonging to the nodes
        self.number_of_objects += 1

        for attrib in Object:
            val = Object[attrib]
            self.countMatrix[attrib][val] += 1

    def addObject(self, Object):
        self.objects.append(Object)

    def isLeaf(self):
        return (len(self.children_indices) == 0)

    def listAllObjects(self):

        #print "self report"
        #self.report()
        
        if self.isLeaf():
            return self.objects
        else:
            global NODES
            
            objs = []
            for child_idx in self.children_indices:
                #print child_idx
                child = NODES[child_idx]
                objs = objs + child.listAllObjects()
            return objs

    def appendChild(self, child_index):
        self.children_indices.append(child_index)        

    def removeChild(self, child_index):
        del self.children_indices[child_index]

    def getCountMatrix(self):
        return self.countMatrix

    def setCountMatrix(self, cm):
        self.countMatrix = cm # looks like ugly hack but isn't!

    def report(self):
        print "Node [", self.node_index,"], number_of_objects: ", self.number_of_objects, ". Children indices = ", self.children_indices

NODES = []
current_node_index = 0


O1 = {'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O2 = {'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}

N1 = Node()
N1.addObjectsStats(O1)
N1.addObject(O1)

N2 = Node()
N2.addObjectsStats(O2)
N2.addObject(O2)

N3 = Node()
N3.appendChild( N1.node_index )
N3.appendChild( N2.node_index )

'''
N1.report()
N2.report()
N3.report()

print ''
print N1.listAllObjects()
print ''
print N3.listAllObjects()
'''

N4 = Node()
N4.appendChild( N1.node_index )
N3.removeChild( N1.node_index )
N3.appendChild( N4.node_index )

N1.report()
N2.report()
N3.report()
N4.report()

print N3.listAllObjects()
