class FanControl:
    def __init__(self, fan_gui):
        self.fan_gui = fan_gui

        #Create Fan object
        self.fan = Fan()

        #Set initial value
        self.fan_gui.set_speed(self.fan.get_speed())
        self.fan_gui.set_radius(self.fan.get_radius())
        self.fan_gui.set_color(self.fan.get_color())
        self.fan_gui.set_on(self.fan.is_on())

        #Set event handlers
        self.fan_gui.speed_scale.config(command=self.change_speed)
        self.fan_gui.radius_scale.config(command=self.change_radius)
        self.fan_gui.color_btn.config(command=self.change_color)
        self.fan_gui.on_off_btn.config(command=self.toggle_fan)

    def change_speed(self, speed):
        self.fan.set_speed(int(speed))
    
    def change_radius(self, radius):
        self.fan.set_radius(int(radius))
    
    def change_color(self):
        color = self.fan_gui.ask_color()
        if color:
            self.fan.set_color(color)
    
    def toggle_fan(self):
        on = self.fan.is_on()
        self.fan.set_on(not on)
        self.fan_gui.set_on(self.fan.is_on())