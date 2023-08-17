import tkinter as tk

class UIHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.input_field = tk.Entry(self.root)
        self.input_field.pack()

    def display_message(self, message):
        message_label = tk.Label(self.root, text=message)
        message_label.pack()

    def get_user_input(self):
        user_input = self.input_field.get()
        self.input_field.delete(0, 'end')
        return user_input