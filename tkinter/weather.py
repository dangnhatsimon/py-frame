from tkinter import *
import requests
import json

root = Tk()
root.title("Weather")
root.iconbitmap('D:/Python/TKinter/search_book_open_search_locate_6178.ico')
root.geometry("400x400")

def zipLookup():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)
    
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=3DDCC83E-D83E-4B8C-A3E5-B8AB461D43C7")
        # api = api_request.json()
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
        
        root.configure(background = weather_color)
        myLabel = Label(
        root, text=city + " Air Quality " + str(quality) + " " + category,
        font=("Times New Romans", 15),
        background = weather_color
    )
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text= "Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()
