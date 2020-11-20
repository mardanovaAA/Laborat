import tkinter as tk
import time
from random import randint

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg = 'white')
canv.pack(fill = tk.BOTH, expand = 1)

COLORS = ['red', 'blue', 'maroon', 'gold', 'coral']

def hit(event = 0):
    global target
    if ((event.x - 400)**2 + (event.y - 300)**2) <= ((200)**2):
            canv.delete(target)
            target = canv.create_oval(200, 100, 600, 500, fill = COLORS[randint(0, 4)])
            canv.itemconfig(target) 
              

screen1 = canv.create_text(400, 50, text='', font='28')
canv.itemconfig(screen1, text = 'Простая игрушка для изучения функционала tkinter')
screen1 = canv.create_text(400, 550, text = '', font = '28')
canv.itemconfig(screen1, text = 'Тыкните на круг')
target = canv.create_oval(200, 100, 600, 500, fill = COLORS[randint(0, 4)])
canv.itemconfig(target)
canv.bind('<Button-1>', hit)                        
canv.update()

root.mainloop()