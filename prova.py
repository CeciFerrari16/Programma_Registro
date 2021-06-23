# Python program to create a table

from tkinter import *


class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(root, width=20, fg='blue',
							font=('Arial',16,'bold'))
				
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])

# take the data
lst = [(1,'Raj','Mumbai',19),
	(2,'Aaryan','Pune',18),
	(3,'Vaishnavi','Mumbai',20),
	(4,'Rachna','Mumbai',21),
	(5,'Shubham','Delhi',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()







d = {
    "Disegno e storia dell'arte" : [],
    "Ed. Civica" : [],
    "Fisica" : [],
    "Informatica" : [],
    "Inglese" : [],
    "Latino" : [],
    "Itaiano" : [],
    "Matematica" : [],
    "Religione" : [],
    "Ed. Fisica" : [],
    "Scienze" : [],
    "Storia" : []
} 
print(list(d))
'''
import tkinter as tk

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame = tk.Frame(root)
frame.grid(row=1, column=0, sticky='nsew')

for i in range(3):
    frame.columnconfigure(i, weight=1)

frame.rowconfigure(1, weight=1)

tk.Label(root, text='Title centered').grid(row=0, column=0)
tk.Label(frame, text='Top left').grid(row=0, column=0, sticky='w')
tk.Label(frame, text='Top center').grid(row=0, column=1)
tk.Label(frame, text='Top right').grid(row=0, column=2, sticky='e')
tk.Label(frame, text='Center').grid(row=1, column=1)
tk.Label(frame, text='Bottom left').grid(row=2, column=0, sticky='w')
tk.Label(frame, text='Bottom center').grid(row=2, column=1)
tk.Label(frame, text='Bottom right').grid(row=2, column=2, sticky='e')
tk.Label(root, text='Footer centered').grid(row=2, column=0)
root.mainloop()


import tkinter as tk

root = tk.Tk()

T1 = tk.Text(root)
T1.tag_configure("center", justify='center')
T1.insert("1.0", "text")
T1.tag_add("center", "1.0", "end")
T1.pack()

root.mainloop()
'''