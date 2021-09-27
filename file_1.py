import tkinter as tk
from tkinter.constants import END
import json 
from PIL import ImageTk 
from data import d 
import datetime
import calendar
from tkcalendar import Calendar, DateEntry
import matplotlib.pyplot as plt

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
    "Filosofia",
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

lab = tk.Label(m, font = ("Arial Bold", 17)) 
lab.place(x = 101, y = 500, anchor = "sw") 

#Create a Calendar using DateEntry
cal = DateEntry(
    m, 
    width = 10,
    font = ("Arial", 14), 
    background= "blue", 
    foreground= "white",
    #bd=2
)
cal.place(x = 463, y = 470, anchor = "sw")

#how to save data
def text_marks():
    file = open("data.json", "r")
    marks = file.read() 
    file.close()
    return marks

def get_month(materia, voto):
    with open("data.json", "r") as file:
        dct = eval(file.read()) 
        file.close()
    index_voto = dct[materia].index(voto)
    with open("day.json", "r") as file:
        dct1 = eval(file.read()) 
        file.close()
    data = dct1[materia][index_voto]
    x = data.split("-")
    month = int(x[1])
    return month
    
def get_average(month):
    with open("a_month.json", "r") as file:
        dct2 = eval(file.read()) 
        file.close()
    data = dct2[month]
    if data == []:
        media = 0
    else:
        media = sum(data)/len(data)
    return media

def save_month(voto):
    with open("a_month.json", "r") as file:
        dct2 = eval(file.read()) 
        file.close()
    data = get_month(variable.get(), voto)
    month = calendar.month_name[data]
    print(month)
    dct2[month].append(int(voto))
    json_file = json.dumps(dct2) 
    with open("a_month.json", "w") as file:
        file.write(json_file)
        file.close()

def delete_month():
    mydate = datetime.datetime.now()
    with open("a_month.json", "r") as file:
        dct2 = eval(file.read()) 
        file.close()
    data = mydate.strftime("%B")
    elem = dct2[data][-1]
    dct2[data].remove(elem)
    json_file = json.dumps(dct2)
    with open("a_month.json", "w") as file:
        file.write(json_file)
        file.close()

def save_day():
    with open("day.json", "r") as file:
        dct1 = eval(file.read()) 
        file.close()
    data = str(cal.get_date())
    dct1[variable.get()].append(data)
    #print(dct1)
    json_file = json.dumps(dct1) 
    with open("day.json", "w") as file:
        file.write(json_file)
        file.close()

def delete_day():
    with open("day.json", "r") as file:
        dct1 = eval(file.read())
        file.close()
    elem = dct1[variable.get()][-1]
    dct1[variable.get()].remove(elem)
    json_file = json.dumps(dct1)
    with open("day.json", "w") as file:
        file.write(json_file)
        file.close()

def save_marks():
    save_day()
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
        save_month(str(int(data)))

def delete_marks():
    delete_day()
    delete_month()
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
                font = ("Arial", 19 ,"bold"),
                bg = "white",
                width = 10,
                anchor = "w"
            )
            check_mark(mark, lst[i][1])
            mark.grid(row = i, column = j)
    
    average_mark = tk.Label(
        m,
        fg = "black",
        bg = "white",
        text = media(marklist),
        font = ("Arial", 30 ,"bold"),
        width = 7,
        height = 2
    )
    average_mark.place(x = 597, y = 325, anchor = "ne")
    check_mark(average_mark, media(marklist))

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

def graphic():
    months = ["September", "October", "November", "December", "January", "February", "March", "April", "May", "June"]
    rainfall = []
    for m in months:
        rainfall.append(get_average(m))
    
    plt.bar(range(len(rainfall)), rainfall, align = "center", color = "blue")
    plt.xticks(range(len(rainfall)), months, rotation = "vertical")
    plt.show()

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

tag_average = tk.Label( 
    m, 
    fg = "black", 
    text = "Media Generale",
    font = ("Arial", 23 ,"bold"),
    width = 12,
    #anchor = "e",
    bg = "white"
)
tag_average.place(x = 624, y = 258, anchor = "ne")

tag_marks = tk.Label(
    m,
    fg = "black",
    text = "Vedi Grafico della Media",
    font = ("Arial", 19, "bold"),
    bg = "white"
)
tag_marks.place(x = 655, y = 60, anchor = "ne")

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

marksheet_button = tk.Button(
    m,
    text = "Apri Grafico",
    relief = tk.RAISED,
    font = ("Arial Bold", 15, "bold"),
    command = graphic
)
marksheet_button.place(x = 440, y = 125, anchor = "nw")

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
