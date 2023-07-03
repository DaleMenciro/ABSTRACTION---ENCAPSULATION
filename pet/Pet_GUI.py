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

        #animal type entry

        #age label

        #age entry

        #submit button