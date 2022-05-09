
from matplotlib import pyplot
figura = pyplot.figure()
x = list(range(15))
y = [n**2 for n in x]
y2 = [n+5 for n in y]
y3 = [n+12 for n in y]
pyplot.bar(x, y)
pyplot.plot(x, y2)
pyplot.scatter(x, y3)
pyplot.savefig('./13nod/pyplot_fig.png')

pyplot.show()
