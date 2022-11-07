import requests
import json

city_name = input("Anna kaupungin nimi: ")
API_key = "24325c7a805383c33b9030224db0602c"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
vastaus = requests.get(pyyntö).json()
lämpötilaKelvin = int(vastaus["main"]["temp"])
lämpötilaC = int(lämpötilaKelvin-273.15)

print(f"Lämpötila muutettuna celsius: {lämpötilaC} astetta")