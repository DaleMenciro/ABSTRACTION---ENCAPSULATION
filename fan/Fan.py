class Fan:
    '''
    Attributes:
    __speed : int - fan's speed
    __on : bool - specifies whether the fan is on or off (the default is False)
    __radius : float - radius of fan
    __color : str - color of the fan

    Methods:
     get_speed - gets fan's speed
     set_speed - sets fan's speed
     is_on - returns the current state of the fan (on/off).
     set_on - set the electric fan whenever it is on/off
     get_radius - gets fan's radius
     set_radius - sets fan's radiues
     get_color - gets fan's color
     set_color - sets fan's color
    '''
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius= 5, color= 'blue', on=False):
        """
        Initializes a Fan object with the specified properties.

        Arguments:
            speed (int): The speed of the fan. Defaults to SLOW.
            radius (float): The radius of the fan. Defaults to 5.
            color (str): The color of the fan. Defaults to 'blue'.
            on (bool): Whether the fan is turned on. Defaults to False.
        """
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def is_on(self):
        return self.__on
    
    def set_on(self, on):
        self.__on = on
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

        