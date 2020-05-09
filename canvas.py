import tkinter as tk
import math as m



root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=400) #background='grey'
canvas.pack()

def paint(event):
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	canvas.create_oval(x1, y1, x2, y2, fill='green')

canvas.bind("<B1-Motion>", paint)

label = tk.Label(root, text="Drag your left button of mouse to paint.")
label.pack(side='bottom')

def text():
	retrun 'Mix'

tk.mainloop()
