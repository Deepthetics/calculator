from tkinter import *
import tkinter.font as font
from services.calculator_service import calculator_service


class HistoryView:
    def __init__(self, root, handle_open_calculator_view):
        self._root = root
        self._handle_open_calculator_view = handle_open_calculator_view
        self.frame = None
        self._equation_frame = None
        self._equations = []

        self._initialize()

    def destroy_view(self):
        self.frame.destroy()

    def _handle_equation_button_click(self, history_view_result):
        self._handle_open_calculator_view(history_view_result)

    def _initialize_frame(self):
        self.frame = Frame(master=self._root)
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

    def _initialize_equation_frame(self):
        self._equation_frame = Frame(master=self.frame)
        self._equation_frame.grid(column=0, row=0, sticky="nsew")

        self._equations = calculator_service.get_all_equations()[::-1]

        for i, equation in enumerate(self._equations):
            equation_button = Button(master=self._equation_frame, text=f"{equation.expression} = {equation.result}",
                                     height=3, bg="#F0F0F0", relief=GROOVE, command=lambda: self._handle_equation_button_click(equation.result))

            equation_button.grid(column=0, row=i, sticky="nsew")

            self._equation_frame.columnconfigure(0, weight=1)
            for row_num in range(self._equation_frame.grid_size()[1]):
                self._equation_frame.rowconfigure(row_num, weight=1)

    def _initialize(self):
        self._initialize_frame()
        self._initialize_equation_frame()
