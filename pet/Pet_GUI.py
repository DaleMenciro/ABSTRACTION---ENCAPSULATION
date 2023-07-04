import tkinter as tk
from tkinter import messagebox

class PetGUI:
    def __init__(self, master, pet):
        self.master = master
        self.pet = pet

        self.master.title("Pet GUI")
        self.master.geometry("300x200")
        self.master.config(bg="#f0f0f0")

        #name label
        self.name_label = tk.Label(
            self.master, text = "Name" , font=("Arial", 12), bg="#f0f0f0"
        )
        self.name_label.pack()

        #name entry
        self.name_entry = tk.Entry(self.master, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        #animal type label
        self.animal_type_label = tk.Label(
            self.master, text="Animal Type:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.animal_type_label.pack()

        #animal type entry
        self.animal_type_entry = tk.Entry(self.master, font=("Arial", 12))
        self.animal_type_entry.pack(pady=5)
        
        #age label
        self.age_label = tk.Label(
            self.master, text="Age:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.age_label.pack()

        #age entry
        self.age_entry = tk.Entry(self.master, font=("Arial", 12))
        self.age_entry.pack(pady=5)

        #submit button
        self.submit_button = tk.Button(
            self.master,
            text = "Submit",
            font= ("Arial", 12),
            bg = "#66bb6a",
            fg = "white",
            activebackground= "#4caf50",
            activeforeground= "white",
            command= self.submit,
        )
        self.submit_button.pack(pady= 10)

    def submit(self):
        #get the input values
        name = self.name_entry.get()
        animal_type = self.animal_type_entry.get()
        age = self.age_entry.get()


    
    def show_pet_information(self):
        #get pet's info
        name = self.pet.get_name()
        animal_type = self.pet.get_animal_type()
        age = self.pet.get_age()

        #create info display
        info = f"Pet's name: {name}\nAnimal type: {animal_type}\nAge: {age}"
        #pack and label
        info_label = tk.Label(
            self.master, text=info, font=("Arial", 12), bg="#f0f0f0"
            )
        info_label.pack(pady=10)


def create_gui(pet):
    root = tk.Tk()
    gui = PetGUI(root, pet)
    root.mainloop()