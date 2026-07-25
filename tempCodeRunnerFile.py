import customtkinter as ctk
from gui.home import HomePage

# Initialize the CustomTkinter app theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main application window
app = ctk.CTk()
app.title("AstroAI Pro")
app.geometry("1200x700")

# Load the HomePage view from the gui package
HomePage(app)

# Start the application event loop
app.mainloop()