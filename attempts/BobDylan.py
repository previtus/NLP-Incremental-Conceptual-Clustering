# BobDylan.py - our implementation of the Incremental Conceptual Clustering
from Node import *


def BobDylan(Node, Object):
    # Add Object to the hierarchy represented by Node
    return ""



O1 = {'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O2 = {'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
Objects = [O1, O2]

Root = Node()

for Object in Objects:
    print Object
    BobDylan( Root, Object )
