import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize weather history list
search_history = []

# Function to update weather background and icon
def update_visuals(weather_desc):
    if "rain" in weather_desc:
        app.configure(bg="#b3d1ff")
        icon_label.config(text="🌧️")
    elif "clear" in weather_desc:
        app.configure(bg="#ffffcc")
        icon_label.config(text="☀️")
    elif "cloud" in weather_desc:
        app.configure(bg="#d9d9d9")
        icon_label.config(text="☁️")
    elif "snow" in weather_desc:
        app.configure(bg="#e0f7fa")
        icon_label.config(text="❄️")
    else:
        app.configure(bg="#e6f2ff")
        icon_label.config(text="🌈")

# Function to get current weather
def get_weather():
    city_name = city_entry.get().strip()
    if not city_name:
        result_label.config(text="❗ Please enter a city name.", fg="red")
        return

    api_key = "c122ee56a9a8f997ce02119b8a8858d5"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        weather = data["weather"][0]["description"].title()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"📍 {city_name}\n"
            f"🌤️ {weather}\n"
            f"🌡️ {temperature}°C\n"
            f"💧 {humidity}% humidity\n"
            f"💨 {wind_speed} m/s wind"
        )
        result_label.config(text=result, fg="black")

        update_visuals(weather.lower())  # Set background/icon based on weather

        # Add to history
        if city_name not in search_history:
            search_history.append(city_name)
            history_list.insert(tk.END, city_name)

    except requests.exceptions.HTTPError:
        result_label.config(text="❌ City not found or API error.", fg="red")
    except Exception as e:
        result_label.config(text=f"⚠️ Error: {str(e)}", fg="red")

# Setup GUI
app = tk.Tk()
app.title("Weather App ⛅")
app.geometry("600x400")
app.configure(bg="#e6f2ff")

# Date and Time
now = datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
time_label = tk.Label(app, text=now, font=("Segoe UI", 10, "italic"), bg="#e6f2ff", fg="gray")
time_label.pack(pady=5)

# Weather Icon
icon_label = tk.Label(app, text="🌈", font=("Arial", 40), bg="#e6f2ff")
icon_label.pack()

# Title
title_label = tk.Label(app, text="Weather Info", font=("Arial Rounded MT Bold", 20), bg="#e6f2ff", fg="#333")
title_label.pack(pady=5)

# Input and button
city_entry = tk.Entry(app, font=("Segoe UI", 14), width=25, justify="center", bd=2, relief="groove")
city_entry.pack(pady=5)

get_button = tk.Button(app, text="Get Weather", font=("Segoe UI", 12, "bold"), bg="#4CAF50", fg="white",
                       padx=20, pady=5, bd=0, activebackground="#45a049", command=get_weather)
get_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="", font=("Segoe UI", 12), bg="#e6f2ff", justify="left", wraplength=400)
result_label.pack(pady=10)

# History Frame
history_frame = tk.Frame(app, bg="#e6f2ff")
history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

tk.Label(history_frame, text="🔁 Search History", font=("Segoe UI", 10, "bold"), bg="#e6f2ff", fg="black").pack()
history_list = tk.Listbox(history_frame, width=20, height=10, font=("Segoe UI", 10))
history_list.pack(pady=5)

# Footer
footer = tk.Label(app, text="Made with ❤️ using OpenWeatherMap API", font=("Segoe UI", 8, "italic"),
                  bg="#e6f2ff", fg="gray")
footer.pack(side="bottom", pady=10)

app.mainloop()
