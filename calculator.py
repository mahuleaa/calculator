import tkinter as tk
from tkinter import ttk
import ast

# Function to perform calculation
def calculate():
    expression = entry.get()
    try:
        result = ast.literal_eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except (ValueError, SyntaxError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character in the entry field
def delete_character():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

# Create GUI window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(False, False)

# Create a themed style
style = ttk.Style()
style.theme_use("clam")  # Choose from 'clam', 'alt', 'default', 'classic'

# Change background and foreground colors
style.configure("TLabel", background="#EFEFEF", foreground="#333333")
style.configure("TEntry", fieldbackground="white", borderwidth=5)  # Set the borderwidth for TEntry
style.configure("TButton", background="#4C4C4C", foreground="white", font=("Arial", 14, "bold"))

# Create a frame with a black border
frame = ttk.Frame(window, borderwidth=2, relief="solid")
frame.pack(padx=10, pady=10)

# Add a heading
heading = ttk.Label(frame, text="Calculator", font=("Arial", 24, "bold"))
heading.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Create an entry field
entry = ttk.Entry(frame, width=30, font=("Arial", 20))
entry.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

# Create number buttons
buttons = [
    ttk.Button(frame, text=str(i), command=lambda num=i: button_click(num))
    for i in range(1, 10)
]

# Create operator buttons
operators = ["+", "-", "*", "/"]
operator_buttons = [
    ttk.Button(frame, text=op, command=lambda opr=op: button_click(opr))
    for op in operators
]

# Special buttons
button_0 = ttk.Button(frame, text="0", command=lambda: button_click(0))
button_clear = ttk.Button(frame, text="C", command=clear_entry)
button_delete = ttk.Button(frame, text="DEL", command=delete_character)
button_equal = ttk.Button(frame, text="=", command=calculate)

# Place number buttons on the grid
for i, button in enumerate(buttons, 2):
    button.grid(row=(i - 2) // 3 + 2, column=(i - 2) % 3, padx=5, pady=5)

button_0.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Place operator buttons on the grid
for i, button in enumerate(operator_buttons, 2):
    button.grid(row=i, column=3, padx=5, pady=5)

button_clear.grid(row=2, column=4, padx=5, pady=5)
button_delete.grid(row=3, column=4, padx=5, pady=5)
button_equal.grid(row=4, column=4, rowspan=2, padx=5, pady=5)

# Add spacing between buttons
button_spacing = 10
frame.grid_columnconfigure((0, 1, 2, 3), minsize=button_spacing)
frame.grid_rowconfigure((2, 3, 4, 5), minsize=button_spacing)

# Start the GUI main loop
window.mainloop()
