class UI:
    def __init__(self, calculator_service):
        self._calculator_service = calculator_service

    def start(self):
        self.print_instructions()

        while True:
            expression = input("Syötä lauseke: ")

            if expression == "x":
                break
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
        print("Jos haluat sulkea ohjelman, syötä 'x'.")
        print("")