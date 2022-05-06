from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import random

root = Tk()
root.title("Simple Weather App. By Edward Roy.")
root.geometry("900x500+300+200")
root.resizable(False, False)

print("A Simple Weather App by Edward Roy, dedicated to JiaXing \'Jahtavius\' Wang")

def upper_text(text):
    string = ''
    for i in range(0, len(text)):
        if i == 0:
            string += text[0].upper()
        elif text[i-1] == ' ' and i != 0:
            string += text[i].upper()
        else:
            string += text[i].lower()
    return string

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="Local Time", font=("Helvetica", 14, "bold"))

        # weather
        api_key = '179de25f0c0f539fe06433499ab9f8f8'
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key

        json_data = requests.get(api).json()
        print(f"\nJson Data for {upper_text(city)}:")
        print(json_data)

        condition = json_data['weather'][0]['main']
        description = upper_text(json_data['weather'][0]['description'])
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=str(temp) + "°")
        c.config(text= str(condition) + " | Feels Like " + str(temp+random.randint(-1,1)) + "°")
        w.config(text=str(wind)+" km/h")
        h.config(text=str(humidity)+"%")
        d.config(text=str(description))
        p.config(text=str(pressure)+" hPa")

    except Exception as e:
        messagebox.showerror("Simple Weather App", "Invalid Entry.")


# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# search box
search_image = PhotoImage(file="search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

img = Image.open("search_icon.png")
img = img.resize((40, 40))
search_icon = ImageTk.PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather,
                      activebackground='#404040')
myimage_icon.place(x=400, y=32)

# logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# bottom box
frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
h.place(x=270, y=430)
d = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 15, "bold"), bg="#1ab5ef")
p.place(x=650, y=430)

root.mainloop()
