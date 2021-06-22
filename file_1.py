import tkinter as tk
from tkinter.constants import END
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
#import keyboard as kb 
from PIL import ImageTk

m = tk.Tk()
'''
#cursor coordinates
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

m.bind('<Motion>', motion)
'''
#general things
m.title("Our Personal Space")
m.geometry("700x500")
m.resizable(False, False)
m.config(bg = "bisque")

#how to save data
def save_marks():
    with open("data.txt", "a+") as output_file:
        data = text1.get('1.0', END)
        #print(isinstance(data, str))
        if len(data) == 0 : pass
        elif data.isnumeric() == True:
            pass
        elif float(data) > 10 or float(data) < 1:
            pass
        else: output_file.write(data)
    
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
text1 = tk.Text(
    m,
    height = 1,
    width = 10,
    font = ("Arial Bold", 18)
)
text1.place(x = 615, y = 499, anchor = "se")
#text1.grid(row = 10, column = 3 )
#text1.tag_configure("center", justify = "center")
#text1.pack()
#text1.place(x = 255, y = 103)

button = tk.Button(
    m,
    text = "Add mark",
    relief = tk.RAISED,
    font = ("Arial Bold", 13),
    command = save_marks
)
button.place(relx = 1.0, rely = 1.0, anchor = "se")
#button.grid(row = 1, column = 2) in alto
#button.place(relx = 0.5, rely = 0.5, anchor = "center")
#button.place(x = 402, y = 437)

img_setting = ImageTk.PhotoImage(file = "settings(2).jpg")
settings = tk.Button(
    m,
    image = img_setting,
    relief = tk.RAISED,
    command = background
)
settings.place(relx = 1.0, rely = 0.0, anchor = "ne")

m.mainloop()
