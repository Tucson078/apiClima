import requests

class Clima():
    city = ""
    api_key = "03b9403c9b7130a2cc695d264a22c2c1"
    temp = 0
    description = 0
    humidity = 0


    def obtener_clima(self, city):
        self.city = city
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        res = requests.get(self.url)
        data = res.json()

        self.temp = data["main"]["temp"]
        self.description = data["weather"][0]["description"]
        self.humidity = data["main"]["humidity"]

        self.todas = (self.temp,self.description,self.humidity)
        print(self.todas)