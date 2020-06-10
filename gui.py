from tkinter import *
from tkinter import ttk
import random
#VARIABLES
selected_algo = "Selection"

#FUNCTIONS
#DRAW
lol = [2,50,1,66,3]

def DrawData(data):
	c_width = 800
	x_width = c_width / len(data) + 1 
	offset = 30
	spacing = 10

	for i,height in enumerate(data):
		pass

	#(width,padx,pady,height)
	canI.create_rectangle(500,20,0,100,fill='red')


# ROOT INIT()
root = Tk()
root.title("SORTING BOY")
root.config(bg="black")

#UI FRAME 
userI =Frame(root,height= 600, width= 200,bg='grey')
userI.grid(row = 0, column = 0,padx=8,pady=8)

#CANVAS FRAME
canI = Canvas(root, height=600,width=800)
canI.grid(row=0,column=1,padx=8,pady=8)

#USER INTERFACE OPTIONS
#HEADING
Label(userI,text='Sort bot',bg='grey').grid(row=0,column=0,sticky=W)

#SELECT ALGO
Label(userI,text='Algorithm : ').grid(row=1,column=0)
algoMenu = ttk.Combobox(userI,textvariable=selected_algo,values=['Bubblesort','Selection Sort'])
algoMenu.grid(row=1,column=1)
algoMenu.current(0)

#SCALING
Label(userI,text='Scale').grid(row=2,column=0)

#GENERATE BUTTON
gen = Button(userI,text='Generate Data')
gen.grid(row = 3,column=0)

#SORT BUTTON
sort = Button(userI,text='START SORTING')
sort.grid(row=4,column=0)

DrawData(lol)
root.mainloop()