# Attributes description

# example from Cobweb (1986)

from collections import defaultdict

attributes = defaultdict(list)

attributes['BodyCover'].append('hair')
attributes['BodyCover'].append('feathers')
attributes['BodyCover'].append('cornified-skin')
attributes['BodyCover'].append('moist-skin')
attributes['BodyCover'].append('scales')

attributes['HeartChamber'].append('four')
attributes['HeartChamber'].append('imperfect-four')
attributes['HeartChamber'].append('three')
attributes['HeartChamber'].append('two')

attributes['BodyTemp'].append('regulated')
attributes['BodyTemp'].append('unregulated')

attributes['Fertilization'].append('internal')
attributes['Fertilization'].append('external')

#print "ATTRIBUTES: ", attributes.items()

'''
items = []
items.append(['hair','four','regulated','internal'])
items.append(['feathers','four','regulated','internal'])
items.append(['cornified-skin','imperfect-four','unregulated','internal'])
items.append(['moist-skin','three','unregulated','external'])
items.append(['scales','two','unregulated','external'])

print "ITEMS: ", items
'''
