from tkinter import *
import os
import sys

py = sys.executable

#window

root = Tk()
# root.geometry('600x800')
root.title('QUIZTROPHIC')
root.config(bg = '#CBD18F')

root.geometry('700x800')

def start():
    # root.destroy()
    os.system('%s %s' % (py, 'quiz.py'))
    

button1 = Button(root, text = 'start', command = start)

button2= Button(root, text = 'Instructions')

button1.pack(pady = 20)
button2.pack(pady= 20)


root.mainloop()