from tkinter import *
import tkinter.font as font
from services.calculator_service import calculator_service


class CalculatorView:
    def __init__(self, root, handle_open_history_view, entry_content, history_view_result=None):
        self._root = root
        self._handle_open_history_view = handle_open_history_view
        self.frame = None
        self.entry = None
        self._entry_content = entry_content
        self._history_view_result = history_view_result
        self._button_frame = None
        self._button_font = font.Font(size=14)

        self._initialize()

    def destroy_view(self):
        self.frame.destroy()

    def _handle_input_button_click(self, button_text):
        content = self.entry.get()
        if content == "Invalid input":
            self._handle_clear_button_click()
        self.entry.insert(END, button_text)

    def _handle_equality_button_click(self):
        expression = self.entry.get()
        self.entry.delete(0, END)
        result = calculator_service.calculate(expression)

        if result:
            self.entry.insert(0, result)
        else:
            self.entry.insert(0, "Invalid input")

    def _handle_backspace_button_click(self):
        content = self.entry.get()
        if content == "Invalid input":
            self._handle_clear_button_click()
        else:
            self.entry.delete(len(self.entry.get())-1)

    def _handle_clear_button_click(self):
        self.entry.delete(0, END)

    def _handle_ms_button_click(self):
        calculator_service.memory_store()

    def _handle_mr_button_click(self):
        last = calculator_service.memory_recall()
        if last:
            self.entry.insert(END, last)

    def _handle_mc_button_click(self):
        calculator_service.memory_clear()

    def _initialize_frame(self):
        self.frame = Frame(master=self._root)
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def _initialize_entry(self):
        entry_font = font.Font(size=24, weight="bold")

        self.entry = Entry(
            master=self.frame, bd=0, cursor="arrow", font=entry_font, justify=RIGHT)
        self.entry.grid(column=0, row=0, padx=3, pady=3, sticky="nsew")

        if self._history_view_result:
            self.entry.insert(0, self._entry_content +
                              str(self._history_view_result))
        else:
            self.entry.insert(0, self._entry_content)

    def _initialize_button_frame(self):
        self._button_frame = Frame(master=self.frame)
        self._button_frame.grid(column=0, row=1, padx=(
            3, 3), pady=(0, 3), sticky="nsew")
        self._button_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self._button_frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

    def _initialize_digit_buttons(self):
        digit_font = font.Font(size=14, weight="bold")

        digit_0 = Button(master=self._button_frame, text="0", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("0"))
        digit_0.grid(column=0, row=5, sticky="nsew")

        digit_1 = Button(master=self._button_frame, text="1", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("1"))
        digit_1.grid(column=0, row=4, sticky="nsew")

        digit_2 = Button(master=self._button_frame, text="2", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("2"))
        digit_2.grid(column=1, row=4, sticky="nsew")

        digit_3 = Button(master=self._button_frame, text="3", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("3"))
        digit_3.grid(column=2, row=4, sticky="nsew")

        digit_4 = Button(master=self._button_frame, text="4", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("4"))
        digit_4.grid(column=0, row=3, sticky="nsew")

        digit_5 = Button(master=self._button_frame, text="5", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("5"))
        digit_5.grid(column=1, row=3, sticky="nsew")

        digit_6 = Button(master=self._button_frame, text="6", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("6"))
        digit_6.grid(column=2, row=3, sticky="nsew")

        digit_7 = Button(master=self._button_frame, text="7", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("7"))
        digit_7.grid(column=0, row=2, sticky="nsew")

        digit_8 = Button(master=self._button_frame, text="8", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("8"))
        digit_8.grid(column=1, row=2, sticky="nsew")

        digit_9 = Button(master=self._button_frame, text="9", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                         activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("9"))
        digit_9.grid(column=2, row=2, sticky="nsew")

        decimal_point = Button(master=self._button_frame, text=",", bg="#FCFCFC", font=digit_font, relief=GROOVE,
                               activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("."))
        decimal_point.grid(column=1, row=5, sticky="nsew")

    def _initialize_equality_button(self):
        equality_button = Button(master=self._button_frame, text="=", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                 activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_equality_button_click)
        equality_button.grid(column=2, row=5, sticky="nsew")

    def _initialize_operator_buttons(self):
        plus_button = Button(master=self._button_frame, text="+", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                             activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("+"))
        plus_button.grid(row=5, column=3, sticky="nsew")

        minus_button = Button(master=self._button_frame, text="-", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("-"))
        minus_button.grid(row=4, column=3, sticky="nsew")

        multiplication_button = Button(master=self._button_frame, text="x", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                       activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("*"))
        multiplication_button.grid(row=3, column=3, sticky="nsew")

        division_button = Button(master=self._button_frame, text="/", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                 activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("/"))
        division_button.grid(row=2, column=3, sticky="nsew")

        power_button = Button(master=self._button_frame, text="^", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("**"))
        power_button.grid(row=5, column=4, sticky="nsew")

        modulo_button = Button(master=self._button_frame, text="mod", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                               activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("%"))
        modulo_button.grid(row=4, column=4, sticky="nsew")

        abs_button = Button(master=self._button_frame, text="abs", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                            activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("abs("))
        abs_button.grid(row=3, column=4, sticky="nsew")

        sqrt_button = Button(master=self._button_frame, text="sqrt", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                             activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("sqrt("))
        sqrt_button.grid(row=2, column=4, sticky="nsew")

        log_button = Button(master=self._button_frame, text="log", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                            activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("log("))
        log_button.grid(row=1, column=4, sticky="nsew")

    def _initialize_parenthesis_buttons(self):
        left_parenthisis = Button(master=self._button_frame, text="(", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                  activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("("))
        left_parenthisis.grid(column=0, row=1, sticky="nsew")

        right_parenthisis = Button(master=self._button_frame, text=")", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                   activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click(")"))
        right_parenthisis.grid(column=1, row=1, sticky="nsew")

    def _initialize_backspace_button(self):
        backspace_button = Button(master=self._button_frame, text=u"\u232B", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                  activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_backspace_button_click)
        backspace_button.grid(column=4, row=0, sticky="nsew")

    def _initialize_clear_button(self):
        clear_button = Button(master=self._button_frame, text="C", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_clear_button_click)
        clear_button.grid(column=3, row=0, sticky="nsew")

    def _initialize_memory_buttons(self):
        memory_store = Button(master=self._button_frame, text="MS", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_ms_button_click)
        memory_store.grid(column=2, row=0, sticky="nsew")

        memory_recall = Button(master=self._button_frame, text="MR", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                               activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_mr_button_click)
        memory_recall.grid(column=1, row=0, sticky="nsew")

        memory_clear = Button(master=self._button_frame, text="MC", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_mc_button_click)
        memory_clear.grid(column=0, row=0, sticky="nsew")

    def _initialize_constant_buttons(self):
        e_button = Button(master=self._button_frame, text="e", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                          activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("e"))
        e_button.grid(column=2, row=1, sticky="nsew")

        pi_button = Button(master=self._button_frame, text=u"\u03C0", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                           activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("pi"))
        pi_button.grid(column=3, row=1, sticky="nsew")

    def _initialize(self):
        self._initialize_frame()
        self._initialize_entry()
        self._initialize_button_frame()
        self._initialize_digit_buttons()
        self._initialize_equality_button()
        self._initialize_operator_buttons()
        self._initialize_parenthesis_buttons()
        self._initialize_backspace_button()
        self._initialize_clear_button()
        self._initialize_memory_buttons()
        self._initialize_constant_buttons()
