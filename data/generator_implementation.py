import numpy
import matplotlib.pyplot as plt
from pylab import *

# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 5
map_y = 5
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)
# print(map_grid)
map_grid[1, 1] = 2
map_grid[2, 3] = 4

plt.imshow(map_grid, cmap=plt.cm.hot, interpolation='nearest', vmin=0, vmax=5)
plt.colorbar()
graph_x = len(map_grid)
graph_y = len(map_grid[0])
xlim(left=-0.5, right=graph_y)  # set range of x-axis
ylim(bottom=graph_x, top=-0.5)  # set range of y-axis
my_x_ticks = numpy.arange(-0.5, graph_y, 1)
my_y_ticks = numpy.arange(-0.5, graph_x, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.grid(True)
plt.show()

numpy.savetxt("../data/01.txt", map_grid, fmt=' '.join(['%i'] *map_x))