from tkinter import *
import tkinter.font as font
from services.stats_service import stats_service


class StatsView:
    """
    Luokka, joka vastaa käyttöliittymän Stats-näkymää.
    """

    def __init__(self, root):
        """
        Luokan konstruktori, joka luo uuden Stats-näkymää vastaavan olion.
        """

        self._root = root
        self._frame = None
        self._normal_cdf_frame = None
        self._x_entry = None
        self._mean_entry = None
        self._sd_entry = None
        self._calculate_button = None
        self._result_output = None
        self._button_font = font.Font(size=14)
        self._label_font = font.Font(size=14)

        self._initialize()

    def destroy_view(self):
        """
        Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _handle_calculate_button_click(self):
        self._result_output.delete(0.0, END)

        point = self._x_entry.get()
        mean = self._mean_entry.get()
        std = self._sd_entry.get()
        result = stats_service.normal_cdf(point=point, mean=mean, std=std)

        if result:
            self._result_output.insert(0.0, f"Result: {result}")
        else:
            self._result_output.insert(0.0, f"Invalid input")

    def _initialize_frame(self):
        self._frame = Frame(master=self._root)
        self._frame.grid(column=0, row=0, sticky="nsew")
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=0)

    def _initialize_normal_cdf_frame(self):
        self._normal_cdf_frame = LabelFrame(
            master=self._frame, text="Normal Distribution CDF", font=self._label_font)
        self._normal_cdf_frame.grid(
            column=0, row=0, padx=3, pady=3, sticky="nsew")
        self._normal_cdf_frame.columnconfigure([0, 1, 2], weight=1)
        self._normal_cdf_frame.rowconfigure([0, 1, 2], weight=1)

        self._initialize_normal_cdf_entries()
        self._initialize_calculate_button()
        self._initalize_result_output()

    def _initialize_normal_cdf_entries(self):
        entry_font = font.Font(size=12)

        x_label = Label(master=self._normal_cdf_frame,
                        text="x", font=self._label_font)
        x_label.grid(column=0, row=0, sticky="ew")
        self._x_entry = Entry(master=self._normal_cdf_frame, font=entry_font)
        self._x_entry.grid(column=0, row=1, sticky="ew")

        mean_label = Label(master=self._normal_cdf_frame,
                           text="mean", font=self._label_font)
        mean_label.grid(column=1, row=0, sticky="ew")
        self._mean_entry = Entry(
            master=self._normal_cdf_frame, font=entry_font)
        self._mean_entry.grid(column=1, row=1, sticky="ew")

        sd_label = Label(master=self._normal_cdf_frame,
                         text="sd", font=self._label_font)
        sd_label.grid(column=2, row=0, sticky="ew")
        self._sd_entry = Entry(master=self._normal_cdf_frame, font=entry_font)
        self._sd_entry.grid(column=2, row=1, sticky="ew")

    def _initialize_calculate_button(self):
        self._calculate_button = Button(master=self._normal_cdf_frame, text="Calculate", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                        activebackground="#C8C8C8", command=self._handle_calculate_button_click)
        self._calculate_button.grid(column=0, row=2, sticky="ew")

    def _initalize_result_output(self):
        self._result_output = Text(
            master=self._normal_cdf_frame, font=self._label_font, height=1, width=20)
        self._result_output.grid(column=1, row=2, columnspan=2, sticky="ew")

    def _initialize(self):
        self._initialize_frame()
        self._initialize_normal_cdf_frame()
