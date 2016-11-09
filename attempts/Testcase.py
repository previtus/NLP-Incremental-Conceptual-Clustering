# Testcase
# 1.) write here all the attributes (like "BodyCover") and its possible values (like "hair")
from collections import defaultdict

attributes = defaultdict(list)

attributes['BodyCover'].append('hair')
attributes['BodyCover'].append('feathers')
attributes['BodyCover'].append('cornified-skin')
attributes['BodyCover'].append('moist-skin')
attributes['BodyCover'].append('scales')

attributes['BodyTemp'].append('regulated')
attributes['BodyTemp'].append('unregulated')

attributes['HeartChamber'].append('four')
attributes['HeartChamber'].append('imperfect-four')
attributes['HeartChamber'].append('three')
attributes['HeartChamber'].append('two')

attributes['Fertilization'].append('internal')
attributes['Fertilization'].append('external')

# plus for our example
attributes['BodyCover'].append('slimy')
attributes['HeartChamber'].append('many')
attributes['Fertilization'].append('parasytic')


# Example.py

from BobDylan import *

# 2.) Include the data here:


O1 = {NAME_CAT: 'fish', 'BodyCover': 'scales', 'HeartChamber': 'two', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O2 = {NAME_CAT: 'amphibian', 'BodyCover': 'moist-skin', 'HeartChamber': 'three', 'BodyTemp': 'unregulated', 'Fertilization': 'external'}
O3 = {NAME_CAT: 'mammal', 'BodyCover': 'hair', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}
O4 = {NAME_CAT: 'bird', 'BodyCover': 'feathers', 'HeartChamber': 'four', 'BodyTemp': 'regulated', 'Fertilization': 'internal'}

Objects = [O1, O2, O3, O4]


# 3.) now this should be ok >>

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
