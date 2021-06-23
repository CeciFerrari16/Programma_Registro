import time
import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread

gui = tk.Tk()
gui.geometry('360x270')
gui.configure(bg='white')

style = ttk.Style()
style.theme_create('custom', settings={
    'header.TLabel': {'configure': {
        'background': 'white',
        'foreground': 'dark green',
        'font': 'Times 16 bold',
        'padding': (10, 0)}},
    'TLabel': {'configure': {'background': 'white', 'font': 'Times 12'}},
    'TFrame': {'configure': {'background': 'white'}}})
style.theme_use('custom')

table_frame = ttk.Frame(gui)
table_frame.pack(pady=(36, 0))

values = [('Count', 'Date', 'Time', 'Phrase'),
          ('5', '12/12/10', '03:15', 'blue car'),
          ('13', '09/09/98', '16:20', 'red door')]

total_rows = len(values)
total_columns = len(values[0])

for i in range(total_rows):
    for j in range(total_columns):
        if i == 0:
            label = ttk.Label(table_frame, text=values[i][j], style='header.TLabel')
            label.grid(row=i, column=j)
        elif i == 1:
            if j == 0:
                count1 = tk.StringVar()
                count1.set(values[i][j])
                label = ttk.Label(table_frame, textvariable=count1)
                label.grid(row=i, column=j)
            else:
                label = ttk.Label(table_frame, text=values[i][j])
                label.grid(row=i, column=j)
        elif i == 2:
            if j == 0:
                count2 = tk.StringVar()
                count2.set(values[i][j])
                label = ttk.Label(table_frame, textvariable=count2)
                label.grid(row=i, column=j)
            else:
                label = ttk.Label(table_frame, text=values[i][j])
                label.grid(row=i, column=j)


def increment_count():
    increment_count.status = 'run'

    while increment_count.status == 'run':
        new_minute1 = int(count1.get()) + 1
        count1.set(str(new_minute1))

        new_minute2 = int(count2.get()) - 1
        count2.set(str(new_minute2))

        time.sleep(1)


Thread(target=increment_count).start()

gui.mainloop()
increment_count.status = 'exit'
'''
sub = "\n".join(d.keys())
subjects_label = tk.Label(
    m,
    text = sub,
    bg = "white",
    font = ("Arial Bold", 13),
    justify = "left")
subjects_label.place(x = 0, y = 0)

marks = []
with open("data.json", "r") as file:
    dct = eval(file.read())
for e in dct.values():
    if 
    marks.append(", ".join(e))
print(marks)
mark = "\n".join(marks)
marks_label = tk.Label(
    m,
    text = mark,
    bg = "white",
    font = ("Arial Bold", 13),
    justify = "left")
marks_label.place(x = 89, y = 1)


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

import tkinter as tk

root = tk.Tk()

T1 = tk.Text(root)
T1.tag_configure("center", justify='center')
T1.insert("1.0", "text")
T1.tag_add("center", "1.0", "end")
T1.pack()

root.mainloop()
'''