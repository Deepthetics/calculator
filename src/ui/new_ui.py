from tkinter import *
from ui.calculator_view import CalculatorView
from ui.history_view import HistoryView
from ui.stats_view import StatsView


class UI:
    """
    Luokka, joka vastaa käyttöliittymän eri näkymien esittämisestä ja niiden välillä siirtymisestä.
    """

    def __init__(self, root):
        """
        Luokan konstruktori, joka luo olion, joka vastaa kehystä, missä käyttöliittymän eri näkymiä voidaan esittää.
        """

        self._root = root
        self._menu = None
        self._current_view = None
        self._calculator_view_entry_content = ""

    def start(self):
        """
        Käynnistää käyttöliittymän.
        """

        self._configure_root()
        self._initialize_menu()
        self.open_calculator_view()

    def _close_current_view(self):
        if self._current_view:
            self._current_view.destroy_view()

        self._current_view = None

    def open_calculator_view(self, history_view_result=None):
        """
        Avaa Calculator-näkymän.

        Args:
            history_view_result: Vapaaehtoinen, oletusarvoltaan None. Muussa tapauksessa float-arvo, joka kuvaa History-näkymässä valittua tulosta, joka siirretään Calculator-näkymään.
        """

        self._close_current_view()

        self._current_view = CalculatorView(
            self._root, self._calculator_view_entry_content, history_view_result)

    def open_history_view(self):
        """
        Avaa History-näkymän.
        """

        self._close_current_view()

        self._current_view = HistoryView(
            self._root, self.open_calculator_view)

    def open_stats_view(self):
        """
        Avaa Stats-näkymän.
        """

        self._close_current_view()

        self._current_view = StatsView(
            self._root)

    def _configure_root(self):
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.minsize(400, 550)
        self._root.geometry("400x550")

    def _initialize_menu(self):
        self._menu = Menu(master=self._root)

        self._menu.add_command(
            label="Calculator", command=self._handle_calculator_button_click)
        self._menu.add_command(
            label="History", command=self._handle_history_button_click)
        self._menu.add_command(
            label="Stats", command=self._handle_stats_button_click)

        self._root.config(menu=self._menu)

    def _handle_calculator_button_click(self):
        if not isinstance(self._current_view, CalculatorView):
            self.open_calculator_view()

    def _handle_history_button_click(self):
        if not isinstance(self._current_view, HistoryView):
            if isinstance(self._current_view, CalculatorView):
                self._calculator_view_entry_content = self._current_view._entry.get()
            self.open_history_view()

    def _handle_stats_button_click(self):
        if not isinstance(self._current_view, StatsView):
            if isinstance(self._current_view, CalculatorView):
                self._calculator_view_entry_content = self._current_view._entry.get()
            self.open_stats_view()
