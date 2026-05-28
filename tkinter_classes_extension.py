"""
=========================================================
FINAL TERM PROJECT
Course: Object Oriented Programming (OOP)

Project Title:
Object-Oriented Analysis and Extension of Tkinter Library

Project Description:
This project analyzes the Tkinter library using Object-
Oriented Programming concepts such as inheritance,
encapsulation, abstraction, and polymorphism.

The project includes:
1. Analysis of Tkinter classes
2. OOP design understanding
3. Custom subclass extensions
4. Working GUI implementation

Classes Extended:
- CustomWindow → extends Tk
- CustomFrame → extends Frame
- CustomLabel → extends Label
- CustomEntry → extends Entry
- CustomButton → extends Button

Purpose of Extension:
The purpose of this extension is to demonstrate how
Tkinter classes can be customized using inheritance
and additional functionality.

Features:
✔ Custom GUI window
✔ Custom styling
✔ User input handling
✔ Validation
✔ Message box interaction

=========================================================
"""
import tkinter as tk
from tkinter import messagebox


# =================================
# Custom Window Extension
# =================================
class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter OOP Extension Project")
        self.geometry("500x350")
        self.configure(bg="lightblue")

# =================================
# Custom Frame Extension
# =================================
class CustomFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg="white",
            padx=20,
            pady=20,
            bd=3,
            relief="ridge"
        )

# =================================
# Custom Label Extension
# =================================
class CustomLabel(tk.Label):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            font=("Arial", 14, "bold"),
            bg="white"
        )

# =================================
# Custom Entry Extension
# =================================
class CustomEntry(tk.Entry):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=30,
            font=("Arial", 12)
        )

    def get_input(self):
        return self.get()

