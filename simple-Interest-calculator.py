from tkinter import *
import random


window = Tk()
window.geometry('750x800')
window.configure(bg="black")

def simpleInterest():
    principal = int(principalEntry.get())
    time = int(timeEntry.get())
    rate = int(rateEntry.get())

    simpleInterestCalculated = principal * time * rate/100

    output_msg = Label(result_frame, text = "Your simple interest is "+str(simpleInterestCalculated), font = ('Calibri',12), width = 42)
    output_msg.place(x =20, y = 780)
    output_msg.pack()



#heading

headingLabel = Label(window,text = "Simple Interst Calculator", fg = "green", bg = "black", font = ("Bauhaus 93", 34), bd = 4 ).pack()

principalLabel = Label(window,text = "Principal", fg = "green", bg = "black", font = ("Bauhaus 93", 28))
principalLabel.place(x = 20, y = 120)
principalEntry = Entry(window, fg = "green",bg = "darkgrey", width = 40, font = ("Bauhaus 93",12))
principalEntry.place(x = 190, y = 125)

timeLabel = Label(window,text = "Time", fg = "green", bg = "black", font = ("Bauhaus 93", 28))
timeLabel.place(x = 20, y = 180)
timeEntry = Entry(window, fg = "green",bg = "darkgrey", width = 40, font = ("Bauhaus 93",12))
timeEntry.place(x = 190, y = 185)

rateLabel = Label(window,text = "Rate", fg = "green", bg = "black", font = ("Bauhaus 93", 28))
rateLabel.place(x = 20, y = 240)
rateEntry = Entry(window, fg = "green",bg = "darkgrey", width = 40, font = ("Bauhaus 93",12))
rateEntry.place(x = 190, y = 245)

calculateButton = Button(window,text = "Calculate", width = 20, fg = "green", bg = "black", font = ("Bauhaus 93",12), command = simpleInterest)
calculateButton.place(x = 20, y = 500)

result_frame = LabelFrame(window, text = "result",fg = "green", bg = "black", font = ("Bauhaus 93", 12))
result_frame.pack(padx = 20, pady = 20)
result_frame.place(x = 20,y = 700)

result_label = Label(result_frame,text = "",fg = "green", bg = "black",  font = ("Bauhaus 93",12), width = 33)
result_label.place(x = 20,y = 780)
result_label.pack()

window.mainloop()