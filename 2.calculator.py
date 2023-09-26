
import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error")

# Function to clear the input field
def reset():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Function to handle button clicks
def button_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        calculate()
    elif text == "C":
        reset()
    else:
        entry.insert(tk.END, text)

# Create a grid of buttons
row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

    btn.bind("<Button-1>", button_click)

# Create a "Reset" button
reset_button = tk.Button(root, text="C", padx=20, pady=20)
reset_button.grid(row=5, column=3, padx=5, pady=5)
reset_button.bind("<Button-1>", button_click)

# Create a result label
result_label = tk.Label(root, text="", pady=10)
result_label.grid(row=row_val, column=0, columnspan=4)

# Run the GUI
root.mainloop()



