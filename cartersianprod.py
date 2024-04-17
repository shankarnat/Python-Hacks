# Using Generator to generate Cartesian Products

colors = ['black', 'white']
size = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c,s) for c in colors for s in size):
    print(tshirt)