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
    countMatrix = [] # null, needs initialization
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
        countMatrix = []
        self.children_indices = []
        self.objects = []
        
        self.initCountMatrix()

    def initCountMatrix(self):
        global attributes

        self.countMatrix = []
        attrib_index = 0
        for attrib in attributes:
            #print attrib
            self.countMatrix.append([])
            val_index = 0

            for val in attributes[attrib]:
                self.countMatrix[attrib_index].append([])
                #print val
                self.countMatrix[attrib_index][val_index] = 0
                val_index+=1
            attrib_index+=1
                
        #print "Counts: ", self.countMatrix.items()
        #print self.countMatrix['BodyCover']['hair']

    def addObjectsStats(self, Object):
        # updates the number_of_objects and countMatrix, not children
        # because children points to hierarchy of nodes, whereas the counts talk about the objects belonging to the nodes
        self.number_of_objects += 1

        attrib_index = 0
        for attrib in attributes:
            val_index = 0

            for val in attributes[attrib]:
                if (val == Object[attrib]):
                    self.countMatrix[attrib_index][val_index] += 1
                    break # break out of the first one
                
                val_index+=1
            attrib_index+=1

    def addObject(self, Object):
        self.objects.append(Object)

    def isLeaf(self):
        return (len(self.children_indices) == 0)

    def listAllObjects(self):
        # recurrent, digs deep
        
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

    def getAllListsFromChildren(self):
        AllLists = []
        for child_idx in self.children_indices:
            child = NODES[child_idx]
            AllLists.append( child.listAllObjects() )
        return AllLists

    def getAllListsFromChildrenWithIdx(self):
        AllLists = []
        for child_idx in self.children_indices:
            child = NODES[child_idx]
            AllLists.append( [child.listAllObjects(), child_idx] )
        return AllLists

    def appendChild(self, child_index):
        self.children_indices.append(child_index)        

    def appendChildObj(self, child):
        self.children_indices.append(child.node_index)        

    def removeChild(self, child_index):
        self.children_indices.remove(child_index)

    def getCountMatrix(self):
        return [self.number_of_objects, self.countMatrix]

    def setCountMatrix(self, cm):
        self.number_of_objects = cm[0]
        self.countMatrix = cm[1]
        # looks like ugly hack but isn't!

    def updateCountMatrixFromChildren(self):
        global NODES
        self.number_of_objects = 0
        self.initCountMatrix()
        
        for child_idx in self.children_indices:
            child = NODES[child_idx]
            #child.reportCounts()
            
            self.number_of_objects += child.number_of_objects

            attrib_index = 0
            for attrib in attributes:
                val_index = 0
                for val in attributes[attrib]:
                    #print attrib, val, child.countMatrix[attrib_index][val_index]
                    
                    self.countMatrix[attrib_index][val_index] += child.countMatrix[attrib_index][val_index]

                    val_index += 1
                attrib_index += 1

    def getChildrenById(self, idx):
        return NODES[idx]

    # TODO> Split and Merge
    def split(self):
        print "TODO"
        # return list of children as nodes

    def merge(self, node):
        print "TODO"
        # insert all children from 'enemy node' into this one. Update counts.

    # Debug functions
    def report(self):
        print "Node [", self.node_index,"], list: ", self.isLeaf(),", number_of_objects: ", self.number_of_objects, ". Children indices = ", self.children_indices

    def reportCounts(self):
        print "objects:", self.number_of_objects
        print "counts:", self.countMatrix

    def reportTree(self):
        self.report()

        global NODES
        for child_idx in self.children_indices:
            NODES[child_idx].reportTree()

    def output(self, text_file, parent_id):
        text_file.write("    { key : "+ str(self.node_index)+", ")
        text_file.write("parentNode : "+str(parent_id)+", ")
        if(self.isLeaf()):
            text_file.write("name: \""+ str(self.objects[0]['NameDebug'])+"\", ")
        text_file.write("title : \""+ str(self.number_of_objects)+ " objects\"")
#        text_file.write("Children indices = "+ str(self.children_indices))
        text_file.write(" },\n")


    def outputTree(self, text_file, parent_id):
        self.output(text_file, parent_id)

        global NODES
        for child_idx in self.children_indices:
            NODES[child_idx].outputTree(text_file, self.node_index)


NODES = []
current_node_index = 0

# PLAYGROUND:
'''

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

N4 = Node()
N4.appendChild( N1.node_index )
N3.removeChild( N1.node_index )
N3.appendChild( N4.node_index )

N4.setCountMatrix( N1.getCountMatrix() )

#N4.updateCountMatrixFromChildren()

N3.updateCountMatrixFromChildren()
print "N1: "
N1.reportCounts()
print "N3: "
N3.reportCounts()

print "\nN1 --- N4: "
N1.report()
N2.report()
N3.report()
N4.report()

print "\nAll objects: "
print N3.listAllObjects()

'''
