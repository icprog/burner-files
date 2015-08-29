#!/usr/bin/python
import Tkinter
from Tkconstants import *
from time import sleep

WIDTH = 20
HEIGHT = 10
SCALE = 10
R = 6

class SimDisplay(object):
	def __init__(self):
		self.tk = Tkinter.Tk()
		self.tk.after_idle(self.idle)

	def run(self):
		self.frame = Tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
		self.frame.pack(fill=BOTH,expand=1)

		canvas = Tkinter.Canvas(self.frame, width=WIDTH * SCALE, height=HEIGHT * SCALE)
		canvas.pack(fill=X, expand=1)

		self.pixels = [canvas.create_oval(x * SCALE, y * SCALE, (x + 1) * SCALE, (y + 1) * SCALE)
				for x in range(WIDTH)
				for y in range(HEIGHT)]
				
		self.button = Tkinter.Button(self.frame,text="Exit",command=self.tk.destroy)
		self.button.pack(side=BOTTOM)

		self.i = 0
		self.tk.mainloop()

	def idle(self):
		print self.i
		self.i += 1

sd = SimDisplay()
sd.run()
