from tkinter import Tk
from ui.new_ui import UI


def main():
    window = Tk()
    window.title("Calculator")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
