import tkinter as tk
from functools import partial
from ip_s import ip_service
from graph import graph_service
from tree import tree_service


def submit_view(root):
    submit_view.controller = None

    def set_controller(_controller):
        submit_view.controller = _controller

    submit_view.set_controller = set_controller

    def calcul_vlsm():
        return submit_view.controller.get_data()

    submit_view.calcul_vlsm = calcul_vlsm

    submit_view.view = tk.Frame(root)
    submit_view.button = tk.Button(submit_view.view, text="   Submit   ", command=partial(calcul_vlsm))

    input1 = tk.StringVar(submit_view.view)
    input1_name = tk.Entry(submit_view.view, textvariable=input1, highlightthickness=2, width="20")

    input2 = tk.StringVar(submit_view.view)
    input2_name = tk.Entry(submit_view.view, textvariable=input2, highlightthickness=2, width="20")

    submit_view.button.grid(column=0, row=0)
    input1_name.grid(column=1, row=0)
    input2_name.grid(column=2, row=0)


def submit_controller(content_view, header_view, sort_view, result_view=None, graph_view=None, tree_view=None):
    submit_controller.content = content_view
    submit_controller.header = header_view
    submit_controller.result = result_view
    submit_controller.graph = graph_view
    submit_controller.sort = sort_view
    submit_controller.tree = tree_view

    def set_result_view(result_v):
        submit_controller.result = result_v

    submit_controller.set_result_view = set_result_view

    def set_graph_view(graph_v):
        submit_controller.graph = graph_v

    submit_controller.set_graph_view = set_graph_view

    def set_tree_view(tree_v):
        submit_controller.tree = tree_v

    submit_controller.set_tree_view = set_tree_view

    def get_data():
        content_data = submit_controller.content.get_sub_division()
        header_data = submit_controller.header.get_ip()
        sort_data = submit_controller.sort.get_sort()

        ip_service(*header_data)
        ip_service.set_sub_network(content_data)

        submit_controller.result.controller.set_service(ip_service)

        graph_service(ip_service.sub_networks.values(), ip_service.sub_networks.keys(), sort_data)
        submit_controller.graph.controller.set_service(graph_service)

        tree_service(ip_service.sub_networks)
        submit_controller.tree.controller.set_service(tree_service)

        submit_controller.result.update_data()
        submit_controller.graph.render_fig()
        submit_controller.tree.render_fig()

    submit_controller.get_data = get_data
