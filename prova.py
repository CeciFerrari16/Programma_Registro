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

def get_day(): pass

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
    
def all_marks(): #tutti i voti
    card = tk.Tk()
    card.title("Marks in Cronological Order")
    card.geometry("500x500")
    #card.resizable(False, False)
    #card.config(bg = get_colour())

    def reverse_list(file_name):
        with open(file_name, "r") as file:
            dct = eval(file.read()) 
            file.close()
        list_elem = dct[variable1.get()]
        list_elem.reverse()
        return list_elem

    vote_list = reverse_list("data.json")
    time_list = reverse_list("day.json")

    def create_label(vote, time):
        lab = tk.Label(
            card,
            fg = "black",
            bg = get_colour(),
            text = vote + " " + time,
            font = ("Arial", 20 ,"bold"),
            width = 7,
            #height = 2     
        )
        lab.pack()

    for n in range(len(vote_list)):
        create_label(vote_list[n], time_list[n])

tag_marks = tk.Label(
    m,
    fg = "black",
    text = "Vedi Voti per Materia",
    font = ("Arial", 19, "bold"),
    bg = "white"
)
tag_marks.place(x = 655, y = 20, anchor = "ne")

marksheet_button = tk.Button(
    m,
    text = "Apri Scheda Voti",
    relief = tk.RAISED,
    font = ("Arial Bold", 15, "bold"),
    command = all_marks
)
marksheet_button.place(x = 440, y = 125, anchor = "nw")

'''
        if colours.index(i) < 3:
            button.grid(row = 1, column = colours.index(i) + 1)
        elif colours.index(i) >= 3 and colours.index(i) < 6:
            button.grid(row = 2, column = colours.index(i) - 2)
        else:
            button.grid(row = 3, column = colours.index(i) - 5)
            '''
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

MODIFICHE UTILI DA FARE AL PROGRAMMA:
1) finestra principale con media per ogni materia
2) aggiungi alla finestra principale un grafico con andamento media generale
3) mettere finestra supplementare che faccia vedere tutti i voti aggiunti in ordine cronologicoùù
'''