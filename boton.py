from api import Clima
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
        self.f4 = tkinter.Frame(self.ventana)
        self.f5 = tkinter.Frame(self.ventana)
        self.f6 = tkinter.Frame(self.ventana)
        self.f1.grid(column=0, row=0)
        self.f2.grid(column=0, row=1)
        self.f3.grid(column=0, row=2)
        self.f4.grid(column=0, row=3)
        self.f5.grid(column=0, row=4)
        self.f6.grid(column=0, row=5)

        self.etiqueta = tkinter.Label(self.f1, text = "Ingrese la ciudad")

        self.texto = tkinter.Entry(self.f2)

        self.datos = tkinter.Label(self.f3)
        self.datos.pack()

        self.bt1 = tkinter.Button(self.f4, text = "Obtener datos", command = self.obtenerDatos)
        self.bt1.pack()

        self.etiqueta.pack()
        self.texto.pack()
        self.datos.pack()

        self.bt2 = tkinter.Button(self.f5, text = "Temperatura", command = self.mostrarTemperatura)
        self.bt3 = tkinter.Button(self.f5, text = "Descripcion", command = self.mostrarDescripcion)
        self.bt4 = tkinter.Button(self.f5, text = "Humedad", command = self.mostrarHumedad)
        
        self.bt2.grid(column=0,row=0)
        self.bt3.grid(column=1,row=0)
        self.bt4.grid(column=2,row=0)

        self.resultados = tkinter.Label(self.f6)
        self.resultados.pack()

        self.clima = Clima()
        self.ventana.mainloop()

    def obtenerDatos(self):
        self.clima.obtener_clima(self.texto.get())
        self.datos.config(text = "Datos obtenidos")
        self.texto.delete(first=0,last=tkinter.END)

    def mostrarTemperatura(self):
        self.resultados.config(text = (self.clima.temp))

    def mostrarDescripcion(self):
        self.resultados.config(text = (self.clima.description))

    def mostrarHumedad(self):
        self.resultados.config(text = (self.clima.humidity))            


app = AppClima()
