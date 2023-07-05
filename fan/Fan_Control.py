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
        self.fan_view.speed_scale.config(command=self.change_speed)
        self.fan_view.radius_scale.config(command=self.change_radius)
        self.fan_view.color_btn.config(command=self.change_color)
        self.fan_view.on_off_btn.config(command=self.toggle_fan)