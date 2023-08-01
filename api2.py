import requests

class Clima():
    city = ""
    api_key = "03b9403c9b7130a2cc695d264a22c2c1"
    temperaturaHoy = 0
    description = 0
    humidity = 0


    def obtener_clima(self, city):
        self.city = city
        self.url = f"https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.api_key}&units=metric&cnt=7"
        self.urlVieja = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        res = requests.get(self.url)
        resVieja = requests.get(self.urlVieja)
        data = res.json()
        dataVieja = resVieja.json()

        self.tempHoy = dataVieja["main"]["temp"]
        self.sensacionTermica = dataVieja["main"]["feels_like"]
        self.tempMaxHoy = dataVieja["main"]["temp_max"]
        self.tempMinHoy = dataVieja["main"]["temp_min"]

clima = Clima()
clima.obtener_clima("Buenos Aires")

