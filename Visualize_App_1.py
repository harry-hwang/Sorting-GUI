#import os
from tkinter import*
#import tkinter.messagebox # to extract the metadata of the file
from tkinter import ttk # is for the look for button and widgets
from ttkthemes import themed_tk as tk
#import threading
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sort
#import numpy as np
#from threading import Thread
'''============================== Window =============================='''
root = tk.ThemedTk()
root.get_themes()
root.set_theme("arc")
root.title("Visualize Sort Algorithms")
root.configure(background = "gray26")
root.geometry("1000x800")
'''=========================== Bottom Frame ==========================='''
''' App '''

''' UI '''
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)
bottomframe.configure(background = "gray26")

'''============================== Top Frame =============================='''
''' App '''
global g_type
g_type = ''
global N
N = 0
global bar_plot
bar_plot = ''
global start_fig
start_fig = plt.figure()
global var
var = StringVar()
global ax
ax = start_fig.add_subplot(1,1,1)
def algo_type():
    print(var.get())

def go():
    global g_type
    global var
    global N
    global bar_plot
    global start_fig
    global ax
    lst = [x + 1 for x in range(N)]
    random.seed(123)
    random.shuffle(lst)

    if var.get() == "b":
        title = "Bubble sort"
        generator = sort.bubblesort(lst)
    elif var.get() == "i":
        title = "Insertion sort"
        generator = sort.insertionsort(lst)
    elif var.get() == "q":
        title = "Quicksort"
        generator = sort.quicksort(lst, 0, N - 1)
    else:
        title = "Selection sort"
        generator = sort.selectionsort(lst)
     
    ax.set_title(title)
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(lst, rects, iteration):
        for rect, val in zip(rects, lst):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(start_fig, func=update_fig,
                                   fargs=(bar_plot, iteration), frames=generator, interval=1,
                                   repeat=False)
    start_fig.canvas.draw()

def set_number(n):
    global start_fig
    global bar_plot
    global ax
    if ax != None:
        ax.cla()
    n = int(float(n))
    global N
    N = n
    lst1 = [x + 1 for x in range(n)]
    random.seed(123)
    random.shuffle(lst1)

    lst2 = [x + 1 for x in range(n)]

    bar_plot = ax.bar(lst2, lst1)
    plt.xlabel("Value of data point")
    plt.title("Sorting Plot")
    plt.xticks(lst2, lst1)

    canvas = FigureCanvasTkAgg(start_fig, master=bottomframe)
    canvas.get_tk_widget().grid(row=1)
    canvas.draw()

def print_value(val):
    print(int(float(val)))

''' UI '''
topframe = Frame(root)
topframe.pack(side = TOP)
topframe.configure(background = "gray26")

# Create a scale label
scalelabel = ttk.Label(topframe, text = 'Range from 1 to 100:', font = "Arial 15 italic", foreground = "white")
scalelabel.grid(row = 0, column=1)
scalelabel.configure(background = "gray26")

# Create scale
scale = ttk.Scale(topframe, from_= 1, to=100, length= 300, orient= HORIZONTAL, command = set_number)
scale.set(25) #default volume for the scale bar
scale.grid(row = 0, column = 2, pady = 15)

# Create a sort label
sortlabel = ttk.Label(topframe, text = 'Algorithms:', font = "Arial 30 italic", foreground = "white")
sortlabel.grid(column=1, rowspan=2)
sortlabel.configure(background = "gray26")

# 4 radio buttons
rb1 = ttk.Radiobutton(topframe, variable = var, text = 'Bubble Sort', value = 'b', command = algo_type)
rb2 = ttk.Radiobutton(topframe, variable = var, text = 'Quick Sort', value = 'q', command = algo_type)
rb3 = ttk.Radiobutton(topframe, variable = var, text = 'Insert Sort', value = 'i', command = algo_type)
rb4 = ttk.Radiobutton(topframe, variable = var, text = 'Selection Sort', value = 's', command = algo_type)
rb1.grid(row=1, column=2, pady = 20)
rb2.grid(row=1, column=3, pady = 20)
rb3.grid(row=2, column=2, pady = 20)
rb4.grid(row=2, column=3, pady = 20)

# Create a GO button
GObtn = ttk.Button(topframe, text = "GO !", command = go, style='Fun.TButton')
GObtn.grid(row=3, column=2, pady = 10)































#root.protocol("WM_DELETE_WINDOW", on_closing)
if __name__ == "__main__":
  root.mainloop()