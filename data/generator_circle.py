import numpy


# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 50
map_y = 50
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)
# print(map_grid)
map_grid[24, 0] = 2
map_grid[0, 24] = 2
map_grid[24,49] = 2
map_grid[49,24] = 2
map_grid[7,7] = 2
map_grid[24, 24] = 4

numpy.savetxt("../data/03.txt", map_grid, fmt=' '.join(['%i'] *map_x))