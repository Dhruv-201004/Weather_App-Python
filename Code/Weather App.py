from tkinter import *
import requests
import json
from datetime import datetime
from PIL import Image

#Initialising Program Window

root = Tk()
root.geometry("900x700")
root.resizable(0,0)
root.configure(bg="#00FFFF")
root.title("Weather App")

#BackGround Image

bg=PhotoImage(file="Weather App.png")
label=Label(root,image=bg)
label.place(x=0,y=0,width=1000,height=300)

#App Icon

image_icon=PhotoImage(file="Logo.png")
root.iconphoto(False,image_icon)


#Functions to fetch and display weather info

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

city_value = StringVar()

def showWeather():
    api_key = "7febb35f2635e1ed7acec50d9f21e5bd"

    # Get city name from user from the Input field
    city_name = city_value.get()

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&exclude=hourly&appid=' + api_key

    # Get the response from fetched url
    response = requests.get(weather_url)

    # Changing response from json to python readable format
    weather_info = response.json()

    tfield.delete("1.0", "end")

    #Condition for data fetching
    if weather_info['cod'] == 200:
        kelvin = 273

        # Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)


        weather = (f"\n\nWeather of: {city_name}\n\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\n"
                   f"Pressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\n\nInfo: {description}")
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather,)


#Frontend part of code - Interface

city_head = Label(root, anchor="center",text='Enter City Name', font='Arial 18 bold').pack(pady=5)
inp_city = Entry(root,justify="center", textvariable=city_value, width=24,bg="#EEEED1" ,font='Arial 18 bold').pack(pady=5)

b=Button(root, command=showWeather, text="Check Weather", font="Arial 13", bg='lightblue', fg='black',activebackground="teal", padx=10, pady=10).pack(pady=30)

#Output

weather_now = Label(root,anchor="center", text="The Weather is:", font='arial 18 bold').pack(pady=30)
tfield = Text(root,font="Arial 18 bold", width=100, height=25,bg="#EEEED1")
tfield.pack()
root.mainloop()