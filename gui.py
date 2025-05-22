import tkinter as tk

def on_click():
    label.config(text="Hello, " + entry.get())

# Create main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x150")

# Add widgets
entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=on_click)
button.pack()

label = tk.Label(root, text="")
label.pack(pady=10)

# Run the application
root.mainloop()
