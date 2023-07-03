from Car import Car
from Car_GUI import create_gui

if __name__ == "__main__":
    #create car object
    car = Car(2023, "Lexus")

    #start GUI
    create_gui(car)