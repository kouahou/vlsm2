import tkinter as tk
import graphviz


def tree_view(root):
    tree_view.controller = None

    tree_view.view = tk.LabelFrame(root)

    def set_controller(_controller):
        tree_view.controller = _controller

    tree_view.set_controller = set_controller

    def render_fig():
        data = tree_view.controller.service.get_data()

        dot = graphviz.Digraph('Subnet', comment='Sub network', format='png')

        for key, val in data.items():
            dot.node(key, label=str(val))

        links = []
        for i, key in enumerate(data.keys()):
            if i + 1 < len(data.keys()):
                links.append(f'{key}{list(data.keys())[i+1]}')

        dot.edges(links)

    tree_view.render_fig = render_fig


def tree_controller(view_):
    tree_controller.view = view_
    tree_controller.service = None

    def set_service(service_):
        tree_controller.service = service_

    tree_controller.set_service = set_service


def tree_service(data):
    tree_service.data = data

    def set_data(_data):
        tree_service.data = _data

    tree_service.set_data = set_data

    def get_data():
        return tree_service.data

    tree_service.get_data = get_data
