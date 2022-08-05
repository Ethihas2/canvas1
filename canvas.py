from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("600x600")
root.title("Canvas")

label_entry = Label(root,text="Enter a color: ")
label_entry.place(relx=0.7,rely=0.9,anchor=CENTER)

color_entry = Entry(root)
color_entry.insert(0, "black")
color_entry.place(relx=0.88,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=590,height=510,bg="white",highlightbackground="light gray")
canvas.pack()

img = ImageTk.PhotoImage(Image.open('start_point1.png'))
my_img = canvas.create_image(50,50,image=img)

old_x = 50
old_y = 50

new_x = 50
new_y = 50

direction = ""

def draw(direction,old_x,old_y,new_x,new_y):
    input_color = color_entry.get()
    
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()