from tkinter import *  #tkinter library used 
from tkinter import ttk  #used for combo box
import  requests
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=60fd7b70690214e872e699249067f892").json( )
    w_lable1.config(text=data["weather"][0]["main"])
    wb_lable1.config(text=data ["weather"][0]["description"])
    temp_lable1.config(text=str(data["main"]["temp"]-273.15))
    press_lable1.config(text=data["main"]["pressure"])


import pyttsx3
voice_handeler=pyttsx3.init()
voices=voice_handeler.getProperty('voices')
voice_handeler.setProperty('voice',voices[1].id)
voice_handeler.say("Hello everyone welcome to our weather app project please enter the city name")
voice_handeler.runAndWait()


win = Tk()
win.title("Weather App")
win.config(bg="light blue")
win.geometry("500x540")

name_lable=Label(win,text="Weather App",   #for title fg is for custamize the button65
                 font=("Time New Roman",30,"bold"))      #for font
name_lable.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry","Pune","Mumbai","satara","koregaon","kolhpur",]

com = ttk.Combobox(win,text="Weather App",values=list_name,    
                 font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_lable = Label(win,text="Weather climate",     #for title
                 font=("Time New Roman",15,))      #for font
w_lable.place(x=25,y=260,height=50,width=210)

w_lable1=Label(win,text="",     #substitute lables
                 font=("Time New Roman",15,))      
w_lable1.place(x=250,y=260,height=50,width=210)


wb_lable = Label(win,text="Weather description",     
                 font=("Time New Roman",15,))      
wb_lable.place(x=25,y=330,height=50,width=210)

wb_lable1 = Label(win,text="",     #substitute lables
                 font=("Time New Roman",15,))  
wb_lable1.place(x=250,y=330,height=50,width=210)


temp_lable = Label(win,text=" Temprature",     
                 font=("Time New Roman",15,))      
temp_lable.place(x=25,y=400,height=50,width=210)

temp_lable1=Label(win,text="",     #substitute lables
                 font=("Time New Roman",15,))      
temp_lable1.place(x=250,y=400,height=50,width=210)



press_lable = Label(win,text="Pressure",     
                 font=("Time New Roman",15,))      
press_lable.place(x=25,y=470,height=50,width=210)


press_lable1=Label(win,text="",     #substitute lables
                 font=("Time New Roman",15,))      
press_lable1.place(x=250,y=470,height=50,width=210)


done_button =Button(win,text="done",# for after chossing  state and done button 
                     font=("Time New Roman",20,"bold"),command=data_get)   #function calling

done_button.place(y=190,height=50,width=100,x=200)   #xaixs show middle position of done button ,y axis shows upper position from app




win.mainloop()


import pyttsx3
voice_handeler=pyttsx3.init()
voices=voice_handeler.getProperty('voices')
voice_handeler.setProperty('voice',voices[1].id)
voice_handeler.say("thank you for visiting our app")
voice_handeler.runAndWait()

