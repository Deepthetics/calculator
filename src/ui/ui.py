class UI:
    def __init__(self, calculator_service):
        self._calculator_service = calculator_service

    def start(self):
        self.print_instructions()

        while True:
            expression = input("Syötä lauseke: ")

            if expression == "x":
                break
            elif expression == "s":
                self._calculator_service.memory_store()
            elif expression == "r":
                print(f"Talletettu tulos: {self._calculator_service.memory_recall()}")
            elif expression == "c":
                self._calculator_service.memory_clear()
            else:
                result = self._calculator_service.calculate(expression)
                if result:
                    print(f"{expression} = {result}")
                    print("")
                else:
                    print("Syöte on virheellinen")
                    print("")

    def print_instructions(self):
        print("--Laskin--")
        print("")
        print("Tuetut laskutoimitukset:")
        print("-yhteenlasku: '+'")
        print("-vähennyslasku: '-'")
        print("-kertolasku: '*'")
        print("-jakolasku: '/'")
        print("-potenssi: '**'")
        print("-jakojäännös: '%'")
        print("-itseisarvo: 'abs(x)', missä 'x' on reaaliluku")
        print("-neliöjuuri: 'sqrt(x)', missä 'x' on reaaliluku")
        print("")
        print("Jos haluat tallettaa viimeisimmän tuloksen muistiin, syötä 's'.")
        print("")
        print("Jos haluat palauttaa viimeisimmän tuloksen muistista, syötä 'r'.")
        print("")
        print("Jos haluat tyhjentää muistin, syötä 'c'.")
        print("")
        print("Jos haluat sulkea ohjelman, syötä 'x'.")
        print("")
