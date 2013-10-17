#-------------------------------------------------------------------------------
# Name:        GameOfLife
# Purpose:
#
# Author:      Sashich
#
# Created:     30/08/2013
# Copyright:   (c) Sashich 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Tkinter
import tkMessageBox
import copy                                 # we need this to use "deepcopy" method

MAX = 6                                     # side of our game-square + 1
SIZE = 50                                   # cell's size on the screen
#l = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
l =  [[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[1,1,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def showpic(a):
    top = Tkinter.Tk()
    C = Tkinter.Canvas(top, bg="green", height=367, width=367)

    for i in range(0, MAX+1):
        for j in range(0, MAX+1):
            coordinates = 10+SIZE*j+a, 10+SIZE*i, 10+SIZE*(j+1)+a, 10+SIZE*(i+1)

            if l[i][j]:                                         # a cell is alive
                C.create_rectangle(coordinates, fill="blue")
            else:                                               # else - it's dead
                C.create_rectangle(coordinates, fill="grey")

    C.pack()
    top.mainloop()

def number_of_living_neighbours(i, j):      # returns the number of the nearby living cells
    m = 0

    if 0 > i > MAX or 0 > j > MAX:          # if smth went wrong
        print "ERROR!!!", i, j

    if not j:                               # a cell is in left vertical column
        j1 = 0
        j2 = j1 + 1
        if l[i][j2]: m += 1

    elif j == MAX:                          # a cell is in right vertical column
        j2 = MAX
        j1 = j2 - 1
        if l[i][j1]: m += 1

    else:
        j1 = j - 1
        j2 = j + 1
        if l[i][j1]: m += 1
        if l[i][j2]: m += 1

    if i:                                   # we make sure that a cell is not in the highest line
        for c in l[i-1][j1:j2+1]:
            if c: m += 1                    # otherwise there's no need to count living neighbours in the higher line

    if i<MAX:                               # same with the lowest line
        for c in l[i+1][j1:j2+1]:
            if c: m += 1

    return m

def main():
    global l                                # l must be defined here as global to avoid confusion with a local variable
    l2 = copy.deepcopy(l)                   # let's make an exact copy of l-list. It'll be used as a temporary buffer during calculations

    for k in range (0, 5):                  # number of game steps we show on the screen
        showpic(0)

        for i in range(0, MAX+1):
            for j in range (0, MAX+1):

                a = number_of_living_neighbours(i,j)

                if l[i][j]:                 # if a cell is alive
                    if a > 3 or a < 2:      # and "neighbours' condition" doesn't met
                        l2[i][j] = 0        # it dies
                                            # we use l2-list here because l-list must stay untouched inside this loop
                else:                       # else - a cell is dead
                    if a == 3:              # but if it has 3 neighbours
                        l2[i][j] = 1        # it returns to life

        l = copy.deepcopy(l2)               # and now, when the calculations loop is over, we can change l

if __name__ == '__main__':
    main()

