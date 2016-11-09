# Example.py

from BobDylan import *

O1 = {NAME_CAT: 'fish', 'BodyCover': 'scales', 'HeartChamber': 'two', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O2 = {NAME_CAT: 'amphibian', 'BodyCover': 'moist-skin', 'HeartChamber': 'three', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O3 = {NAME_CAT: 'mammal', 'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O4 = {NAME_CAT: 'bird', 'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}

# examples for description of algorithm
O5_similar = {NAME_CAT: 'platypus', 'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O5_different = {NAME_CAT: 'alien', 'BodyCover': 'slimy', 'HeartChamber': 'many', 'BodyTemp': 'regulated', 'Fertilization': 'parasytic'}

Objects = [O1, O2, O3, O4]
#Objects = [O1, O2, O3, O4, O5_similar]
#Objects = [O1, O2, O3, O4, O5_different]


Root = Node()

for Object in Objects:
    BobDylan( Root, Object )

    #Root.reportTree()

print "\nFinal tree structure:"
Root.reportTree()
fileout = "viewer/data.js"
text_file = open(fileout, "w")
text_file = open(fileout, "a")
text_file.write("var nodeDataArray = [\n")
Root.outputTree(text_file, -1)
text_file.write("];")
text_file.close()
