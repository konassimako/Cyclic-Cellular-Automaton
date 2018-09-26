# -*- coding: cp1253 -*-
""" CYCLIC CELLULAR AUTOMATON
    MAIN PROGRAM
    Created by Konstantinos Asimakopoulos in 24/5/2016
    © Copyright 2016 Konstantinos Asimakopoulos. All rights reserved. 
"""

from Tkinter import *
from random import randint
from classes import *

#******************************************************************************

def Next_state(event=None):
    global root,myworld
    n=0
    for i in range(0,48):
        for j in range (0,24):
            level=world.a[i][j].color
            if level!=9:
                check_conditions(i,j,n,level+1)
            else:
                check_conditions(i,j,n,0)

def check_conditions(i,j,n,level):
    global root,myworld
    if (i!=0 and i!=47 and j!=0 and j!=23) and (world.a[i-1][j-1].color==level or world.a[i-1][j].color==level or world.a[i-1][j+1].color==level or world.a[i][j-1].color==level or world.a[i][j+1].color==level or world.a[i+1][j-1].color==level or world.a[i+1][j].color==level or world.a[i+1][j+1].color==level):
        n=change_color(i,j,n,level)
    elif (i==0 and j==0):
        if (world.a[i][j+1].color==level or world.a[i+1][j].color==level or world.a[i+1][j+1].color==level):
            n=change_color(i,j,n,level)
    elif (i==0 and j==23):
        if (world.a[i][j-1].color==level or world.a[i+1][j-1].color==level or world.a[i+1][j].color==level):    
            n=change_color(i,j,n,level)
    elif (i==47 and j==0):
        if (world.a[i][j+1].color==level or world.a[i-1][j].color==level or world.a[i-1][j+1].color==level):
            n=change_color(i,j,n,level)
    elif (i==47 and j==23):
        if (world.a[i][j-1].color==level or world.a[i-1][j].color==level or world.a[i-1][j-1].color==level):
            n=change_color(i,j,n,level)
    elif (i==0):
        if (world.a[i][j+1].color==level or world.a[i][j-1].color==level or world.a[i+1][j-1].color==level or world.a[i+1][j].color==level or world.a[i+1][j+1].color==level):
            n=change_color(i,j,n,level)
    elif (j==0):
        if (world.a[i-1][j].color==level or world.a[i+1][j].color==level or world.a[i-1][j+1].color==level or world.a[i][j+1].color==level or world.a[i+1][j+1].color==level):
            n=change_color(i,j,n,level)
    elif (i==47):
        if (world.a[i-1][j-1].color==level or world.a[i-1][j].color==level or world.a[i-1][j+1].color==level or world.a[i][j-1].color==level or world.a[i][j+1].color==level):
            n=change_color(i,j,n,level)
    elif (j==23):
        if (world.a[i-1][j-1].color==level or world.a[i-1][j].color==level or world.a[i][j-1].color==level or world.a[i+1][j-1].color==level or world.a[i+1][j].color==level):
            change_color(i,j,n,level)



def change_color(i,j,n,level):
    global root,myworld
    n+=1
    world.a[i][j].color=level
    world.frames[i][j].configure(background=world.Colours[world.a[i][j].color])
    return n
                
#******************************************************************************

myworld=world()
root=Tk()
root.wm_geometry("800x500+300+100")
root.title("Cyclic Cellular Automaton")
root.configure(background="#00aaff")
Button(root,text="Next state",command=Next_state).place(x=450,y=450)
Button(root,text="   Exit   ",command=root.destroy).place(x=250,y=450)
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="Options", menu=subMenu)
subMenu.add_command(label="View next state",command=Next_state)
subMenu.add_command(label="Exit",command=root.destroy)
Label(root,text="Press space to view the next state",bg="#00aaff",fg="black",font=("Helvetica","16")).place(x=200,y=45,width=400,height=40)
root.bind("<space>",Next_state)
myworld.create_world(root)
root.mainloop()
