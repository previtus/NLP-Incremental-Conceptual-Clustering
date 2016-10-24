# Node class

class Node:
    '''
    Node in the concept cluster hierarchy
    '''
    tmp = 0
    
    def __init__(self, a, b):
        Node.tmp += 1
   
    def displayNode(self):
        print "Node: ", self.tmp

#node = Node(a, b)
