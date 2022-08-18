import tkinter as tk


def header_view(parent):
    header_view.view = tk.LabelFrame(parent)
    header_view.view.config(text="", width="10")

    label = tk.Label(header_view.view, text='   Major Network                                                    ')
    header_view.major_text = tk.StringVar(header_view.view)
    ip_entry = tk.Entry(header_view.view, textvariable=header_view.major_text, highlightthickness=2)

    label.grid(column=0, row=0)
    ip_entry.grid(column=1, row=0, rowspan=3)

    def get_ip():
        return header_view.major_text.get().split("/")

    header_view.get_ip = get_ip

