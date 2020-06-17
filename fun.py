from tkinter import *

root = Tk()

def su():
	sum = 0
	sum = int(e1.get()) + int(e2.get())
	print(sum)

root.title("Boo App")
root.config(bg='black')

head = Label(root,text='Calculator',
			font=('Arial Bold',20),
			fg='white',
			bg='black')
head.pack()

a = Label(root,text='a')
a.pack()

e1 = Entry(root)
e1.pack()

b = Label(root,text='b')
b.pack()

e2 = Entry(root)
e2.pack()

add = Button(root,text='ADD them',command=su)
add.pack()



root.mainloop()