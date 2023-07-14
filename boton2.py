from api2 import Clima
import time
import tkinter

class AppClima():
    temp_datosHoy = "0"
    lugar_Hoy = "Buenos Aires"
    sensacion_Hoy = "0"



    def __init__(self):
        self.clima = Clima()
        self.clima.obtener_clima(self.lugar_Hoy)
        self.temp_datosHoy = self.clima.tempHoy
        self.sensacion_Hoy = (self.clima.tempMinHoy,self.clima.tempMaxHoy,"Sensacion termica de",self.clima.sensacionTermica)
        self.ventana = tkinter.Tk()
        self.ventana.title("Clima")
        self.ventana.resizable(height=0,width=0)
        self.ventana.geometry("400x600")

        #Inicio de la aplicacion

        self.f1 = tkinter.Entry(self.ventana)
        self.f1.grid()

        self.bt1 = tkinter.Button(self.ventana, text = "Obtener datos", command = self.obtenerDatos)
        self.bt1.grid()
        self.bt1.grid(column=0, row=1,padx=5,pady=5)

        #Datos Hoy

        self.datosHoy = tkinter.Frame(self.ventana, bg="Blue", width=400, height=200)

        self.fila1hoy = tkinter.Label(self.datosHoy,text  = (self.temp_datosHoy))
        self.fila2hoy = tkinter.Label(self.datosHoy,text = (self.lugar_Hoy))
        self.fila3hoy = tkinter.Label(self.datosHoy, text = (self.sensacion_Hoy))
        self.imagenHoy = tkinter.Frame(self.datosHoy,bg="Green", width=100, height=50)
        self.imagenHoy.grid(column=1, row=1,padx=5,pady=5)

        self.fila1hoy.grid(column=0, row=1,padx=5,pady=5)
        self.fila2hoy.grid(column=0, row=2,padx=5,pady=5)
        self.fila3hoy.grid(column=0, row=3,padx=5,pady=5)

        self.datosHoy.grid(column=0, row=2,padx=5,pady=5)
        
        self.fila1hoy.grid(column=0, row=0)
        self.fila2hoy.grid(column=0, row=1)
        self.fila3hoy.grid(column=0, row=2)

        self.temperaturaHoy = tkinter.Frame(self.ventana,bg="Blue", width=400, height=200)
        self.temperaturaSemana = tkinter.Frame(self.ventana,bg="Blue", width=400, height=200)

        self.temperaturaHoy.grid(column=0, row=3,padx=5,pady=5)
        self.temperaturaSemana.grid(column=0, row=4,padx=5,pady=5)

        self.clima = Clima()
        self.ventana.mainloop()

    def obtenerDatos(self):
        self.clima.obtener_clima(self.f1.get())
        self.f1.delete(first=0,last=tkinter.END)


a = AppClima()