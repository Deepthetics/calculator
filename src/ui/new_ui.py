from tkinter import *
from ui.calculator_view import CalculatorView
from ui.history_view import HistoryView


class UI:
    def __init__(self, root):
        self._root = root
        self._menu = None
        self._current_view = None
        self._calculator_view_entry_content = ""

    def start(self):
        self._configure_root()
        self._initialize_menu()
        self._open_calculator_view()

    def _close_current_view(self):
        if self._current_view:
            self._current_view.destroy_view()

        self._current_view = None

    def _open_calculator_view(self, history_view_result=None):
        self._close_current_view()

        self._current_view = CalculatorView(self._root, self._open_history_view, self._calculator_view_entry_content,
                                            history_view_result)

    def _open_history_view(self):
        self._close_current_view()

        self._current_view = HistoryView(
            self._root, self._open_calculator_view)

    def _configure_root(self):
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.geometry("320x480")
        self._root.minsize(320, 480)

    def _initialize_menu(self):
        self._menu = Menu(master=self._root)
        self._menu.add_command(
            label="Calculator", command=self._handle_calculator_button_click)
        self._menu.add_command(
            label="History", command=self._handle_history_button_click)
        self._root.config(menu=self._menu)

    def _handle_calculator_button_click(self):
        self._open_calculator_view()

    def _handle_history_button_click(self):
        self._calculator_view_entry_content = self._current_view.entry.get()
        self._open_history_view()
