import tkinter as tk
from Car import Car

class GUICar:
    #initializing GUICar object with master window and car object
    def __init__(self, master, car):
        self.master = master
        self.car = car

        self.master.title ("Car GUI")
        self.master.geometry ("300x200")
        self.master.config(bg="#f0f0f0") #background color

