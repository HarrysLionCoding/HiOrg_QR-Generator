import tkinter
from tkinter import messagebox

def ende():
    messagebox.showinfo(title="Achtung!", message="Programm wird geschlossen!")
    gui.destroy()

gui = tkinter.Tk()

abschluss = tkinter.Button(gui,text="Programm beenden", command=ende).pack()

gui.mainloop()
