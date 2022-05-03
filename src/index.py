from tkinter import Tk
from ui.ui import UI
from services.calculator_service import CalculatorService


def main():
    window = Tk()
    window.title("Calculator")
    calculator_service = CalculatorService()

    ui_view = UI(window, calculator_service)
    ui_view.initialize()

    window.mainloop()


if __name__ == "__main__":
    main()
