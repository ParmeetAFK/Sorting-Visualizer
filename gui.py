from tkinter import *
from tkinter import ttk
import time
import random

#VARIABLES
selected_algo = "Selection"
global data
status = 'Hello World'
# ------------------------------------------------- FUNCTIONS -------------------------------------------------
# --------------------------------------------- RANDOM DATA GENERATOR ----------------------------------------
def gendata():
	global data
	data = []
	s_val = sca.get()
	data = gen_num(s_val,10,1000)
	DrawData(data)

#------------------------------------------------- STATUS --------------------------------------------------
def caption(status):
	zo = Label(root,text=status,
				  fg='white',
				  bg='black',
				  font=('Fugaz One',40),
				  width=25)
	zo.grid(row=1,column=1,padx=0,pady=2)


# ------------------------------------------- GETS SCALE NUMBER ---------------------------------------------
def gen_num(scale,minv,maxv):
	for i in range(0,scale):
		data.append(random.randint(minv,maxv))
		lol = ['This is good data','Thats Sweet','You look good today','Keep Going','I can sort that easily','Watch me sort this data','Select One and let me sort']
		status = lol[random.randint(0,6)]
		caption(status)
	return data

def whatsort():
	#'Bubblesort','Selection Sort','Merge Sort','Heap Sort','Insertion Sort','Quick Sort'
	sort = algoMenu.get()
	if sort == 'Bubblesort':
		bubble()
	elif sort == 'Selection Sort':
		selection_sort()
	elif sort == 'Merge Sort':
		pass
	elif sort == 'Heap Sort':
		pass
	elif sort == 'Insertion Sort':
		pass
	else:
		#Quick Sort 
		pass

# ------------------------------------------------ ALGORITHMS ---------------------------------------------------

def selection_sort():
	for i in range(len(data)):
		min_val = data[i]
		for j in range(len(data)):
			if min_val < data[j]:
				temp = data[i]
				data[i] = data[j]
				data[j] = temp

	DrawData(data)

def bubble():
	counter = 0
	print("d")
	issort = False
	while not issort:
		for i in range(len(data)-1-counter):
			if data[i] < data[i+1]:
				data[i],data[i+1] = data[i+1],data[i]
				issort = False
				print("d")
			else:
				issort = True

		counter += 1

	DrawData(data)



# --------------------------------------------------- DRAW GRAPH ----------------------------------------------
def DrawData(data):
	canI.delete("all")
	c_width = 1000
	c_height = 600
	x_width = c_width / len(data) + 1 
	offset = 3
	spacing = 1

	#NORMALIAZING THE DATA

	ndata = [i/max(data) for i in data]

	for i,height in enumerate(ndata): 
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 540
		x1 = (i + 1 ) * x_width + offset
		y1 = c_height

	#(x,y,width,height)
	#(x0,y0,x1,y1)
		canI.create_rectangle(x0,y0,x1,y1,fill='black')
		#canI.create_text(x0 + 2 , y0, anchor=SW, text=data[i])
	root.update()


# ----------------------------------------------- ROOT INIT() ------------------------------------------------

root = Tk()
root.title("Wayne Power")
root.config(bg="black")
root.state("zoomed")

#----------------------------------------------------UI FRAME -----------------------------------------------
userI =Frame(root,height= 600, width= 200,bg='black')
userI.grid(row = 0, column = 0,padx=8,pady=8,sticky=N)

#-------------------------------------------------- CANVAS FRAME --------------------------------------------
canI = Canvas(root, height=600,width=1085)
canI.grid(row=0,column=1,padx=5,pady=8)


# ---------------------------------------------- USER INTERFACE OPTIONS --------------------------------------
# --------------------------------------------------- HEADING ------------------------------------------------
Label(userI,text='Wayne',
			  fg='white',
			  bg='black',
			  font=('Fugaz One',40)).grid(row=0,column=0,padx=8)

Label(userI,text='Enterprise',
			  fg='white',
			  bg='black',
			  font=('Fugaz One',35)).grid(row=1,column=0,padx=8)

Label(userI,text='------------------------------',
			  fg='white',
			  bg='black',
			  font=('Algerian',10)).grid(row=2,column=0,pady=1,padx=1,columnspan=2)

#--------------------------------------------------- SELECT ALGO --------------------------------------------
Label(userI,text='Algorithm',
			  fg='white',
			  bg='black',
			  font=('Hobo Std',18),).grid(row=3,column=0,padx=1,pady=8,sticky=W)

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

algoMenu = ttk.Combobox(userI,textvariable=selected_algo,values=['Bubblesort','Selection Sort','Merge Sort','Heap Sort','Insertion Sort','Quick Sort'],width=20)
algoMenu.grid(row=4,column=0,padx=8,pady=8)
algoMenu.current(0)

# ------------------------------------------------------- SCALING -------------------------------------------
Label(userI,text='Scale',
			fg='white',
			bg='black',
		    font=('Hobo Std',18)).grid(row=5,column=0,pady=8,padx=1,sticky=W)

sca = Scale(userI,from_=10,to=1000,bg='black',fg='white',orient=HORIZONTAL,length=220)
sca.grid(row=6,column=0,pady=4,padx=8)

# -------------------------------------------------------- -GENERATE BUTTON------------------------------------
gen = Button(userI,text='Generate Data',
			command=gendata,bg='black',fg='white',height=1,width=15,borderwidth=10,font=('Fugaz One',15))
gen.grid(row = 7,column=0,pady=25,padx=8)

#---------------------------------------------------- SORT BUTTON -------------------------------------------
sort = Button(userI,text='START SORTING',
			  command=whatsort,bg='black',fg='white',height=1,width=15,borderwidth=10,font=('Fugaz One',15))
sort.grid(row=8,column=0,pady=0,padx=8)

caption(status)

root.mainloop()