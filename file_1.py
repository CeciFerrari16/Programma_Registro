import tkinter as tk
from tkinter.constants import END
#from tkinter.filedialog import asksaveasfilename
#from tkinter.messagebox import askyesno
import json
#import keyboard as kb 
from PIL import ImageTk 
from data import d 
import datetime 

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

colours = [
    "pink", 
    "lavender", 
    "khaki", 
    "white", 
    "bisque2", 
    "aquamarine4", 
    "cadet blue", 
    "indianRed3", 
    "red",
    "black"
]

def get_colour():
    with open("colour.txt", "r") as file:
        col = file.read()
        file.close()
    return str(col)

#general things
m.title("Registro Elettronico")
m.geometry("700x500")
m.resizable(False, False) 
m.config(bg = get_colour()) 

def check_int(lista):
    for e in lista:
        lista[lista.index(e)] = int(e)
    return lista

def media(lista):
    check_int(lista)
    if len(lista) != 0:
        med = round(sum(lista)/ len(lista), 2)
    else:
        med = "-"
    return med

def clock():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    lab.config(text = time)
    #lab['text'] = time
    m.after(1000, clock) # run itself again after 1000 ms

lab = tk.Label(m, font = ("Arial Bold", 13)) 
lab.place(x = 101, y = 500, anchor = "sw") 

#how to save data
def text_marks():
    file = open("data.json", "r")
    marks = file.read() 
    file.close()
    return marks
    
def save_marks():
    with open("data.json", "r") as file:
        dct = eval(file.read()) 
        file.close()
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
        file.close()
    elem = dct[variable.get()][-1]
    dct[variable.get()].remove(elem)
    json_file = json.dumps(dct)
    with open("data.json", "w") as file:
        file.write(json_file)
        file.close()

def check_mark(label, num):
    if num != "-":
        if num < 6:
            label.config(fg = "red")
        else: pass
    else: pass

def list_update(dict): 
    value = dict[variable.get()]
    d1 = [s.rstrip() for s in value] 
    dict[variable.get()] = d1 
    json_file = json.dumps(dict) 
    with open("data.json", "w") as file:
        file.write(json_file)
        file.close()
    
def marks_list(d, lista):
    lista.clear()
    for v in d.values():
        for e in v:
            lista.append(e)
    check_int(lista)
    return lista

marklist = []

def update(): # marks table
    marks = eval(text_marks())
    lst = [(k, media(v)) for k, v in marks.items()] 
    marks_list(marks, marklist)

    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows): 
        for j in range(total_columns):
            mark = tk.Label(
                m, 
                fg = "black", 
                text = lst[i][j],
                font = ("Arial", 21 ,"bold"),
                width = 10,
                anchor = "w"
            )
            check_mark(mark, lst[i][1])
            mark.grid(row = i, column = j)
    
    average_mark = tk.Label(
        m,
        fg = "white",
        bg = "midnightblue",
        text = media(marklist),
        font = ("Arial", 25 ,"bold"),
        width = 5,
        height = 2
    )
    average_mark.place(x = 700, y = 0, anchor = "ne")

def background(): #impostazioni
    bg = tk.Tk()
    bg.title("Colour Settings")
    #bg.geometry("400x300")
    bg.resizable(False, False)
    bg.config(bg = get_colour())

    #color settings for background
    def change(colour):
        m.configure(bg = str(colour))
        bg.configure(bg=str(colour))
        save_colour(colour)

    for i in colours:
        button = tk.Button(
            bg, 
            text= i,
            relief = tk.RAISED,
            font = ("Arial Bold", 13),
            command = lambda i=i: change(i))
        button.pack()

def save_colour(colour):
    with open("colour.txt", "w") as file:
        file.truncate(0)
        file.write(str(colour))
        file.close()

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
drop_down_menu.place(x = 464, y = 500, anchor = "se") 

#buttons
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

update_button = tk.Button(
    m,
    text = "Update",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = update
)
update_button.place(x = 36, y = 500, anchor = "sw")

img_setting = ImageTk.PhotoImage(file = "settings(2).jpg")
settings = tk.Button(
    m,
    image = img_setting,
    relief = tk.RAISED,
    command = background
)
settings.place(relx = 0.0, rely= 1.0, anchor = "sw")

clock()
update()
m.mainloop()
