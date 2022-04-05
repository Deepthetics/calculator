
from services.calculator_service import CalculatorService
from ui.ui import UI


def main():
    calculator_service = CalculatorService()
    ui = UI(calculator_service)
    ui.start()


if __name__=="__main__":
    main()