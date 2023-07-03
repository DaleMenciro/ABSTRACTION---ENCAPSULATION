class Pet: #class representing pet

    '''
    Attributes:
    __name (for the name of a pet)
    __animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
    __age (for the pet’s age)

    Methods:
        set_name() - ssigns a value to the __name field.
        set_animal_type()- assigns a value to the __animal_type field
        set_age() - assigns a value to the __age field.
        get_name() - returns the value of the __name field
        get_animal_type() - returns the value of the __animal_type field
        get_age() - returns the value of the __age field

    '''
    def __init__ (self):
        #initializing attributes
        self __name= ""
        self __animal_type = ""
        self _age = 0

    def set_name (self, name):
        try:
            #check if the input is string
            if isinstance(name, str):
                self.__name = name
            else:
                raise ValueError ("Name should be a string")
        except ValueError as e:
            print(e)
    
    def set_animal_type(self, animal_type):
        try:
            #check if the input is string
            if isinstance(animal_type, str):
                self.__animal_type = animal_type
            else:
                raise ValueError ("Animal type should be a string")
        except ValueError as e:
            print(e)
    
    def set_age (self, age):
        try: 
            #Convert input to an integer
            age = int(age)
