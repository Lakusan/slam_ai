import tkinter as tk
from tkinter import ttk


"""_summary_
    For Tkinter widgets:

    Button
    Checkbutton
    Entry
    Label
    Listbox
    Radiobutton
    Scale
    Spinbox
    Text

    For ttk widgets:

    Button
    Checkbutton
    Entry
    Label
    Treeview
    Radiobutton
    Scale
    Spinbox
    Combobox
"""

class WidgetExamples(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        # Tkinter Widgets
        tk.Label(self, text="Tkinter Widgets").pack()

        tk.Button(self, text="Button").pack()
        tk.Checkbutton(self, text="Checkbutton").pack()
        tk.Entry(self).pack()
        tk.Label(self, text="Label").pack()
        tk.Listbox(self).pack()
        tk.Radiobutton(self, text="Radiobutton").pack()
        tk.Scale(self, orient="horizontal").pack()
        tk.Spinbox(self, from_=1, to=10).pack()
        tk.Text(self).pack()

        # ttk Widgets
        ttk.Separator(self, orient="horizontal").pack(pady=10)
        ttk.Label(self, text="ttk Widgets").pack()

        ttk.Button(self, text="Button").pack()
        ttk.Checkbutton(self, text="Checkbutton").pack()
        ttk.Entry(self).pack()
        ttk.Label(self, text="Label").pack()
        ttk.Treeview(self).pack()
        ttk.Radiobutton(self, text="Radiobutton").pack()
        ttk.Scale(self, orient="horizontal").pack()
        ttk.Spinbox(self, from_=1, to=10).pack()
        ttk.Combobox(self, values=["Option 1", "Option 2", "Option 3"]).pack()

root = tk.Tk()
widget_examples = WidgetExamples(root)
root.mainloop()