import tkinter as tk

# Function to update the expression
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Calculator")

# StringVar for entry
entry_var = tk.StringVar()

# Entry widget
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=equal)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=clear)
        button.grid(row=row, column=col, columnspan=4, sticky="we")
        continue
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), command=lambda t=text: press(t))
    button.grid(row=row, column=col)

# Run the GUI
root.mainloop()
