# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math
from random import randint
from enum import Enum
import numpy
from pylab import *
import copy
import tkinter
import sys
import matplotlib
import route_planner as rp
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from dijkstra import *

import tkinter as tk
from tkinter import *
from threading import Timer
from random import randint

# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target



# Set the initial state
time_step = 0
mode ="rimea4.txt"


def state_machine():
    list = rp.Planner().open_list(map_grid)
    for element in list:
        min_point = rp.Planner().find_min(map_grid, element, target)
        if min_point!=target:
            map_grid[min_point[0], min_point[1]] = 2
            map_grid[element[0], element[1]] = 1
        else:
            map_grid[element[0], element[1]] = 1
        map_grid[target[0], target[1]] = 4

def state_dijmachine():
    global field
    list = rp.Planner().open_list(map_grid)
    for element in list:
        min_point = rp.Planner().find_dijkmin(map_grid, field, element)
        if min_point!=target:
            map_grid[min_point[0], min_point[1]] = 2
            map_grid[element[0], element[1]] = 1
        else:
            map_grid[element[0], element[1]] = 1
        map_grid[target[0], target[1]] = 4

def circle_path():
    list = rp.Planner().open_list(map_grid)
    for element in list:
        distance = math.sqrt((target[0]-element[0])**2+(target[1]-element[1])**2)
        min_point = [element[0]+int(1/distance*(target[0]-element[0])),element[1]+int(1/distance*(target[1]-element[1]))]
        map_grid[element[0], element[1]] = 1
        map_grid[min_point[0],min_point[1]] = 2

class Application(tk.Tk):
    '''
    GUI interface
    '''
    def __init__(self):
        '''Initialization'''
        super().__init__()
        #self.wm_title("MLCMS- Group H")
        self.text = tk.StringVar()
        self.text.set("Time step: 0")
        label = tk.Label(self, text="MLCMS- Group H", font='Arial')
        label.pack(pady=50)

        self.createWidgets()



    def createWidgets(self):
        global map_grid, field
        global target, start_list
        map_grid = numpy.loadtxt("./data/" + mode)
        start_list = rp.Planner().open_list(map_grid)
        target = numpy.where(map_grid==4)
        field, cost = dijstra_field(map_grid)
        '''Interface'''
        self.title('Simulation program')


        label_time = tk.Label(self, textvariable=self.text, font='Arial')
        label_time.pack(pady=50)
        footframe = tk.Frame(master=self).pack(side=tk.BOTTOM)
        tk.Button(master=footframe, text='Scenario 3: Path in a circle', command=self.circle).pack(side=tk.BOTTOM)
        tk.Button(master=footframe, text='Next step', command=self.simple).pack(side=tk.BOTTOM)
        tk.Button(master=footframe, text='Exit', command=self._quit).pack(side=tk.BOTTOM)
        #self.simple()  # draw
        #plt.close()

    def simple(self):
        state_dijmachine()
        self.draw()

    def circle(self):
        global mode, start_list
        mode="03"
        list = rp.Planner().open_list(map_grid)
        for element, element_start in zip(list,start_list):
            distance = math.sqrt((target[0] - element_start[0]) ** 2 + (target[1] - element_start[1]) ** 2)
            min_point = [element_start[0] + int(time_step / distance * (target[0] - element_start[0])),
                             element_start[1] + int(time_step / distance * (target[1] - element_start[1]))]
            if (min_point != target)and(element != target):
                map_grid[element[0], element[1]] = 1
                map_grid[min_point[0], min_point[1]] = 2
        self.draw()


    def draw(self):
        '''Draw graphs'''

        # Draw grid maps
        global time_step
        time_step += 1
        self.text.set("Time_step: "+str(time_step))
        plt.imshow(map_grid, cmap=plt.cm.hot, interpolation='nearest', vmin=0, vmax=5)
        #plt.colorbar()
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
        #plt.close()




    def _quit(self):
        '''Quit'''
        self.quit()  # stop mainloop
        self.destroy()  # destroy all





if __name__ == '__main__':
    app = Application()

    # loop of main:
    app.mainloop()