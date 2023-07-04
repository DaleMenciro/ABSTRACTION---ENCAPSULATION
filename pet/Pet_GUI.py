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

        #submit button