from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno

# ------------
app = Tk()
# =================== frames ========================
frame1 = Frame(app)
frame1.pack(side=TOP)
# ----
title_label = Label(frame1, text="Facture", font=("courier", 40, 'bold'))
title_label.pack()
# ----
frame2 = Frame(app, bd=5)
frame2.pack(side=TOP)
# ----
frame3 = Frame(app)
frame3.pack(side=TOP)
# ============================================

# ======--- text field -----======
text_input = Text(frame2,bg="aliceblue", fg='black', font=('TkFixedFont'))
text_input.pack(expand = True)
# ============ in text field ===============
header = "{0} {1} {2}\n".format("-"*35,"Facture", "-"*35)
text_input.insert(END, header)
fields = "{0:10}{1:40}{2:20}{3:8}\n".format("Qty", "Product", "PU", "PV/TVAC")

text_input.insert(END, fields)
rs = (("1", "FANTA CITRON", "2500", "2500"),
        ("1", "BUFFET PER HEAD", "10000", "10000"),
        ("1", "MUKEKE GRILLE OIGNONS", "16000", "16000"),)

for i in rs:
    fields = "{0:10}{1:40}{2:20}{3:10}\n".format(i[0], i[1], i[2], i[3])
    text_input.insert(END, fields)
    
footer = "{0:70}{1}".format("TOTAL","28500")
text_input.insert(END, footer)


# --------- functions ---------
def save():
    filepath = asksaveasfilename(
        defaultextension = "csv",
        filetypes = [("Text Files", "*.csv"), ("All Files", "*.*")])

    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        text = text_input.get('1.0', END)
        output_file.write(text)

def printR():
    pass

def delete():
    text_input.delete('1.0', END)

def exit():
    iExit = askyesno("Attention", "You are on your way to quit\nAre you sure you want quit")
    if iExit > 0:
        app.destroy()
# ----------------------------------

# ============---------------===============
# =====--------- Buttons -----------========
save_button = Button(frame3, text="Save", height=3, width=10, command=save)
save_button.grid(row=0, column=0, padx=2)
# ----------------
print_button = Button(frame3, text="Print", height=3, width=10, command=printR)
print_button.grid(row=0, column=1, padx=2)
# ----------------
delete_button = Button(frame3, text="Delete", height=3, width=10, command=delete)
delete_button.grid(row=0, column=2, padx=2)
# ----------------
quit_button = Button(frame3, text="Exit", height=3, width=10, command=exit)
quit_button.grid(row=0, column=3, padx=2)
# ============================================

app.mainloop()  


'''
import tkinter as tk

root = tk.Tk()

T1 = tk.Text(root)
T1.tag_configure("center", justify='center')
T1.insert("1.0", "text")
T1.tag_add("center", "1.0", "end")
T1.pack()

root.mainloop()
'''