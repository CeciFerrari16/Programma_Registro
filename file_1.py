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

colours = [
    "pink", 
    "lavender", 
    "khaki", 
    "white", 
    "bisque2", 
    "aquamarine4", 
    "cadet blue", 
    "indianRed3", 
    "red"
]

def get_colour():
    with open("colour.txt", "r") as file:
        col = file.read()
        file.close()
    return str(col)

#general things
m.title("Registro Elettronico")
m.geometry("700x500")
m.resizable(False, False) # non si può ridimensionare la finestra
m.config(bg = get_colour()) #configuro il background con un colore

def media():
    pass

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
    lst = [(k, v) for k, v in marks.items()] #lista formata da tuple

    total_rows = len(lst)
    total_columns = len(lst[0])

    for i in range(total_rows): #crea una tabella con i voti
        for j in range(total_columns):
            
            mark = tk.Label(
                m, 
                fg = "black", #foreground (font)
                text = lst[i][j],# con i determino la tupla in lst e con j determino il voto all'interno della lista presente all'intermìno della tupla 
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
variable = tk.StringVar(m) #stringvar è un oggetto proprio di tk ; variabile stringa
variable.set(subjects[0]) # ogni volta che apro la finestra viene visualizzata la prima materia della lista subjects

drop_down_menu = tk.OptionMenu(m, variable, *subjects) #menù a tendina, variable assume il valore che selezioni nel menù (la materia)
drop_down_menu.place(x = 464, y = 500, anchor = "se") #àncora se => sud est si riferiscono a un punto che prende riferimento dall'angolo sud est

#buttons
text1 = tk.Text(
    m,
    height = 1,
    width = 10,
    font = ("Arial Bold", 18)
)
text1.place(x = 597, y = 499, anchor = "se") #=> text1 è la casella per inserire il testo
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
