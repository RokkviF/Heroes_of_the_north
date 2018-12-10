from Tkinter import *
import Tkinter

path = "Title.jpg"
root = Tk()
root.title("test")
frame = Frame(root)
Frame(width=200, height=150).pack()
button1 = Tkinter.Button(frame, text="1 Player").pack()
button2 = Button(frame, text="2 Player").pack()
button1.place(x= 80, height=100, width=100)
frame.pack() 
root.mainloop()