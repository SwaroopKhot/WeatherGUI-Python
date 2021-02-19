import tkinter as tk
import requests 
from PIL import ImageTk
 


# Root Screen:
root = tk.Tk()
root.title('Weather Enquiry')

def check_weather(weather) :
	try :
		City_Name = weather['name']
		Country_Name = weather['sys']['country']
		Clouds_Types = weather['weather'][0]['description']
		Tempreature = weather['main']['temp']
		Temp_feel =  weather['main']['feels_like']
		Pressure = weather['main']['pressure']
		Humidity = weather['main']['humidity']
		Wind_Speed = weather['wind']['speed']
		Sunrise = weather['sys']['sunrise'] 
		sunset =  weather['sys']['sunrise']

		final_str = 'City Entered: {0} \nCountry Name: {1} \nClouds Types: {2} \nTempreature: {3}°C \nFeels Like: {4}°C \nPressure: {5} Atm \nHumidity: {6}% \nWind speed: {7}m/s \nSunrise: {8}-UTC \nSunset: {9}-UTC'.format(City_Name, Country_Name,Clouds_Types, Tempreature, Temp_feel, Pressure, Humidity, Wind_Speed, Sunrise, sunset)
		# print(final_str)

	except:
		final_str = 'Their might be error in network connection or in UID key or City might not be avaiable. \nPlease confirm! Thank you...'

	return final_str




def get_weather(city):
	weather_key = '' # Paste Your own ID from OpenWeathermap site.....
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID' : weather_key, 'q': city, 'units':'metric'}
	response = requests.get(url, params=params)
	weather=response.json()

	if weather_key == '':
		label['text'] = 'You have no API Id to run request.\nPlease go to openweathermap.org and paste the UID key and save file...\nThis is an ID Error !'
	else:
		label['text'] = check_weather(weather)

	'''

	# console prints for debug:
	print(weather)
	print("City Name :",weather['name'])
	print("Country Name",weather['sys']['country'])
	print("Clouds Types : ",weather['weather'][0]['description'])
	print("Tempreature : ",weather['main']['temp'])
	print("Tempreature Feels like :",weather['main']['feels_like'])
	print("Pressure : ",weather['main']['pressure'])
	print("Humidity : ",weather['main']['humidity'])
	print("Wind Speed : ",weather['wind']['speed'])
	print("Sunrise & Sunset : ",weather['sys']['sunrise'] , weather['sys']['sunrise'])

	'''
	





image = ImageTk.PhotoImage(file = "bg1.jpg")  # Paste full path of this image or there will be an error- '_PhotoImage__photo'
canvas = tk.Canvas(root, height=500, width= 700)
canvas.create_image(190 , 170, image = image)
canvas.pack()



frame = tk.Frame(root, bg="#dff2f3", bd=4)
frame.place(relwidth=0.75, relx=0.5, rely=0.1, relheight=0.1, anchor='n')

entry= tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, bg='#acd2df', text = "Get Weather", font=20, command=lambda: get_weather(entry.get()))
button.place(relwidth=0.3, relx=0.7, relheight=1)

lower_frame = tk.Frame(root, bg="#d1e5e6", bd=2)
lower_frame.place(relx=0.5,rely=0.25, relwidth=0.75, relheight=0.6,anchor='n')

label = tk.Label(lower_frame, bg='#fcffee')
label.place(relwidth=1, relheight=1)




root.mainloop()
