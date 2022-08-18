import tkinter as tk


def content_view(root):
    content_view.view = tk.LabelFrame(root)

    content_view.view.config(text="")

    sub_label = tk.Label(content_view.view, text='Subnests', width="10", )

    name_label = tk.Label(content_view.view, text='Name')
    size_label = tk.Label(content_view.view, text='Size')

    name_label.grid(column=1, row=0)
    size_label.grid(column=2, row=0)

    content_view.entries_names = []
    content_view.input_names = []
    content_view.entries_size = []
    content_view.input_size = []
    content_view.nb_row = 6

    def add_sub_label():
        nonlocal sub_label
        sub_label.grid(column=0, row=0, rowspan=content_view.nb_row)

    content_view.add_sub_label = add_sub_label

    def set_nb_row(nb):
        content_view.nb_row = nb

    content_view.set_nb_row = set_nb_row

    def create_lines(old_input_name=[], old_input_size=[]):
        for i in range(content_view.nb_row):
            input_text = old_input_name[i] if 0 <= i < len(old_input_name) else tk.StringVar(content_view.view)
            my_entry = tk.Entry(content_view.view, textvariable=input_text)
            content_view.entries_names.append(my_entry)
            content_view.input_names.append(input_text)

        for i in range(content_view.nb_row):
            input_text = old_input_size[i] if 0 <= i < len(old_input_size) else tk.StringVar(content_view.view)
            size_entry = tk.Entry(content_view.view, textvariable=input_text)
            content_view.entries_size.append(size_entry)
            content_view.input_size.append(input_text)

    content_view.create_lines = create_lines

    def add_name_in_view(column, row):
        for i, en_name in enumerate(content_view.entries_names):
            en_name.grid(column=column, row=row + i)

    content_view.add_name_in_view = add_name_in_view

    def add_size_in_view(column, row):
        for i, en_size in enumerate(content_view.entries_size):
            en_size.grid(column=column, row=row + i)

    content_view.add_size_in_view = add_size_in_view

    def get_sub_division():
        size = len(content_view.input_names) if len(content_view.input_names) < len(content_view.input_size) else len(content_view.input_size)

        names = [n.get() for n in content_view.input_names if len(n.get()) != 0]
        sizes = [int(n.get()) for n in content_view.input_size if len(n.get()) != 0]

        return dict(zip(names, sizes))

    content_view.get_sub_division = get_sub_division
