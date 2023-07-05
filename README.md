# Abstraction and Encapsulation

This repository contains three programs that demonstrate the concepts of abstraction and encapsulation: The Fan Class, The Car Class, and The Pet Class. Each program showcases the implementation of these principles in different scenarios.

## The Fan Class
Design a class named Fan to represent a fan. The class includes the following:

- Three constants: SLOW, MEDIUM, and FAST, with values 1, 2, and 3, respectively, to represent the fan speed.
    - Private instance variables:
            
            speed (an integer) to specify the speed of the fan.
            on (a boolean) to specify whether the fan is on (default is False).
            radius (a float) to specify the radius of the fan
            color (a string) to specify the color of the fan.
- Accessor (getter) and mutator (setter) methods for all four instance variables.
- A constructor that creates a fan object with the specified speed (default is SLOW), radius (default is 5), color (default is blue), and on/off state (default is off).

## The Car Class
The Car Class is defined in CarClass.py and tested in TestCar.py.

The Car class has the following data attributes:

    __year_model (for the car's year model)
    __make (for the make of the car)
    __speed (for the car's current speed)

The Car class includes the following methods:

    __init__: Initializes the Car object with the year model and make provided as arguments. The __speed attribute is set to 0.
    accelerate(): Increases the speed of the car by 5 each time it is called.
    brake(): Decreases the speed of the car by 5 each time it is called.
    get_speed(): Returns the current speed of the car.

To test the Car class, run the main program. It creates a Car object and calls the accelerate method five times. After each call to accelerate, it retrieves and displays the current speed of the car. Then, it calls the brake method five times, retrieves the current speed, and displays it.

## The Pet Class
- The Pet Class is defined in PetClass.py and tested in TestPet.py.

-The Pet class has the following data attributes:

    __name (for the name of the pet)
    __animal_type (for the type of animal the pet is, e.g., 'Dog', 'Cat', 'Bird')
    __age (for the age of the pet)

The Pet class includes the following methods:

    set_name(): Assigns a value to the __name attribute.
    set_animal_type(): Assigns a value to the __animal_type attribute.
    set_age(): Assigns a value to the __age attribute.
    get_name(): Returns the value of the __name attribute.
    `get_animal_type()

To test the Pet class, run the main program. It creates an object of the Pet class and prompts the user to enter the name, type, and age of their pet. The entered data is stored as attributes of the object. The program then uses the accessor methods to retrieve the pet's name, type, and age, and displays this data on the screen.

## Installation requirements

- tkinter


```bash
    pip install tkinter
```
