import tkinter as tk
from functools import partial


def change_view(root):
    change_view.view = tk.LabelFrame(root)

    label = tk.Label(change_view.view, text="        Numbers of subnests:                 ")
    change_view.entry_text = tk.StringVar(change_view.view)
    entry = tk.Entry(change_view.view, textvariable=change_view.entry_text, highlightthickness=2, width="15")

    def change_number():
        return change_view.entry_text.get()

    change_view.button = tk.Button(change_view.view, text="   Change    ",
                            command=partial(change_number))

    label.grid(column=0, row=0)
    entry.grid(column=1, row=0)
    change_view.button.grid(column=2, row=0)

    change_view.change_number = change_number
