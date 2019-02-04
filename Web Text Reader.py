from tkinter import *
import requests as r
from bs4 import BeautifulSoup as bs
import  pyttsx3 as sp
app = Tk()
app.title("WEBSITE TEXT READER")
wwidth = "300"
wheight = "300"
text = "Your Website Link Here !"
app.geometry(wwidth+"x"+wheight)
label = Label(text=text)
label.place(x=(int(wwidth)//2)-50,y=(int(wheight)//2)-50)
inpbox = Entry(width=50)
inpbox.place(x=(int(wwidth)//2)-110,y=(int(wheight)//2))
button = Button(text='Submit Your Website')
button.place(x=(int(wwidth)//2)-110,y=(int(wheight)//2)+50)
def fetch_and_speak(event):
	url = r.get(inpbox.get())
	data = url.text
    
	soup = bs(data,'html.parser')
	for nonsense in soup(['script','style']):
		nonsense.extract()
	text = soup.get_text()


        

	initsp = sp.init()
	initsp.say(text)
	initsp.runAndWait()


app.bind("<Button-1>",fetch_and_speak)
app.mainloop()