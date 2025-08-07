import tkinter as tk
from tkinter import messagebox

# Perform the operation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {num1} {op} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Set up the window
window = tk.Tk()
window.title("🧮 Basic Calculator")
window.geometry("350x300")
window.config(bg="white")

# Widgets
tk.Label(window, text="Enter first number:", bg="white").pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:", bg="white").pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

tk.Label(window, text="Select operation (+, -, *, /):", bg="white").pack(pady=5)
operation = tk.Entry(window)
operation.pack()

tk.Button(window, text="Calculate", command=calculate, bg="#4CAF50", fg="white").pack(pady=15)

result_label = tk.Label(window, text="Result: ", bg="white", font=("Arial", 12))
result_label.pack()

# Run the app
window.mainloop()
