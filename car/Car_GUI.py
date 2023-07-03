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

        #label for speed
        self.speed_label = tk.Label(
            self.master, text = "Current Speed: 0", font=("Arial", 16), bg="#f0f0f0"
        )
        self.speed_label.pack(pady=20)
        
        #frame for buttons
        self.button_frames = tk.Frame(self.master,bg="#f0f0f0")
        self.button_frames.pack()
        
        #acceleration button
        #brake button

root = tk.Tk()
car_gui = GUICar(root, Car)
root.mainloop()