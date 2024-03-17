import tkinter as tk

def welcome():
    # Create main window
    root = tk.Tk()
    root.title("Welcome")

    # Configure window size and position
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create welcome label
    welcome_label = tk.Label(root, text="Welcome to Work Night", font=("Calibri", 20))
    welcome_label.pack(pady=30)

    # Create Start button
    start_button = tk.Button(root, text="Start", font=("Calibri", 16),command=root.destroy)
    start_button.pack()
    
    # Create welcome label
    about_label = tk.Label(root, text="Magis Debuggers SY2023-2024", font=("Calibri", 12))
    about_label.pack(pady=50)

    # Run the application
    root.mainloop()