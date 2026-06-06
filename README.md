# 🧠 Tkinter OOP Analysis Project

## 🎥 Project Presentation
👉 Presentation Video: https://youtu.be/UIy3640KAkQ?si=TWuecKVjP4fe6ycV

This video contains the complete presentation and explanation of our Tkinter OOP Analysis Project.

---

## 📌 Overview
This project is a Final Term assignment for Object Oriented Programming.  
We selected the Python library **Tkinter** and performed a complete OOP-based analysis of its internal structure, classes, and design principles.

Along with analysis, we also developed a custom extension using Tkinter to demonstrate real-world OOP implementation.

---

## 🎯 Objectives
- To understand the architecture of the Tkinter library  
- To analyze its main classes and OOP principles  
- To design class diagrams representing relationships  
- To implement a custom extension using inheritance  
- To evaluate strengths and limitations of the library design  

---

## 📚 Library Chosen
👉 **Tkinter (Python GUI Library)**

Tkinter is Python’s standard GUI toolkit used for building desktop applications.
---

## 🏗️ OOP Concepts Applied

### 1. Inheritance
Tkinter widgets inherit from base widget classes.

### 2. Encapsulation
Each widget manages its own properties like text, color, size, etc.

### 3. Polymorphism
Different widgets behave differently using common methods like `pack()`, `grid()`.

### 4. Abstraction
Complex GUI implementation is hidden behind simple classes and methods.

---

## 📊 Class Diagram
The class diagram for Tkinter hierarchy is included in the `diagrams/` folder.

---

## 💻 Custom Extension
We created a custom class by extending Tkinter widgets to demonstrate OOP usage in real applications.

### Example:
```python
import tkinter as tk

class MyButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="blue", fg="white")

root = tk.Tk()
btn = MyButton(root, text="Click Me")
btn.pack()

root.mainloop()
