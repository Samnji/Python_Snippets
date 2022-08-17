from tkinter import *
from tkinter.ttk import *

def sayHello():
	textbox1 = Message("")
	textbox1.place(x=100, y=170, height=30, width=80)
	name = textbox1.get()
	message = str("Hello " + name)
	textbox1["text"] = message
	textbox1["bg"] = "red"
	textbox1["fg"] = "white"
	
window = Tk()
window.title("Greetings")
window.geometry("350x350")

lablel = Label(text="Enter your name:")
lablel.place(x=100, y=100)

textbox2 = Entry()
textbox2["justify"] = "center"
textbox2.place(x=200, y=100)
textbox2.focus()

button = Button(text="Click me", command = sayHello)
button.place(x=100, y=150, height=30, width=80)



window.mainloop()