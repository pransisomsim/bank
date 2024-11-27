import tkinter as tk

class WindowGenerator:
    def __init__(self):
        self.current_window = None

    def create_window(self, title):
        if self.current_window is not None:
            self.current_window.destroy()

        self.current_window = tk.Tk()
        self.current_window.title(title)
        self.current_window.config(bg='#bbc6a4')

        self.current_window.grid_rowconfigure(0, weight=1)
        self.current_window.grid_columnconfigure(0, weight=1)
        return self

    def add_frame(self, row, column, padx=10, pady=10, sticky='nsew',frame=None):
        frame = tk.Frame(frame if frame else self.current_window)
        frame.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        return frame

    def add_label(self, text, frame=None, row=0, column=0, padx=2, pady=2, sticky='nsew'):
        label = tk.Label(frame if frame else self.current_window, text=text)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return label

    def add_entry(self, frame=None, row=0, column=0, padx=2, pady=2):
        entry = tk.Entry(frame if frame else self.current_window)
        entry.grid(row=row, column=column, padx=padx, pady=pady)
        return entry

    def add_listbox(self, frame=None, row=0, column=0, height=5, width=25, padx=10, pady=10, sticky='nsew', font=('Arial', 12)):
        listbox = tk.Listbox(frame if frame else self.current_window, font=font, height=height, width=width)
        listbox.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return listbox

    def add_button(self, text, command, frame=None, row=0, column=0, columnspan=1, padx=10, pady=10,bg='#444b3b',fg='#ffffff', sticky='nsew'):
        button = tk.Button(frame if frame else self.current_window, text=text, command=command, bg=bg, fg=fg)
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return button

    def add_radio_button(self, text, variable, value, command, frame=None, row=0, column=0, padx=2, pady=2, sticky='w'):
        radiobutton = tk.Radiobutton(frame if frame else self.current_window, text=text, variable=variable, value=value, command=command)
        radiobutton.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return radiobutton

    def run(self):
        if self.current_window:
            self.current_window.mainloop()

