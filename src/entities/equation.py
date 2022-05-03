class Equation:
    """Luokka, joka kuvaa yksittäistä laskettua lauseketta, eli yhtälöä.

    Attributes:
        expression: Merkkijonoarvo, joka kuvaa lauseketta.
        result: Merkkijonoarvo, joka kuvaa lasketun lausekkeen tulosta.
    """

    def __init__(self, expression, result):
        """Luokan konstruktori, joka luo uuden yhtälöä kuvaavan olion.

        Args:
            expression: Merkkijonoarvo, joka kuvaa lauseketta.
            result: Float-arvo, joka kuvaa lasketun lausekkeen tulosta.
        """

        self.expression = expression
        self.result = result
