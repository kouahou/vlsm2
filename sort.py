import tkinter as tk
from tkinter import ttk


def sort_view(root):
    sort_view.view = tk.LabelFrame(root)

    label = tk.Label(sort_view.view, text="               Sort results by:                      ")
    list_tri = ["Name", "Size"]
    sort_view.list_combo = ttk.Combobox(sort_view.view, values=list_tri, width="25")
    sort_view.list_combo.current(0)

    label.grid(column=0, row=0)
    sort_view.list_combo.grid(column=1, row=0)

    def get_sort():
        return sort_view.list_combo.get()

    sort_view.get_sort = get_sort
