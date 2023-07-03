class Car:
    '''
     a class to represent car objects
    
    Class Attributes:
    
    __year_model (for the car’s year model)
    __make (for the make of the car)
    __speed (for the car’s current speed)

    Methods:
    
    accelerate()
    brake()
    get_speed()
    
    '''
    def __init__(self, year_model,make):
        #Initialize the Car objects 
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 #Start with an initial speed of 0

    def accelerate (self):
        #increase speed by 5
        self.__speed += 5