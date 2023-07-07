from api2 import Clima
import time
import tkinter

class AppClima():
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Clima")
        self.ventana.resizable(False,False)

        self.f1 = tkinter.Frame(self.ventana)
        self.f2 = tkinter.Frame(self.ventana)
        self.f3 = tkinter.Frame(self.ventana)
        self.f1.grid(column=0, row=0)
        self.f2.grid(column=0, row=1)
        self.f3.grid(column=0, row=2)

        self.etiqueta = tkinter.Label(self.f1, text = "Ingrese la ciudad")
        self.etiqueta.pack()

        self.clima = Clima()
        self.ventana.mainloop()