class FanControl:
    def __init__(self, fan_gui):
        self.fan_gui = fan_gui

        #Create Fan object
        self.fan = Fan()

        #Set initial value
        self.fan_view.set_speed(self.fan.get_speed())
        self.fan_view.set_radius(self.fan.get_radius())
        self.fan_view.set_color(self.fan.get_color())
        self.fan_view.set_on(self.fan.is_on())

        #Set event handlers