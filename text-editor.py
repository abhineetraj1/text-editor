import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
from tkinter.messagebox import askyesno

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.filename = None
        self.master.title("Text Editor - Abhineet Raj")
        self.master.geometry("800x600+0+0")

        #Create a text widget
        self.text = tk.Text(self.master, font=("Arial", 12))
        self.text.pack(fill=tk.BOTH, expand=1)

        #Create a menubar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        #Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create a format menu
        format_menu = tk.Menu(menubar, tearoff=0)
        format_menu.add_command(label="Change Font", command=self.change_font)
        menubar.add_cascade(label="Format", menu=format_menu)

    def new_file(self):
        #Creates a new file
        if self.text.edit_modified():
            answer = askyesno("Save", "Do you want to save changes?")
            if answer == "yes":
                self.save_file()
        self.text.delete(1.0, tk.END)
        self.filename = None

    def open_file(self):
        #Opens an existing file
        if self.text.edit_modified():
            answer = askyesno("Save", "Do you want to save changes?")
            if answer == "yes":
                self.save_file()
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        self.filename = filedialog.askopenfilename(filetypes=filetypes)
        if self.filename:
            with open(self.filename, "r") as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, f.read())
            self.master.title(f"Text Editor - {self.filename}")

    def save_file(self):
        #Saves the current file
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        #Saves the current file as a new file
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        self.filename = filedialog.asksaveasfilename(filetypes=filetypes)
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get(1.0, tk.END))
            self.master.title(f"Text Editor - {self.filename}")

    def change_font(self):
        #Changes the font of the text widget
        font = Font(family="Arial", size=12)
        new_font = font.actual()
        new_font = tk.font.Font(self.master, new_font)
        font = filedialog.askdirectory(initialdir="/", title="Select font directory")
        if font:
            new_font.config(family=font)
            self.text.config(font=new_font)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

# Made by Abhineet Raj [https://github.com/abhineetraj1]
# GNU LICENSE