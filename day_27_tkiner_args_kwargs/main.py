import tkinter
import turtle


window = tkinter.Tk()
window.title("my First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a label", font=("Arial",24,"bold"))
my_label.pack(side="left")

my_label["text"] = "new Text"
my_label.config(text="New Text")
tim = turtle.Turtle()