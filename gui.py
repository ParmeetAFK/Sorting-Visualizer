from tkinter import *
from tkinter import ttk
import random
#VARIABLES
selected_algo = "Selection"

# ------------------------------------------------- FUNCTIONS -------------------------------------------------

lol = [2,3,4,1,3,5]
# --------------------------------------------------- DRAW GRAPH ----------------------------------------------
def DrawData(data):
	c_width = 800
	c_height = 600
	x_width = c_width / len(data) + 1 
	offset = 3
	spacing = 10

	#NORMALIAZING THE DATA

	ndata = [i/max(data) for i in data]

	for i,height in enumerate(ndata): 
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 540
		x1 = (i + 1 ) * x_width + offset
		y1 = c_height

	#(x,y,width,height)
	#(x0,y0,x1,y1)
		canI.create_rectangle(x0,y0,x1,y1,fill='red')
		canI.create_text(x0 + 2 , y0, anchor=SW, text=data[i])


# ----------------------------------------------- ROOT INIT() ------------------------------------------------

root = Tk()
root.title("SORTING BOY")
root.config(bg="black")

#----------------------------------------------------UI FRAME -----------------------------------------------
userI =Frame(root,height= 600, width= 200,bg='black')
userI.grid(row = 0, column = 0,padx=8,pady=8,sticky=N)

#-------------------------------------------------- CANVAS FRAME --------------------------------------------
canI = Canvas(root, height=600,width=820)
canI.grid(row=0,column=1,padx=8,pady=8)

# ---------------------------------------------- USER INTERFACE OPTIONS --------------------------------------
# --------------------------------------------------- HEADING ------------------------------------------------
Label(userI,text='Sort bot',
			  fg='white',
			  bg='black',
			  font=('Algerian',20)).grid(row=0,column=0,padx=8)

Label(userI,text='------------------------------------------------------------------------------',
			  fg='white',
			  bg='black',
			  font=('Algerian',10)).grid(row=1,column=0,pady=1,padx=1,columnspan=2)

#--------------------------------------------------- SELECT ALGO --------------------------------------------
Label(userI,text='Algorithm -------------------- ',
			  fg='white',
			  bg='black',
			  font=('Arial Bold',20),).grid(row=2,column=0,padx=1,pady=8,sticky=W)

# ------------------------------------------------- COMBOBOX ------------------------------------------------

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'black',
                                      	'relief':"flat",
                                        'padding' : 10,
                                       'fieldbackground': 'white',
                                       'background': 'black'
                                       }}}
                         )

combostyle.theme_use('combostyle') 

algoMenu = ttk.Combobox(userI,textvariable=selected_algo,values=['Bubblesort','Selection Sort'],width=50)
algoMenu.grid(row=3,column=0,padx=8,pady=8)
algoMenu.current(0)

# ------------------------------------------------------- SCALING -------------------------------------------
Label(userI,text='Scale ---------------------------',
			fg='white',
			bg='black',
		    font=('Arial Bold',20)).grid(row=4,column=0,pady=8,padx=1,sticky=W)

# -------------------------------------------------------- -GENERATE BUTTON------------------------------------
gen = Button(userI,text='Generate Data')
gen.grid(row = 6,column=0)

#---------------------------------------------------- SORT BUTTON -------------------------------------------
sort = Button(userI,text='START SORTING')
sort.grid(row=7,column=0)

DrawData(lol)
root.mainloop()