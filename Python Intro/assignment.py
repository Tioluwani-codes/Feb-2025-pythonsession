# Import the tkinter module for creating GUI applications
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a label and entry field for the user's name
        self.name_label = tk.Label(self)
        self.name_label["text"] = "What's your name?"
        self.name_label.pack(side="top")

        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side="top")

        # Create a label and entry field for the user's favorite color
        self.color_label = tk.Label(self)
        self.color_label["text"] = "What's your favorite color?"
        self.color_label.pack(side="top")

        self.color_entry = tk.Entry(self)
        self.color_entry.pack(side="top")

        # Create a button to submit the user's input
        self.submit_button = tk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.print_greeting
        self.submit_button.pack(side="top")

        # Create a label to display the personalized greeting
        self.greeting_label = tk.Label(self)
        self.greeting_label.pack(side="top")

    def print_greeting(self):
        # Get the user's input from the entry fields
        name = self.name_entry.get()
        color = self.color_entry.get()

        # Create a personalized greeting
        greeting = f"Hello, {name}! Your favorite color, {color}, is awesome!"

        # Display the greeting in the label
        self.greeting_label["text"] = greeting

# Create the main window
root = tk.Tk()
root.title("Personalized Greeting")

# Create an instance of the Application class
app = Application(master=root)

# Start the main event loop
app.mainloop()




