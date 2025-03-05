import tkinter as tk            # for creating the GUI
import requests                 # for fetching weather data from the OpenWeather API
from tkinter import messagebox  # for showing pop-up error messages

def get_weather(city):
    api_key = "92b80276db8821606d5b387abf6575e1"
    # url for current weather
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        # make request to 'OpenWeather'
        response = requests.get(url)
        # parse the response as json
        data = response.json()
        # if response is successful, get temperature and weather description
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return temperature, description
        else:
            messagebox.showerror("Error", "City not found or API request failed.")
            return None, None
    except requests.exceptions.RequestException:
        # handle network errors
        messagebox.showerror("Error", "Network error. Please check your internet connection.")
        return None, None
