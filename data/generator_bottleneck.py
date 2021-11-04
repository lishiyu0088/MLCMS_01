import numpy
from random import randint

# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 17
map_y = 21
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)


for i in range(0,8):
    map_grid[10, i]=3

for i in range(13,21):
    map_grid[10, i]=3

for i in range(20):
    map_grid[0, i] = 2


map_grid[16,10]=4
numpy.savetxt("../data/bottleneck.txt", map_grid, fmt=' '.join(['%i'] *map_y))