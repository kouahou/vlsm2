import tkinter as tk


def result_view(root):
    result_view.controller = None
    result_view.view = tk.LabelFrame(root)

    result_view.view.config(text="")

    list_label = []

    columns = [
        "Subnet Name", "Needed Size",
        "Allocated Size", "Address", " Mask",
        "Dec Mask", "Assignable Range",
        "Broadcast"]

    for i, column in enumerate(columns):
        label = tk.Label(result_view.view, text=f"{column} ")
        label.grid(column=i, row=0)

    def set_controller(_controller):
        result_view.controller = _controller

    result_view.set_controller = set_controller

    def update_data():
        result = result_view.controller.service.result()
        if len(list_label) != 0:
            for la in list_label:
                la.destroy()

        for j, r in enumerate(result):
            for i, column in enumerate(r):
                label = tk.Label(result_view.view, text=f"{column} ")
                label.grid(column=i, row=j+1)
                list_label.append(label)

    result_view.update_data = update_data


def result_controller(view_):
    result_controller.view = view_
    result_controller.service = None

    def set_service(service_):
        result_controller.service = service_

    result_controller.set_service = set_service
