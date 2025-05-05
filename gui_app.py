import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())

        if n < 0 or r < 0:
            messagebox.showerror("Error", "n and r must be non-negative integers.")
        elif r > n:
            messagebox.showerror("Error", "r cannot be greater than n.")
        else:
            p = math.factorial(n) // math.factorial(n - r)
            c = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            label_result.config(text=f"P({n}, {r}) = {p}\nC({n}, {r}) = {c}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

# GUI setup
root = tk.Tk()
root.title("Permutation & Combination Calculator")

tk.Label(root, text="Enter total items (n):").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Label(root, text="Enter items to choose/arrange (r):").pack()
entry_r = tk.Entry(root)
entry_r.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
