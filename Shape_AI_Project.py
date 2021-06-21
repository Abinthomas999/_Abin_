import requests
from datetime import datetime


#Cridentials and Url..
api_ ="c82c3cf6e80179d831f3a3c78aa66660"
City_ = input("Please inpiut the City name: ")

#Url construction..
Url_ ="https://api.openweathermap.org/data/2.5/weather?q="+City_+"&appid="+api_


#Geting data from url..
Get_Data= requests.get(Url_)
Content_ = Get_Data.json()


#Sorting the data...
Humdty_= Content_['main']['humidity']
Dscrptn_ = Content_['weather'][0]['description']
Wnd_Spd=Content_['wind']['speed']
Date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
Temp_ = '%.2f'%((Content_['main']['temp'])-273.15)
City_= Content_['name']


#Creating and inputing data to a text doc..
fname=open("Shape_AI_Project.txt","w+")

fname.write("\nCurrent Wather Status in %s"%City_)
fname.write("\n...............................")
fname.write("\nCity Name          :%s" %City_)
fname.write("\nTemperature        :%s Celsius" %Temp_)
fname.write("\nHumidity           :%s" %Humdty_)
fname.write("\nWind Speed         :%s" %Wnd_Spd)
fname.write("\nDescription        :%s" %Dscrptn_)

fname.close()

fname=open("Shape_AI_Project.txt","r")
t_file=fname.read()
for a in t_file:
    print(a,end="")
fname.close()



    
'''
Sample Output
.............



Please inpiut the City name: Kochi

Current Wather Status in Kochi
...............................
City Name          :Kochi
Humidity           :85
Wind Speed         :3.58
Description        :overcast clouds
Temperature        :25.99 Celsius
'''
    