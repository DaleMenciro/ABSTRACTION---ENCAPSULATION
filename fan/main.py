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
    
    def run_test(self):