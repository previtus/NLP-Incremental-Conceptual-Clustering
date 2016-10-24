# Node class
from collections import defaultdict
from Attributes import *

class Node:
    '''
    Node in the concept cluster hierarchy
    '''
    tmp = 0

    # Descriptive part - which variables will describe the node
    number_of_objects = 0
    countMatrix = defaultdict(list) # null, needs initialization
    # adressing: Node.countMatrix[<attrib>][<val>] --> <count>
    children = []

    # Funcitonal part - nodes functionality

    def __init__(self):
        # empty node
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

    def addObject(self, Object):
        # updates the number_of_objects and countMatrix, not children
        # because children points to hierarchy of nodes, whereas the counts talk about the objects belonging to the nodes
        self.number_of_objects += 1

        for attrib in Object:
            val = Object[attrib]
            self.countMatrix[attrib][val] += 1

    def displayNode(self):
        print "Node, number_of_objects: ", self.number_of_objects

N = Node()

O = {'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
print O

N.addObject(O)

