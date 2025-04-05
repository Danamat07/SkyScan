import customtkinter as ctk
import requests
from tkinter import messagebox

def get_weather(city):
    api_key = "92b80276db8821606d5b387abf6575e1"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return temperature, description
        else:
            messagebox.showerror("Error", "City not found or API request failed.")
            return None, None
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error. Please check your internet connection.")
        return None, None

def create_gui():
    # Use dark mode and rounded corners
    ctk.set_appearance_mode("System")  # Options: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    root = ctk.CTk()
    root.title("SkyScan - Weather App")

    # Set window size and center it
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    # Title label
    title_label = ctk.CTkLabel(root, text="SkyScan 🌤", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=10)

    # Entry and button frame
    input_frame = ctk.CTkFrame(root)
    input_frame.pack(pady=10)

    city_label = ctk.CTkLabel(input_frame, text="Enter City:")
    city_label.grid(row=0, column=0, padx=10, pady=10)

    city_entry = ctk.CTkEntry(input_frame, width=200)
    city_entry.grid(row=0, column=1, padx=10, pady=10)

    # Result label
    result_label = ctk.CTkLabel(root, text="Weather info will appear here.", wraplength=300, justify="center")
    result_label.pack(pady=20)

    # Button click action
    def on_button_click():
        city = city_entry.get()
        if city:
            temperature, description = get_weather(city)
            if temperature and description:
                result_label.configure(text=f"Temperature: {temperature}°C\nDescription: {description.capitalize()}")
        else:
            messagebox.showwarning("Input Error", "Please enter a city name.")

    # Search button
    search_button = ctk.CTkButton(root, text="Get Weather", command=on_button_click)
    search_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
