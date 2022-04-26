from tkinter import Tk
from services.calculator_service import CalculatorService
from ui.gui import UI

# Old text-based UI main
#def main():
    #calculator_service = CalculatorService()
    #ui = UI(calculator_service)
    #ui.start()

def main():
    window = Tk()
    window.title("Calculator")

    calculator_service = CalculatorService()
    ui_view = UI(window, calculator_service)
    ui_view.initialize()

    window.mainloop()


if __name__ == "__main__":
    main()
