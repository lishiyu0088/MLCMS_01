import numpy
from random import randint

# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 30
map_y = 30
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)


for i in range(30):
    map_grid[i, 29]=3
    map_grid[29,i]=3

for i in range(24):
    map_grid[i, 23] = 3

for i in range(24):
    map_grid[23, 23-i] = 3

skip = 75 // 20
offset = 0
for ped in range(20):
    map_grid[offset // 5, 28 - offset % 5] = 2
    offset = offset + skip
map_grid[25,0]=4
numpy.savetxt("../data/rimea6.txt", map_grid, fmt=' '.join(['%i'] *map_y))