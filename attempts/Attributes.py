# Attributes description

# example from Cobweb (1986)

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


#print "ATTRIBUTES: ", attributes.items()
