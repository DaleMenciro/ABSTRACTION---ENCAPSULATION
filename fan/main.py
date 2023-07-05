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

        #Window For Fan 2