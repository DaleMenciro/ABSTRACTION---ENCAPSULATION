import tkinter as tk
from Fan_GUI import FanGUI
from Fan_Control import FanControl
from Fan import Fan

class FanTest:
    def __init__(self):
        #create two Fan objects with different properties
        self.fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        self.fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)
    
    def display_fan_properties(self,fan_gui,fan):
        fan_gui.set_speed(fan.get_speed())
        fan_gui.set_radius(fan.get_radius())
        fan_gui.set_color(fan.get_color())
        fan_gui.set_on(fan.is_on())
    
    def run_test(self):
        #Window for Fan 1
        window1 = tk.Tk()
        window1.title("Fan 1 Properties")
        fan_gui1 = FanGUI(window1)
        fan_control1 = FanControl(fan_gui1)
        self.display_fan_properties(fan_gui1, self.fan1)
        window1.geometry("300x300")
        window1.configure(bg="#f2f2f2")
        self.center_window(window1)
        window1.mainloop()

        #Window For Fan 2
        window2 = tk.Tk()
        window2.title("Fan 2 Properties")
        fan_gui2 = FanGUI(window2)
        fan_control2 = FanControl(fan_gui2)
        self.display_fan_properties(fan_gui2, self.fan2)
        window2.geometry("300x300")
        window2.configure(bg="#f2f2f2")
        self.center_window(window2)
        window2.mainloop()