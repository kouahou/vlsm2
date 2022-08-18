import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import math

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None


def graph_view(root):
    graph_view.controller = None

    graph_view.view = tk.LabelFrame(root)

    def set_controller(_controller):
        graph_view.controller = _controller

    graph_view.set_controller = set_controller

    def render_fig():
        global canvas
        figure = plt.figure(figsize=(6, 6), dpi=100)
        figure.set_size_inches(6, 4)

        data = graph_view.controller.service.get_data()

        labels = [f'{k} /{v}' for k, v in data.items()]
        sizes = graph_view.controller.service.size

        plt.pie(sizes, labels=labels, shadow=True, startangle=148)

        plt.axis("equal")

        canvasbar = FigureCanvasTkAgg(figure, master=graph_view.view)

        canvasbar.draw()

        canvasbar.get_tk_widget().grid(column=0, row=0)

    graph_view.render_fig = render_fig


def graph_controller(view_):
    graph_controller.view = view_
    graph_controller.service = None

    def set_service(service_):
        graph_controller.service = service_

    graph_controller.set_service = set_service


def graph_service(_sizes, _names, _group):
    graph_service.group = _group
    graph_service.size = _sizes
    graph_service.names = _names

    def set_size(sizes_):
        graph_service.size = sizes_

    graph_service.set_size = set_size

    def set_names(names_):
        graph_service.names = names_

    graph_service.set_names = set_names

    def set_group(group_):
        graph_service.group = group_

    graph_service.set_group = set_group

    def get_data():
        return dict(zip(graph_service.names,
                        list(map(lambda x: 32 - math.ceil(math.log2(int(x))), graph_service.size))))

    graph_service.get_data = get_data

