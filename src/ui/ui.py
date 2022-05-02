from tkinter import *
import tkinter.font as font


class UI:
    def __init__(self, root, calculator_service):
        self._root = root
        self._input_entry = None
        self._button_frame = None
        self._button_font = font.Font(size=14)
        self._calculator_service = calculator_service

    def initialize_input_entry(self):
        input_font = font.Font(size=24, weight="bold")

        self._input_entry = Entry(
            master=self._root, bd=0, cursor="arrow", font=input_font, justify=RIGHT)
        self._input_entry.grid(column=0, row=0, padx=3, pady=3, sticky="nsew")

    def initialize_button_frame(self):
        self._button_frame = Frame(master=self._root)
        self._button_frame.grid(column=0, row=1, padx=(
            3, 3), pady=(0, 3), sticky="nsew")
        self._button_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self._button_frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

    def initialize_digit_buttons(self):
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

    def initialize_equality_button(self):
        equality_button = Button(master=self._button_frame, text="=", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                 activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_equality_button_click)
        equality_button.grid(column=2, row=5, sticky="nsew")

    def initialize_operator_buttons(self):
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

    def initialize_parenthesis_buttons(self):
        left_parenthisis = Button(master=self._button_frame, text="(", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                  activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("("))
        left_parenthisis.grid(column=0, row=1, sticky="nsew")

        right_parenthisis = Button(master=self._button_frame, text=")", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                   activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click(")"))
        right_parenthisis.grid(column=1, row=1, sticky="nsew")

    def initialize_backspace_button(self):
        backspace_button = Button(master=self._button_frame, text=u"\u232B", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                                  activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_backspace_button_click)
        backspace_button.grid(column=4, row=0, sticky="nsew")

    def initialize_clear_button(self):
        clear_button = Button(master=self._button_frame, text="C", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_clear_button_click)
        clear_button.grid(column=3, row=0, sticky="nsew")   

    def initialize_memory_buttons(self):
        memory_store = Button(master=self._button_frame, text="MS", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_ms_button_click)
        memory_store.grid(column=2, row=0, sticky="nsew")

        memory_recall = Button(master=self._button_frame, text="MR", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                               activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_mr_button_click)
        memory_recall.grid(column=1, row=0, sticky="nsew")

        memory_clear = Button(master=self._button_frame, text="MC", bg="#FCFCFC", font=self._button_font, relief=GROOVE,
                              activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=self._handle_mc_button_click)
        memory_clear.grid(column=0, row=0, sticky="nsew")

    def initialize_constant_buttons(self):
        e_button = Button(master=self._button_frame, text="e", bg="#FCFCFC", font=self._button_font, relief=GROOVE, 
                          activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("e"))
        e_button.grid(column=2, row=1, sticky="nsew")

        pi_button = Button(master=self._button_frame, text=u"\u03C0", bg="#FCFCFC", font=self._button_font, relief=GROOVE, 
                          activebackground="#C8C8C8", height=1, width=2, padx=0, pady=0, command=lambda: self._handle_input_button_click("pi"))
        pi_button.grid(column=3, row=1, sticky="nsew")

    def configure_root(self):
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
        self._root.geometry("320x480")
        self._root.minsize(320, 480)

    def initialize(self):
        self.configure_root()
        self.initialize_input_entry()
        self.initialize_button_frame()
        self.initialize_digit_buttons()
        self.initialize_equality_button()
        self.initialize_operator_buttons()
        self.initialize_parenthesis_buttons()
        self.initialize_backspace_button()
        self.initialize_clear_button()
        self.initialize_memory_buttons()
        self.initialize_constant_buttons()

    def _handle_input_button_click(self, button_text):
        content = self._input_entry.get()
        if content == "Invalid input":
            self._handle_clear_button_click()
        self._input_entry.insert(END, button_text)

    def _handle_equality_button_click(self):
        expression = self._input_entry.get()
        self._input_entry.delete(0, END)
        result = self._calculator_service.calculate(expression)

        if result:
            self._input_entry.insert(0, result)
        else:
            self._input_entry.insert(0, "Invalid input")

    def _handle_backspace_button_click(self):
        content = self._input_entry.get()
        if content == "Invalid input":
            self._handle_clear_button_click()
        else:
            self._input_entry.delete(len(self._input_entry.get())-1)

    def _handle_clear_button_click(self):
        self._input_entry.delete(0, END)

    def _handle_ms_button_click(self):
        self._calculator_service.memory_store()

    def _handle_mr_button_click(self):
        last = self._calculator_service.memory_recall()
        if last:
            self._input_entry.insert(END, last)

    def _handle_mc_button_click(self):
        self._calculator_service.memory_clear()
