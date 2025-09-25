import requests
import tkinter as tk
from tkinter import messagebox
def get_weather():
 city_name = city_entry.get()
 api_key = "c122ee56a9a8f997ce02119b8a8858d5" # Replace with your actual API key
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
 weather = data["weather"][0]["description"]
 temperature = data["main"]["temp"]
 humidity = data["main"]["humidity"]
 wind_speed = data["wind"]["speed"]
 result = (
 f"Weather in {city_name}:\n"
 f"Description: {weather}\n"
 f"Temperature: {temperature}°C\n"
 f"Humidity: {humidity}%\n"
 f"Wind Speed: {wind_speed} m/s"
 )
 result_label.config(text=result, fg="black", bg="lightpink") # Added background color to result
label
 except requests.exceptions.HTTPError:
 messagebox.showerror("Error", f"City '{city_name}' not found or API error.")
 except Exception as e:
 messagebox.showerror("Error", str(e))
# GUI Setup
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300") # Adjusted size for better layout
# Set background color for the entire window
app.configure(bg="#D3E5FF")
# Title label
title_label = tk.Label(app, text="Weather Information", font=("Helvetica", 16, "bold"), bg="#D3E5FF")
title_label.pack(pady=10)
# City entry
tk.Label(app, text="Enter city name:", font=("Helvetica", 12), bg="#D3E5FF").pack(pady=5)
city_entry = tk.Entry(app, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)
# Weather button
tk.Button(app, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="lightgreen",
fg="black", relief="raised").pack(pady=15)
# Result label with color
result_label = tk.Label(app, text="", font=("Helvetica", 12), justify="left", bg="lightblue", padx=10,
pady=10)
result_label.pack(pady=10)
app.mainloop()