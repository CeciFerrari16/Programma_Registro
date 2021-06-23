import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
import json
#import keyboard as kb 
from PIL import ImageTk
from data import d

m = tk.Tk()
'''
#cursor coordinates
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

m.bind('<Motion>', motion)
'''
subjects = [
    "Arte",
    "Ed. Civica",
    "Fisica",
    "Informatica",
    "Inglese",
    "Latino",
    "Italiano",
    "Matematica",
    "Religione",
    "Ed. Fisica",
    "Scienze",
    "Storia"
]

#general things
m.title("Registro Elettronico")
m.geometry("700x500")
m.resizable(False, False)
m.config(bg = "bisque")

#how to save data
def text_marks():
    file = open("data.json", "r")
    marks = file.read()
    file.close()
    return marks
    
def save_marks():
    with open("data.json", "r") as file:
        dct = eval(file.read())
    data = text1.get('1.0', END)
    #print(isinstance(data, str))
    if len(data) == 0 : pass
    elif data.isnumeric() == True:
        pass
    elif float(data) > 10 or float(data) < 1:
        pass
    else:
        dct[variable.get()].append(data)
        list_update(dct)

def delete_marks():
    with open("data.json", "r") as file:
        dct = eval(file.read())
    elem = dct[variable.get()][-1]
    dct[variable.get()].remove(elem)
    json_file = json.dumps(dct)
    with open("data.json", "w") as file:
        file.write(json_file)

def list_update(dict): # remove \n from list and update data.json
    value = dict[variable.get()]
    d1 = [s.rstrip() for s in value]
    dict[variable.get()] = d1
    json_file = json.dumps(dict)
    with open("data.json", "w") as file:
        file.write(json_file)
    
def background():
    bg = tk.Tk()
    bg.title("Colour Settings")
    bg.geometry("400x300")
    bg.resizable(False, False)
    bg.config(bg = "bisque")

'''
#objects
img = ImageTk.PhotoImage(file = "rsz_forest.jpg")
label = tk.Label(
    m,
    image = img
)
label.place(x = 0, y = 0)
'''
#drop down menu subjects
variable = tk.StringVar(m)
variable.set(subjects[0]) 

drop_down_menu = tk.OptionMenu(m, variable, *subjects)
drop_down_menu.place(x = 464, y = 499, anchor = "se")

text1 = tk.Text(
    m,
    height = 1,
    width = 10,
    font = ("Arial Bold", 18)
)
text1.place(x = 597, y = 499, anchor = "se")
#text1.grid(row = 10, column = 3 )
#text1.tag_configure("center", justify = "center")
#text1.pack()
#text1.place(x = 255, y = 103)

save_button = tk.Button(
    m,
    text = "Add",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = save_marks
)
save_button.place(x = 641, y = 500, anchor = "se")
#button.grid(row = 1, column = 2) in alto
#button.place(relx = 0.5, rely = 0.5, anchor = "center")
#button.place(x = 402, y = 437)

delete_button = tk.Button(
    m,
    text = "Delete",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = delete_marks
)
delete_button.place(relx = 1.0, rely = 1.0, anchor = "se")

img_setting = ImageTk.PhotoImage(file = "settings(2).jpg")
settings = tk.Button(
    m,
    image = img_setting,
    relief = tk.RAISED,
    command = background
)
settings.place(relx = 0.0, rely= 1.0, anchor = "sw")

# marks table
marks = eval(text_marks())
class Table:
	def __init__(self, root):
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = tk.Entry(root, fg = 'black', font = ('Arial', 12 ,'bold'), width = 12)
				self.e.grid(row=i, column=j)
				self.e.insert(END, lst[i][j])
                #self.e.place(x = 43, y = 54, anchor= "nw")

lst = [(k, v) for k, v in marks.items()]

total_rows = len(lst)
total_columns = len(lst[0])

marks_label = Table(m)

m.mainloop()
