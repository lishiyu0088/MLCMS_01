import numpy


# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 50
map_y = 7
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)
for i in range(50):
    map_grid[i, 0] = 3


for i in range(5):
    map_grid[0, i+1] = 3


for i in range(50):
    map_grid[i, 6] = 3


for i in range(5):
    map_grid[49, i+1] = 3

map_grid[1, 3] = 2
map_grid[49, 3] = 4

numpy.savetxt("../data/rimea1.txt", map_grid, fmt=' '.join(['%i'] *map_y))