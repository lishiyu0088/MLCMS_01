import numpy


# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 11
map_y = 11
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)
# print(map_grid)
map_grid[0, 4] = 2
map_grid[0, 5] = 2
map_grid[0, 6] = 2
map_grid[0, 7] = 2
map_grid[4,3] = 3
map_grid[5,3] = 3
map_grid[6,3] = 3
map_grid[6,4] = 3
map_grid[6,5] = 3
map_grid[6,6] = 3
map_grid[6,7] = 3
map_grid[5,7] = 3
map_grid[4,7] = 3
map_grid[10,5] = 4

numpy.savetxt("../data/chicken.txt", map_grid, fmt=' '.join(['%i'] *map_y))