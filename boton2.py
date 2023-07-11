from api2 import Clima
import time
import tkinter

class AppClima():
    temp_datosHoy = "12°"
    lugar_Hoy = "Valentin Alsina"
    sensacion_Hoy = "12°/9° Sensacion termica 9°"




    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Clima")
        self.ventana.resizable(height=0,width=0)
        self.ventana.geometry("400x600")

        self.f1 = tkinter.Label(self.ventana, text = "Ingrese una ciudad")
        self.f1.grid()

        self.datosHoy = tkinter.Frame(self.ventana, bg="Blue", width=400, height=200)

        self.fila1hoy = tkinter.Label(self.datosHoy,text  = (self.temp_datosHoy))
        self.fila2hoy = tkinter.Label(self.datosHoy,text = (self.lugar_Hoy))
        self.fila3hoy = tkinter.Label(self.datosHoy, text = (self.sensacion_Hoy))
        self.imagenHoy = tkinter.Frame(self.datosHoy,bg="Green", width=100, height=50)
        self.imagenHoy.grid(column=1, row=1,padx=5,pady=5)

        self.fila1hoy.grid(column=0, row=1,padx=5,pady=5)
        self.fila2hoy.grid(column=0, row=2,padx=5,pady=5)
        self.fila3hoy.grid(column=0, row=3,padx=5,pady=5)

        self.datosHoy.grid(column=0, row=1,padx=5,pady=5)
        
        self.fila1hoy.grid(column=0, row=0)
        self.fila2hoy.grid(column=0, row=1)

        self.temperaturaHoy = tkinter.Frame(self.ventana,bg="Blue", width=400, height=200)
        self.temperaturaSemana = tkinter.Frame(self.ventana,bg="Blue", width=400, height=200)

        self.temperaturaHoy.grid(column=0, row=2,padx=5,pady=5)
        self.temperaturaSemana.grid(column=0, row=3,padx=5,pady=5)

        self.clima = Clima()
        self.ventana.mainloop()


a = AppClima()