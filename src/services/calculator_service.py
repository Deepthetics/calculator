from math import sqrt


class CalculatorService:
    """Sovelluslogiikasta vastaava luokka"""
    
    def __init__(self):
        pass
    
    def calculate(self, expression):
        """Laskee lausekkeen arvon.

        Args:
            expression: Merkkijonoarvo, joka kuvaa lauseketta.

        Returns:
            Palauttaan lasketun lausekkeen arvon.
            Jos lauseketta ei voida laskea, palauttaa False.
        """

        try:
            result = eval(expression)
            return result
        except:
            return False