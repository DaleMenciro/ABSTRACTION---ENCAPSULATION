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
        self.button_frame = tk.Frame(self.master,bg="#f0f0f0")
        self.button_frame.pack()

        #acceleration button
        self.acceleration_button = tk.Button(
            self.button_frame,
            text="Accelerate",
            font= ("Arial", 12),
            bg = "#66bb6a",
            fg = "white",
            activebackground="#4caf50",
            activeforeground= "white",
            command= self.accelerate
        )
        self.acceleration_button.grid(row = 0, column= 0, padx = 10)

        #brake button
        self.brake_button = tk.Button(
            self.button_frame,
            text= "Brake",
            font= ("Arial", 12),
            bg = "#ef5350",
            fg = "white",
            activebackground= "#e53935",
            activeforeground= "white",
            command= self.brake,
        )
        self.brake_button.grid(row= 0, column= 1, padx= 10)

    def update_speed_label(self):
        # Update the speed label with the current speed
        speed = self.car.get_speed()
        self.speed_label.configure(text=f"Current Speed: {speed}")

    def accelerate(self):
        # Call the car's accelerate method and update the speed label
        self.car.accelerate()
        self.update_speed_label()

    def brake(self):
        # Call the car's brake method and update the speed label
        self.car.brake()
        self.update_speed_label()


def create_gui(car):
    # Create the main Tkinter window and the CarGUI object
    root = tk.Tk()
    gui = GUICar(root, car)
    root.mainloop()