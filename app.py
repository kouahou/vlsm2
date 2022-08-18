import tkinter as tk
from header import header_view
from content import content_view
from change import change_view
from sort import sort_view
from submit import submit_view, submit_controller


def app_view(root):
    app_view.view = tk.Frame(root)

    app_view.controller = None

    app_view.view.configure(background="#4c283c", highlightthickness=4)

    # Create Header view
    header_view(app_view.view)
    header_view.view.grid(padx=20, ipadx=5, pady=20)
    app_view.header_view = header_view

    content_view(app_view.view)
    content_view.create_lines()
    content_view.add_name_in_view(1, 2)
    content_view.add_size_in_view(2, 2)
    content_view.add_sub_label()
    content_view.view.grid(padx=10, ipadx=5, ipady=5)

    app_view.content_view = content_view

    sort_view(app_view.view)
    sort_view.view.grid(padx=20, ipadx=5)

    app_view.sort_view = sort_view

    def change_nb(event):
        app_view.render_content(int(app_view.change_view.entry_text.get()))

    app_view.change_nb = change_nb

    change_view(app_view.view)
    change_view.view.grid(padx=20, ipadx=5)
    change_view.button.bind('<Button-1>', app_view.change_nb)
    app_view.change_view = change_view

    def get_data(event):
        ip = app_view.header_view.get_ip()

    app_view.get_data = get_data

    submit_view(app_view.view)
    submit_view.view.grid(padx=20, ipadx=5, pady=20)
    submit_view.button.bind('<Button-1>', app_view.get_data)
    submit_controller(content_view, header_view, sort_view)
    submit_view.set_controller(submit_controller)
    app_view.submit_view = submit_view

    def set_controller(_controller):
        app_view.controller = _controller

    app_view.set_controller = set_controller

    def render_change():
        app_view.change_view.view.destroy()

        change_view(app_view.view)
        change_view.view.grid(padx=20, ipadx=5)
        change_view.button.bind('<Button-1>', app_view.change_nb)
        app_view.change_view = change_view

    app_view.render_change = render_change

    def render_sort():
        app_view.sort_view.view.destroy()

        sort_view(app_view.view)
        sort_view.view.grid(padx=20, ipadx=5)
        app_view.sort_view = sort_view

    app_view.render_sort = render_sort

    def render_submit():
        result_view = app_view.submit_view.controller.result
        graph_view = app_view.submit_view.controller.graph
        tree_view = app_view.submit_view.controller.tree

        app_view.submit_view.view.destroy()

        submit_view(app_view.view)
        submit_view.view.grid(padx=20, ipadx=5, pady=20)
        submit_controller(app_view.content_view, app_view.header_view, app_view.sort_view)

        submit_view.set_controller(submit_controller)

        submit_view.controller.set_result_view(result_view)
        submit_view.controller.set_graph_view(graph_view)
        submit_view.controller.set_tree_view(tree_view)

        app_view.submit_view = submit_view

    app_view.render_submit = render_submit

    def render_content(nb=7):
        list_names = app_view.content_view.input_names
        list_size = app_view.content_view.input_size
        app_view.content_view.view.destroy()

        content_view(app_view.view)
        content_view.set_nb_row(nb)
        content_view.create_lines(list_names, list_size)
        content_view.add_name_in_view(1, 2)
        content_view.add_size_in_view(2, 2)
        content_view.add_sub_label()
        content_view.view.grid(padx=10, ipadx=5, ipady=5)

        app_view.content_view = content_view

        app_view.render_change()
        app_view.render_sort()
        app_view.render_submit()

    app_view.render_content = render_content

    def change_number(var):
        app_view.controller.change_number(var)
        app_view.render_content(int(var.get()))

    app_view.change_number = change_number

