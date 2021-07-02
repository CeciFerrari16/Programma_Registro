import tkinter as tk
from tkinter.constants import END
#from tkinter.filedialog import asksaveasfilename
#from tkinter.messagebox import askyesno
import json
#import keyboard as kb 
from PIL import ImageTk #serve per importare jpg
from data import d # prende il dizionario vuoto dei voti
import datetime # per clock()

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
m.resizable(False, False) # non si può ridimensionare la finestra
m.config(bg = "pink") #configuro il background con un colore

def clock():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    lab.config(text = time)
    #lab['text'] = time
    m.after(1000, clock) # run itself again after 1000 ms

lab = tk.Label(m, font = ("Arial Bold", 13)) #etichetta per aggiungere l'ora all'interfaccia
lab.place(x = 101, y = 500, anchor = "sw") # aggiunta all'interfaccia + àncora

#how to save data
def text_marks():
    file = open("data.json", "r")
    marks = file.read() #tutto il contenuto del file data.json è trasformato in stringa e assegnato alla variabile marks
    file.close()
    return marks
    
def save_marks():
    with open("data.json", "r") as file:
        dct = eval(file.read()) #converte stringa in dizionario quando possibile
        file.close()
    data = text1.get('1.0', END) #assegna alla variabile data il contenuto della casellla di testo text1
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
    dct[variable.get()].remove(elem) #elimina l'ultimo voto della materia scelta
    json_file = json.dumps(dct)
    with open("data.json", "w") as file:
        file.write(json_file)
        file.close()

def list_update(dict): # remove \n from list and update data.json
    value = dict[variable.get()]
    d1 = [s.rstrip() for s in value] 
    dict[variable.get()] = d1 #riassegno il valore aggiornato al dizionario
    json_file = json.dumps(dict) #serve per modificare i file json
    with open("data.json", "w") as file:
        file.write(json_file) #aggiorno il file
        file.close()
    
def update(): # marks table
    marks = eval(text_marks())
    lst = [(k, v) for k, v in marks.items()]

    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows):
        for j in range(total_columns):
            
            mark = tk.Label(
                m, 
                fg = "black",
                text = lst[i][j],
                font = ("Arial", 12 ,"bold"),
                width = 12,
                anchor = "w"
            )
            mark.grid(row = i, column = j)

def background(): #impostazioni
    bg = tk.Tk()
    bg.title("Colour Settings")
    bg.geometry("400x300")
    bg.resizable(False, False)
    bg.config(bg = "bisque")
    
    #color settings for background
    def change_pink(): 
        m.configure(bg ="pink")
        bg.configure(bg= "pink")

    button_pink = tk.Button(bg, 
    text = "pink",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_pink)
    #button_pink.grid(row = 1, column = 2)
    button_pink.pack()

    def change_lavender(): 
        m.configure(bg ="lavender")
        bg.configure(bg ="lavender")

    button_lavender = tk.Button(bg, 
    text = "lavender",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_lavender)
    #button_lavender.grid(row = 1, column = 3)
    button_lavender.pack()
    
    def change_khaki(): 
        m.configure(bg ="khaki")
        bg.configure(bg ="khaki" ) 
    
    button_khaki = tk.Button(bg,
    text = "khaki",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_khaki)
    #button_khaki.grid(row = 1, column = 4)
    button_khaki.pack()

    def change_white(): 
        m.configure(bg= "white")
        bg.configure(bg= "white")

    button_white = tk.Button(bg, 
    text ="white",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_white ) 
    button_white.pack()
    #button_white.grid(row= 1, column= 5)

    def change_bisque() : 
        m.configure(bg="bisque2")
        bg.configure(bg="bisque2")

    button_bisque = tk.Button(bg,
    text ="bisque",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_bisque ) 
    #button_bisque.grid(row=1, colum=6)
    button_bisque.pack()

    def change_aquamarine(): 
        m.configure(bg="aquamarine4")
        bg.configure(bg= "aquamarine4")

    button_aquamarine= tk.Button(bg,
    text= "aquamarine",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_aquamarine)
    button_aquamarine.pack()

    def change_blue(): 
        m.configure(bg="cadet blue")
        bg.configure(bg= "cadet blue")

    button_blue = tk.Button(bg,
    text= "blue",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_blue)
    button_blue.pack()

    def change_red(): 
        m.configure(bg="indianRed3")
        bg.configure(bg="indianRed3")
        
    button_red = tk.Button(bg,
    text= "red",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = change_red)
    button_red.pack()

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
