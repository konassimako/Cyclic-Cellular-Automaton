# -*- coding: cp1253 -*-
""" CYCLIC CELLULAR AUTOMATON
    CLASSES
    Created by Konstantinos Asimakopoulos in 24/5/2016
    © Copyright 2016 Konstantinos Asimakopoulos. All rights reserved.
"""

from random import randint
from Tkinter import *

class block:
    "This is a class of blocks for the cyclic cellular automaton"
    number=0
    
    def __init__(self,color,position_x,position_y):
        self.color=color
        self.position_x=position_x
        self.position_y=position_y
        block.number+=1


class world(block):
    "This is the world containing all the blocks"
    a=[] # Contains all the block instances
    frames=[] # Contains all the frames
    outer_frame=0
    Colours=("Black","White","Brown","Purple","Blue","Green","Yellow","Orange","Red","Magenta")
    
    def __init__(self):
        for i in range(0,48):
            temp1=[]
            for j in range (0,24):
                b=randint(0,9)
                temp1.append(block(b,i,j))
            world.a.append(temp1)
                        

        
    def create_world(self,root):
        self.root=root
        world.outer_frame=Frame(root,bd=5,relief=RAISED)
        world.outer_frame.place(x=100,y=100,width=605,height=305)
        for i in range(0,48):
            temp2=[]
            for j in range (0,24):
                frame=Frame(world.outer_frame)
                frame.configure(background=world.Colours[world.a[i][j].color])
                frame.place(x=((world.a[i][j].position_x))*12.5,y=((world.a[i][j].position_y))*12.5,width=12.5,height=12.5)
                temp2.append(frame)            
            world.frames.append(temp2)
            

    
