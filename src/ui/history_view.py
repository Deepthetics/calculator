from tkinter import *
import tkinter.font as font
import functools
from services.calculator_service import calculator_service


class HistoryView:
    """
    Luokka, joka vastaa käyttöliittymän History-näkymää.
    """

    def __init__(self, root, handle_open_calculator_view):
        """
        Luokan konstruktori, joka luo uuden History-näkymää vastaavan olion.
        """

        self._root = root
        self._handle_open_calculator_view = handle_open_calculator_view
        self._frame = None
        self._equation_canvas = None
        self._equation_frame = None
        self._button_font = font.Font(size=14)

        self._initialize()

    def destroy_view(self):
        """
        Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _handle_clear_button_click(self):
        calculator_service.delete_all_equations()
        self._initialize_equation_frame()

    def _handle_equation_button_click(self, history_view_result):
        self._handle_open_calculator_view(history_view_result)

    def _initialize_frame(self):
        self._frame = Frame(master=self._root)
        self._frame.grid(column=0, row=0, sticky="nsew")
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=0)
        self._frame.rowconfigure(1, weight=1)

    def _initialize_clear_button(self):
        clear_button = Button(master=self._frame, text="Clear History", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", command=self._handle_clear_button_click)
        clear_button.grid(column=0, row=0, padx=0, pady=0, sticky="nw")

    def _initialize_equation_frame(self):
        self._equation_canvas = Canvas(master=self._frame)
        self._equation_canvas.grid(
            column=0, row=1, padx=0, pady=0, sticky="nsew")

        scrollbar = Scrollbar(master=self._frame, orient="vertical", bg="#FCFCFC",
                              activebackground="#C8C8C8", width=20, command=self._equation_canvas.yview)
        scrollbar.grid(column=1, row=1, sticky="ns")

        self._equation_frame = Frame(master=self._equation_canvas)
        self._equation_canvas.create_window(
            0, 0, window=self._equation_frame, anchor="nw")

        self._equation_canvas.configure(yscrollcommand=scrollbar.set)
        self._equation_canvas.bind("<Configure>", lambda e: self._equation_canvas.configure(
            scrollregion=self._equation_canvas.bbox("all")))

        equations = calculator_service.get_all_equations()

        if equations:
            equations = equations[::-1]
        else:
            return

        for i, equation in enumerate(equations):
            equation_button = Button(master=self._equation_frame, text=f"{equation.expression} = {equation.result}", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                     activebackground="#C8C8C8", height=2, command=functools.partial(self._handle_equation_button_click, history_view_result=equation.result))
            equation_button.grid(column=0, row=i, padx=0,
                                 pady=0, sticky="nsew")

        for row_num in range(self._equation_frame.grid_size()[1]):
            self._equation_frame.rowconfigure(row_num, weight=1)

    def _initialize(self):
        self._initialize_frame()
        self._initialize_clear_button()
        self._initialize_equation_frame()
