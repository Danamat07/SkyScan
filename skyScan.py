import tkinter as tk  # for creating the GUI
import requests  # for fetching weather data from the OpenWeather API
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


def create_gui():
    # create main window
    root = tk.Tk()
    root.title("SkyScan")

    # set window size and center it on the screen
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    # set the position and size of the window
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

    # create and place widgets
    city_label = tk.Label(root, text="Enter city name:")
    city_label.grid(row=0, column=0, padx=10, pady=10)
    # create an entry widget for the user to input the city name
    city_entry = tk.Entry(root)
    city_entry.grid(row=0, column=1, padx=10, pady=10)
    # label for displaying results
    result_label = tk.Label(root, text="Weather info will appear here.")
    result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    # define action at button-click
    def on_button_click():
        # get city name input
        city = city_entry.get()
        if city:
            # fetch weather data and update result label
            temperature, description = get_weather(city)
            if temperature and description:
                result_label.config(text=f"Temperature: {temperature}°C\nDescription: {description.capitalize()}")
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")

    # create a button that calls on_button_click() when pressed
    search_button = tk.Button(root, text="Get Weather", command=on_button_click)
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # run the main loop to display the window
    root.mainloop()


if __name__ == "__main__":
    create_gui()
