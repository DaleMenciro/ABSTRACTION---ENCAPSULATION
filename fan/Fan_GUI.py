import tkinter as tk
import tkinter.colorchooser as colorchooser

class FanGUI:
    def __init__(self, parent):
        self.parent = parent

        #GUI elements
        self.speed_scale = tk.Scale(self.parent, from_=1, to=3, orient=tk.HORIZONTAL, label="Speed")
        self.radius_scale = tk.Scale(self.parent, from_=1, to=10, orient=tk.HORIZONTAL, label="Radius")
        self.color_btn = tk.Button(self.parent, text="Select Color")
        self.on_off_btn = tk.Button(self.parent, text="Turn On/Off")
        self.status_label = tk.Label(self.parent, text="Fan Status: ")

        #Elements layout

