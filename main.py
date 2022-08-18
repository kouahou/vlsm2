import tkinter as tk
from app import app_view
from tkinter import ttk
from result import result_view, result_controller
from graph import graph_view, graph_controller
from tree import tree_view, tree_controller


def main():
    app_main = tk.Tk()

    app_main.title("VLSM")

    app_main.config(background="#4c283c", highlightthickness=6)

    w = app_main.winfo_reqwidth()
    h = app_main.winfo_reqheight()
    ws = app_main.winfo_screenwidth()
    hs = app_main.winfo_screenheight()

    # create a view and place it on the root window
    app_view(app_main)

    note_book = ttk.Notebook(app_main)

    result_view(note_book)
    graph_view(note_book)
    tree_view(note_book)

    app_view.view.grid(row=0, column=0)

    result_view.view.grid()
    graph_view.view.grid()
    tree_view.view.grid()

    result_controller(result_view.view)
    graph_controller(result_view.view)
    tree_controller(result_view.view)

    app_controller(app_view.view)

    app_view.set_controller(app_controller)
    result_view.set_controller(result_controller)
    graph_view.set_controller(graph_controller)
    tree_view.set_controller(tree_controller)
    app_view.submit_view.controller.set_result_view(result_view)
    app_view.submit_view.controller.set_graph_view(graph_view)
    app_view.submit_view.controller.set_tree_view(tree_view)

    note_book.add(result_view.view, text="vlsm")
    note_book.add(graph_view.view, text="Graph")
    note_book.add(tree_view.view, text="Tree")

    note_book.grid()

    return app_main


def app_controller(view_):
    app_controller.view = view_

    def update_label(label, stringvar):
        """
        Met à jour le texte d'un label en utilisant une StringVar.
        """
        text = stringvar.get()
        label.config(text=text)
        stringvar.set('merci')

    app_controller.update_label = update_label

    def change_number(input_number):
        print(input_number.get())

    app_controller.change_number = change_number


if __name__ == "__main__":
    app = main()
    app.mainloop()

